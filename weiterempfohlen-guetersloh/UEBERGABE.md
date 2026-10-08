# Übergabe: „Weiterempfohlen.“ – von Gütersloh nach Bielefeld

Stand: 8. Oktober 2026. Dieser Ordner enthält alles, was für den Gütersloh-Pitch von unikat media gebaut wurde. Er ist die Grundlage, um das Konzept für Bielefeld umzubauen.

**Wichtigste Regel für die neue Sitzung:** Die Gütersloh-Fassungen laufen weiter und werden nicht verändert. Für Bielefeld werden neue Artefakte mit neuen Links angelegt.

## Worum es geht

„Weiterempfohlen.“ (Arbeitstitel) ist eine Videoserie, in der sich Betriebe einer Stadt gegenseitig empfehlen. Am Ende jeder Folge fragt der Host: „Und wo gehst du hin, wenn du nicht hier bist?“ Die Antwort ist der nächste Betrieb. Kein Betrieb zahlt für seinen Auftritt, die Stadt ist Absender. Unikat media (Bielefeld) produziert.

## Was es für Gütersloh gibt

Alle Links sind privat im Konto von Stefan Wietfeld. Mit dem Artifact-Werkzeug (`action: "read"`) lassen sie sich lesen.

| Was | Link | Quelle in diesem Ordner |
| --- | --- | --- |
| Präsentation, 24 Folien (Slides) | https://claude.ai/artifact/VKwaWqWwi1uLJKmYK5oeV3 | `praesentation/project/` |
| Pitch-Website (eine HTML-Datei plus Bilder) | https://claude.ai/artifact/KRu4GyC49QjQ4C1MmGwKNa | `website/` |
| Markenbuch, 13 Folien (Slides) | https://claude.ai/artifact/CcRfi2odZsHvMAboEH6wct | `markenbuch/project/` |
| Umsetzungsplan mit E-Mail-Vorlagen (Claude Docs, **intern**) | https://claude.ai/code/artifact/75937cee-b669-44e1-a015-d2b63a5f7a07 | `dokumente/markdown/`, `dokumente/pdf/01_…` |
| Ablauf einer Folge und eines Drehtags (Docs) | https://claude.ai/code/artifact/29d89f82-dafe-49f6-a347-d3d88afc1edd | `…/02_…` |
| Muster-Monatsbericht (Docs) | https://claude.ai/code/artifact/71b708ee-4dc8-4adf-9797-9aac776bbb05 | `…/03_…` |
| Infoblatt für Betriebe (Docs) | https://claude.ai/code/artifact/cdd5606a-2a9d-45e6-91d8-fafcfb8bf777 | `…/04_…` |
| Sponsoring-Unterlage (Docs, letzter Abschnitt intern) | https://claude.ai/code/artifact/b2ab4a39-3bf3-4c73-b66b-52717160bc79 | `…/05_…` |
| Logos und Aufkleber | im Logo-Paket | `marke/` |
| Mails an Gütersloh Marketing und conceptGT | – | `mails/` |

Die Mails an Gütersloh sollten am 8. Oktober 2026 rausgehen. Nachfassen etwa am 15. Oktober.

## Ordner und Werkzeuge

Alle Befehle laufen aus diesem Ordner (`weiterempfohlen-guetersloh/`). Playwright ist global installiert, Chromium unter `/opt/pw-browsers`. Für die Skripte braucht es Python mit `pillow` und `fonttools`, für die Logos zusätzlich `uharfbuzz`.

**Website**
- Quelltext: `website/src.html`. HTML, CSS und JavaScript stehen in einer Datei, ohne Framework. Platzhalter wie `%%HEADPERF%%` oder `%%STICKER%%` füllt das Build-Skript.
- `python3 website/build.py` erzeugt:
  - `website/weiterempfohlen.html`: die Datei, die veröffentlicht wird. Die Schriften stecken als Base64 darin, damit beim Öffnen nichts nachlädt.
  - `website/local.html`: die Vorschau.
- Bilder:
  - `website/img/*.jpg` sind die Quellen.
  - `python3 website/make_webp.py` erzeugt daraus `website/img-web/*.webp`, die großen Fotos zusätzlich als `-m.webp` fürs Handy.
- Veröffentlichen: `weiterempfohlen.html` als Artifact, die Bilder als Dateien unter `img/…webp` mit Quelle `img-web/…webp`. Für Bielefeld ohne `url`, damit ein neuer Link entsteht.
- WordPress-Paket: `python3 website/build_dist.py` erzeugt `website/dist/` und `website/Weiterempfohlen_Pitch-Website.zip`.
- Tests:
  - `node website/tests/perftest.js` prüft Ladeverhalten, Schriften und Fotos.
  - `node website/tests/test_dist.js` prüft das WordPress-Paket.
  - Weitere Skripte machen Bildschirmfotos nach `website/shots/`.
- Rechner-Logik: im Script-Teil unter `/* Sponsoring-Rechner */` mit den Konstanten `KOSTEN`, `P_PRES`, `P_RUB` und `AKT`.

**Präsentation und Markenbuch (Artifact-Typ „Slides“)**
- Typ: https://claude.ai/artifact/8jTsAFQMFDb2oA8MsPJ2eL
- Neues Deck: zuerst mit `type_url` anlegen. Danach `deck.json` und die Folien mit `root` auf `praesentation` (bzw. `markenbuch`) und `files` veröffentlichen.
- Aufbau: Jede Folie ist eine `<section>` mit 1920 × 1080 Pixeln, die Sprechernotizen stehen in `<aside>`.
- Seitenzahlen: Die Fußzeilen-Nummern sind fest eingetragen. Wird eine Folie eingefügt, müssen danach alle Fußzeilen und das Verzeichnis auf der Anhang-Folie neu nummeriert werden.
- Render-Prüfung: `node render/rs.js <folie>` (Präsentation) bzw. `node render/rsmb.js <folie>` (Markenbuch). Das Skript meldet Elemente, die zu weit nach unten laufen, und legt ein Bild ab.
- Bilder im Markenbuch:
  - Es nutzt Bilder aus dem Asset-Speicher des Gütersloh-Markenbuchs (`/_blob/<id>`). Übernehmen lassen sie sich mit Artifact `publish`, `asset: true`, `from_url` und `asset_ids`.
  - Der Aufkleber (`6c76ac4202627da733e8f556af352a48`) trägt „GÜTERSLOH EMPFIEHLT“ und muss neu erzeugt werden.
- Die Präsentation nutzt keine solchen Bilder.

**Logos**
- `python3 marke/make_logos.py` erzeugt Wortmarke, Zeichen und Aufkleber aus der Schrift Bricolage Grotesque (Ausgabe in `marke/logos/`).
- Aufkleber-Text in Zeile 100: `top = "GÜTERSLOH EMPFIEHLT"`.
- Das fertige Logo-Paket liegt in `marke/Logo-Paket/`.

**Dokumente**
- Sie liegen in Claude Docs. In `dokumente/markdown/` steht der Text als Markdown, als Grundlage für die Bielefeld-Fassungen.
- Für Bielefeld neue Docs anlegen.
- Der Umsetzungsplan ist intern, er enthält Mail-Vorlagen, Gesprächsnotizen und Recherchen. Nie an Externe geben.

## Inhaltlicher Stand (Gütersloh)

- **Rubriken:**
  - Immer dabei: „Zu Gast bei …“, „Neu in GT“, „Wer steckt dahinter?“
  - Als Zusatz möglich: „Eine Schicht bei …“, „Wo gibt's das beste …?“ und der Award „Lieblingsort des Jahres“.
- **Drehtag:** ein Tag, drei Betriebe, drei aufeinanderfolgende Folgen. Zwei Stunden pro Betrieb, drei Personen im Team.
- **Testphase:**
  - Dauer und Umfang: vier Monate, 16 teilnehmende Betriebe (einer pro Woche), sechs Drehtage, Auswertung jeden Monat.
  - Ausstieg: keiner. Stattdessen gibt es jeden Monat eine Auswertung.
  - Preis: 4.850 € netto pro Monat, also 19.400 € gesamt, fester Preis. Danach entscheidet die Stadt über eine Jahresserie mit rund 48 Betrieben, der Preis dafür wird erst dann festgelegt.
- **Pro teilnehmenden Betrieb** (so heißt es überall, nicht „pro Folge“):
  - Fünf Posts: Ankündigung, Neugier-Post, Teaser, Video, Abschluss.
  - In den Kosten außerdem enthalten: Instagram-Account mit Beiträgen und Betreuung, Weiterempfohlen-Website, komplettes Konzept.
- **Partner:** Sie zahlen direkt an die Stadt, unikat media stellt der Stadt monatlich 4.850 € in Rechnung. Es gibt keinen Deckel und keine Garantie.
  - **Presenting-Partner:** 1.200 € pro Monat oder 4.800 € einmalig, exklusiv. Dazu eine eigene Partner-Folge außerhalb der Empfehlungskette, klar gekennzeichnet.
  - **Serien-Partner:** 600 € pro Monat, bis zu fünf, Nennung „Mit Unterstützung von …“ in jeder Folge. Eine Rubrik-Patenschaft ist erst eine Idee für die Jahresserie.
  - **Aktions-Partner (Extra):** S 1.750 €, M 3.500 € oder L 9.000 € (L etwa für den Adventskalender mit bis zu drei Drehtagen). Davon fließen 500, 1.000 oder 2.000 € in die Serie, der Rest bezahlt die Aktion. Höchstens vier Aktionen.
  - **Beispiele im Rechner:**

    | Fall | Besetzung | Anteil der Stadt pro Monat |
    | --- | --- | --- |
    | Start | Presenting + 3 Serien-Partner | 1.850 € |
    | Gut besetzt (Voreinstellung) | Presenting + 5 Serien-Partner | 650 € |
    | Mit Aktionen | dazu L + M | 0 €, dazu 100 € Plus |
- **Codewort:** Wer es im Betrieb nennt, bekommt etwas aufs Haus. Was und wie lange, entscheidet der Betrieb, gezählt wird per Strichliste.
- **Absage:** Wer nicht vor die Kamera will, bekommt einen „Dreh ohne Gesicht“. Außerdem gibt es drei Reserve-Orte und eine Zuschauerwahl.
- **Referenz @bielefoodies:**
  - Ein abgeschlossenes Projekt mit über 2.000 echten Followern in drei Monaten, etwa 20 € Werbebudget und 109 Beiträgen.
  - Der Kanal ist seit etwa einem Dreivierteljahr inaktiv. Unikat media hat alles produziert außer der ursprünglichen Idee.
- **Kontakt:** Stefan Wietfeld, unikat media, 0521 30436986, info@unikat.media.

## Feste Regeln (gelten auch für Bielefeld)

- **Inhalt:**
  - Niemand wird bewertet: keine Noten, Sterne oder Superlative.
  - Partner kaufen nie einen Platz in der Empfehlungskette.
  - KI-generierte Bilder als solche kennzeichnen.
  - Fremde Fotos mit Quelle und Lizenz nennen. Die Gütersloh-Fotos (Teutoburger Wald, M. Wallenfang, CC BY-SA 4.0) zeigen Gütersloh und müssen für Bielefeld ersetzt werden. Das Foto „Hinter den Kulissen“ stammt von unikat media.
- **@bielefoodies:** Warum der Kanal endete, nur so sagen: Der Initiator musste sich aus persönlichen Gründen zurückziehen. Keine weiteren Details, auch nicht in internen Unterlagen. Nicht „pausiert“ sagen.
- **Sprache:**
  - Deutsch, kurze klare Sätze, keine Fachsprache.
  - In Unterlagen „Sie“, auf Instagram „du“.
  - Preise immer netto.
- **Git:** Committen und pushen nur, wenn der Nutzer darum bittet.

## Was für Bielefeld anders ist

Alles hier ist zu prüfen und mit dem Nutzer zu klären, bevor gebaut wird.

- **Ansprechpartner:** Wer in Bielefeld zuständig ist, muss neu recherchiert werden, voraussichtlich Bielefeld Marketing und die Wirtschaftsförderung. Aktuelle Namen und Adressen gibt es nur aus den Impressen und Teamseiten.
- **Größe:** Bielefeld ist etwa dreimal so groß wie Gütersloh und hat viele Stadtteile.
  - Umfang: Anzahl der Betriebe, Drehtage und der Preis müssen vielleicht anders aussehen.
  - Kette: Sie kann bewusst durch die Stadtteile laufen.
- **@bielefoodies ist dort eine lokale Referenz.** Man kennt den Kanal in Bielefeld.
  - Abgrenzung: Sie muss klar sein, denn dort war es ein Gastro-Kanal, hier ist die Stadt Absender und kein Betrieb zahlt.
  - Nachfragen: Fragen zum Ende des Kanals sind wahrscheinlicher. Siehe Regel oben.
- **Gütersloh-Bezüge ersetzen:**
  - Orte und Termine: Dreieckplatz, Berliner Straße, Isselhorst, Michaeliswoche, Weihnachtsmarkt-Termine.
  - Namen: Rubrik „Neu in GT“, Aufkleber „Gütersloh empfiehlt“, Abgrenzungsfolie mit bestehenden Lokalkanälen.
  - Hintergrund: die Hinweise zur Zusammenlegung von Gütersloh Marketing und conceptGT.
- **Bestehende Bielefelder Kanäle und Formate** neu recherchieren (für die Folie „Was es schon gibt – und was fehlt“).
- **Zeitplan:** Gütersloh startet Mitte November. Für Bielefeld einen eigenen Zeitplan festlegen.
- **Geschäftsfrage für unikat media:** Soll Gütersloh das Format exklusiv bekommen, oder laufen beide Städte parallel? Das vor dem Versand an Bielefeld klären.
