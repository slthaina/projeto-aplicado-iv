
from pathlib import Path
import pandas as pd

PASTA = Path("data/raw")
arquivos = sorted(PASTA.glob("*.csv"))

problemas = []

for arquivo in arquivos:
    df = pd.read_csv(arquivo)

    if not {"data_iniSE", "SE"}.issubset(df.columns):
        problemas.append({
            "arquivo": arquivo.name,
            "problema": "Colunas ausentes"
        })
        continue

    datas = pd.to_datetime(df["data_iniSE"], errors="coerce")
    semanas = pd.to_numeric(df["SE"], errors="coerce")

    # O ano epidemiológico é determinado pela quinta-feira
    # da semana, pois as semanas vão de domingo a sábado.
    datas_validas = datas.notna()
    quinta = datas + pd.Timedelta(days=4)
    ano_epi = quinta.dt.year

    inicio_ano = pd.to_datetime(
        ano_epi.astype("Int64").astype(str) + "-01-04",
        errors="coerce"
    )

    inicio_semana1 = inicio_ano - pd.to_timedelta(
        (inicio_ano.dt.weekday + 1) % 7,
        unit="D"
    )

    semana_calculada = (
        ((datas - inicio_semana1).dt.days // 7) + 1
    )

    se_calculada = ano_epi * 100 + semana_calculada

    divergencias = (
        datas_validas
        & semanas.notna()
        & (semanas != se_calculada)
    )

    invalidas = ~datas_validas | semanas.isna()

    for i in df.index[divergencias | invalidas]:
        problemas.append({
            "arquivo": arquivo.name,
            "data_iniSE": df.loc[i, "data_iniSE"],
            "SE_informada": df.loc[i, "SE"],
            "SE_calculada": (
                int(se_calculada.loc[i])
                if pd.notna(se_calculada.loc[i])
                else None
            ),
            "problema": (
                "Data ou SE inválida"
                if invalidas.loc[i]
                else "SE divergente"
            )
        })

print(f"Arquivos encontrados: {len(arquivos)}")
print(f"Arquivos com divergências: {len(set(p['arquivo'] for p in problemas))}")
print(f"Registros com problemas: {len(problemas)}")

if problemas:
    relatorio = pd.DataFrame(problemas)
    destino = Path("reports/validacao_se_epidemiologica.csv")
    destino.parent.mkdir(parents=True, exist_ok=True)
    relatorio.to_csv(destino, index=False)
    print(relatorio.to_string(index=False))
    print(f"\nRelatório salvo em: {destino}")
else:
    print("Nenhuma divergência encontrada na numeração das semanas.")
