# Baut das WordPress-Paket in website/dist und die ZIP-Datei aus website/weiterempfohlen.html.
# Vorher: python3 website/build.py  (und bei neuen Fotos python3 website/make_webp.py)
# Aufruf aus dem Ordner weiterempfohlen-paderborn: python3 website/build_dist.py
import os, shutil, glob
w = open('website/weiterempfohlen.html').read()
head = ('<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<meta name="robots" content="noindex, nofollow">\n<meta name="theme-color" content="#121718">\n')
start = w.index('<link rel="preload" as="image"'); end = w.index('<svg width="0"')
meta = w[:start]  # <title> und <meta description>
style = w[start:end].rstrip().replace('<style>\n/* Layout', '<style>\n[hidden]{display:none!important}\n/* Layout', 1)
out = head + meta + '<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">\n' + style + '\n</head>\n<body>\n' + w[end:].rstrip() + '\n</body>\n</html>\n'
assert 'fonts.googleapis' not in out and out.count('<title>') == 1
shutil.rmtree('website/dist', ignore_errors=True)
shutil.copytree('website/dist-vorlage', 'website/dist')
open('website/dist/index.html', 'w').write(out)
for f in glob.glob('website/img-web/*.webp'):
    shutil.copy(f, 'website/dist/img/')
if os.path.exists('website/Weiterempfohlen_Pitch-Website.zip'):
    os.remove('website/Weiterempfohlen_Pitch-Website.zip')
shutil.make_archive('website/Weiterempfohlen_Pitch-Website', 'zip', 'website/dist')
print(len(out), 'Zeichen in dist/index.html')
