# Fotos nachladen (Bielefeld)

Stand: 8. Oktober 2026. `hero.jpg` und `stadtbild.jpg` in diesem Ordner sind **Platzhalter** (dunkler Farbverlauf mit dem Hinweis „PLATZHALTER – Foto folgt“). Wikimedia Commons war aus der Arbeitsumgebung gesperrt. Die Website erst veröffentlichen, wenn beide echten Fotos eingesetzt sind.

Bildunterschriften, Bildnachweis im Fuß der Seite und `aria-label` sind schon auf die beiden Fotos unten eingestellt. Wird ein anderes Foto verwendet, müssen diese Texte in `website/src.html` angepasst werden.

## 1. Titelfoto: `hero.jpg`

- Commons-Dateiseite: https://commons.wikimedia.org/wiki/File:Altstadt_Bielefeld.jpg
- Urheber: BfB Bielefeld. Lizenz: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/deed.de)
- Herunterladen: Auf der Dateiseite „Herunterladen“ bzw. „Originaldatei“ wählen. Mindestens **2000 px Breite**, gern das Original.
- Zuschnitt: Querformat **3:2**, Ziel **2000 × 1333 px**. Das Motiv (Altstadt, Häuserzeile) etwa mittig, eher leicht unter der Mitte. Die Seite zeigt das Bild mit `center 58%` und auf dem Handy mit `62% center`, links unten liegt Text auf einer dunklen Fläche.
- Speichern als: `website/img/hero.jpg` (JPEG, Qualität etwa 85–90). Den Platzhalter überschreiben.

## 2. Bandfoto „Bielefeld empfiehlt Bielefeld.“: `stadtbild.jpg`

- Commons-Dateiseite: https://commons.wikimedia.org/wiki/File:Skyline_der_Stadt_Bielefeld.jpg
- Urheber: Hakanneu. Lizenz: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/deed.de)
- Motiv: Skyline der Stadt mit der Sparrenburg.
- Herunterladen: mindestens **2000 px Breite**.
- Zuschnitt: Ziel **2000 × 1309 px** (etwa 3:2). Die Seite zeigt das Bild als breites Band mit `center 35%`. Die Sparrenburg und die Silhouette der Stadt sollten im oberen bis mittleren Drittel liegen, unten liegt der Schriftzug auf einem dunklen Verlauf.
- Speichern als: `website/img/stadtbild.jpg`. Den Platzhalter überschreiben.

## Reserve

- https://commons.wikimedia.org/wiki/File:Siegfriedplatz,_Bielefeld_-_panoramio.jpg (INDALOMANIA, CC BY-SA 3.0). Bei Verwendung Bildnachweis und Lizenz (3.0!) in `src.html` anpassen.

## Danach

Aus dem Ordner `weiterempfohlen-bielefeld`:

```
python3 website/make_webp.py
python3 website/build.py
python3 website/build_dist.py
node website/tests/perftest.js
node website/tests/test_dist.js
```

Dann in `website/dist-vorlage/img/BILDER_HIER_ABLEGEN.txt` und `website/dist-vorlage/LIESMICH.txt` den Hinweis auf die Platzhalter entfernen und `build_dist.py` noch einmal ausführen.

Hinweis zur Lizenz: CC BY-SA verlangt Urheber, Lizenz und Hinweis auf Änderungen. Die Seite nennt „zugeschnitten und abgedunkelt“. Das passt, solange die Fotos nur zugeschnitten werden; die Abdunklung macht die Seite selbst.
