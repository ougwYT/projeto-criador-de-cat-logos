import subprocess
import sys
from pathlib import Path

try:
    import qrcode
except ImportError:
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "qrcode[pil]"])
    import qrcode

URL_WHATSAPP = "https://wa.me/5511939593526"
SAIDA = Path("docs/assets/qrcode_whatsapp.png")

SAIDA.parent.mkdir(parents=True, exist_ok=True)

img = qrcode.make(URL_WHATSAPP)

with SAIDA.open("wb") as arquivo:
    img.save(arquivo)

print("QR Code gerado:", SAIDA)
