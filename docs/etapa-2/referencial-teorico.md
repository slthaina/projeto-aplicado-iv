# Etapa 2 — Referencial Teórico

# Referencial Teórico

## Arboviroses, clima e dados epidemiológicos

Dengue, zika e chikungunya compartilham o vetor *Aedes aegypti*, cuja biologia e capacidade de transmissão dependem da temperatura. Modelos mecanísticos indicam que a adequação térmica à transmissão é não linear e difere entre os três vírus (MORDECAI et al., 2017; 2019), e projeções globais sugerem redistribuição do risco sob mudanças climáticas (RYAN et al., 2019). Esses resultados vêm de dados laboratoriais e de simulação. Verificar se eles aparecem em séries de vigilância de campo, município a município e ao longo de mais de uma década, é a lacuna que este projeto aborda.

Os dados epidemiológicos vêm do InfoDengue, que integra notificações e variáveis climáticas por município e semana epidemiológica e usa *nowcasting* para corrigir o atraso de notificação (CODEÇO et al., 2016; 2018). Abordagens bayesianas de correção de atraso, como a de Bastos et al. (2019), sustentam esse tipo de estimativa. Por isso, a variável de casos estimados é tratada como estimativa dinâmica, sujeita a revisão retrospectiva.

## Abordagens para análise das séries temporais

Na literatura recente, diversas abordagens buscam mapear essas dinâmicas, frequentemente utilizando a modelagem da dengue como base metodológica para as demais arboviroses. Lowe et al. (2021), por exemplo, modelaram, em microrregiões brasileiras, o efeito combinado de eventos hidrometeorológicos extremos e urbanização sobre o risco de dengue. A vantagem é a estrutura espaço-temporal com covariáveis. A limitação, para os fins deste projeto, é o foco no risco agregado, sem caracterizar mudanças na sazonalidade de cada doença. Cazelles et al. (2005) usaram análise de *wavelets* para mostrar que a relação entre clima e dengue é não estacionária. O método capta variações de frequência ao longo do tempo, mas seus resultados são menos diretos de traduzir em indicadores de temporada (início, duração, intensidade). Para analisar os efeitos do clima que podem aparecer com atraso, os modelos de defasagem distribuída não lineares (DLNM) permitem representar simultaneamente relações não lineares entre exposição e resposta e os efeitos ao longo das semanas seguintes (GASPARRINI; ARMSTRONG; KENWARD, 2010). Neste projeto, são utilizadas defasagens de 0 a 4 semanas, podendo chegar a 8–12, buscando uma análise mais simples e direta da relação entre clima e casos.

Para analisar as mudanças ao longo do tempo, o projeto utiliza a decomposição STL, que separa tendência, sazonalidade e resíduo e pode ser robusta a valores extremos (CLEVELAND et al., 1990). Essa etapa ajuda a diferenciar a sazonalidade esperada de possíveis mudanças na série. Entre os métodos de detecção de mudanças, o PELT permite identificar alterações com eficiência computacional, mas seus resultados dependem da função de custo e da penalização utilizadas (KILLICK; FEARNHEAD; ECKLEY, 2012; TRUONG; OUDRE; VAYATIS, 2020).

## Modelagem preditiva

No escopo da modelagem preditiva, diferentes algoritmos apresentam vantagens e restrições metodológicas. O modelo SARIMAX, por exemplo, incorpora variáveis exógenas e é interpretável, mas pressupõe relações lineares (HYNDMAN; ATHANASOPOULOS, 2021). Já o XGBoost captura não linearidades e interações entre casos defasados e clima (CHEN; GUESTRIN, 2016), com menor interpretabilidade e maior demanda de engenharia de atributos. Modelos de aprendizado profundo, como LSTM, foram descartados para manter a metodologia enxuta e interpretável, visto que abordagens tradicionais e de *machine learning* frequentemente apresentam desempenho competitivo em séries temporais com menor exigência paramétrica (MAKRIDAKIS; SPILIOTIS; ASSIMAKOPOULOS, 2018). Em previsão de arboviroses, Johansson et al. (2019) mostram o valor de avaliações padronizadas entre modelos, o que fundamenta a validação em janela expansiva adotada aqui.

## Referências

BASTOS, L. S. et al. A modelling approach for correcting reporting delays in disease surveillance data. *Statistics in Medicine*, v. 38, n. 22, p. 4363-4377, 2019.

CAZELLES, B. et al. Nonstationary influence of El Niño on the synchronous dengue epidemics in Thailand. *PLoS Medicine*, v. 2, n. 4, e106, 2005.

CHEN, T.; GUESTRIN, C. XGBoost: a scalable tree boosting system. In: *PROCEEDINGS OF THE 22ND ACM SIGKDD INTERNATIONAL CONFERENCE ON KNOWLEDGE DISCOVERY AND DATA MINING*, 2016. p. 785-794.

CLEVELAND, R. B.; CLEVELAND, W. S.; MCRAE, J. E.; TERPENNING, I. STL: a seasonal-trend decomposition procedure based on loess. *Journal of Official Statistics*, v. 6, n. 1, p. 3-73, 1990.

CODEÇO, C. T. et al. InfoDengue: a nowcasting system for the surveillance of dengue fever transmission. *bioRxiv*, 2016. Disponível em: https://www.biorxiv.org/content/10.1101/046193. Acesso em: 25 ago. 2026.

CODEÇO, C.; COELHO, F. C.; CRUZ, O. G.; OLIVEIRA, S. B.; CASTRO, T. G.; BASTOS, L. S. InfoDengue: a nowcasting system for the surveillance of arboviruses in Brazil. *Revue d'Épidémiologie et de Santé Publique*, v. 66, supl. 5, p. S386, out. 2018. Disponível em: https://doi.org/10.1016/j.respe.2018.05.408. Acesso em: 25 ago. 2026.

GASPARRINI, A.; ARMSTRONG, B.; KENWARD, M. G. Distributed lag non-linear models. *Statistics in Medicine*, v. 29, n. 21, p. 2224-2234, 2010.

HYNDMAN, R. J.; ATHANASOPOULOS, G. *Forecasting: principles and practice*. 3. ed. Melbourne: OTexts, 2021. Disponível em: https://otexts.com/fpp3/. Acesso em: 25 ago. 2026.

JOHANSSON, M. A. et al. An open challenge to advance probabilistic forecasting for dengue epidemics. *PNAS*, v. 116, n. 48, p. 24268-24274, 2019.

KILLICK, R.; FEARNHEAD, P.; ECKLEY, I. A. Optimal detection of changepoints with a linear computational cost. *Journal of the American Statistical Association*, v. 107, n. 500, p. 1590-1598, 2012.

LOWE, R. et al. Combined effects of hydrometeorological hazards and urbanisation on dengue risk in Brazil: a spatiotemporal modelling study. *The Lancet Planetary Health*, v. 5, n. 4, p. e209-e219, 2021.

MAKRIDAKIS, S.; SPILIOTIS, E.; ASSIMAKOPOULOS, V. Statistical and Machine Learning forecasting methods: Concerns and ways forward. *PLoS ONE*, v. 13, n. 3, e0194889, 2018.

MORDECAI, E. A.; COHEN, J. M.; EVANS, M. V.; GUDAPATI, P.; JOHNSON, L. R.; LIPPI, C. A. et al. Detecting the impact of temperature on transmission of Zika, dengue, and chikungunya using mechanistic models. *PLOS Neglected Tropical Diseases*, v. 11, n. 4, e0005568, 2017. Disponível em: https://doi.org/10.1371/journal.pntd.0005568. Acesso em: 25 ago. 2026.

MORDECAI, E. A. et al. Thermal biology of mosquito-borne disease. *Ecology Letters*, v. 22, n. 10, p. 1690-1708, 2019.

RYAN, S. J. et al. Global expansion and redistribution of Aedes-borne virus transmission risk with climate change. *PLOS Neglected Tropical Diseases*, v. 13, n. 3, e0007213, 2019.

TRUONG, C.; OUDRE, L.; VAYATIS, N. Selective review of offline change point detection methods. *Signal Processing*, v. 167, 107299, 2020.
