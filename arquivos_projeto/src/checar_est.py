import pandas as pd
from pathlib import Path

for f in sorted(Path("data/raw/epidemio").glob("*/*.csv")):
    d = pd.read_csv(f)
    print(f.name, "| casos_est=0:", (d["casos_est"] == 0).sum(),
          "| soma casos:", int(d["casos"].sum()), "| soma casos_est:", round(d["casos_est"].sum()))