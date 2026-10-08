# Wandelt die JPG-Quellen in website/img in WebP für die Website um (website/img-web).
# Große Fotos bekommen zusätzlich eine Handyfassung mit 900 px Breite (-m.webp).
# Aufruf aus dem Ordner weiterempfohlen-paderborn: python3 website/make_webp.py
import os
from PIL import Image
SRC, OUT = 'website/img', 'website/img-web'
BIG = {'hero': 1920, 'stadtbild': 1920, 'drehtag': 1600, 'theke': 1200}
QUALITY = {'hero': 60, 'stadtbild': 60}  # dunkel überlagerte Hintergründe vertragen mehr Kompression
os.makedirs(OUT, exist_ok=True)
for f in sorted(os.listdir(SRC)):
    if not f.endswith('.jpg'):
        continue
    n = f[:-4]
    im = Image.open(f'{SRC}/{f}').convert('RGB')
    w = BIG.get(n, im.width)
    d = im if im.width <= w else im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    d.save(f'{OUT}/{n}.webp', 'WEBP', quality=QUALITY.get(n, 78), method=6)
    if n in BIG:
        m = im.resize((900, round(im.height * 900 / im.width)), Image.LANCZOS)
        m.save(f'{OUT}/{n}-m.webp', 'WEBP', quality=62 if n in QUALITY else 76, method=6)
    print(n)
