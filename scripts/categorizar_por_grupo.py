import re
from pathlib import Path

import pandas as pd
import pdfplumber

CSV_PRODUTOS = "dados/produtos.csv"
CSV_SAIDA = "dados/produtos_categorizados.csv"

ARQUIVOS_GRUPOS = {
    "ELETRICA": "entrada/grupos/grupo_eletrica.pdf",
    "FERRAMENTAS": "entrada/grupos/grupo_ferramentas.pdf",
    "HIDRAULICA": "entrada/grupos/grupo_hidraulica.pdf",
    "UTILIDADES": "entrada/grupos/grupos_utilidades.pdf",
}


def extrair_codigos_pdf(caminho_pdf):
    codigos = set()

    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()

            if not texto:
                continue

            for linha in texto.splitlines():
                linha = linha.strip()

                resultado = re.match(r"^(\d+)\s+", linha)

                if resultado:
                    codigos.add(resultado.group(1))

    return codigos


mapa_categoria = {}

for categoria, caminho in ARQUIVOS_GRUPOS.items():
    caminho_pdf = Path(caminho)

    if not caminho_pdf.exists():
        print(f"Arquivo não encontrado: {caminho_pdf}")
        continue

    codigos = extrair_codigos_pdf(caminho_pdf)

    for codigo in codigos:
        mapa_categoria[codigo] = categoria

    print(f"{categoria}: {len(codigos)} produtos")


df = pd.read_csv(CSV_PRODUTOS, dtype=str).fillna("")

df["codigo"] = df["codigo"].astype(str).str.strip()

df["categoria"] = df["codigo"].map(mapa_categoria).fillna("SEM GRUPO")

df.to_csv(
    CSV_SAIDA,
    index=False,
    encoding="utf-8-sig"
)

print()
print("=" * 50)
print("Produtos categorizados por grupo.")
print(df["categoria"].value_counts())
print("=" * 50)
