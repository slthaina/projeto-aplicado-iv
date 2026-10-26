
from pathlib import Path
import shutil

# Pasta principal do projeto
raiz = Path.cwd()

# Pasta onde estão as figuras originais
origem = raiz / "arquivos_projeto" / "data" / "processed"

# Pasta de destino
destino = raiz / "figuras"
destino.mkdir(parents=True, exist_ok=True)

if not origem.exists():
    print(f"Pasta de origem não encontrada: {origem}")
    print("Confira se o terminal está na pasta principal do projeto.")
    raise SystemExit(1)

# Localizar imagens PNG
imagens = list(origem.glob("*.png"))

if not imagens:
    print(f"Nenhum arquivo PNG encontrado em: {origem}")
    print("Confira se as imagens estão nessa pasta ou em subpastas.")
    raise SystemExit(0)

for imagem in imagens:
    arquivo_destino = destino / imagem.name
    shutil.copy2(imagem, arquivo_destino)
    print(f"Copiado: {imagem.name}")

print(f"\nTotal de imagens copiadas: {len(imagens)}")
print(f"Destino: {destino}")
