"""
Coleta epidemiológica (InfoDengue) por município x doença x período.

- Um arquivo CSV por combinação, salvo exatamente como a API devolveu.
- Se o arquivo já existe, é pulado (a coleta pode ser retomada e nunca sobrescreve).
- Cada tentativa é registrada em um log (data/hora, parâmetros, status, nº de linhas).
- "Sem linhas" (a API não devolveu semanas) fica registrado separadamente de
  "linhas com casos = 0" (a API devolveu a semana com zero casos).
"""
import csv
import io
import sys
import time
from datetime import datetime
from pathlib import Path

import requests

sys.path.append(str(Path(__file__).resolve().parent.parent))
import config as cfg


def baixar(geocode, doenca, ano_ini, ano_fim):
    params = {
        "geocode": geocode,
        "disease": doenca,
        "format": "csv",
        "ew_start": 1,
        "ew_end": 53,
        "ey_start": ano_ini,
        "ey_end": ano_fim,
    }
    ultimo_erro = ""
    for tentativa in range(1, cfg.TENTATIVAS + 1):
        try:
            r = requests.get(cfg.URL_API, params=params, timeout=cfg.TIMEOUT)
            if r.status_code == 200:
                return r.text, "ok", ""
            ultimo_erro = f"HTTP {r.status_code}"
        except requests.RequestException as e:
            ultimo_erro = str(e)[:200]
        time.sleep(cfg.PAUSA_SEGUNDOS * tentativa * 2)
    return None, "falha", ultimo_erro


def contar_linhas(texto):
    leitor = csv.reader(io.StringIO(texto))
    return max(sum(1 for _ in leitor) - 1, 0)  # desconta o cabeçalho


def main():
    cfg.DIR_LOGS.mkdir(parents=True, exist_ok=True)
    caminho_log = cfg.DIR_LOGS / "log_coleta_epidemio.csv"
    novo_log = not caminho_log.exists()

    combinacoes = [
        (g, nome, d, p, a, b)
        for g, nome in cfg.MUNICIPIOS.items()
        for d in cfg.DOENCAS
        for p, (a, b) in cfg.PERIODOS.items()
    ]
    print(f"{len(combinacoes)} combinações a verificar.")

    with open(caminho_log, "a", newline="", encoding="utf-8") as f_log:
        log = csv.writer(f_log)
        if novo_log:
            log.writerow(["data_hora", "geocode", "municipio", "doenca",
                          "periodo", "status", "n_linhas", "detalhe"])

        for i, (geocode, nome, doenca, periodo, a, b) in enumerate(combinacoes, 1):
            pasta = cfg.DIR_RAW / doenca
            pasta.mkdir(parents=True, exist_ok=True)
            destino = pasta / f"{geocode}_{nome}_{doenca}_{periodo}.csv"
            rotulo = f"[{i}/{len(combinacoes)}] {nome} | {doenca} | {periodo}"

            if destino.exists():
                print(f"{rotulo}: já existe, pulando")
                continue

            texto, status, detalhe = baixar(geocode, doenca, a, b)
            agora = datetime.now().isoformat(timespec="seconds")

            if status == "ok":
                n = contar_linhas(texto)
                destino.write_text(texto, encoding="utf-8")
                if n == 0:
                    status, detalhe = "sem_linhas", "API respondeu sem semanas"
                print(f"{rotulo}: {status} ({n} linhas)")
                log.writerow([agora, geocode, nome, doenca, periodo, status, n, detalhe])
            else:
                print(f"{rotulo}: FALHA ({detalhe})")
                log.writerow([agora, geocode, nome, doenca, periodo, status, "", detalhe])

            f_log.flush()
            time.sleep(cfg.PAUSA_SEGUNDOS)

    print("Fim. Rode de novo para tentar apenas o que falhou.")


if __name__ == "__main__":
    main()