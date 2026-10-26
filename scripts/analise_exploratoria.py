
from pathlib import Path
import re

import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# CAMINHOS E CONFIGURAÇÕES
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
PASTA_PROCESSED = BASE_DIR / "data" / "processed"
PASTA_REPORTS = BASE_DIR / "reports" / "analise_exploratoria"

PASTA_REPORTS.mkdir(parents=True, exist_ok=True)

DOENCAS = {"dengue", "chikungunya"}
ANOS = {2022, 2023}

COLUNA_CASOS = "casos_est"


# ============================================================
# CALENDÁRIO EPIDEMIOLÓGICO
# ============================================================

def primeiro_domingo_epi(ano):
    """Calcula o início da semana epidemiológica 1."""
    quatro_janeiro = pd.Timestamp(f"{ano}-01-04")
    deslocamento = (quatro_janeiro.weekday() + 1) % 7

    return quatro_janeiro - pd.Timedelta(days=deslocamento)


def criar_calendario(ano):
    """Cria o calendário esperado de semanas epidemiológicas."""
    inicio = primeiro_domingo_epi(ano)
    fim = primeiro_domingo_epi(ano + 1)

    datas = pd.date_range(
        start=inicio,
        end=fim,
        freq="7D",
        inclusive="left"
    )

    return {
        ano * 100 + numero: data
        for numero, data in enumerate(datas, start=1)
    }


# ============================================================
# IDENTIFICAÇÃO DOS ARQUIVOS
# ============================================================

def identificar_arquivo(caminho):
    """
    Espera nomes como:
    dengue_manaus_2022.csv
    chikungunya_porto_alegre_2023.csv
    """
    partes = caminho.stem.split("_")

    if len(partes) < 3:
        return None

    doenca = partes[0].lower()

    try:
        ano = int(partes[-1])
    except ValueError:
        return None

    municipio = "_".join(partes[1:-1])

    if doenca not in DOENCAS or ano not in ANOS:
        return None

    return doenca, municipio, ano


# ============================================================
# LEITURA E AVALIAÇÃO DA COMPLETUDE
# ============================================================

arquivos = sorted(PASTA_PROCESSED.glob("*.csv"))

if not arquivos:
    raise FileNotFoundError(
        f"Nenhum CSV encontrado em {PASTA_PROCESSED}"
    )

completude = []
series_completas = []
arquivos_considerados = 0

for arquivo in arquivos:
    identificacao = identificar_arquivo(arquivo)

    # Exclui zika e arquivos fora do período definido.
    if identificacao is None:
        continue

    doenca, municipio, ano = identificacao
    arquivos_considerados += 1

    df = pd.read_csv(arquivo)

    colunas_obrigatorias = {"data_iniSE", "SE", COLUNA_CASOS}
    ausentes = colunas_obrigatorias - set(df.columns)

    if ausentes:
        completude.append({
            "arquivo": arquivo.name,
            "doenca": doenca,
            "municipio": municipio,
            "ano": ano,
            "status": "VERIFICAR_COLUNAS",
            "colunas_ausentes": ", ".join(sorted(ausentes)),
        })
        continue

    df["data_iniSE"] = pd.to_datetime(
        df["data_iniSE"], errors="coerce"
    ).dt.normalize()

    df["SE"] = pd.to_numeric(df["SE"], errors="coerce")
    df[COLUNA_CASOS] = pd.to_numeric(
        df[COLUNA_CASOS], errors="coerce"
    )

    calendario = criar_calendario(ano)
    semanas_esperadas = set(calendario)

    # Ano epidemiológico derivado do código SE.
    df["ano_SE"] = (df["SE"] // 100).where(
        df["SE"].notna()
    )

    # Preserva o arquivo, mas analisa somente o ano correto.
    anual = df[df["ano_SE"] == ano].copy()

    semanas_validas = anual["SE"].dropna().astype(int)
    semanas_observadas = set(semanas_validas)

    faltantes = sorted(semanas_esperadas - semanas_observadas)

    duplicadas = int(
        anual["SE"].dropna().duplicated().sum()
    )

    SE_invalidas = int(
        df["SE"].isna().sum()
        + (
            df["SE"].notna()
            & (
                (df["SE"] % 1 != 0)
                | (df["SE"] < 10000)
                | (df["SE"] > 999999)
            )
        ).sum()
    )

    casos_ausentes = int(anual[COLUNA_CASOS].isna().sum())

    # Confere se a data corresponde ao código SE.
    datas_divergentes = 0

    for _, linha in anual.iterrows():
        if pd.isna(linha["SE"]) or pd.isna(linha["data_iniSE"]):
            continue

        se = int(linha["SE"])
        data_esperada = calendario.get(se)

        if (
            data_esperada is None
            or linha["data_iniSE"] != data_esperada
        ):
            datas_divergentes += 1

    # Uma série só entra na EDA principal se estiver completa.
    esta_completa = (
        len(faltantes) == 0
        and duplicadas == 0
        and SE_invalidas == 0
        and casos_ausentes == 0
        and datas_divergentes == 0
        and len(anual) == len(semanas_esperadas)
    )

    status = "COMPLETA" if esta_completa else "INCOMPLETA"

    completude.append({
        "arquivo": arquivo.name,
        "doenca": doenca,
        "municipio": municipio,
        "ano": ano,
        "registros_arquivo": len(df),
        "registros_ano_epi": len(anual),
        "semanas_esperadas": len(semanas_esperadas),
        "semanas_observadas": len(semanas_observadas),
        "semanas_faltantes": len(faltantes),
        "codigos_SE_faltantes": ", ".join(map(str, faltantes)),
        "SE_duplicadas": duplicadas,
        "SE_invalidas": SE_invalidas,
        "casos_ausentes": casos_ausentes,
        "datas_SE_divergentes": datas_divergentes,
        "status": status,
    })

    if esta_completa:
        anual = anual.sort_values("SE").copy()
        anual["doenca"] = doenca
        anual["municipio"] = municipio
        anual["ano"] = ano

        series_completas.append(anual)


# ============================================================
# RELATÓRIO DE COMPLETUDE
# ============================================================

df_completude = pd.DataFrame(completude)

caminho_completude = (
    PASTA_REPORTS / "completude_series.csv"
)

df_completude.to_csv(
    caminho_completude,
    index=False,
    encoding="utf-8-sig"
)

print("=" * 60)
print("ANÁLISE EXPLORATÓRIA")
print("=" * 60)

print(f"Arquivos encontrados: {len(arquivos)}")
print(f"Arquivos no escopo: {arquivos_considerados}")

if not df_completude.empty:
    print("\nResumo da completude:")
    print(df_completude["status"].value_counts().to_string())

    incompletas = df_completude[
        df_completude["status"] != "COMPLETA"
    ]

    if not incompletas.empty:
        print("\nSéries que precisam de atenção:")
        print(incompletas.to_string(index=False))

print(f"\nRelatório salvo em: {caminho_completude}")


# ============================================================
# ESTATÍSTICAS DESCRITIVAS
# ============================================================

if not series_completas:
    print(
        "\nNenhuma série passou por todos os critérios de "
        "completude. As estatísticas e os gráficos não foram "
        "gerados. Consulte o relatório de completude."
    )
    raise SystemExit(0)

dados = pd.concat(series_completas, ignore_index=True)

resumos = []

for (doenca, municipio, ano), grupo in dados.groupby(
    ["doenca", "municipio", "ano"]
):
    grupo = grupo.sort_values("SE")
    casos = grupo[COLUNA_CASOS]

    indice_pico = casos.idxmax()
    linha_pico = grupo.loc[indice_pico]

    resumos.append({
        "doenca": doenca,
        "municipio": municipio,
        "ano": ano,
        "semanas": len(grupo),
        "total_casos_estimados": casos.sum(),
        "media_semanal": casos.mean(),
        "mediana_semanal": casos.median(),
        "desvio_padrao_semanal": casos.std(),
        "minimo_semanal": casos.min(),
        "maximo_semanal": casos.max(),
        "SE_pico": int(linha_pico["SE"]),
        "data_pico": linha_pico["data_iniSE"].date(),
    })

df_resumo = pd.DataFrame(resumos)

caminho_resumo = PASTA_REPORTS / "resumo_estatistico.csv"

df_resumo.to_csv(
    caminho_resumo,
    index=False,
    encoding="utf-8-sig"
)

print("\nResumo estatístico:")
print(df_resumo.round(2).to_string(index=False))
print(f"\nRelatório salvo em: {caminho_resumo}")


# ============================================================
# GRÁFICOS DE EVOLUÇÃO SEMANAL
# ============================================================

for doenca in sorted(DOENCAS):
    for ano in sorted(ANOS):
        recorte = dados[
            (dados["doenca"] == doenca)
            & (dados["ano"] == ano)
        ]

        if recorte.empty:
            continue

        fig, ax = plt.subplots(figsize=(12, 6))

        for municipio, grupo in recorte.groupby("municipio"):
            grupo = grupo.sort_values("SE")

            semanas = grupo["SE"].astype(int) % 100

            ax.plot(
                semanas,
                grupo[COLUNA_CASOS],
                marker="o",
                markersize=3,
                linewidth=1.5,
                label=municipio.replace("_", " ").title()
            )

        ax.set_title(
            f"Evolução semanal de casos estimados: "
            f"{doenca.title()} ({ano})"
        )
        ax.set_xlabel("Semana epidemiológica")
        ax.set_ylabel("Casos estimados por semana")
        ax.legend(title="Município")
        ax.grid(True, alpha=0.3)
        fig.tight_layout()

        destino = PASTA_REPORTS / (
            f"serie_semanal_{doenca}_{ano}.png"
        )

        fig.savefig(destino, dpi=150)
        plt.close(fig)

        print(f"Gráfico salvo em: {destino}")


# ============================================================
# COMPARAÇÃO DOS TOTAIS ESTIMADOS
# ============================================================

for doenca in sorted(DOENCAS):
    resumo_doenca = df_resumo[
        df_resumo["doenca"] == doenca
    ]

    if resumo_doenca.empty:
        continue

    tabela = resumo_doenca.pivot(
        index="municipio",
        columns="ano",
        values="total_casos_estimados"
    )

    ax = tabela.plot(
        kind="bar",
        figsize=(11, 6)
    )

    ax.set_title(
        f"Total anual de casos estimados: {doenca.title()}"
    )
    ax.set_xlabel("Município")
    ax.set_ylabel("Soma das estimativas semanais")
    ax.legend(title="Ano")
    ax.grid(axis="y", alpha=0.3)

    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()

    destino = PASTA_REPORTS / f"totais_anuais_{doenca}.png"

    plt.savefig(destino, dpi=150)
    plt.close()

    print(f"Gráfico salvo em: {destino}")


# ============================================================
# FINALIZAÇÃO
# ============================================================

print("\n" + "=" * 60)
print("ANÁLISE EXPLORATÓRIA CONCLUÍDA")
print("=" * 60)
print(f"Relatórios e gráficos: {PASTA_REPORTS}")
print(f"Séries completas analisadas: {len(series_completas)}")
print("Os arquivos de entrada não foram modificados.")
