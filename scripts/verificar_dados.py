
from pathlib import Path
import pandas as pd

# Pastas do projeto
BASE_DIR = Path(__file__).resolve().parent.parent
PASTA_DADOS = BASE_DIR / "data" / "processed"
PASTA_RELATORIOS = BASE_DIR / "reports"

PASTA_RELATORIOS.mkdir(parents=True, exist_ok=True)

resultados = []

arquivos = sorted(PASTA_DADOS.glob("*.csv"))

if not arquivos:
    raise FileNotFoundError(
        f"Nenhum CSV encontrado em {PASTA_DADOS}"
    )

for arquivo in arquivos:
    df = pd.read_csv(arquivo)

    # Identifica o ano esperado pelo nome do arquivo
    partes = arquivo.stem.split("_")
    ano_esperado = int(partes[-1])

    if "data_iniSE" not in df.columns:
        print(f"Coluna data_iniSE ausente: {arquivo.name}")
        continue

    datas = pd.to_datetime(
        df["data_iniSE"], errors="coerce"
    )

    datas_validas = datas.dropna()
    datas_no_ano = datas_validas[
        datas_validas.dt.year == ano_esperado
    ]

    semanas = (
        df.loc[datas.notna(), "SE"]
        if "SE" in df.columns
        else pd.Series(dtype="float64")
    )

    semanas_duplicadas = int(semanas.duplicated().sum())

    resultados.append({
        "arquivo": arquivo.name,
        "status": "OK",
        "registros": len(df),
        "datas_invalidas": int(datas.isna().sum()),
        "datas_fora_do_ano": int(
            (datas_validas.dt.year != ano_esperado).sum()
        ),
        "datas_duplicadas": int(
            datas_validas.duplicated().sum()
        ),
        "semanas_duplicadas": semanas_duplicadas,
        "casos_est_ausentes": (
            int(df["casos_est"].isna().sum())
            if "casos_est" in df.columns else None
        ),
        "casos_ausentes": (
            int(df["casos"].isna().sum())
            if "casos" in df.columns else None
        ),
        "primeira_data": (
            datas_validas.min().date()
            if not datas_validas.empty else None
        ),
        "ultima_data": (
            datas_validas.max().date()
            if not datas_validas.empty else None
        ),
        "datas_unicas_no_ano": int(
            datas_no_ano.nunique()
        ),
    })

relatorio = pd.DataFrame(resultados)

# Marca problemas objetivos para conferência
colunas_problema = [
    "datas_invalidas",
    "datas_fora_do_ano",
    "datas_duplicadas",
    "semanas_duplicadas",
]

for coluna in colunas_problema:
    relatorio.loc[
        relatorio[coluna] > 0, "status"
    ] = "VERIFICAR"

caminho_saida = (
    PASTA_RELATORIOS / "validacao_dados.csv"
)

relatorio.to_csv(caminho_saida, index=False)

print(f"Arquivos encontrados: {len(arquivos)}")
print(f"Arquivos verificados: {len(relatorio)}")
print("\nResumo dos status:")

print(relatorio["status"].value_counts())

print("\nRelatório completo:")
print(relatorio.to_string(index=False))

print(f"\nRelatório salvo em: {caminho_saida}")
