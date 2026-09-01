# O clima já está deixando uma marca? Detectando mudanças na dinâmica temporal de arboviroses e sua associação com variáveis climáticas em municípios brasileiros

**Projeto Aplicado IV — Tecnologia em Ciência de Dados — 2026.2**

Professor Gustavo Scalabrini Sampaio

**ODS relacionada:** ODS 11 — Cidades e Comunidades Sustentáveis

---

## Autoria e desenvolvimento

| Nome          | Matrícula     | Função no projeto |
| ---------------------------- | ------------- | ----------------- |
| *Thainá Silva Leite*         | *10730503* | *Coordenação e desenvolvimento integral do projeto: pesquisa, coleta e tratamento de dados, análise, modelagem, desenvolvimento do produto, documentação e apresentação.*     |

---

# 1. Introdução

## 1.1 Contexto

Em 2024, a dengue alcançou níveis elevados de ocorrência em escala global: segundo o relatório *Dengue: global situation, surveillance and progress – 2024 update*, publicado pela Organização Mundial da Saúde (OMS, 2025), foram notificados 14.434.584 casos em todas as seis regiões da organização, o maior volume de casos notificados já registrado pela OMS em um único ano. O Brasil concentrou a maior parte desse total, com mais de 10 milhões de casos notificados e 6.321 óbitos registrados, constituindo o país com o maior número de casos notificados de dengue em 2024 (OMS, 2025). O Brasil concentra, portanto, uma parcela expressiva da carga global de casos notificados de dengue e apresenta, adicionalmente, importante circulação de outras arboviroses urbanas transmitidas pelo mesmo vetor, como chikungunya e zika.

Dengue, zika e chikungunya compartilham o vetor urbano *Aedes aegypti* (Diptera: Culicidae), mas são causadas por patógenos distintos. Estudos mecanísticos indicam que a temperatura exerce influência sobre o potencial de transmissão dos diferentes sistemas *Aedes*-vírus, com respostas térmicas que podem apresentar faixas distintas de maior adequação à transmissão dos patógenos (MORDECAI et al., 2017). Se os padrões identificados a partir de modelos mecanísticos e dados laboratoriais também se refletem nos dados de vigilância de campo ao longo de mais de uma década permanece uma questão pouco explorada. Essa lacuna motiva a investigação da dinâmica temporal dessas arboviroses e de sua associação com as condições climáticas observadas nos municípios brasileiros.

Há indícios preliminares de mudanças na distribuição espacial da ocorrência notificada dessas doenças no Brasil: indicadores do próprio sistema InfoDengue já registraram aumento da atividade epidemiológica da dengue em latitudes mais altas, incluindo a região Sul do país (FIOCRUZ, 2022). Essa evidência observacional indica uma mudança na distribuição geográfica dos casos notificados, mas não permite, isoladamente, estabelecer uma relação causal com o clima. Esse tipo de evidência motiva a investigação sistemática, em série temporal, de como o padrão sazonal de cada arbovirose se comporta ao longo dos anos e se variações nesse padrão apresentam associação temporal com a variação das condições climáticas nos mesmos municípios.

Este projeto está inserido na interseção entre Entomologia, Ecologia de Vetores, Climatologia, Epidemiologia e Ciência de Dados, com foco na análise de séries temporais de dengue, zika e chikungunya, buscando caracterizar mudanças na dinâmica epidemiológica dessas arboviroses e investigar sua associação com a variação temporal das condições climáticas.

## 1.2 Motivação

O InfoDengue constitui uma importante fonte de dados para o monitoramento das arboviroses no Brasil, reunindo informações epidemiológicas e ambientais por município e semana epidemiológica. A plataforma utiliza técnicas de *nowcasting* para estimar casos ainda não registrados no sistema de notificação, permitindo acompanhar a evolução temporal de dengue, chikungunya e zika (INFO DENGUE, 2026).

A extensão da série histórica possibilita investigar padrões que não seriam identificados em períodos mais curtos, como mudanças na sazonalidade, na intensidade e no período de ocorrência das arboviroses. Como a variável `casos_est` corresponde a estimativas produzidas pelo *nowcasting* e pode ser revisada retrospectivamente à medida que novas notificações são incorporadas, esses valores serão tratados como estimativas dinâmicas da incidência, e não como contagens observacionais definitivas (INFO DENGUE, 2026).

Do ponto de vista da gestão pública, identificar mudanças nos padrões temporais das arboviroses pode contribuir para o planejamento das ações de vigilância e prevenção, especialmente em municípios nos quais a dinâmica epidemiológica vem se modificando ao longo do tempo.

---

## 1.3 Perguntas de pesquisa

O projeto é organizado em torno de duas perguntas de pesquisa:

**RQ1 (núcleo científico).** Os municípios selecionados apresentam mudanças no início, na duração ou na intensidade das temporadas de dengue, zika e chikungunya ao longo da série histórica disponível?

**RQ2 (relação com o clima).** As mudanças identificadas na dinâmica temporal das arboviroses apresentam associação com a variação temporal das condições climáticas locais?

As análises propostas investigam associações entre a dinâmica epidemiológica das arboviroses e as condições climáticas, sem estabelecer, por si só, relações de causalidade.

---

## 1.4 Objetivo geral

Desenvolver um produto analítico baseado em séries temporais para caracterizar mudanças na dinâmica sazonal de dengue, zika e chikungunya em municípios brasileiros selecionados e investigar sua associação com a variação temporal das condições climáticas locais.

## 1.5 Objetivos específicos

1. Construir e integrar séries temporais semanais de dengue, zika e chikungunya e variáveis climáticas para os municípios brasileiros selecionados, utilizando dados do InfoDengue e, quando necessário, fontes complementares.

2. Caracterizar a dinâmica sazonal das arboviroses por meio de indicadores de início, pico, fim, duração e intensidade das temporadas, identificando tendências e possíveis pontos de mudança ao longo da série histórica.

3. Investigar a associação entre as mudanças identificadas na dinâmica temporal das arboviroses e a variação das condições climáticas nos municípios analisados, considerando diferentes defasagens temporais quando pertinentes.

4. Desenvolver um produto analítico que sintetize os padrões históricos, as mudanças identificadas e suas associações com as condições climáticas, permitindo a exploração dos resultados por município e arbovirose.

---

## 2. Justificativa

O projeto apresenta contribuições científicas, tecnológicas e sociais.

#### Contribuição científica

O InfoDengue tem sido utilizado em estudos de monitoramento e previsão de arboviroses, especialmente em análises de curto prazo (CODEÇO et al., 2018). Este projeto amplia essa perspectiva ao investigar mudanças na dinâmica temporal de dengue, zika e chikungunya ao longo de uma série histórica de mais de uma década e sua associação com variáveis climáticas. A comparação entre as três arboviroses permite avaliar se esses padrões apresentam comportamentos distintos ao longo do tempo.

#### Contribuição tecnológica

O produto integra dados epidemiológicos e climáticos em uma ferramenta de análise de séries temporais, permitindo visualizar padrões sazonais, possíveis mudanças na dinâmica das arboviroses e sua associação com as condições climáticas (Lowe *et al*., 2021). O código e a documentação do projeto serão disponibilizados publicamente para favorecer sua reprodutibilidade (Peng, 2011; Wilkinson *et al*., 2016).

#### Contribuição social

A análise de mudanças nos padrões temporais das arboviroses pode contribuir para o planejamento de ações de vigilância e prevenção em saúde pública. O projeto está alinhado à ODS 11, Cidades e Comunidades Sustentáveis, especialmente à Meta 11.b, relacionada ao planejamento e à implementação de políticas voltadas à adaptação e à resiliência diante de riscos ambientais e climáticos. A proposta também apresenta relação com os ODS 3, Saúde e Bem-Estar, e 13, Ação Climática.

O produto possui caráter analítico e não substitui sistemas oficiais de vigilância ou produz diagnósticos epidemiológicos. Seu objetivo é demonstrar a aplicação de Ciência de Dados na análise de padrões temporais e de sua relação com variáveis climáticas.

# 3. Público-alvo e cliente

O público-alvo principal do produto são profissionais da vigilância epidemiológica municipal, especialmente aqueles envolvidos no monitoramento de arboviroses nas Secretarias Municipais de Saúde. Como público secundário, consideram-se pesquisadores e estudantes interessados na análise de séries temporais epidemiológicas e ambientais.

O cliente potencial é uma Secretaria Municipal de Saúde, com foco no setor de vigilância epidemiológica. Essa definição orientará as funcionalidades e a apresentação dos resultados, priorizando informações que possam apoiar a análise da dinâmica temporal das arboviroses e sua relação com as condições climáticas. Sempre que possível, essa perspectiva será confrontada com necessidades identificadas na literatura e com contribuições de profissionais da área.

### Requisitos funcionais do produto

- **RF1** — Selecionar município.
- **RF2** — Selecionar doença (dengue, zika ou chikungunya).
- **RF3** — Visualizar série histórica de incidência.
- **RF4** — Visualizar mudanças detectadas na dinâmica sazonal (changepoints e indicadores de temporada).
- **RF5** — Visualizar variáveis climáticas associadas.
- **RF6** — Visualizar previsão de curto prazo (1 a 4 semanas).
- **RF7** — Visualizar semanas com comportamento epidemiológico atípico.

---

# 4. Descrição da base de dados

## 4.1 Fonte principal: InfoDengue

A principal fonte de dados será o InfoDengue, plataforma de vigilância desenvolvida por pesquisadores da FGV/EMAp e da Fiocruz, que integra dados epidemiológicos e ambientais para o monitoramento de arboviroses no Brasil.

**Volume e cobertura:** a plataforma disponibiliza dados agregados por município e semana epidemiológica, com séries históricas superiores a uma década para diversos municípios brasileiros. A cobertura efetivamente utilizável será avaliada na etapa exploratória, priorizando séries com pelo menos 8 anos de dados e completude suficiente para as análises propostas.

**Múltiplos agravos:** a plataforma disponibiliza dados para dengue, zika e chikungunya, permitindo a comparação entre as três arboviroses em diferentes municípios e períodos.

**Nowcasting:** o InfoDengue utiliza técnicas de *nowcasting* para estimar casos ainda não registrados devido ao atraso entre ocorrência e notificação. A variável `casos_est` é atualizada retrospectivamente à medida que novas informações são incorporadas e, por isso, será tratada como uma estimativa dinâmica da incidência.

**Acesso:** os dados serão obtidos por meio da API pública do InfoDengue, com consultas parametrizadas por município, doença e período.

### Variável de resposta

A principal variável epidemiológica será a incidência estimada, calculada a partir de `casos_est` e da população do município. A disponibilidade e a estabilidade dessa variável serão avaliadas na etapa exploratória antes da definição final dos procedimentos analíticos.

O indicador `p_rt1`, que representa a probabilidade estimada de Rt > 1, será utilizado apenas de forma descritiva no produto, sem participação nas análises principais.

### Variáveis de interesse

**Variável epidemiológica:** `casos_est` e incidência estimada.

**Variáveis climáticas:** temperatura mínima, média e máxima; umidade mínima, média e máxima.

**Variáveis temporais:** semana epidemiológica e ano.

**Variáveis de identificação:** município e código IBGE.

**Indicadores auxiliares:** `p_rt1` e nível de alerta (`nivel`).

A seleção definitiva das variáveis será realizada após a avaliação exploratória da completude e qualidade dos dados.

### Granularidade e período

A unidade temporal principal será a semana epidemiológica. Será utilizado o maior período histórico disponível com qualidade e comparabilidade suficientes, priorizando séries com pelo menos 8 anos de cobertura temporal.

## 4.2 Fonte complementar: INMET

O InfoDengue será utilizado como fonte climática principal. O INMET será consultado quando houver ausência de variáveis relevantes, inconsistências ou necessidade de validação de informações climáticas.

# 5. Seleção dos municípios

A análise será inicialmente conduzida em três municípios, podendo ser ampliada para até cinco conforme a disponibilidade dos dados, a complexidade computacional e o cronograma do projeto.

### Critérios de seleção

Serão priorizados municípios que apresentem:

* séries históricas com pelo menos 8 anos de cobertura;
* boa completude dos dados epidemiológicos e climáticos;
* diferentes contextos climáticos e regionais;
* variação suficiente na ocorrência das arboviroses para permitir a análise temporal;
* condições adequadas para comparação entre diferentes contextos epidemiológicos.

Também serão considerados municípios de interesse epidemiológico que apresentem baixa atividade histórica e mudanças recentes na ocorrência das arboviroses. Quando pertinente, serão priorizados municípios localizados em regiões nas quais tenham sido descritas mudanças recentes na distribuição da ocorrência das doenças.

A seleção definitiva será realizada após a etapa exploratória dos dados.

# 6. Solução proposta

O projeto propõe o desenvolvimento de um produto analítico baseado em séries temporais para caracterizar mudanças na dinâmica temporal de dengue, zika e chikungunya e investigar sua associação com a variação das condições climáticas. A solução integrará dados epidemiológicos e climáticos, aplicará métodos de análise de séries temporais e apresentará os resultados de forma organizada por município e arbovirose, permitindo a identificação de padrões sazonais, tendências e possíveis mudanças ao longo da série histórica.

## 6.1 Etapa 1 — Coleta e preparação dos dados

Os dados serão obtidos via API do InfoDengue (para as três doenças) e, quando necessário, complementados com dados do INMET.

Serão realizados:

* tratamento de valores ausentes, com identificação explícita de semanas sem registro;
* distinção entre zero casos e dado ausente — um valor de zero casos não será automaticamente tratado como dado faltante, e valores ausentes não serão convertidos indiscriminadamente em zero;
* interpolação considerada apenas para variáveis climáticas, quando justificável, e não para dados epidemiológicos;
* padronização de datas e organização por semana epidemiológica e por ano;
* integração entre dados epidemiológicos e climáticos;
* criação de variáveis defasadas;
* análise de completude das séries, doença a doença e município a município.

## 6.2 Etapa 2 — Caracterização de sazonalidade e detecção de mudanças (núcleo científico)

Esta é a etapa central do projeto, conduzida antes da modelagem preditiva.

### Indicadores quantitativos de sazonalidade

Para cada série (município × doença × ano), serão calculados:

* **Indicador 1 — Início da temporada**: primeira semana epidemiológica em que a incidência ultrapassa um limiar definido como o **percentil 75 da distribuição histórica** da série, mantido por pelo menos 2 a 3 semanas consecutivas.
* **Indicador 2 — Pico**: semana de maior incidência estimada no ano.
* **Indicador 3 — Fim da temporada**: última semana em que a incidência permanece acima do limiar definido.
* **Indicador 4 — Duração**: número de semanas entre início e fim da temporada.
* **Indicador 5 — Intensidade**: calculado por meio do pico de incidência, da incidência acumulada no período e da área sob a curva da temporada — permitindo diferenciar uma temporada mais longa de uma temporada mais intensa.

O limiar (percentil 75, mínimo de semanas consecutivas) poderá ser ajustado durante a fase exploratória caso se mostre inadequado para alguma série específica, com justificativa documentada.

### Indicador de antecipação

Definido como a diferença, em semanas, entre a semana de início da temporada em um período recente e a semana de início no período histórico de referência, permitindo afirmações do tipo "a temporada começou, em média, X semanas mais cedo" — mais interpretável do que a simples inspeção visual de um gráfico.

### Comparação entre períodos

Os indicadores de duração, intensidade e início serão comparados entre janelas temporais definidas a priori: 2010–2014, 2015–2019, 2020–2024 e, se houver dados suficientes, 2025–2026.

### Detecção de pontos de mudança (changepoint)

O *changepoint* poderá identificar alterações em média, variância, tendência ou estrutura sazonal da série. Será utilizado o método **PELT (Pruned Exact Linear Time)** como abordagem principal, por seu equilíbrio entre eficiência computacional e capacidade de detectar múltiplos pontos de mudança. A detecção será aplicada sobre a série dessazonalizada (após decomposição, tipicamente via STL), de modo a evitar confundir a variação sazonal anual esperada com uma mudança estrutural real no regime da série.

A sequência analítica seguirá a lógica abaixo, para evitar a suposição prévia de que qualquer mudança identificada é necessariamente climática:

```
Série epidemiológica
        ↓
Mudança detectada (changepoint / indicadores de temporada)
        ↓
Momento aproximado da mudança
        ↓
Comparação com variáveis climáticas no mesmo período
        ↓
Avaliação de associação temporal (não causal)
```

## 6.3 Etapa 3 — Associação com variáveis climáticas (análise complementar)

Serão testadas defasagens climáticas limitadas e justificadas pela literatura — tipicamente entre 0 e 4 semanas, com possibilidade de estender até 8–12 semanas caso a literatura consultada indique relevância biológica para defasagens maiores (ex. tempo de desenvolvimento larval do vetor).

Para manter o modelo parcimonioso, nem todas as variáveis climáticas disponíveis serão incluídas automaticamente. Serão priorizadas:

* **Principais**: temperatura média ou mínima; precipitação.
* **Complementares**: umidade, incluída apenas se justificada por correlação relevante ou por resultado da etapa de seleção de variáveis (literatura, análise de correlação, importância de variáveis, validação temporal).

## 6.4 Etapa 4 — Modelagem preditiva de curto prazo (aplicação)

**Problema de previsão definido explicitamente**: prever a incidência estimada de cada arbovirose para as próximas 1 a 4 semanas, utilizando informações disponíveis até a semana corrente (*t*).

Serão comparados exatamente dois modelos:

* **Modelo 1 — SARIMAX**, incorporando variáveis climáticas selecionadas como variáveis exógenas, funcionando como referência estatística.
* **Modelo 2 — XGBoost**, construído a partir de casos das semanas anteriores, médias móveis, variáveis climáticas selecionadas (com suas defasagens), mês/semana do ano, e indicadores derivados da etapa de decomposição de tendência.

Não será utilizado LSTM nem qualquer modelo adicional além dos dois definidos acima, de modo a manter a metodologia enxuta, definida e reprodutível dentro do prazo da disciplina.

---

# 7. Avaliação dos resultados

Caso a etapa preditiva seja implementada, SARIMAX e XGBoost serão comparados por meio de validação temporal em janela expansiva (*walk-forward validation*), utilizando apenas informações disponíveis até cada momento da previsão (HYNDMAN; ATHANASOPOULOS, 2021).

As métricas principais serão **MAE** e **RMSE**, com **sMAPE** como medida complementar (HYNDMAN; ATHANASOPOULOS, 2021).

Os pontos de mudança identificados pelo PELT serão avaliados com base nos critérios do método e quanto à estabilidade e plausibilidade temporal, considerando, quando disponíveis, informações epidemiológicas e literatura sobre os períodos analisados (KILLICK; FEARNHEAD; ECKLEY, 2012).

A interpretação dos resultados será restrita à identificação de padrões e associações, sem atribuição automática de causalidade.

# 8. Detecção de comportamentos atípicos

Serão identificadas semanas com comportamento epidemiológico atípico em relação ao padrão esperado da série, utilizando os resíduos ou intervalos de previsão, caso a etapa preditiva seja implementada.

O objetivo será sinalizar padrões que possam merecer investigação posterior, sem classificá-los automaticamente como surtos ou estabelecer causalidade.

---

# 9. Limitações previstas

O projeto reconhece as seguintes limitações:

* caráter observacional dos dados, que limita a inferência de causalidade entre variáveis climáticas e dinâmica epidemiológica;
* subnotificação de casos, especialmente em municípios menores;
* possíveis mudanças no sistema de vigilância ao longo do período, incluindo critérios diagnósticos e cobertura de testagem;
* mudanças demográficas nos municípios analisados;
* ausência de variáveis socioambientais relevantes, como saneamento, urbanização e ações de controle vetorial;
* diferenças na qualidade e completude dos dados entre municípios;
* número limitado de municípios, sem pretensão de representatividade estatística nacional;
* possível instabilidade dos indicadores em séries com baixa incidência, especialmente para zika e chikungunya;
* revisões retrospectivas dos valores de `casos_est` decorrentes do processo de *nowcasting*.

As associações identificadas serão interpretadas considerando a possível influência de fatores não contemplados na base, como mobilidade populacional, imunidade da população, ações de controle vetorial e mudanças nos sistemas de vigilância.

---

# 10. Critérios de sucesso do projeto

O projeto será considerado concluído quando:

* pelo menos 3 municípios selecionados apresentarem séries adequadas para análise;
* as séries disponíveis de dengue, zika e chikungunya forem avaliadas conforme sua completude e qualidade;
* os indicadores de início, duração e intensidade das temporadas forem calculados;
* o método PELT for aplicado às séries selecionadas, quando tecnicamente adequado;
* forem investigadas as associações temporais entre os padrões epidemiológicos identificados e as variáveis climáticas;
* as análises forem reproduzíveis a partir do código disponibilizado;
* o painel analítico apresentar os principais resultados para os municípios selecionados;
* código-fonte e documentação estiverem disponíveis publicamente no GitHub.

---

# 11. Produto final

# 11. Produto final

O produto final será um painel analítico interativo, organizado nas seguintes abas:

* **Aba 1 — Visão geral:** principais resultados da análise, incluindo indicadores de sazonalidade, mudanças identificadas e associações com variáveis climáticas.

* **Aba 2 — Histórico:** evolução semanal da incidência estimada de dengue, zika e chikungunya ao longo da série histórica.

* **Aba 3 — Sazonalidade:** indicadores de início, pico, fim, duração e intensidade das temporadas, além da decomposição das séries em tendência, sazonalidade e resíduo.

* **Aba 4 — Mudanças:** pontos de mudança identificados nas séries, com apresentação simplificada dos resultados e acesso aos principais parâmetros do método utilizado.

* **Aba 5 — Clima:** evolução das variáveis climáticas selecionadas e sua relação temporal com os padrões epidemiológicos, incluindo as defasagens analisadas.

---

# 12. Caráter extensionista

O projeto terá caráter extensionista por meio da disponibilização pública de:

* código-fonte e documentação;
* metodologia e instruções para reprodução das análises;
* resultados obtidos nas séries analisadas;
* painel analítico, quando tecnicamente viável;
* orientações para obtenção dos dados nas fontes oficiais.

A disponibilização desses materiais permitirá que estudantes, pesquisadores e profissionais interessados consultem, reproduzam e explorem as análises desenvolvidas no projeto.

---

# 13. Referências

## Referências

CHEN, T.; GUESTRIN, C. XGBoost: a scalable tree boosting system. In: **PROCEEDINGS OF THE 22ND ACM SIGKDD INTERNATIONAL CONFERENCE ON KNOWLEDGE DISCOVERY AND DATA MINING**, 2016. p. 785-794.

CLEVELAND, R. B.; CLEVELAND, W. S.; MCRAE, J. E.; TERPENNING, I. STL: a seasonal-trend decomposition procedure based on loess. **Journal of Official Statistics**, v. 6, n. 1, p. 3-73, 1990.

CODEÇO, C. T. et al. InfoDengue: a nowcasting system for the surveillance of dengue fever transmission. **bioRxiv**, 2016. Disponível em: https://www.biorxiv.org/content/10.1101/046193. Acesso em: 25 ago. 2026.

CODEÇO, C.; COELHO, F. C.; CRUZ, O. G.; OLIVEIRA, S. B.; CASTRO, T. G.; BASTOS, L. S. InfoDengue: a nowcasting system for the surveillance of arboviruses in Brazil. **Revue d'Épidémiologie et de Santé Publique**, v. 66, supl. 5, p. S386, out. 2018. Disponível em: https://doi.org/10.1016/j.respe.2018.05.408. Acesso em: 25 ago. 2026.

FGV EMAP. **FGV e Fiocruz monitoram avanço da dengue no Brasil**. 2024. Disponível em: https://emap.fgv.br/en/news/fgv-and-fiocruz-monitor-spread-dengue-fever-brazil. Acesso em: 25 ago. 2026.

FIOCRUZ. **Monitoramento de dengue indica pontos de atenção no Brasil**. Agência Fiocruz de Notícias, 2022. Disponível em: https://agencia.fiocruz.br/monitoramento-de-dengue-indica-pontos-de-atencao-brasil. Acesso em: 25 ago. 2026.

HYNDMAN, R. J.; ATHANASOPOULOS, G. **Forecasting: principles and practice**. 3. ed. Melbourne: OTexts, 2021. Disponível em: https://otexts.com/fpp3/. Acesso em: 25 ago. 2026.

INFODENGUE. **Sobre nós**. [S. l.], [s. d.]. Disponível em: https://info.dengue.mat.br/informacoes/. Acesso em: 25 ago. 2026.

INSTITUTO NACIONAL DE METEOROLOGIA (INMET). **Banco de Dados Meteorológicos para Ensino e Pesquisa**. [S. l.], [s. d.]. Disponível em: https://portal.inmet.gov.br/dadoshistoricos. Acesso em: 25 ago. 2026.

KILLICK, R.; FEARNHEAD, P.; ECKLEY, I. A. Optimal detection of changepoints with a linear computational cost. **Journal of the American Statistical Association**, v. 107, n. 500, p. 1590-1598, 2012.

LOWE, R. et al. Combined effects of hydrometeorological hazards and urbanisation on dengue risk in Brazil: a spatiotemporal modelling study. **The Lancet Planetary Health**, v. 5, n. 4, p. e209-e219, 2021.

MORDECAI, E. A.; COHEN, J. M.; EVANS, M. V.; GUDAPATI, P.; JOHNSON, L. R.; LIPPI, C. A. et al. Detecting the impact of temperature on transmission of Zika, dengue, and chikungunya using mechanistic models. **PLOS Neglected Tropical Diseases**, v. 11, n. 4, e0005568, 2017. Disponível em: https://doi.org/10.1371/journal.pntd.0005568. Acesso em: 25 ago. 2026.

MORDECAI, E. A. et al. Thermal biology of mosquito-borne disease. **Ecology Letters**, v. 22, n. 10, p. 1690-1708, 2019.

ORGANIZAÇÃO DAS NAÇÕES UNIDAS (ONU). **Objetivos de Desenvolvimento Sustentável: ODS 11: cidades e comunidades sustentáveis**. [S. l.], [s. d.]. Disponível em: https://www.undp.org/sustainable-development-goals. Acesso em: 25 ago. 2026.

ORGANIZAÇÃO MUNDIAL DA SAÚDE (OMS). **Dengue: global situation, surveillance and progress: 2024 update**. **Weekly Epidemiological Record**, 2025. Disponível em: https://www.who.int/publications/i/item/who-wer10052-665-678. Acesso em: 25 ago. 2026.

PENG, R. D. Reproducible research in computational science. **Science**, v. 334, n. 6060, p. 1226-1227, 2011.

PLOS NEGLECTED TROPICAL DISEASES. **Phenotypic variation in populations of the mosquito vector, Aedes aegypti, and implications for predicting the effects of temperature and climate change on dengue transmission**. **PLOS Neglected Tropical Diseases**, v. 19, 2025. Disponível em: https://doi.org/10.1371/journal.pntd.0013623. Acesso em: 25 ago. 2026.

PLOS NEGLECTED TROPICAL DISEASES. **Seasonal temperature variation influences climate suitability for dengue, chikungunya, and Zika transmission**. **PLOS Neglected Tropical Diseases**, v. 12, n. 4, e0006451, 2018. Disponível em: https://doi.org/10.1371/journal.pntd.0006451. Acesso em: 25 ago. 2026.

WILKINSON, M. D. et al. The FAIR Guiding Principles for scientific data management and stewardship. **Scientific Data**, v. 3, n. 1, p. 160018, 2016.

---

# 15. Próximas etapas

**Fase 1 — Dados:** acesso à API do InfoDengue; avaliação da qualidade e completude das séries; seleção dos municípios.

**Fase 2 — Séries temporais:** construção das séries; decomposição em tendência, sazonalidade e resíduo; cálculo dos indicadores de início, pico, fim, duração e intensidade das temporadas.

**Fase 3 — Mudanças:** aplicação do método PELT às séries selecionadas e análise dos pontos de mudança identificados.

**Fase 4 — Clima:** seleção das variáveis climáticas; definição das defasagens; análise da associação temporal entre as condições climáticas e os padrões epidemiológicos identificados.

**Fase 5 — Produto:** desenvolvimento do painel analítico; organização da documentação; disponibilização do código e dos resultados no GitHub.

