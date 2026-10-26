import pandas as pd
import matplotlib.pyplot as plt

def plotar_sazonalidade_periodos():
    print("Carregando base de dados integrada...")
    df = pd.read_csv("data/processed/epidemio_clima_semanal.csv")

    # Extrair o ano e a semana do ano a partir do código SE (ex: 202045 -> Ano 2020, Semana 45)
    df['ano'] = df['SE'].astype(str).str[:4].astype(int)
    df['semana_do_ano'] = df['SE'].astype(str).str[-2:].astype(int)

    # Função para classificar as linhas nos três períodos de interesse
    def classificar_periodo(ano):
        if 2010 <= ano <= 2014: return '2010-2014'
        elif 2015 <= ano <= 2019: return '2015-2019'
        elif 2020 <= ano <= 2024: return '2020-2024'
        return None

    df['periodo'] = df['ano'].apply(classificar_periodo)
    df = df.dropna(subset=['periodo']) # Remove anos fora do escopo

    periodos = ['2010-2014', '2015-2019', '2020-2024']
    
    # Criar uma figura com 3 gráficos empilhados (3 linhas, 1 coluna)
    print("Gerando os gráficos segmentados...")
    fig, axes = plt.subplots(3, 1, figsize=(12, 16), sharex=True)
    cols_agrupar = ['casos_est_dengue', 'casos_est_zika', 'casos_est_chikungunya', 'tempmed']

    for i, p in enumerate(periodos):
        df_p = df[df['periodo'] == p]
        sazonalidade = df_p.groupby('semana_do_ano')[cols_agrupar].mean().reset_index()
        
        ax1 = axes[i]
        
        # Eixo esquerdo: Casos
        ax1.plot(sazonalidade['semana_do_ano'], sazonalidade['casos_est_dengue'], label='Dengue', color='#d62728', linewidth=2)
        ax1.plot(sazonalidade['semana_do_ano'], sazonalidade['casos_est_zika'], label='Zika', color='#1f77b4', linewidth=2)
        ax1.plot(sazonalidade['semana_do_ano'], sazonalidade['casos_est_chikungunya'], label='Chikungunya', color='#ff7f0e', linewidth=2)
        ax1.set_ylabel(f'Média de Casos\n({p})', fontweight='bold')
        ax1.grid(True, linestyle='--', alpha=0.5)
        
        # Posicionar legenda de casos apenas no primeiro gráfico para evitar poluição visual
        if i == 0:
            ax1.legend(loc='upper left')
        
        # Eixo direito: Temperatura
        ax2 = ax1.twinx()
        ax2.plot(sazonalidade['semana_do_ano'], sazonalidade['tempmed'], label='Temp. Média (°C)', color='#7f7f7f', linestyle='dashed', linewidth=2)
        ax2.set_ylabel('Temp. Média (°C)', fontweight='bold', color='#7f7f7f')
        ax2.tick_params(axis='y', labelcolor='#7f7f7f')
        
        if i == 0:
            ax2.legend(loc='upper right')

    # Ajustes finais no layout
    axes[-1].set_xlabel('Semana Epidemiológica do Ano (1 a 53)', fontweight='bold')
    plt.suptitle('Sazonalidade: Comportamento Médio de Arboviroses vs Temperatura', fontsize=16, y=0.92, fontweight='bold')
    
    # Salvar a imagem
    caminho_saida = "data/processed/grafico_sazonalidade_periodos.png"
    plt.savefig(caminho_saida, dpi=300, bbox_inches='tight')
    print(f"Sucesso! Gráfico salvo em: {caminho_saida}")

if __name__ == "__main__":
    plotar_sazonalidade_periodos()