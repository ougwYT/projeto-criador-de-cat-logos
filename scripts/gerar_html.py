import re
import unicodedata
from html import escape
from pathlib import Path

import pandas as pd

CSV_ENTRADA = "dados/produtos_com_imagem.csv"

HTML_SAIDA = "docs/index.html"

PASTA_IMAGENS_HTML = "imagens_nomeadas_corretamente"
LOGO = "assets/logo.png"
QRCODE = "assets/qrcode_whatsapp.png"

ORDEM_CATEGORIAS = [
    "ELETRICA",
    "FERRAMENTAS",
    "HIDRAULICA",
    "UTILIDADES",
    "SEM GRUPO"
]


SITE = "https://www.nucleuomnis.com.br/senafix/index.php"
WHATSAPP_NUMERO = "5511939593526"
WHATSAPP_LINK = f"https://wa.me/{WHATSAPP_NUMERO}"


def converter_preco(valor):
    try:
        return float(valor)
    except (ValueError, TypeError):
        return 0.0


def formatar_preco_brasil(preco):
    return (
        f"{preco:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def build_card(row):
    codigo = str(row.get("codigo", "")).strip()
    produto = str(row.get("produto", "")).strip()
    imagem = str(row.get("imagem", "")).strip()

    preco = converter_preco(
        row.get("preco_atacado", "")
    )
    preco_formatado = formatar_preco_brasil(preco)
    unidade = str(row.get("unidade", "")).strip().upper()
    texto_preco = "Preço"
    if unidade == "CT":
        texto_preco = "Preço do cento"
    caminho_imagem = f"{PASTA_IMAGENS_HTML}/{imagem}"
    preco_html = ""

    if preco > 0:

        preco_html = f"""
        <div class="preco">
        <span>{texto_preco}</span>
        <strong>R$ {preco_formatado}</strong>
    </div>
        """

    return f"""
    <article class="card">

        <div class="card-img">
            <img src="{escape(caminho_imagem)}" alt="{escape(produto)}">
        </div>

        <div class="card-body">

            <p class="codigo">
                Código {escape(codigo)}
            </p>

            <h2 class="nome">
                {escape(produto)}
            </h2>

            
                {preco_html}
            

        </div>

    </article>
    """


def gerar_id_categoria(categoria):
    texto = str(categoria).lower()

    texto = unicodedata.normalize(
        "NFKD",
        texto
    )

    texto = texto.encode(
        "ascii",
        "ignore"
    ).decode("utf-8")

    texto = re.sub(
        r"[^a-z0-9]+",
        "-",
        texto
    )

    return texto.strip("-")


df = pd.read_csv(CSV_ENTRADA).fillna("")

if "catalogo" in df.columns:
    df = df[
        df["catalogo"]
        .astype(str)
        .str.upper()
        .str.strip() == "SIM"
    ]

df = df[
    df["imagem"]
    .astype(str)
    .str.strip() != ""
]

df = df[
    df["imagem"]
    .astype(str)
    .str.lower()
    .str.strip() != "nan"
]

# ==========================================
# ESTATÍSTICAS DA CAPA
# ==========================================

total_produtos_catalogo = len(df)

total_categorias = (
    df["categoria"].nunique()
    if "categoria" in df.columns
    else 0
)

html_categorias = []


if "categoria" in df.columns:

    for categoria in ORDEM_CATEGORIAS:

        grupo = df[
            df["categoria"] == categoria
        ]

        if grupo.empty:
            continue

        cards_categoria = []

        for _, row in grupo.iterrows():

            cards_categoria.append(
                build_card(row)
            )

        bloco_categoria = f"""




<section
    class="capa-categoria"
    id="categoria-{gerar_id_categoria(categoria)}"
    data-categoria="{categoria}"
>

    <h1>
        {escape(str(categoria))}
    </h1>

</section>

<section class="categoria-bloco"  data-categoria="{categoria}">

    <div class="catalogo">

        {''.join(cards_categoria)}

    </div>

</section>

"""

        html_categorias.append(
            bloco_categoria
        )

    total_produtos_catalogo = len(df)

    total_categorias = (
        df["categoria"].nunique()
        if "categoria" in df.columns
        else 0
    )

else:

    cards = []

    for _, row in df.iterrows():

        cards.append(
            build_card(row)
        )

    html_categorias.append(
        f"""
<section class="catalogo">
{''.join(cards)}
</section>
"""
    )


indice_itens = []

for categoria in ORDEM_CATEGORIAS:
    if "categoria" in df.columns:
        grupo = df[df["categoria"] == categoria]
        if grupo.empty:
            continue

    indice_itens.append(
        f"""
        <li>
            <a href="#categoria-{gerar_id_categoria(categoria)}">
                {escape(categoria)}
            </a>
        </li>
        """
    )

indice = f"""
<section class="indice-catalogo">

    <h1>Índice</h1>

    <ol>
        {''.join(indice_itens)}
    </ol>

</section>
"""
capa = f"""
<section class="capa-catalogo">

    <div class="capa-conteudo">

        <img src="{LOGO}" alt="Senna Fix" class="logo-capa">

        <h1>Catálogo Senna Fix</h1>

        <p class="subtitulo-capa">
            Ferramentas • Elétrica • Fixação • Pintura • Utilidades
        </p>

        <div class="contato-capa">
            <p>WhatsApp: (11) 93959-3526</p>
            <p>https://www.nucleuomnis.com.br/senafix/index.php</p>
        </div>
        <div class="estatisticas-capa">
    <div>
        <strong>{total_produtos_catalogo}</strong>
        <span>Produtos</span>
    </div>

    <div>
        <strong>{total_categorias}</strong>
        <span>Categorias</span>
    </div>
</div>
        
        
        
        <div class="qr-container">
        
        <img src="{QRCODE}" alt="QR Code WhatsApp">
        <p>Escaneie para solicitar orçamento</p>
        
        </div>

    </div>

</section>
"""
pagina_final = f"""

<section class="pagina-final">

    <div class="pagina-final-conteudo">

        <img src="{LOGO}" alt="Senna Fix" class="logo-final">

        <h1>Senna Fix</h1>

        <p>
            Distribuidora de materiais elétricos, ferramentas,
            hidráulica e utilidades.
        </p>

        <div class="pagina-final-contato">
            <p>WhatsApp: (11) 93959-3526</p>
            <p>Site: {SITE}</p>
        </div>

        <div class="qr-container">
            <img src="{QRCODE}" alt="QR Code WhatsApp">
            <p>Escaneie para solicitar orçamento</p>
        </div>
        <div class="slogan-final">
    Qualidade, variedade e confiança para o seu negócio.
    </div>

    </div>

</section>
"""
botoes_categoria = []

for categoria in ORDEM_CATEGORIAS:

    if "categoria" in df.columns:
        grupo = df[df["categoria"] == categoria]

        if grupo.empty:
            continue

    botoes_categoria.append(
        f"""
        <a href="#categoria-{gerar_id_categoria(categoria)}" class="btn-categoria">
            {escape(categoria)}
        </a>
        """
    )
html = f"""<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="utf-8">
    <title>Catálogo Senna Fix</title>
    <link rel="stylesheet" href="style.css">
    <link rel="icon" type="image/png" href="assets/logo_redondo.png">
</head>

<body id="topo">

{capa}

{indice}

<header class="topo-catalogo">
    <a href="#inicial_page">
        <img src="{LOGO}" alt="Senna Fix" class="logo-catalogo">
    </a>
</header>

<section class="hero-catalogo" id="inicial_page">

    <h1>Catálogo Senna Fix</h1>

    <p>Ferramentas, elétrica, hidráulica e utilidades.</p>

    <a href="{WHATSAPP_LINK}" class="botao-whatsapp" target="_blank">
        Solicitar orçamento pelo WhatsApp
    </a>




    <div class="filtros-categoria">

        {''.join(botoes_categoria)}

    </div>

</section>

{''.join(html_categorias)}
{pagina_final}



</body>

</html>
"""
Path("catalogo").mkdir(exist_ok=True)
with open(HTML_SAIDA, "w", encoding="utf-8") as arquivo:
    arquivo.write(html)

print()
print("=" * 50)
print("HTML gerado.")
print(f"Produtos no catálogo: {len(df)}")
print("=" * 50)
