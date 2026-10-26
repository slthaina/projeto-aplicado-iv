import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analisar_lags():
    print("Carregando base de dados integrada...")
    df = pd.read_csv("data/processed/epidemio_clima_semanal.csv")
    
    # Ordenar chronologicamente por município e SE
    df = df.sort_values(["municipio_geocodigo", "SE"]).reset_index(drop=True)
    
    # Criar lags de 0 a 8 semanas para variáveis climáticas principais
    max_lags = 8
    variaveis_clima = ['tempmed', 'tempmin', 'umidmed']
    doencas = ['dengue', 'zika', 'chikungunya']
    
    print("Gerando colunas de defasagem (lags) para temperatura e humidade...")
    for var in variaveis_clima:
        for lag in range(1, max_lags + 1):
            df[f'{var}_lag_{lag}'] = df.groupby('municipio_geocodigo')[var].shift(lag)
            
    # Salvar a base atualizada com os lags para a etapa preditiva futura
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/epidemio_clima_lags.csv", index=False)
    print("Base com lags salva em: data/processed/epidemio_clima_lags.csv")
    
    # Calcular a correlação cruzada entre casos e lags climáticos
    resultados_corr = []
    
    for doenca in doencas:
        col_casos = f'casos_est_{doenca}'
        if col_casos not in df.columns:
            continue
            
        for var in variaveis_clima:
            # Lag 0 (mesma semana)
            corr_lag0 = df[col_casos].corr(df[var])
            resultados_corr.append({
                'doenca': doenca,
                'variavel_clima': var,
                'lag_semanas': 0,
                'correlacao': corr_lag0
            })
            
            # Lags 1 a 8
            for lag in range(1, max_lags + 1):
                col_lag = f'{var}_lag_{lag}'
                corr = df[col_casos].corr(df[col_lag])
                resultados_corr.append({
                    'doenca': doenca,
                    'variavel_clima': var,
                    'lag_semanas': lag,
                    'correlacao': corr
                })
                
    df_corr = pd.DataFrame(resultados_corr)
    df_corr.to_csv("data/processed/correlacao_lags_clima.csv", index=False)
    print("Matriz de correlação salva em: data/processed/correlacao_lags_clima.csv")
    
    # Plotar o gráfico de lags para Temperatura Média
    print("Gerando gráfico de correlação por defasagem...")
    fig, ax = plt.subplots(figsize=(10, 6))
    
    df_tempmed = df_corr[df_corr['variavel_clima'] == 'tempmed']
    
    for doenca in doencas:
        dados_d = df_tempmed[df_tempmed['doenca'] == doenca]
        if not dados_d.empty:
            ax.plot(dados_d['lag_semanas'], dados_d['correlacao'], marker='o', linewidth=2, label=doenca.capitalize())
            
    ax.set_title('Correlação Cruzada: Temperatura Média vs Casos Estimados (por Lag)', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Defasagem / Lag em Semanas (0 = Mesma semana)', fontweight='bold')
    ax.set_ylabel('Coeficiente de Correlação de Pearson', fontweight='bold')
    ax.set_xticks(range(0, max_lags + 1))
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(loc='upper right')
    
    caminho_grafico = "data/processed/grafico_lags_clima.png"
    plt.savefig(caminho_grafico, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Gráfico de lags salvo em: {caminho_grafico}")

if __name__ == "__main__":
    analisar_lags()