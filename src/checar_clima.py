import pandas as pd
from pathlib import Path

arquivos = sorted(Path("data/raw/epidemio/dengue").glob("*.csv"))
print("Colunas:", pd.read_csv(arquivos[0]).columns.tolist(), "\n")

clima = ["tempmin", "tempmed", "tempmax", "umidmin", "umidmed", "umidmax", "precipitacao"]
for f in arquivos:
    d = pd.read_csv(f)
    cols = [c for c in clima if c in d.columns]
    vazios = {c: int(d[c].isna().sum()) for c in cols}
    print(f.name, "| vazios:", vazios,
          "| tempmed:", round(d["tempmed"].min(), 1), "a", round(d["tempmed"].max(), 1))