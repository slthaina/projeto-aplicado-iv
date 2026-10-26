
import os
import time
from pathlib import Path

import pandas as pd
import requests
from dotenv import load_dotenv

# Configuração do projeto
RAIZ = Path(__file__).resolve().parent.parent
PASTA_RAW = RAIZ / "data" / "raw"
PASTA_RAW.mkdir(parents=True, exist_ok=True)

load_dotenv(RAIZ / ".env")
API_KEY = os.getenv("MOSQLIMATE_API_KEY")
URL = "https://api.mosqlimate.org/api/datastore/infodengue"

CAPITAIS = {
    "manaus": 1302603,
    "recife": 2611606,
    "brasilia": 5300108,
    "sao_paulo": 3550308,
    "porto_alegre": 4314902,
}

DOENCAS = ["dengue", "zika", "chikungunya"]
ANOS = [2022, 2023]
PER_PAGE = 100
MAX_TENTATIVAS = 4


def consultar_api(doenca, cidade, geocode, ano):
    parametros = {
        "disease": doenca,
        "start": f"{ano}-01-01",
        "end": f"{ano + 1}-01-01",
        "geocode": geocode,
        "page": 1,
        "per_page": PER_PAGE,
    }

    registros = []
    total_paginas = None

    while True:
        resposta = None

        for tentativa in range(1, MAX_TENTATIVAS + 1):
            try:
                resposta = requests.get(
                    URL,
                    params=parametros,
                    headers={"X-UID-Key": API_KEY},
                    timeout=60,
                )
                resposta.raise_for_status()
                break
            except requests.RequestException as erro:
                if tentativa == MAX_TENTATIVAS:
                    raise RuntimeError(
                        f"Falha na consulta: {doenca}, {cidade}, {ano}, "
                        f"página {parametros['page']}: {erro}"
                    ) from erro
                time.sleep(2 * tentativa)

        dados = resposta.json()

        if not isinstance(dados, dict) or not isinstance(
            dados.get("items"), list
        ):
            raise RuntimeError(
                f"Resposta inesperada da API para {doenca}, {cidade}, {ano}: "
                f"{str(dados)[:500]}"
            )

        paginacao = dados.get("pagination", {})
        paginas = paginacao.get("total_pages", 1)

        if not isinstance(paginas, int) or paginas < 1:
            raise RuntimeError(
                f"Paginação inválida para {doenca}, {cidade}, {ano}: "
                f"{paginacao}"
            )

        if total_paginas is None:
            total_paginas = paginas
        elif paginas != total_paginas:
            raise RuntimeError(
                f"Total de páginas mudou durante a consulta: "
                f"{doenca}, {cidade}, {ano}"
            )

        registros.extend(dados["items"])

        print(
            f"  Página {parametros['page']}/{total_paginas} | "
            f"registros acumulados: {len(registros)}"
        )

        if parametros["page"] >= total_paginas:
            break

        parametros["page"] += 1
        time.sleep(0.2)

    return registros


def main():
    if not API_KEY:
        raise SystemExit(
            "Chave MOSQLIMATE_API_KEY não encontrada no arquivo .env."
        )

    total = len(DOENCAS) * len(CAPITAIS) * len(ANOS)
    concluidos = 0
    falhas = []

    print(f"Coletas planejadas: {total}")
    print("Os CSVs existentes com o mesmo nome serão substituídos.")

    for doenca in DOENCAS:
        for cidade, geocode in CAPITAIS.items():
            for ano in ANOS:
                nome = f"{doenca}_{cidade}_{ano}.csv"
                destino = PASTA_RAW / nome

                print(f"\n[{concluidos + 1}/{total}] {nome}")

                try:
                    registros = consultar_api(
                        doenca, cidade, geocode, ano
                    )

                    if not registros:
                        print(
                            "ERRO: API retornou zero registros. "
                            "Nenhum CSV foi gravado para esta consulta."
                        )
                        falhas.append(nome)
                        continue

                    df = pd.DataFrame(registros)

                    if "data_iniSE" not in df.columns:
                        print(
                            "ERRO: resposta sem coluna data_iniSE. "
                            "Nenhum CSV foi gravado."
                        )
                        falhas.append(nome)
                        continue

                    # Salva a resposta original, sem completar semanas,
                    # preencher casos com zero ou filtrar datas.
                    df.to_csv(
                        destino,
                        index=False,
                        encoding="utf-8-sig",
                    )

                    print(
                        f"Salvo: {nome} | registros: {len(df)} | "
                        f"colunas: {len(df.columns)}"
                    )
                    concluidos += 1

                except Exception as erro:
                    print(f"FALHA: {nome} | {erro}")
                    falhas.append(nome)

    print("\n===== RESUMO DA COLETA =====")
    print(f"Coletas planejadas: {total}")
    print(f"Arquivos salvos: {concluidos}")
    print(f"Consultas com falha: {len(falhas)}")

    if falhas:
        print("Verificar estes arquivos/consultas:")
        for nome in falhas:
            print(f" - {nome}")
        raise SystemExit(1)

    print("Coleta finalizada sem falhas registradas.")


if __name__ == "__main__":
    main()
