import json
import os
import re
from pathlib import Path

import pandas as pd

CSV_PRODUTOS = "dados/produtos_categorizados.csv"

CSV_SAIDA = "dados/produtos_com_imagem.csv"

PASTA_IMAGENS = Path().parent / 'docs' / "imagens_nomeadas_corretamente"

JSON_EXCLUIDOS = "config/produtos_excluidos.json"


# ==========================
# INDEXA IMAGENS
# ==========================

mapa_imagens = {}

for arquivo in os.listdir(PASTA_IMAGENS):

    if not arquivo.lower().endswith(
        (".jpg", ".jpeg", ".png", ".webp")
    ):
        continue

    match = re.match(
        r"(\d+)_",
        arquivo
    )

    if not match:
        continue

    codigo = match.group(1)

    mapa_imagens[codigo] = arquivo


# ==========================
# CARREGA PRODUTOS
# ==========================

df = pd.read_csv(
    CSV_PRODUTOS,
    dtype=str
)

if os.path.exists(JSON_EXCLUIDOS):
    with open(JSON_EXCLUIDOS, "r", encoding="utf-8") as arquivo:
        produtos_excluidos = json.load(arquivo)
else:
    produtos_excluidos = {}

resultado = []
catalogo_status = []
encontradas = 0

for _, row in df.iterrows():

    codigo = str(
        row["codigo"]
    ).strip()
    catalogo = "NAO" if codigo in produtos_excluidos else "SIM"

    imagem = mapa_imagens.get(
        codigo,
        ""
    )

    if imagem:
        encontradas += 1

    resultado.append(imagem)
    catalogo_status.append(catalogo)


df["imagem"] = resultado
df["catalogo"] = catalogo_status
faltantes = df[df["imagem"].fillna("").astype(str).str.strip() == ""]

faltantes.to_csv(
    "dados/produtos_sem_imagem.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Arquivo gerado: dados/produtos_sem_imagem.csv")


df.to_csv(
    CSV_SAIDA,
    index=False,
    encoding="utf-8-sig"
)

print()
print("=" * 50)
print(f"Produtos: {len(df)}")
print(f"Imagens encontradas: {encontradas}")
print(f"Imagens faltando: {len(df)-encontradas}")
print("=" * 50)
