import pandas as pd
from pathlib import Path

for f in sorted(Path("data/raw/epidemio").glob("*/*.csv")):
    d = pd.read_csv(f)
    print(f.name, "| linhas:", len(d), "| SE:", d["SE"].min(), "a", d["SE"].max(),
          "| casos=0:", (d["casos"] == 0).sum(), "| casos vazios:", d["casos"].isna().sum())