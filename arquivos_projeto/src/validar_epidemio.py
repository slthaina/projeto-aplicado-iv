"""
Validação e consolidação dos dados epidemiológicos brutos.

Gera:
- data/processed/epidemio_semanal.csv : tabela única (município x doença x semana).
  Semanas ausentes entram como linhas com casos vazios (NaN) e semana_ausente=True.
  Elas NUNCA são preenchidas com zero.
- outputs/relatorio_validacao.csv : um resumo por município x doença x período.

Os arquivos em data/raw não são alterados.
"""
import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).resolve().parent.parent))
import config as cfg

# Regras de classificação (documentar no projeto)
LIMIAR_SEM_CIRCULACAO = 0.95  # proporção de semanas com 0 casos
LIMIAR_ESPARSA = 0.50

COLUNAS_UTEIS = ["data_iniSE", "SE", "casos", "casos_est", "p_inc100k", "pop"]


def ler_arquivo(geocode, nome, doenca, periodo):
    caminho = cfg.DIR_RAW / doenca / f"{geocode}_{nome}_{doenca}_{periodo}.csv"
    if not caminho.exists():
        return None
    d = pd.read_csv(caminho)
    colunas = [c for c in COLUNAS_UTEIS if c in d.columns]
    d = d[colunas].copy()
    d["geocode"], d["municipio"] = geocode, nome
    d["doenca"], d["periodo"] = doenca, periodo
    return d


def main():
    pedacos = []
    for geocode, nome in cfg.MUNICIPIOS.items():
        for doenca in cfg.DOENCAS:
            for periodo in cfg.PERIODOS:
                d = ler_arquivo(geocode, nome, doenca, periodo)
                if d is None:
                    print(f"AVISO: arquivo ausente: {nome} | {doenca} | {periodo}")
                    continue
                pedacos.append(d)

    bruto = pd.concat(pedacos, ignore_index=True)

    # Semanas esperadas por período = todas as SE que aparecem em qualquer série do período
    esperadas = bruto.groupby("periodo")["SE"].apply(lambda s: sorted(s.unique())).to_dict()

    tabelas, resumo = [], []
    for (geocode, nome, doenca, periodo), d in bruto.groupby(
            ["geocode", "municipio", "doenca", "periodo"]):
        dup = int(d.duplicated("SE").sum())
        d = d.drop_duplicates("SE")
        grade = pd.DataFrame({"SE": esperadas[periodo]})
        full = grade.merge(d, on="SE", how="left")
        full["semana_ausente"] = full["casos"].isna()
        for col, val in [("geocode", geocode), ("municipio", nome),
                         ("doenca", doenca), ("periodo", periodo)]:
            full[col] = val

        n_esp = len(full)
        n_aus = int(full["semana_ausente"].sum())
        obs = full.loc[~full["semana_ausente"], "casos"]
        prop_zeros = float((obs == 0).mean()) if len(obs) else float("nan")
        # série truncada: ausências contíguas no final
        truncada = bool(full["semana_ausente"].iloc[-1]) if n_esp else False

        if prop_zeros >= LIMIAR_SEM_CIRCULACAO:
            classe = "sem_circulacao_relevante"
        elif prop_zeros >= LIMIAR_ESPARSA:
            classe = "esparsa"
        else:
            classe = "ok"

        igual = (bool((obs == full.loc[~full["semana_ausente"], "casos_est"]).all())
                 if "casos_est" in full else None)

        resumo.append({
            "municipio": nome, "doenca": doenca, "periodo": periodo,
            "semanas_esperadas": n_esp, "semanas_ausentes": n_aus,
            "serie_truncada": truncada, "duplicatas_removidas": dup,
            "soma_casos": float(obs.sum()), "semanas_zero": int((obs == 0).sum()),
            "prop_zeros": round(prop_zeros, 3), "classificacao": classe,
            "casos_est_igual_casos": igual,
        })
        full["classificacao_serie"] = classe
        tabelas.append(full)

    tabela = pd.concat(tabelas, ignore_index=True)
    tabela["ano_se"] = tabela["SE"] // 100
    tabela["semana_se"] = tabela["SE"] % 100

    cfg.DIR_RAW.parent.parent.joinpath("processed").mkdir(parents=True, exist_ok=True)
    cfg.DIR_LOGS.parent.mkdir(parents=True, exist_ok=True)
    saida_tab = cfg.RAIZ / "data" / "processed" / "epidemio_semanal.csv"
    saida_rel = cfg.RAIZ / "outputs" / "relatorio_validacao.csv"
    tabela.to_csv(saida_tab, index=False)
    pd.DataFrame(resumo).to_csv(saida_rel, index=False)

    print(f"Tabela: {saida_tab} ({len(tabela)} linhas)")
    print(f"Relatório: {saida_rel}")
    rel = pd.DataFrame(resumo)
    print("\nClassificação das séries:")
    print(rel.groupby(["doenca", "periodo"])["classificacao"].value_counts().to_string())
    print("\nSéries com semanas ausentes:")
    print(rel.loc[rel["semanas_ausentes"] > 0,
                  ["municipio", "doenca", "periodo", "semanas_ausentes"]].to_string(index=False))


if __name__ == "__main__":
    main()