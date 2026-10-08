# Bilder im Markenbuch (Bielefeld)

Stand: 8. Oktober 2026. Die Folien in `project/slides/` nutzen Bilder aus dem Asset-Speicher des Gütersloh-Markenbuchs (https://claude.ai/artifact/CcRfi2odZsHvMAboEH6wct). Die Referenzen `/_blob/<id>` stehen unverändert im HTML.

Alle acht Assets sind SVG-Dateien. Sie wurden heruntergeladen und angesehen. Nur der Aufkleber trägt einen Stadtnamen.

## Übersicht

| ID | Inhalt | Folien | Gütersloh-Bezug | Aktion |
| --- | --- | --- | --- | --- |
| `6c76ac4202627da733e8f556af352a48` | Aufkleber rund, gelb, „GÜTERSLOH EMPFIEHLT – Weiter empfohlen. – 2026 – Pfeil“ (1000 × 1000) | stadt | **Ja, Text „GÜTERSLOH EMPFIEHLT“** | **Ersetzen** durch `marke/logos/aufkleber.svg` (neu, „BIELEFELD EMPFIEHLT“) |
| `0fe83f2c368e9c3b132279545dc384ea` | Logo mit Zeichen, hell (Wortmarke Papierweiß, gelbes Zeichen, gelber Punkt) | titel | nein | übernehmen |
| `ea87db50736b0058159b32982119c393` | Logo mit Zeichen, dunkel (Wortmarke Tinte, gelbes Zeichen, gelber Punkt) | logo, regeln | nein | übernehmen |
| `34bb11b8ce46f67fb698656fe34d1566` | Wortmarke Tinte mit gelbem Punkt | varianten, social, stadt | nein | übernehmen |
| `9c5a48e734bd2f306c786e8c8cef11dc` | Wortmarke Papierweiß mit gelbem Punkt | varianten, social | nein | übernehmen |
| `fbfc33eb30a31444920211c7d660ea27` | Wortmarke einfarbig Tinte | varianten, social | nein | übernehmen |
| `67fb108870aad1b6ebbfb93cd211ac7c` | Zeichen: gelber Kreis, Pfeil in Tinte | varianten, social (2×) | nein | übernehmen |
| `5d11f62951b0ba639a1b98b5021c687f` | Zeichen: Kreis in Tinte, gelber Pfeil | varianten | nein | übernehmen |

## Referenzen pro Folie

| Folie | Datei | IDs |
| --- | --- | --- |
| 01 titel | `titel.html` | `0fe83f2c…` |
| 03 logo | `logo.html` | `ea87db50…` |
| 04 varianten | `varianten.html` | `34bb11b8…`, `9c5a48e7…`, `fbfc33eb…`, `67fb1088…`, `5d11f629…` |
| 05 regeln | `regeln.html` | `ea87db50…` |
| 09 social | `social.html` | `67fb1088…` (2×), `9c5a48e7…`, `fbfc33eb…`, `34bb11b8…` |
| 11 stadt | `stadt.html` | **`6c76ac42…` (ersetzen)**, `34bb11b8…` |

Die Folien kern, farben, schrift, sprache, video, aktionen und paket nutzen keine Bilder.

## Vorgehen für den Hauptagenten

1. Die sieben Logo-Assets ohne Stadtbezug ins neue Bielefeld-Markenbuch kopieren: Artifact `publish`, `asset: true`, `from_url` = Gütersloh-Markenbuch, `asset_ids` = die sieben IDs oben. Die neuen URLs aus dem Ergebnis in die Folien eintragen.
2. Den Aufkleber neu hochladen: `marke/logos/aufkleber.svg` (SVG wie das Original; alternativ `marke/logos/aufkleber.png`, 2000 × 2000, transparent). Die neue URL in `stadt.html` statt `/_blob/6c76ac4202627da733e8f556af352a48` eintragen. Der alt-Text dort lautet bereits „Bielefeld empfiehlt“.
3. Fotos: Das Markenbuch nutzt keine Fotos. Die Gütersloh-Fotos (Teutoburger Wald) betreffen nur die Website.
