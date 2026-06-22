import subprocess
import sys

ETAPAS = [
    "scripts/extrair_pdf.py",
    "scripts/categorizar_por_grupo.py",
    "scripts/produtos_com_imagens.py",
    "scripts/gerar_qrcode.py",
    "scripts/gerar_html.py",
    "scripts/gerar_pdf.py"
]

for etapa in ETAPAS:

    print()
    print("=" * 60)
    print(f"Executando: {etapa}")
    print("=" * 60)

    resultado = subprocess.run(
        [sys.executable, etapa]
    )

    if resultado.returncode != 0:

        print()
        print(f"Erro em {etapa}")
        sys.exit(1)

print()
print("=" * 60)
print("CATÁLOGO GERADO COM SUCESSO")
print("=" * 60)
