import pandas as pd
import numpy as np
import os

def calcular_indicadores_temporada():
    print("Carregando base de dados integrada...")
    df = pd.read_csv("data/processed/epidemio_clima_semanal.csv")

    # Extrair Ano e Semana Epidemiológica da coluna SE
    df['ano'] = df['SE'].astype(str).str[:4].astype(int)
    df['semana_do_ano'] = df['SE'].astype(str).str[-2:].astype(int)

    # Função de classificação de períodos
    def classificar_periodo(ano):
        if 2010 <= ano <= 2014: return '2010-2014'
        elif 2015 <= ano <= 2019: return '2015-2019'
        elif 2020 <= ano <= 2024: return '2020-2024'
        return None

    df['periodo'] = df['ano'].apply(classificar_periodo)
    df = df.dropna(subset=['periodo'])

    doencas = ['dengue', 'zika', 'chikungunya']
    municipios = df['municipio_geocodigo'].unique()
    resultados = []

    for muni in municipios:
        df_muni = df[df['municipio_geocodigo'] == muni]
        
        for doenca in doencas:
            col_casos = f'casos_est_{doenca}'
            if col_casos not in df_muni.columns:
                continue

            # 1. Limiar: Percentil 75 histórico do município para a doença
            limiar_p75 = df_muni[col_casos].quantile(0.75)

            for (periodo, ano), grupo in df_muni.groupby(['periodo', 'ano']):
                grupo = grupo.sort_values('semana_do_ano')
                casos = grupo[col_casos].values
                semanas = grupo['semana_do_ano'].values

                if len(casos) == 0 or np.isnan(casos).all() or np.sum(casos) == 0:
                    continue

                # Indicador 2: Pico
                idx_pico = np.argmax(casos)
                semana_pico = semanas[idx_pico]
                valor_pico = casos[idx_pico]

                # Condição de estar acima do limiar
                acima_limiar = casos > limiar_p75

                # Indicador 1: Início (primeira semana com 2+ semanas consecutivas acima do P75)
                semana_inicio = np.nan
                for k in range(len(acima_limiar) - 1):
                    if acima_limiar[k] and acima_limiar[k + 1]:
                        semana_inicio = semanas[k]
                        break

                # Indicador 3: Fim (última semana acima do P75)
                indices_acima = np.where(acima_limiar)[0]
                semana_fim = semanas[indices_acima[-1]] if len(indices_acima) > 0 else np.nan

                # Indicador 4: Duração em semanas
                duracao = (semana_fim - semana_inicio + 1) if (not np.isnan(semana_inicio) and not np.isnan(semana_fim) and semana_fim >= semana_inicio) else np.nan

                # Indicador 5: Intensidade (Casos Acumulados no Ano)
                intensidade_acumulada = np.sum(casos)

                resultados.append({
                    'municipio_geocodigo': muni,
                    'doenca': doenca,
                    'periodo': periodo,
                    'ano': ano,
                    'limiar_p75_historico': round(limiar_p75, 2),
                    'semana_inicio': semana_inicio,
                    'semana_pico': semana_pico,
                    'valor_pico': round(valor_pico, 1),
                    'semana_fim': semana_fim,
                    'duracao_semanas': duracao,
                    'intensidade_acumulada': round(intensidade_acumulada, 1)
                })

    df_res = pd.DataFrame(resultados)
    
    # Salvar resultados detalhados por ano
    caminho_saida = "data/processed/indicadores_sazonalidade.csv"
    os.makedirs("data/processed", exist_ok=True)
    df_res.to_csv(caminho_saida, index=False)
    print(f"Indicadores anuais salvos em: {caminho_saida}")

    # Resumo consolidado por Período (Média dos indicadores)
    resumo_periodos = df_res.groupby(['doenca', 'periodo'])[[
        'semana_inicio', 'semana_pico', 'duracao_semanas', 'intensidade_acumulada'
    ]].mean().round(1)
    
    print("\n=== RESUMO MÉDIO DOS INDICADORES POR PERÍODO ===")
    print(resumo_periodos.to_string())

if __name__ == "__main__":
    calcular_indicadores_temporada()