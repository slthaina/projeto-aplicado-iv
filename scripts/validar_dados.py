
from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
PASTA = RAIZ / "data" / "raw"
PASTA_RELATORIOS = RAIZ / "reports"
PASTA_RELATORIOS.mkdir(parents=True, exist_ok=True)

CAPITAIS = [
    "manaus", "recife", "brasilia", "sao_paulo", "porto_alegre"
]
DOENCAS = ["dengue", "zika", "chikungunya"]
ANOS = [2022, 2023]

COLUNAS_IMPORTANTES = ["data_iniSE", "SE", "casos_est", "casos"]

resultados = []
total_esperado = len(CAPITAIS) * len(DOENCAS) * len(ANOS)

for doenca in DOENCAS:
    for capital in CAPITAIS:
        for ano in ANOS:
            nome = f"{doenca}_{capital}_{ano}.csv"
            arquivo = PASTA / nome

            resultado = {
                "arquivo": nome,
                "status": "OK",
                "registros": 0,
                "datas_invalidas": 0,
                "datas_fora_do_ano": 0,
                "datas_duplicadas": 0,
                "semanas_duplicadas": 0,
                "casos_est_ausentes": None,
                "casos_ausentes": None,
                "primeira_data": None,
                "ultima_data": None,
            }

            if not arquivo.exists():
                resultado["status"] = "ARQUIVO AUSENTE"
                resultados.append(resultado)
                continue

            try:
                df = pd.read_csv(arquivo, low_memory=False)
                resultado["registros"] = len(df)

                faltantes = [
                    coluna for coluna in COLUNAS_IMPORTANTES
                    if coluna not in df.columns
                ]

                if faltantes:
                    resultado["status"] = (
                        "COLUNAS AUSENTES: " + ", ".join(faltantes)
                    )
                    resultados.append(resultado)
                    continue

                datas = pd.to_datetime(
                    df["data_iniSE"], errors="coerce"
                )

                resultado["datas_invalidas"] = int(datas.isna().sum())

                validas = datas.dropna()
                resultado["datas_fora_do_ano"] = int(
                    (validas.dt.year != ano).sum()
                )

                resultado["datas_duplicadas"] = int(
                    datas.dropna().duplicated().sum()
                )

                semanas = df["SE"].dropna().astype(str).str.replace(
                    r"\.0$", "", regex=True
                )
                resultado["semanas_duplicadas"] = int(
                    semanas.duplicated().sum()
                )

                resultado["casos_est_ausentes"] = int(
                    df["casos_est"].isna().sum()
                )
                resultado["casos_ausentes"] = int(
                    df["casos"].isna().sum()
                )

                if not validas.empty:
                    resultado["primeira_data"] = validas.min().date()
                    resultado["ultima_data"] = validas.max().date()

                problemas = (
                    resultado["registros"] == 0
                    or resultado["datas_invalidas"] > 0
                    or resultado["datas_fora_do_ano"] > 0
                    or resultado["datas_duplicadas"] > 0
                    or resultado["semanas_duplicadas"] > 0
                )

                if problemas:
                    resultado["status"] = "VERIFICAR"

            except Exception as erro:
                resultado["status"] = f"ERRO DE LEITURA: {erro}"

            resultados.append(resultado)

relatorio = pd.DataFrame(resultados)
caminho = PASTA_RELATORIOS / "validacao_dados.csv"
relatorio.to_csv(caminho, index=False, encoding="utf-8-sig")

print(f"Arquivos esperados: {total_esperado}")
print(f"Arquivos verificados: {len(relatorio)}")
print("\nResumo dos status:")
print(relatorio["status"].value_counts().to_string())

problemas = relatorio[relatorio["status"] != "OK"]

if not problemas.empty:
    print("\nArquivos que precisam de atenção:")
    print(problemas.to_string(index=False))
else:
    print("\nTodos os arquivos passaram nas verificações estruturais.")

print(f"\nRelatório salvo em: {caminho}")
print(
    "\nObservação: valores ausentes em casos_est ou casos são "
    "reportados, mas não classificados automaticamente como erro."
)
