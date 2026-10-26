import pandas as pd

d = pd.read_csv("data/raw/epidemio/dengue/2611606_Recife_PE_dengue_2020_2024.csv")
z = pd.read_csv("data/raw/epidemio/zika/2611606_Recife_PE_zika_2020_2024.csv")
cols = ["SE", "tempmin", "tempmed", "tempmax", "umidmin", "umidmed", "umidmax", "versao_modelo"]
m = d[cols].merge(z[cols], on="SE", suffixes=("_dengue", "_zika"))
dif = m[(m["tempmed_dengue"] != m["tempmed_zika"]) &
        ~(m["tempmed_dengue"].isna() & m["tempmed_zika"].isna())]
print("Semanas com tempmed diferente:", len(dif), "de", len(m))
print(dif[["SE", "tempmed_dengue", "tempmed_zika", "versao_modelo_dengue", "versao_modelo_zika"]]
      .head(15).to_string(index=False))
print("\nPrimeira e última SE diferente:", dif["SE"].min(), dif["SE"].max())