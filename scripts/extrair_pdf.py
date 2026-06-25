import re
from pathlib import Path

import pandas as pd
import pdfplumber

PATH_ = Path().parent

PDF_PATH = PATH_ / "entrada" / "lista_de_produtos" / "lista_de_produtos_8.pdf"

RAW_CSV = "dados/produtos_raw.csv"
CSV_FINAL = "dados/produtos.csv"

# ==========================================
# REGEX
# ==========================================

padrao = re.compile(
    r'^(\d+)\s+(.*?)\s+(-?\d+,\d+)\s+(UN|CT|PC|CX|CE|COLLINS)\s+(-?\d+,\d+)\s+(-?\d+,\d+)\s*(.*)$'
)
# ==========================================
# FUNÇÕES
# ==========================================


def limpar(valor):

    if valor is None:
        return ""

    return str(valor).strip()


# ==========================================
# EXTRAÇÃO DO PDF
# ==========================================

linhas = []

with pdfplumber.open(PDF_PATH) as pdf:

    for pagina in pdf.pages:

        texto = pagina.extract_text()

        if not texto:
            continue

        linhas.extend(
            texto.splitlines()
        )

# ==========================================
# SALVA RAW
# ==========================================

pd.DataFrame(
    {"linha": linhas}
).to_csv(
    RAW_CSV,
    index=False,
    encoding="utf-8-sig"
)

print(f"RAW salvo com {len(linhas)} linhas.")
print("\nPRIMEIRAS 20 LINHAS:\n")


# ==========================================
# TESTE DA REGEX
# ==========================================
for linha in linhas:

    resultado = padrao.match(
        linha.strip()
    )

    if resultado:
        print(resultado.groups())
        break

# ==========================================
# PROCESSAMENTO
# ==========================================
produtos = []

produtos = []

for linha in linhas:

    linha = limpar(linha)

    resultado = padrao.match(
        linha.strip()
    )

    if not resultado:
        continue

    codigo = resultado.group(1)
    descricao = limpar(resultado.group(2))
    saldo = resultado.group(3)
    unidade = resultado.group(4)
    atacado = resultado.group(5)
    varejo = resultado.group(6)
    fornecedor = limpar(resultado.group(7))

    descricao = re.sub(
        r"^\-\s*",
        "",
        descricao
    )

    if len(descricao) < 3:
        continue

    atacado = float(
        atacado.replace(".", "")
               .replace(",", ".")
    )

    varejo = float(
        varejo.replace(".", "")
              .replace(",", ".")
    )

    produtos.append({
        "codigo": codigo,
        "produto": descricao,
        "saldo": saldo,
        "unidade": unidade,
        "preco_atacado": atacado,
        "preco_varejo": varejo,
        "fornecedor": fornecedor
    })
# ==========================================
# DATAFRAME FINAL
# ==========================================

print()
print("Produtos capturados:", len(produtos))

df = pd.DataFrame(produtos)

df.to_csv(
    CSV_FINAL,
    index=False,
    encoding="utf-8-sig"
)

print()
print("=" * 50)
print(f"{len(df)} produtos encontrados.")
print(f"CSV salvo em: {CSV_FINAL}")
print("=" * 50)
# for linha in linhas:

#     if "PARAFUSO CHIP" in linha:
#         print(repr(linha))
