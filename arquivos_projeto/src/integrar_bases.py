import pandas as pd
import glob
import os

def integrar_dados():
    # Listar arquivos epidemiológicos
    path_dengue = "data/raw/epidemio/dengue/*.csv"
    
    # 1. Carregar base de Dengue (Casos + Clima Oficial)
    dfs_d = []
    for f in glob.glob(path_dengue):
        df = pd.read_csv(f)
        # Extrai o geocódigo do nome do arquivo (ex: "2611606_Recife..." -> "2611606")
        geocode = os.path.basename(f).split('_')[0]
        df['municipio_geocodigo'] = geocode
        dfs_d.append(df)
        
    if not dfs_d:
        print("Erro: Nenhum arquivo encontrado em data/raw/epidemio/dengue/")
        return
        
    dengue = pd.concat(dfs_d, ignore_index=True)
    
    # Colunas climáticas do InfoDengue
    cols_clima = ["SE", "municipio_geocodigo", "tempmin", "tempmed", "tempmax", "umidmin", "umidmed", "umidmax"]
    
    # Colunas base e métricas de casos
    cols_base_casos = ["SE", "municipio_geocodigo"]
    cols_metricas = ["casos_est", "casos", "notif_ev"]
    
    # Garante que só vai tentar puxar as colunas que realmente existem no CSV
    cols_dengue_casos = cols_base_casos + [c for c in cols_metricas if c in dengue.columns]
    
    # Isolar Clima da Dengue
    clima = dengue[cols_clima].drop_duplicates(subset=["SE", "municipio_geocodigo"])
    
    # Extrair Casos de Dengue e renomear colunas
    renames_d = {c: f"{c}_dengue" for c in cols_metricas}
    dengue_casos = dengue[cols_dengue_casos].rename(columns=renames_d)
    
    # 2. Funcoes auxiliares para Zika e Chikungunya
    def carregar_casos_outras(doenca):
        files = glob.glob(f"data/raw/epidemio/{doenca}/*.csv")
        if not files:
            return pd.DataFrame()
        dfs = []
        for f in files:
            df = pd.read_csv(f)
            df['municipio_geocodigo'] = os.path.basename(f).split('_')[0]
            dfs.append(df)
        df_all = pd.concat(dfs, ignore_index=True)
        
        # Filtra apenas as colunas que existem
        cols_atuais = cols_base_casos + [c for c in cols_metricas if c in df_all.columns]
        renames = {c: f"{c}_{doenca}" for c in cols_metricas}
        return df_all[cols_atuais].rename(columns=renames)
    
    zika_casos = carregar_casos_outras("zika")
    chik_casos = carregar_casos_outras("chikungunya")
    
    # 3. Merge Final
    # Junta Dengue + Clima
    base = pd.merge(dengue_casos, clima, on=["SE", "municipio_geocodigo"], how="outer")
    
    # Junta Zika e Chikungunya se existirem
    if not zika_casos.empty:
        base = pd.merge(base, zika_casos, on=["SE", "municipio_geocodigo"], how="left")
    if not chik_casos.empty:
        base = pd.merge(base, chik_casos, on=["SE", "municipio_geocodigo"], how="left")
        
    os.makedirs("data/processed", exist_ok=True)
    caminho_saida = "data/processed/epidemio_clima_semanal.csv"
    base.to_csv(caminho_saida, index=False)
    
    print(f"Sucesso! Base integrada com {len(base)} linhas salva em: {caminho_saida}")

if __name__ == "__main__":
    integrar_dados()