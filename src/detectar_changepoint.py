import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import STL
import ruptures as rpt
import os

def detectar_changepoint_pelt():
    print("Carregando base de dados integrada...")
    df = pd.read_csv("data/processed/epidemio_clima_semanal.csv")
    
    # Ordenar por Semana Epidemiológica
    df = df.sort_values("SE").reset_index(drop=True)
    
    # Agrupar a soma dos casos por semana para ter a série global dos municípios
    doencas = ['dengue', 'zika', 'chikungunya']
    
    os.makedirs("data/processed", exist_ok=True)
    
    for doenca in doencas:
        col_casos = f'casos_est_{doenca}'
        if col_casos not in df.columns:
            continue
            
        # Criar série agregada no tempo
        serie_temporal = df.groupby('SE')[col_casos].sum().reset_index()
        
        # Preencher eventuais NaNs com 0 para a decomposição
        y = serie_temporal[col_casos].fillna(0).values
        
        if len(y) < 104 or np.sum(y) == 0:  # Necessário pelo menos 2 anos de dados
            print(f"Série de {doenca} insuficiente para decomposição STL/PELT.")
            continue
            
        print(f"\n--- Processando {doenca.upper()} ---")
        
        # 1. Decomposição STL (período de 52 semanas para capturar o ciclo anual)
        stl = STL(y, period=52, robust=True)
        res = stl.fit()
        
        # Serie dessazonalizada = Tendência + Resíduo (ou apenas Tendência)
        tendencia = res.trend
        
        # 2. Algoritmo PELT (modelo 'rbf' para mudanças em média/variância)
        # pen (penalidade): controla a sensibilidade a novas quebras
        algo = rpt.Pelt(model="rbf", min_size=26).fit(tendencia)
        pontos_mudanca = algo.predict(pen=10)
        
        # Mapear os índices dos pontos para as Semanas Epidemiológicas (SE)
        semanas_mudanca = [serie_temporal['SE'].iloc[idx-1] for idx in pontos_mudanca if idx < len(serie_temporal)]
        
        print(f"Pontos de mudança detectados (SE): {semanas_mudanca}")
        
        # 3. Plotar resultado
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8), sharex=True)
        
        # Gráfico 1: Série Original de Casos
        ax1.plot(serie_temporal['SE'].astype(str), y, label=f'Casos Estimados ({doenca})', color='black', alpha=0.6)
        ax1.set_ylabel('Nº de Casos', fontweight='bold')
        ax1.set_title(f'Detecção de Changepoint (PELT) - {doenca.capitalize()}', fontsize=14, fontweight='bold')
        ax1.grid(True, linestyle='--', alpha=0.5)
        ax1.legend(loc='upper left')
        
        # Gráfico 2: Componente de Tendência Dessazonalizada + Pontos de Ruptura
        ax2.plot(serie_temporal['SE'].astype(str), tendencia, label='Tendência (Dessazonalizada - STL)', color='blue', linewidth=2)
        
        # Desenhar linhas verticais para cada ponto de ruptura encontrado
        for idx in pontos_mudanca[:-1]:  # Ignora o último elemento que é o tamanho total da série
            se_rotulo = serie_temporal['SE'].iloc[idx-1]
            ax1.axvline(x=idx-1, color='red', linestyle='--', linewidth=1.5)
            ax2.axvline(x=idx-1, color='red', linestyle='--', linewidth=1.5, label='Changepoint' if idx == pontos_mudanca[0] else "")
            
        ax2.set_ylabel('Tendência Dessazonalizada', fontweight='bold')
        ax2.set_xlabel('Semana Epidemiológica (SE)', fontweight='bold')
        ax2.grid(True, linestyle='--', alpha=0.5)
        ax2.legend(loc='upper left')
        
        # Reduzir quantidade de rótulos no eixo X para legibilidade
        passo_ticks = max(1, len(serie_temporal) // 10)
        plt.xticks(ticks=range(0, len(serie_temporal), passo_ticks), 
                   labels=serie_temporal['SE'].astype(str).iloc[::passo_ticks], 
                   rotation=45)
        
        caminho_grafico = f"data/processed/changepoint_{doenca}.png"
        plt.savefig(caminho_grafico, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Gráfico salvo em: {caminho_grafico}")

if __name__ == "__main__":
    detectar_changepoint_pelt()