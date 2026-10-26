
from pathlib import Path
import pandas as pd

# ============================================================
# CAMINHOS DO PROJETO
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
PASTA_RAW = BASE_DIR / "data" / "raw"
PASTA_PROCESSED = BASE_DIR / "data" / "processed"
PASTA_REPORTS = BASE_DIR / "reports"

PASTA_REPORTS.mkdir(parents=True, exist_ok=True)


# ============================================================
# FUNÇÕES DE CONVERSÃO E CALENDÁRIO
# ============================================================

def converter_datas(df):
    """Converte datas e remove eventual componente de horário."""
    return pd.to_datetime(
        df["data_iniSE"],
        errors="coerce"
    ).dt.normalize()


def converter_semanas(serie):
    """Converte SE para número, preservando valores ausentes."""
    return pd.to_numeric(serie, errors="coerce")


def primeiro_domingo_epi(ano):
    """
    Retorna o domingo da semana epidemiológica 1.

    A semana 1 é a semana que contém 4 de janeiro.
    As semanas começam no domingo e terminam no sábado.
    """
    quatro_janeiro = pd.Timestamp(f"{ano}-01-04")
    deslocamento = (quatro_janeiro.weekday() + 1) % 7

    return quatro_janeiro - pd.Timedelta(days=deslocamento)


def calendario_epidemiologico(ano):
    """
    Cria o calendário de semanas epidemiológicas do ano.

    Retorna um dicionário:
        data de início -> código SE
    """
    inicio = primeiro_domingo_epi(ano)
    fim = primeiro_domingo_epi(ano + 1)

    datas = pd.date_range(
        start=inicio,
        end=fim,
        freq="7D",
        inclusive="left"
    )

    return {
        data: ano * 100 + numero
        for numero, data in enumerate(datas, start=1)
    }


def ano_epidemiologico(se):
    """
    Extrai o ano epidemiológico do código SE.

    Exemplo:
        202401 -> 2024
    """
    if pd.isna(se):
        return None

    valor = int(se)

    if valor < 10000 or valor > 999999:
        return None

    ano = valor // 100
    semana = valor % 100

    if semana < 1 or semana > 53:
        return None

    return ano


# ============================================================
# AUDITORIA DE UM ARQUIVO
# ============================================================

def auditar_arquivo(df, ano_arquivo, nome):
    """
    Audita um arquivo considerando o ano epidemiológico da SE.

    Registros de anos adjacentes são preservados e contabilizados
    separadamente. Eles não são tratados automaticamente como
    semanas extras do ano do arquivo.
    """
    prefixo = nome

    resultado = {
        f"{prefixo}_registros": len(df),
        f"{prefixo}_datas_invalidas": None,
        f"{prefixo}_datas_duplicadas": None,
        f"{prefixo}_SE_invalidas": None,
        f"{prefixo}_SE_duplicadas": None,
        f"{prefixo}_semanas_faltantes": None,
        f"{prefixo}_datas_extras": None,
        f"{prefixo}_SE_divergentes": None,
        f"{prefixo}_registros_SE_ano_alvo": None,
        f"{prefixo}_registros_SE_outros_anos": None,
        f"{prefixo}_colunas_ausentes": False,
    }

    colunas_necessarias = {"data_iniSE", "SE"}

    if not colunas_necessarias.issubset(df.columns):
        resultado[f"{prefixo}_colunas_ausentes"] = True

        faltantes = colunas_necessarias - set(df.columns)
        resultado[f"{prefixo}_colunas_ausentes_lista"] = ", ".join(
            sorted(faltantes)
        )

        return resultado, {}

    datas = converter_datas(df)
    semanas = converter_semanas(df["SE"])

    resultado[f"{prefixo}_datas_invalidas"] = int(
        datas.isna().sum()
    )

    resultado[f"{prefixo}_datas_duplicadas"] = int(
        datas.dropna().duplicated().sum()
    )

    resultado[f"{prefixo}_SE_invalidas"] = int(
        semanas.isna().sum()
    )

    resultado[f"{prefixo}_SE_duplicadas"] = int(
        semanas.dropna().duplicated().sum()
    )

    # Calendário oficial esperado para o ano analisado.
    calendario = calendario_epidemiologico(ano_arquivo)
    datas_esperadas = set(calendario.keys())

    # Determina o ano epidemiológico de cada registro pela SE.
    anos_se = semanas.map(ano_epidemiologico)

    do_ano = anos_se == ano_arquivo

    resultado[f"{prefixo}_registros_SE_ano_alvo"] = int(
        do_ano.sum()
    )

    resultado[f"{prefixo}_registros_SE_outros_anos"] = int(
        (anos_se.notna() & (anos_se != ano_arquivo)).sum()
    )

    # Valida apenas as semanas atribuídas ao ano analisado.
    datas_ano = set(
        datas[do_ano & datas.notna()]
    )

    datas_extras = datas_ano - datas_esperadas
    datas_faltantes = datas_esperadas - datas_ano

    resultado[f"{prefixo}_semanas_faltantes"] = len(
        datas_faltantes
    )

    resultado[f"{prefixo}_datas_extras"] = len(
        datas_extras
    )

    # Compara a SE informada com a esperada para a data.
    divergencias = 0

    for data, se, ano_se in zip(datas, semanas, anos_se):
        if pd.isna(data) or pd.isna(se):
            continue

        # Registros de anos adjacentes são preservados.
        # Só comparamos com o calendário do ano analisado
        # quando a SE atribui o registro a esse ano.
        if ano_se == ano_arquivo:
            se_esperada = calendario.get(data)

            if se_esperada is None or int(se) != se_esperada:
                divergencias += 1

    resultado[f"{prefixo}_SE_divergentes"] = divergencias

    # Mapa de datas para códigos SE, usado na comparação
    # entre o original e o processado.
    mapa = {}

    for data, se in zip(datas, semanas):
        if pd.isna(data):
            continue

        # Preserva o primeiro valor para permitir detectar
        # duplicações separadamente, sem sobrescrever o mapa.
        if data not in mapa:
            mapa[data] = se

    return resultado, mapa


# ============================================================
# LOCALIZAÇÃO DOS ARQUIVOS
# ============================================================

arquivos = sorted(PASTA_PROCESSED.glob("*.csv"))

if not arquivos:
    raise FileNotFoundError(
        f"Nenhum CSV encontrado em: {PASTA_PROCESSED}"
    )


# ============================================================
# EXECUÇÃO DA AUDITORIA
# ============================================================

resultados = []

for arquivo_proc in arquivos:
    arquivo_raw = PASTA_RAW / arquivo_proc.name

    if not arquivo_raw.exists():
        resultados.append({
            "arquivo": arquivo_proc.name,
            "status": "ORIGINAL_AUSENTE",
        })
        continue

    try:
        ano = int(arquivo_proc.stem.split("_")[-1])
    except ValueError:
        resultados.append({
            "arquivo": arquivo_proc.name,
            "status": "ANO_INVALIDO_NO_NOME",
        })
        continue

    raw = pd.read_csv(arquivo_raw)
    proc = pd.read_csv(arquivo_proc)

    calendario = calendario_epidemiologico(ano)

    linha = {
        "arquivo": arquivo_proc.name,
        "ano_arquivo": ano,
        "semanas_esperadas": len(calendario),
        "primeira_data_esperada": min(calendario).date(),
        "ultima_data_esperada": max(calendario).date(),
    }

    # Audita dados originais e processados.
    auditoria_raw, mapa_raw = auditar_arquivo(
        raw, ano, "raw"
    )

    auditoria_proc, mapa_proc = auditar_arquivo(
        proc, ano, "processed"
    )

    linha.update(auditoria_raw)
    linha.update(auditoria_proc)

    # Compara os códigos SE das datas presentes nos dois arquivos.
    datas_comuns = set(mapa_raw) & set(mapa_proc)

    linha["SE_diferentes_raw_processed"] = sum(
        pd.isna(mapa_raw[data])
        or pd.isna(mapa_proc[data])
        or mapa_raw[data] != mapa_proc[data]
        for data in datas_comuns
    )

    # Registros que existem no original e não no processado,
    # ou que foram adicionados durante o processamento.
    linha["datas_removidas_raw_para_processed"] = len(
        set(mapa_raw) - set(mapa_proc)
    )

    linha["datas_adicionadas_no_processed"] = len(
        set(mapa_proc) - set(mapa_raw)
    )

    # Critérios para classificação do arquivo.
    campos_criticos = [
        "processed_datas_invalidas",
        "processed_datas_duplicadas",
        "processed_SE_invalidas",
        "processed_SE_duplicadas",
        "processed_semanas_faltantes",
        "processed_datas_extras",
        "processed_SE_divergentes",
        "raw_SE_divergentes",
    ]

    problema = (
        auditoria_raw.get("raw_colunas_ausentes", False)
        or auditoria_proc.get("processed_colunas_ausentes", False)
    )

    for campo in campos_criticos:
        valor = linha.get(campo)

        if isinstance(valor, (int, float)) and valor > 0:
            problema = True

    if linha["SE_diferentes_raw_processed"] > 0:
        problema = True

    linha["status"] = "VERIFICAR" if problema else "OK"

    resultados.append(linha)


# ============================================================
# SALVAMENTO DO RELATÓRIO
# ============================================================

relatorio = pd.DataFrame(resultados)

caminho_saida = PASTA_REPORTS / "auditoria_semanas.csv"

relatorio.to_csv(
    caminho_saida,
    index=False,
    encoding="utf-8-sig"
)


# ============================================================
# RESUMO NO TERMINAL
# ============================================================

print("=" * 60)
print("AUDITORIA DA COBERTURA SEMANAL")
print("=" * 60)

print(f"Arquivos encontrados: {len(arquivos)}")
print(f"Arquivos auditados: {len(relatorio)}")

print("\nResumo dos status:")
print(relatorio["status"].value_counts(dropna=False))

problemas = relatorio[relatorio["status"] != "OK"]

print("\nArquivos que precisam de atenção:")

if problemas.empty:
    print("Nenhum problema detectado pelas regras aplicadas.")
else:
    colunas_resumo = [
        "arquivo",
        "ano_arquivo",
        "raw_registros",
        "processed_registros",
        "processed_registros_SE_ano_alvo",
        "processed_registros_SE_outros_anos",
        "processed_semanas_faltantes",
        "processed_datas_extras",
        "processed_SE_divergentes",
        "processed_SE_duplicadas",
        "SE_diferentes_raw_processed",
        "status",
    ]

    colunas_disponiveis = [
        c for c in colunas_resumo if c in problemas.columns
    ]

    print(
        problemas[colunas_disponiveis].to_string(index=False)
    )

print(f"\nRelatório salvo em:\n{caminho_saida}")

print(
    "\nObservação: registros de anos epidemiológicos adjacentes "
    "são preservados. A auditoria verifica a cobertura do ano "
    "indicado no nome do arquivo usando o código SE."
)
