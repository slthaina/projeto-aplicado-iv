"""Configuração central do projeto: municípios, doenças e períodos."""
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
DIR_RAW = RAIZ / "data" / "raw" / "epidemio"
DIR_LOGS = RAIZ / "outputs" / "logs"

# Um município por região (código IBGE de 7 dígitos)
MUNICIPIOS = {
    5300108: "Brasilia_DF",       # Centro-Oeste
    1302603: "Manaus_AM",         # Norte
    4314902: "Porto_Alegre_RS",   # Sul
    2611606: "Recife_PE",         # Nordeste
    3550308: "Sao_Paulo_SP",      # Sudeste
}

DOENCAS = ["dengue", "chikungunya", "zika"]

# Períodos (ano inicial, ano final), ambos inclusivos
PERIODOS = {
    "2010_2014": (2010, 2014),
    "2015_2019": (2015, 2019),
    "2020_2024": (2020, 2024),
}

# API pública do InfoDengue (alertcity)
URL_API = "https://info.dengue.mat.br/api/alertcity"
PAUSA_SEGUNDOS = 2
TENTATIVAS = 3
TIMEOUT = 120