import pandas as pd
from pathlib import Path

base = Path("data/raw/epidemio")
clima = ["tempmin", "tempmed", "tempmax", "umidmin", "umidmed", "umidmax"]

print("=== 1. Semanas sem tempmed e o que tempmin mostra nelas ===")
for f in sorted((base / "dengue").glob("*.csv")):
    d = pd.read_csv(f)
    vaz = d[d["tempmed"].isna()]
    if len(vaz):
        print(f.name, "| SE vazias:", vaz["SE"].tolist()[:6], "...",
              "| tempmin nessas semanas:", vaz["tempmin"].round(1).tolist()[:6])

print("\n=== 2. Valores extremos de tempmed (<8 ou >32) ===")
for f in sorted((base / "dengue").glob("*.csv")):
    d = pd.read_csv(f)
    ext = d[(d["tempmed"] < 8) | (d["tempmed"] > 32)]
    if len(ext):
        print(f.name, ext[["SE", "tempmin", "tempmed", "tempmax"]].round(1).to_string(index=False))

print("\n=== 3. Clima igual nas três doenças? ===")
for f in sorted((base / "dengue").glob("*.csv")):
    ref = pd.read_csv(f)[["SE"] + clima]
    for doenca in ["chikungunya", "zika"]:
        outro = pd.read_csv(base / doenca / f.name.replace("dengue", doenca))[["SE"] + clima]
        m = ref.merge(outro, on="SE", suffixes=("", "_o"))
        difer = sum(((m[c] != m[c + "_o"]) & ~(m[c].isna() & m[c + "_o"].isna())).sum() for c in clima)
        if difer:
            print(f.name, "vs", doenca, "-> valores diferentes:", int(difer))
print("Fim (se a seção 3 não listou nada, o clima é igual nas três doenças).")