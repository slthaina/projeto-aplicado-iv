
from pathlib import Path
import pandas as pd

PASTA_RAW = Path("data/raw")
PASTA_PROCESSED = Path("data/processed")

PASTA_PROCESSED.mkdir(parents=True, exist_ok=True)

arquivos = sorted(PASTA_RAW.glob("*.csv"))
total = 0

for arquivo in arquivos:
    dados = pd.read_csv(arquivo)

    # Identifica o ano pelo nome do arquivo.
    ano = int(arquivo.stem.rsplit("_", 1)[1])

    dados["data_iniSE"] = pd.to_datetime(
        dados["data_iniSE"], errors="coerce"
    )

    # Mantém somente registros do ano indicado no arquivo.
    dados = dados[dados["data_iniSE"].dt.year == ano].copy()

    # Ordena os registros cronologicamente.
    dados = dados.sort_values("data_iniSE")

    destino = PASTA_PROCESSED / arquivo.name
    dados.to_csv(destino, index=False, date_format="%Y-%m-%d")

    print(f"{arquivo.name}: {len(dados)} registros processados")
    total += 1

print(f"\nProcessamento concluído: {total} arquivos.")
print(f"Arquivos salvos em: {PASTA_PROCESSED.resolve()}")
