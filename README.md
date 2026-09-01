# O clima já está deixando uma marca? Detectando mudanças na dinâmica temporal de arboviroses e sua associação com variáveis climáticas em municípios brasileiros

**Projeto Aplicado IV — Tecnologia em Ciência de Dados — 2026.2**

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

## 1.2 Motivação

O InfoDengue constitui uma importante fonte de dados para o monitoramento das arboviroses no Brasil, reunindo informações epidemiológicas e ambientais por município e semana epidemiológica. A plataforma utiliza técnicas de *nowcasting* para estimar casos ainda não registrados no sistema de notificação, permitindo acompanhar a evolução temporal de dengue, chikungunya e zika (INFO DENGUE, 2026).

A extensão da série histórica possibilita investigar padrões que não seriam identificados em períodos mais curtos, como mudanças na sazonalidade, na intensidade e no período de ocorrência das arboviroses. Como a variável `casos_est` corresponde a estimativas produzidas pelo *nowcasting* e pode ser revisada retrospectivamente à medida que novas notificações são incorporadas, esses valores serão tratados como estimativas dinâmicas da incidência, e não como contagens observacionais definitivas (INFO DENGUE, 2026).

Do ponto de vista da gestão pública, identificar mudanças nos padrões temporais das arboviroses pode contribuir para o planejamento das ações de vigilância e prevenção, especialmente em municípios nos quais a dinâmica epidemiológica vem se modificando ao longo do tempo.

---

## 1.3 Perguntas de pesquisa

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

A análise de mudanças nos padrões temporais das arboviroses pode contribuir para o planejamento de ações de vigilância e prevenção em saúde pública. O projeto está alinhado à **ODS 11, Cidades e Comunidades Sustentáveis**, especialmente à Meta 11.b, relacionada ao planejamento e à implementação de políticas voltadas à adaptação e à resiliência diante de riscos ambientais e climáticos. A proposta também apresenta relação com os ODS 3, Saúde e Bem-Estar, e 13, Ação Climática.

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

## 4.1 Fonte principal — InfoDengue

A principal fonte de dados será o **InfoDengue**, plataforma de vigilância desenvolvida por pesquisadores da Fundação Getúlio Vargas (FGV/EMAp) e da Fiocruz, com dados oficiais agregados a partir do SINAN (Sistema de Informação de Agravos de Notificação) do Ministério da Saúde.

**Volume e cobertura**: a plataforma cobre a totalidade dos municípios brasileiros participantes do sistema (ampliado para nível nacional a partir de 2021, com apoio do Ministério da Saúde), com séries históricas semanais de mais de uma década de observações por município. O volume exato de pontos temporais efetivamente utilizável, por município e doença, será determinado após a extração exploratória inicial, priorizando séries com pelo menos 8–10 anos de cobertura temporal e completude suficiente para análise de tendência e sazonalidade — não sendo exigida continuidade de 100% dos registros.

**Múltiplos agravos comparáveis**: a plataforma disponibiliza a mesma estrutura de dados para dengue, zika e chikungunya, permitindo a comparação entre as três doenças no mesmo município e período.

**Atualização e nowcasting**: o InfoDengue foi concebido como um sistema de *nowcasting*, corrigindo estatisticamente o atraso natural de notificação e gerando estimativas corrigidas (`casos_est`) atualizadas semana a semana. A atualização contínua da plataforma torna a fonte particularmente adequada para aplicações de monitoramento e previsão temporal, distinguindo-a de bases estáticas pré-processadas.

**Originalidade**: por se tratar de dado governamental de vigilância agregado por uma plataforma de pesquisa (não uma base secundária tipo Kaggle), a fonte exige da equipe trabalho próprio de extração via API, tratamento e integração.

**Acesso**: API pública REST (`https://info.dengue.mat.br/api/`), com consultas parametrizadas por município (código IBGE), doença e intervalo de semanas epidemiológicas.

### Variável de resposta

A variável principal de modelagem será a **incidência estimada** (`casos_est` ajustada pela população do município), priorizada por permitir comparação entre municípios de tamanhos diferentes. A disponibilidade e estabilidade de `casos_est` serão avaliadas na etapa exploratória antes da confirmação definitiva dessa escolha.

O indicador `p_rt1` (probabilidade de Rt > 1) será mantido apenas como **variável descritiva no painel**, sem uso como variável principal nos modelos preditivos ou nas análises de tendência.

### Variáveis de interesse

* `casos` e `casos_est` (por doença);
* incidência estimada (variável de resposta principal);
* `p_rt1` (uso descritivo no painel);
* nível de alerta (`nivel`);
* temperatura mínima, média e máxima;
* umidade mínima, média e máxima;
* semana epidemiológica (`SE`) e ano;
* município e código IBGE.

A seleção definitiva das variáveis será realizada após análise exploratória da completude e qualidade dos dados, doença a doença.

### Granularidade e período

A unidade temporal principal será a **semana epidemiológica**. Será utilizado o maior período histórico disponível com qualidade e comparabilidade suficientes, priorizando séries com pelo menos 8 a 10 anos de cobertura temporal — o período exato será definido apenas após a etapa de extração e avaliação de completude.

---

## 4.2 Fonte complementar — INMET

O InfoDengue será a **fonte climática principal** desde o início do projeto. O INMET será utilizado apenas caso existam variáveis climáticas ausentes na base principal, inconsistências relevantes, ou necessidade pontual de validação — reduzindo a complexidade do projeto sem impedir sua expansão posterior, caso necessário.

---

# 5. Seleção dos municípios

Serão selecionados **3 municípios como amostra principal**, com possibilidade de expansão para até 5 caso a análise exploratória e o cronograma da disciplina permitam. Definir 3 como suficiente garante a viabilidade do projeto mesmo em cenário de restrição de tempo.

### Definição operacional de "município sentinela"

Municípios localizados em regiões de expansão epidemiológica recente, ou historicamente caracterizados por menor atividade de arboviroses, serão tratados como **municípios sentinela** para a investigação de possíveis alterações no padrão temporal da doença — sem que isso implique qualquer afirmação sobre distribuição ou abundância do vetor, para a qual o projeto não possui dados diretos.

Um município será considerado candidato a sentinela quando atender a pelo menos três dos seguintes critérios:

* menor incidência histórica acumulada em relação à média nacional;
* aumento recente e perceptível da atividade epidemiológica nos últimos anos da série;
* localização em região associada, pela literatura ou pelos indicadores do InfoDengue, à expansão recente da ocorrência da doença (ex. região Sul);
* série histórica suficientemente longa (mínimo 8 anos) para permitir comparação entre períodos;
* disponibilidade adequada de variáveis climáticas no mesmo período.

### Demais critérios de seleção

* disponibilidade e completude da série histórica;
* representatividade climática (diferentes regiões/regimes térmicos);
* disponibilidade de séries históricas suficientemente informativas para as doenças analisadas — não sendo exigida a presença simultânea das três doenças em todos os municípios, já que diferenças de ocorrência entre doenças também constituem uma característica relevante para a análise;
* possibilidade de comparação entre diferentes contextos regionais.

A seleção definitiva será realizada após a etapa exploratória da base de dados.

---

# 6. Solução proposta

O projeto é estruturado em três camadas com prioridades explícitas: **(i) núcleo científico** — detecção de mudanças na dinâmica temporal; **(ii) análise complementar** — associação com variáveis climáticas; **(iii) aplicação** — previsão de curto prazo. Essa hierarquia evita que o projeto seja lido apenas como "mais um projeto de previsão de dengue".

## 6.1 Etapa 1 — Coleta e preparação dos dados

Os dados serão obtidos via API do InfoDengue (para as três doenças) e, quando necessário, complementados com dados do INMET.

Serão realizados:

* tratamento de valores ausentes, com identificação explícita de semanas sem registro;
* **distinção entre zero casos e dado ausente** — um valor de zero casos não será automaticamente tratado como dado faltante, e valores ausentes não serão convertidos indiscriminadamente em zero;
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
* **Indicador 5 — Intensidade**: calculado por meio do pico de incidência, da incidência acumulada no período e da área sob a curva da temporada — permitindo diferenciar uma temporada mais **longa** de uma temporada mais **intensa**.

O limiar (percentil 75, mínimo de semanas consecutivas) poderá ser ajustado durante a fase exploratória caso se mostre inadequado para alguma série específica, com justificativa documentada.

### Indicador de antecipação

Definido como a diferença, em semanas, entre a semana de início da temporada em um período recente e a semana de início no período histórico de referência, permitindo afirmações do tipo "a temporada começou, em média, X semanas mais cedo" — mais interpretável do que a simples inspeção visual de um gráfico.

### Comparação entre períodos

Os indicadores de duração, intensidade e início serão comparados entre janelas temporais definidas a priori: 2010–2014, 2015–2019, 2020–2024 e, se houver dados suficientes, 2025–2026.

### Detecção de pontos de mudança (changepoint)

O *changepoint* poderá identificar alterações em média, variância, tendência ou estrutura sazonal da série. Será utilizado o método **PELT (Pruned Exact Linear Time)** como abordagem principal, por seu equilíbrio entre eficiência computacional e capacidade de detectar múltiplos pontos de mudança. A detecção será aplicada sobre a **série dessazonalizada** (após decomposição, tipicamente via STL), de modo a evitar confundir a variação sazonal anual esperada com uma mudança estrutural real no regime da série.

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

**Problema de previsão definido explicitamente**: prever a incidência estimada de cada arbovirose para as próximas **1 a 4 semanas**, utilizando informações disponíveis até a semana corrente (*t*).

Serão comparados exatamente dois modelos:

* **Modelo 1 — SARIMAX**, incorporando variáveis climáticas selecionadas como variáveis exógenas, funcionando como referência estatística.
* **Modelo 2 — XGBoost**, construído a partir de casos das semanas anteriores, médias móveis, variáveis climáticas selecionadas (com suas defasagens), mês/semana do ano, e indicadores derivados da etapa de decomposição de tendência.

Não será utilizado LSTM nem qualquer modelo adicional além dos dois definidos acima, de modo a manter a metodologia enxuta, definida e reprodutível dentro do prazo da disciplina.

---

# 7. Avaliação dos modelos

A comparação entre SARIMAX e XGBoost será realizada por meio de **validação temporal em janela expansiva (*walk-forward validation*)**, e não apenas uma única divisão treino/teste, evitando vazamento de informações futuras para o treinamento.

Métricas de avaliação:

* **Principais**: MAE e RMSE.
* **Opcional**: sMAPE, preferido a MAPE tradicional por lidar melhor com semanas de incidência baixa ou igual a zero, comuns nas séries analisadas.

A etapa de detecção de pontos de mudança (Seção 6.2) será avaliada por meio de critérios estatísticos próprios do método PELT (ex. significância da quebra estrutural identificada) e por checagem de plausibilidade em relação a relatos da literatura ou de boletins epidemiológicos oficiais sobre o mesmo município/período, quando disponíveis.

---

# 8. Detecção de comportamentos atípicos

Uma semana será considerada potencialmente atípica quando o erro de previsão do modelo ultrapassar um limite baseado na distribuição histórica dos resíduos ou no intervalo de previsão do modelo estatístico.

O objetivo não será classificar automaticamente uma situação como "surto", mas identificar **comportamentos epidemiológicos atípicos** que possam merecer atenção em análises posteriores.

---

# 9. Limitações previstas

O projeto reconhece, desde a fase de concepção, as seguintes limitações:

* caráter observacional dos dados, que impossibilita inferir causalidade entre variáveis climáticas e dinâmica epidemiológica;
* subnotificação de casos, especialmente em municípios menores;
* possíveis alterações no próprio sistema de vigilância ao longo do tempo (mudanças de critério diagnóstico, cobertura de testagem);
* mudanças demográficas na população dos municípios ao longo do período analisado;
* ausência, na base utilizada, de variáveis socioambientais relevantes (ex. saneamento, urbanização, cobertura de controle vetorial);
* diferenças na qualidade e completude dos dados entre municípios;
* número limitado de municípios analisados, sem pretensão de representatividade estatística nacional;
* possível instabilidade dos indicadores para doenças com baixa incidência histórica (zika e chikungunya em alguns municípios);
* revisões retrospectivas de `casos_est` pelo sistema de nowcasting, que podem alterar valores já analisados.

As associações identificadas serão interpretadas considerando que fatores não incluídos na base — como mobilidade populacional, imunidade de rebanho, ações de controle vetorial e mudanças na vigilância — também podem influenciar a dinâmica das arboviroses.

---

# 10. Critérios de sucesso do projeto

O projeto será considerado concluído quando:

* pelo menos 3 municípios tiverem sido analisados;
* as três doenças tiverem sido avaliadas nos municípios em que houver dados suficientes;
* as séries e análises forem reprodutíveis a partir do código disponibilizado;
* o método PELT tiver sido aplicado às séries dessazonalizadas selecionadas;
* os indicadores de início, duração e intensidade de temporada tiverem sido calculados;
* SARIMAX e XGBoost tiverem sido comparados por meio de validação temporal;
* o painel analítico estiver funcional para os municípios selecionados;
* código-fonte e documentação estiverem disponíveis publicamente no GitHub.

---

# 11. Produto final

O produto final será um **painel analítico interativo**, organizado nas seguintes abas:

* **Aba 1 — Visão geral**: indicadores principais (o que mudou, quando mudou, se há associação com o clima, e o que se espera para as próximas semanas), priorizados na tela inicial em vez de detalhes estatísticos completos.
* **Aba 2 — Histórico**: casos e incidência ao longo do tempo.
* **Aba 3 — Sazonalidade**: decomposição em tendência e sazonalidade, indicadores de início/pico/fim/duração/intensidade.
* **Aba 4 — Mudanças**: pontos de mudança identificados (changepoints), com uma camada resumida ("mudança detectada em torno de determinado ano") e uma camada técnica detalhada (método PELT, parâmetros e critérios utilizados), separadas para preservar a usabilidade da visão executiva.
* **Aba 5 — Clima**: temperatura e precipitação associadas, incluindo as defasagens testadas.
* **Aba 6 — Previsão**: resultados de SARIMAX e XGBoost para o horizonte de 1 a 4 semanas.
* **Aba 7 — Anomalias**: semanas com desvio em relação ao padrão esperado.

O código-fonte, documentação e instruções para reprodução serão disponibilizados em repositório público no GitHub.

---

# 12. Relação com o doutorado

O projeto apresenta uma **relação conceitual e temática** — e não uma relação metodológica direta — com a linha de pesquisa de doutorado sobre vulnerabilidade de Diptera às mudanças climáticas.

Enquanto o doutorado aborda uma perspectiva mais ampla, envolvendo distribuição geográfica, filogenia, traços funcionais e modelagem hierárquica de comunidades para cinco famílias de Diptera a partir de registros de ocorrência, filogenias datadas e projeções climáticas do CMIP6, o presente projeto concentra-se em um recorte aplicado e temporal:

**Diptera (Culicidae) → múltiplos patógenos com sensibilidade térmica mecanisticamente distinta → dinâmica epidemiológica → possíveis mudanças temporais → associação (não causal) com variáveis climáticas.**

O paralelo conceitual reside na ideia comum aos dois projetos de que características biológicas (traços funcionais de uma espécie, no doutorado; sensibilidade térmica de um patógeno, neste projeto) podem estar associadas a diferentes respostas a um clima em transformação. O **Projeto Aplicado IV não constitui uma etapa metodológica do doutorado** — é um projeto independente, inspirado por uma pergunta relacionada, que utiliza dados, métodos e escopo adequados aos requisitos e ao prazo da disciplina.

---

# 13. Caráter extensionista

Serão disponibilizados publicamente:

* código-fonte e documentação;
* metodologia e instruções de reprodução;
* resultados, incluindo os indicadores de sazonalidade e os pontos de mudança identificados por município e doença;
* painel analítico, quando tecnicamente viável;
* instruções para obtenção dos dados nas fontes oficiais.

---

# 14. Referências

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

**Fase 1 — Dados**: acesso à API do InfoDengue para as três doenças; avaliação de qualidade e completude; seleção dos municípios (incluindo ao menos um sentinela).

**Fase 2 — Séries**: construção das séries temporais; decomposição em tendência/sazonalidade (STL); cálculo dos indicadores de início/pico/fim/duração/intensidade da temporada.

**Fase 3 — Mudanças**: aplicação do método PELT sobre as séries dessazonalizadas; identificação e validação de plausibilidade dos pontos de mudança.

**Fase 4 — Clima**: seleção de variáveis climáticas prioritárias (temperatura, precipitação); teste de defasagens (0–4 semanas, com possível extensão); avaliação de associação temporal com as mudanças identificadas na Fase 3.

**Fase 5 — Previsão**: implementação de SARIMAX e XGBoost; validação temporal em janela expansiva; comparação de desempenho (MAE, RMSE, sMAPE); definição do mecanismo de detecção de anomalias.

**Fase 6 — Produto**: construção do painel analítico (7 abas); documentação; disponibilização do código e dos dados no GitHub.
