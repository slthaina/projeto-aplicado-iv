# O Clima Já Está Deixando uma Marca? Detectando Mudanças na Dinâmica Temporal de Arboviroses e sua Associação com Variáveis Climáticas em Municípios Brasileiros

**Projeto Aplicado IV — Ciência de Dados EaD — 2026/02**

**ODS relacionada:** ODS 11 — Cidades e Comunidades Sustentáveis

---

## Equipe

| Nome          | Matrícula     | Função no projeto |
| ------------- | ------------- | ----------------- |
| *Thainá Silva Leite*         | *10730503* | *Coordenação e desenvolvimento integral do projeto: pesquisa, coleta e tratamento de dados, análise, modelagem, desenvolvimento do produto, documentação e apresentação.*     |

---

# 1. Introdução

## 1.1 Contexto

Em 2024, a dengue atingiu níveis de transmissão sem precedentes no mundo: segundo o relatório *Dengue: global situation, surveillance and progress – 2024 update*, publicado pela Organização Mundial da Saúde (OMS/WHO Weekly Epidemiological Record), foram notificados 14.434.584 casos em todas as seis regiões da organização, o maior volume global já registrado. O Brasil concentrou a maior parte desse total, com mais de 10 milhões de casos reportados e 6.321 óbitos — o maior número de casos de dengue reportados por um único país no mundo em 2024, em um cenário de recorde histórico global da doença. O Brasil concentra, portanto, uma parcela expressiva da carga global de dengue e apresenta, adicionalmente, importante circulação de outras arboviroses urbanas transmitidas pelo mesmo vetor, como chikungunya e zika.

Dengue, zika e chikungunya compartilham o vetor urbano *Aedes aegypti* (Diptera: Culicidae), mas são causadas por patógenos distintos. Estudos mecanísticos indicam diferenças nas relações entre temperatura e potencial de transmissão entre os diferentes sistemas vetor-vírus, com eficiência de transmissão concentrada em uma faixa térmica intermediária (aproximadamente 18°C a 34°C, com pico próximo de 26–29°C, segundo modelos publicados na literatura). Se essas diferenças mecanísticas, observadas em condições controladas, também se manifestam nos dados de vigilância de campo ao longo de mais de uma década é uma questão ainda pouco explorada — e é exatamente essa lacuna que o projeto propõe investigar empiricamente, sem presumir a resposta a priori.

Há indícios preliminares de que a dinâmica espaço-temporal dessas doenças no Brasil vem se modificando: indicadores do próprio sistema InfoDengue já registraram expansão recente da ocorrência de dengue para latitudes mais altas, incluindo a região Sul do país. Esse tipo de evidência observacional motiva a investigação sistemática, em série temporal, de como o padrão sazonal de cada arbovirose vem se comportando ao longo dos anos, e se essa evolução apresenta associação temporal com o comportamento das variáveis climáticas nos mesmos municípios — sem que isso implique, por si só, uma relação de causalidade direta e comprovada.

Este projeto está inserido na interseção entre **Entomologia, Ecologia de Vetores, Climatologia, Epidemiologia e Ciência de Dados**, com foco na caracterização, em série temporal, de possíveis mudanças na dinâmica de transmissão de arboviroses e sua associação com variáveis climáticas — e não na previsão pontual de casos futuros como objetivo central. A proposta mantém uma conexão conceitual (não metodológica) com estudos de vulnerabilidade climática de Diptera: assim como traços funcionais de uma espécie podem estar associados à sua resposta a variações climáticas, a sensibilidade térmica de cada arbovirose, documentada pela literatura mecanística, pode estar associada a diferenças na forma como sua dinâmica temporal se comporta frente a um regime climático em transformação.

## 1.2 Motivação

A maior parte das aplicações de Ciência de Dados sobre o InfoDengue foca exclusivamente na previsão de curto prazo — quantos casos ocorrerão nas próximas semanas. Esse é um problema relevante e será também tratado neste projeto, mas de forma complementar: a proposta busca explorar uma dimensão temporal de mais longo prazo, menos enfatizada em aplicações de previsão operacional, capaz de captar tendências e possíveis pontos de mudança na dinâmica sazonal das arboviroses ao longo dos anos.

O InfoDengue disponibiliza dados epidemiológicos e ambientais organizados por município e semana epidemiológica desde aproximadamente 2010, cobrindo dengue, zika e chikungunya. A atualização contínua da plataforma e o uso de *nowcasting* — sistema que corrige estatisticamente o atraso natural entre a ocorrência de um caso e sua notificação completa no sistema oficial — tornam a fonte particularmente adequada para aplicações de monitoramento e previsão temporal, distinguindo-a de uma base estática pré-processada. Como os valores de `casos_est` são estimativas produzidas por esse sistema de nowcasting e podem sofrer revisões retrospectivas à medida que novas notificações são incorporadas, esses valores serão tratados, ao longo do projeto, como **estimativas dinâmicas da incidência**, e não como contagens observacionais definitivas — uma distinção metodológica relevante para a interpretação dos resultados.

Esse volume histórico de mais de uma década de observações semanais por município é o que viabiliza a análise de tendência de longo prazo e a detecção de possíveis pontos de mudança propostas neste projeto — algo que uma janela temporal mais curta não permitiria de forma confiável.

Do ponto de vista da gestão pública, uma ferramenta capaz de mostrar não apenas "quantos casos teremos semana que vem", mas também se o padrão sazonal de uma doença já mudou nos últimos anos, tem valor estratégico complementar para o planejamento de médio prazo de secretarias municipais de saúde — especialmente em municípios que historicamente registravam baixa atividade epidemiológica dessas doenças.

---

## 1.3 Perguntas de pesquisa

Em vez de uma única pergunta, o projeto é organizado em torno de três perguntas de pesquisa complementares, que também definem a hierarquia de prioridades do trabalho:

**RQ1 (núcleo científico).** Os municípios selecionados apresentam alterações persistentes no início, na duração ou na intensidade das temporadas de dengue, zika e chikungunya ao longo da série histórica disponível?

**RQ2 (análise complementar).** Essas alterações, quando identificadas, apresentam associação temporal com mudanças observadas nas condições climáticas locais?

**RQ3 (aplicação).** Modelos estatísticos e de aprendizado de máquina conseguem prever a incidência de curto prazo dessas arboviroses com desempenho satisfatório, a partir de informações epidemiológicas e climáticas disponíveis até a semana corrente?

O projeto **não pretende estabelecer causalidade** entre mudanças climáticas e comportamento epidemiológico, mas investigar se alterações persistentes nos padrões temporais das arboviroses apresentam associação consistente com mudanças observadas nas condições climáticas.

---

## 1.4 Objetivo geral

Desenvolver um produto analítico baseado em séries temporais capaz de **caracterizar mudanças na dinâmica sazonal de dengue, zika e chikungunya em municípios brasileiros selecionados, investigar sua associação com variáveis climáticas, e produzir previsões de curto prazo como aplicação complementar de apoio à vigilância**.

## 1.5 Objetivos específicos

1. Construir séries temporais semanais de incidência estimada de dengue, zika e chikungunya para municípios brasileiros selecionados, incluindo ao menos um município classificado como "sentinela" segundo os critérios definidos na Seção 5.

2. Integrar os dados epidemiológicos do InfoDengue com variáveis climáticas disponíveis na própria plataforma e, quando necessário, com dados complementares do INMET.

3. Construir indicadores quantitativos de sazonalidade (início, pico, fim, duração e intensidade da temporada) para cada série, conforme definido na Seção 6.2.

4. Decompor cada série temporal em tendência, sazonalidade e resíduo, e aplicar um método de detecção de pontos de mudança sobre a série dessazonalizada.

5. Investigar a associação temporal entre as mudanças identificadas e o comportamento das variáveis climáticas no mesmo período, respeitando a distinção entre associação e causalidade.

6. Desenvolver um modelo estatístico de referência (SARIMAX) para previsão de curto prazo (1 a 4 semanas) da incidência.

7. Desenvolver um modelo de aprendizado de máquina (XGBoost) para o mesmo problema de previsão, e comparar seu desempenho com o modelo estatístico por meio de validação temporal.

8. Identificar semanas em que a incidência observada apresente comportamento atípico em relação ao padrão esperado pelo modelo.

9. Desenvolver um painel analítico que apresente, para cada município e doença, tanto a caracterização histórica e as mudanças identificadas quanto as previsões de curto prazo.

---

# 2. Justificativa

O projeto apresenta contribuições científicas, tecnológicas e sociais.

### Contribuição científica

A proposta busca explorar uma dimensão temporal de longo prazo que é menos enfatizada em aplicações de previsão operacional de curto prazo, investigando de forma comparativa como três arboviroses transmitidas pelo mesmo vetor — mas com diferenças mecanísticas de sensibilidade térmica documentadas na literatura — se comportam ao longo de mais de uma década de dados observacionais reais. O projeto constitui uma aplicação de Ciência de Dados a um problema de ecologia de vetores, estabelecendo uma conexão temática (não metodológica) com o estudo da influência das condições ambientais sobre características funcionais de Diptera.

### Contribuição tecnológica

O diferencial do produto não está apenas na existência de um painel interativo, mas na integração, em uma única ferramenta, de quatro camadas de análise normalmente tratadas de forma isolada: histórico de longo prazo, mudança estrutural, associação climática e previsão de curto prazo.

### Contribuição social

A disponibilização pública do código, da documentação e dos resultados contribuirá para o caráter extensionista da disciplina. A aplicação possui relação direta com o **ODS 11 — Cidades e Comunidades Sustentáveis**, em particular com a Meta 11.b, referente ao aumento do número de cidades com estratégias de gestão de risco e adaptação às mudanças climáticas: municípios que apresentam expansão epidemiológica recente de arboviroses ilustram, de forma concreta, a necessidade de adaptação do planejamento de saúde pública a riscos que antes não faziam parte de sua realidade. O tema também guarda relação com o ODS 3 (Saúde e Bem-Estar) e o ODS 13 (Ação contra a Mudança Global do Clima); como a disciplina exige vínculo com uma das ODS 8, 11 ou 16, o projeto adota a **ODS 11 como ODS principal**.

O produto não terá como finalidade substituir sistemas oficiais de vigilância ou produzir diagnósticos epidemiológicos, mas sim demonstrar como técnicas de Ciência de Dados podem apoiar a interpretação de tendências de longo prazo e de possíveis mudanças no padrão de risco.

---

# 3. Público-alvo e cliente

O usuário primário do produto é a **vigilância epidemiológica municipal** — profissionais responsáveis pelo monitoramento de arboviroses em Secretarias Municipais de Saúde. O usuário secundário são **pesquisadores e estudantes** interessados em séries temporais epidemiológicas e ambientais, o que também orienta decisões de design (ex. disponibilizar uma camada técnica detalhada além da visão executiva).

O produto será desenvolvido considerando como cliente potencial uma **Secretaria Municipal de Saúde**, especialmente o setor responsável pela vigilância epidemiológica. Trata-se, nesta fase, de uma personificação do público-alvo utilizada para orientar o design do produto — a equipe buscará, na medida do possível, validar essa perspectiva com um interlocutor real ou com a literatura sobre necessidades de vigilância municipal, sem que isso seja pré-condição para a conclusão do projeto.

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

CODECO, C.; COELHO, F. C.; CRUZ, O. G.; OLIVEIRA, S. B.; CASTRO, T. G.; BASTOS, L. S. **Infodengue: a nowcasting system for the surveillance of arboviruses in Brazil**. Revue d'Épidémiologie et de Santé Publique, v. 66, supl. 5, p. S386, out. 2018. Disponível em: https://doi.org/10.1016/j.respe.2018.05.408. Acesso em: 1 set. 2026.

CODECO, C. T. et al. **InfoDengue: a nowcasting system for the surveillance of dengue fever transmission**. bioRxiv, 2016. Disponível em: https://www.biorxiv.org/content/10.1101/046193. Acesso em: 1 set. 2026.

FIOCRUZ. **Monitoramento de dengue indica pontos de atenção no Brasil**. Agência Fiocruz de Notícias, 2022. Disponível em: https://agencia.fiocruz.br/monitoramento-de-dengue-indica-pontos-de-atencao-no-brasil. Acesso em: 1 set. 2026.

FGV EMAp. **FGV e Fiocruz monitoram avanço da dengue no Brasil**. 2024. Disponível em: https://emap.fgv.br/en/news/fgv-and-fiocruz-monitor-spread-dengue-fever-brazil. Acesso em: 1 set. 2026.

INFODENGUE. **Sobre nós**. Disponível em: https://info.dengue.mat.br/informacoes/. Acesso em: 1 set. 2026.

INSTITUTO NACIONAL DE METEOROLOGIA (INMET). **Banco de Dados Meteorológicos para Ensino e Pesquisa**. Disponível em: https://portal.inmet.gov.br/dadoshistoricos. Acesso em: 1 set. 2026.

KILLICK, R.; FEARNHEAD, P.; ECKLEY, I. A. **Optimal detection of changepoints with a linear computational cost**. Journal of the American Statistical Association, v. 107, n. 500, p. 1590-1598, 2012. (Referência do método PELT.)

MORDECAI, E. A.; COHEN, J. M.; EVANS, M. V.; GUDAPATI, P.; JOHNSON, L. R.; LIPPI, C. A. et al. **Detecting the impact of temperature on transmission of Zika, dengue, and chikungunya using mechanistic models**. PLOS Neglected Tropical Diseases, v. 11, n. 4, e0005568, 2017. Disponível em: https://doi.org/10.1371/journal.pntd.0005568. Acesso em: 1 set. 2026.

MORDECAI, E. A. et al. **Thermal biology of mosquito-borne disease**. Ecology Letters, v. 22, n. 10, p. 1690-1708, 2019.

CHEN, T.; GUESTRIN, C. **XGBoost: A scalable tree boosting system**. In: Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2016, p. 785-794. (Referência metodológica para XGBoost.)

HYNDMAN, R. J.; ATHANASOPOULOS, G. **Forecasting: principles and practice**. 3. ed. Melbourne: OTexts, 2021. Disponível em: https://otexts.com/fpp3/. Acesso em: 1 set. 2026. (Referência metodológica para SARIMA/SARIMAX, decomposição STL e validação temporal.)

CLEVELAND, R. B.; CLEVELAND, W. S.; MCRAE, J. E.; TERPENNING, I. **STL: A seasonal-trend decomposition procedure based on loess**. Journal of Official Statistics, v. 6, n. 1, p. 3-73, 1990. (Referência metodológica para decomposição STL.)

ORGANIZAÇÃO MUNDIAL DA SAÚDE (OMS/WHO). **Dengue: global situation, surveillance and progress – 2024 update**. Weekly Epidemiological Record, 2025. Disponível em: https://www.who.int/publications/i/item/who-wer10052-665-678. Acesso em: 1 set. 2026.

PLOS NEGLECTED TROPICAL DISEASES. **Seasonal temperature variation influences climate suitability for dengue, chikungunya, and Zika transmission**. PLOS Neglected Tropical Diseases, v. 12, n. 4, e0006451, 2018. Disponível em: https://doi.org/10.1371/journal.pntd.0006451. Acesso em: 1 set. 2026.

PLOS NEGLECTED TROPICAL DISEASES. **Phenotypic variation in populations of the mosquito vector, Aedes aegypti, and implications for predicting the effects of temperature and climate change on dengue transmission**. PLOS Neglected Tropical Diseases, v. 19, 2025. Disponível em: https://doi.org/10.1371/journal.pntd.0013623. Acesso em: 1 set. 2026.

ORGANIZAÇÃO DAS NAÇÕES UNIDAS (ONU). **Objetivos de Desenvolvimento Sustentável — ODS 11: Cidades e Comunidades Sustentáveis**. Disponível em: https://www.undp.org/sustainable-development-goals. Acesso em: 1 set. 2026.

> **Nota**: recomenda-se revisão final das referências com uma ferramenta de formatação ABNT (ex. Mendeley/Zotero com estilo ABNT NBR 6023) antes da entrega definitiva. As referências metodológicas (PELT, STL, XGBoost, SARIMAX) foram adicionadas nesta revisão e devem ser confirmadas quanto a edição/páginas exatas antes da entrega final.

---

# 15. Próximas etapas

**Fase 1 — Dados**: acesso à API do InfoDengue para as três doenças; avaliação de qualidade e completude; seleção dos municípios (incluindo ao menos um sentinela).

**Fase 2 — Séries**: construção das séries temporais; decomposição em tendência/sazonalidade (STL); cálculo dos indicadores de início/pico/fim/duração/intensidade da temporada.

**Fase 3 — Mudanças**: aplicação do método PELT sobre as séries dessazonalizadas; identificação e validação de plausibilidade dos pontos de mudança.

**Fase 4 — Clima**: seleção de variáveis climáticas prioritárias (temperatura, precipitação); teste de defasagens (0–4 semanas, com possível extensão); avaliação de associação temporal com as mudanças identificadas na Fase 3.

**Fase 5 — Previsão**: implementação de SARIMAX e XGBoost; validação temporal em janela expansiva; comparação de desempenho (MAE, RMSE, sMAPE); definição do mecanismo de detecção de anomalias.

**Fase 6 — Produto**: construção do painel analítico (7 abas); documentação; disponibilização do código e dos dados no GitHub.
