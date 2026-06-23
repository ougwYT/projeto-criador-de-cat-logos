

from pathlib import Path

from playwright.sync_api import sync_playwright

HTML_PATH = Path("docs/index.html").resolve()
PDF_PATH = Path("docs/catalogo_sennafix.pdf").resolve()

print("HTML usado:", HTML_PATH)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    try:
        page = browser.new_page(
            viewport={
                "width": 1440,
                "height": 2000
            }
        )

        page.goto(
            HTML_PATH.as_uri(),
            wait_until="load",
            timeout=120000
        )

        page.wait_for_timeout(3000)

        page.add_style_tag(content="""
    .topo-catalogo {
        display: none !important;
    }

    .botao-whatsapp {
        display: none !important;
    }

    body {
        padding-top: 0 !important;
    }
""")
        page.pdf(
            path=str(PDF_PATH),

            format="A4",

            print_background=True,

            prefer_css_page_size=True,

            display_header_footer=True,

            header_template="<div></div>",

            footer_template="""
    <div style="
        width:100%;
        font-size:10px;
        padding:0 20px;
        color:#666;
        display:flex;
        justify-content:space-between;
    ">
        <span>Senna Fix</span>

        <span>
            Página
            <span class="pageNumber"></span>
            de
            <span class="totalPages"></span>
        </span>
    </div>
    """,

            margin={
                "top": "10mm",
                "right": "8mm",
                "bottom": "18mm",
                "left": "8mm",
            }
        )

        print("PDF gerado:", PDF_PATH)

    finally:
        browser.close()

print("gerar_pdf.py finalizado.")
