# Übergabe: „Weiterempfohlen.“ – Bielefeld-Fassung

Stand: 8. Oktober 2026. Dieser Ordner (`weiterempfohlen-bielefeld/`) enthält die Bielefeld-Fassung des Pitches von unikat media. Er ist eine Kopie des Gütersloh-Ordners und wurde auf Bielefeld umgebaut.

**Verbindliche Grundlage:** `BIELEFELD_ENTSCHEIDUNGEN.md` (Entscheidungen von Stefan Wietfeld, Fakten, Kontakte, Zeitplan, Fotos). Dazu gelten die „Festen Regeln“ aus `UEBERGABE.md` (unten übernommen). Die Gütersloh-Fassungen im Ordner `weiterempfohlen-guetersloh/` bleiben unverändert. Gütersloh und Bielefeld laufen parallel.

## Worum es geht

„Weiterempfohlen.“ (Arbeitstitel) ist eine Videoserie, in der sich Betriebe einer Stadt gegenseitig empfehlen. Am Ende jeder Folge fragt der Host: „Und wo gehst du hin, wenn du nicht hier bist? Gern auch in einem anderen Stadtteil.“ Die Antwort ist der nächste Betrieb. Kein Betrieb zahlt für seinen Auftritt, die Stadt ist Absender. Unikat media (Bielefeld) produziert. Leitsatz: „Bielefeld empfiehlt Bielefeld.“

## Was es für Bielefeld gibt

Alle Links werden neu angelegt (privat im Konto von Stefan Wietfeld). Für Bielefeld nie die Gütersloh-Links überschreiben.

| Was | Link | Quelle in diesem Ordner |
| --- | --- | --- |
| Präsentation (Slides) | https://claude.ai/artifact/Gu6YmWFcBX114TS3xq46Cn | `praesentation/project/` |
| Pitch-Website | https://claude.ai/artifact/ULrwmsUiHiDdkcrTDd7iBp | `website/` |
| Markenbuch (Slides) | https://claude.ai/artifact/C4AHY6LVJXgaCMW3T8dwv9 | `markenbuch/project/` |
| Umsetzungsplan mit E-Mail-Vorlagen (Docs, **intern**) | https://claude.ai/code/artifact/44ab5249-93e8-4169-8ad4-3df043427ff9 | `dokumente/markdown/Weiterempfohlen – Umsetzungsplan mit E-Mail-Vorlagen.md` |
| Ablauf einer Folge und eines Drehtags (Docs) | https://claude.ai/code/artifact/904b3f9c-3f2a-4960-95a0-02e9d6ef3c35 | `dokumente/markdown/Weiterempfohlen. – Ablauf einer Folge und eines Drehtags.md` |
| Muster-Monatsbericht (Docs) | https://claude.ai/code/artifact/4d58ce5e-281b-4bec-aef9-cad9947d4860 | `dokumente/markdown/Weiterempfohlen. – Muster-Monatsbericht.md` |
| Infoblatt für Betriebe (Docs) | https://claude.ai/code/artifact/c198aaf6-5d1f-471a-bb1d-916d9f704104 | `dokumente/markdown/Weiterempfohlen. – Infoblatt für Betriebe.md` |
| Sponsoring-Unterlage (Docs, letzter Abschnitt intern) | https://claude.ai/code/artifact/e86f5d38-5843-4f0c-b9f8-efd9f7473e00 | `dokumente/markdown/Weiterempfohlen. – Sponsoring-Unterlage.md` |
| PDFs der fünf Dokumente | folgt, nach dem Anlegen der Docs neu exportieren | `dokumente/pdf/` (zurzeit leer, die alten Gütersloh-PDFs sind hier gelöscht) |
| Logos und Aufkleber „BIELEFELD EMPFIEHLT“ | im Logo-Paket | `marke/` |
| Mails an Bielefeld Marketing und WEGE | – | `mails/` |

Die Links trägt man nach dem Veröffentlichen auch in `dokumente/LINKS_und_LIESMICH.txt` ein.

**Mails in `mails/`:**

- `01_Bielefeld-Marketing.txt`: an Martin Knabenreich, CC Jens Siekmann. Versand Montag, 12. Oktober 2026 (KW 42). Adresse vorher prüfen, Links einsetzen.
- `02_Nachfassen.txt`: etwa am 19. Oktober, wenn keine Antwort kam. Anruf zwei Tage später.
- `03_WEGE_nach-Gespraech.txt`: an Desirée Lukowski (WEGE). Erst nach dem ersten Gespräch mit Bielefeld Marketing und mit deren Einverständnis.

## Ordner und Werkzeuge

Alle Befehle laufen aus `weiterempfohlen-bielefeld/`. Playwright ist global installiert, Chromium unter `/opt/pw-browsers`. Für die Skripte braucht es Python mit `pillow` und `fonttools`, für die Logos zusätzlich `uharfbuzz`.

**Website**
- Quelltext: `weiterempfohlen-bielefeld/website/src.html`. `python3 website/build.py` erzeugt `website/weiterempfohlen.html` (wird veröffentlicht) und `website/local.html` (Vorschau).
- Bilder: `website/img/*.jpg` sind die Quellen, `python3 website/make_webp.py` erzeugt `website/img-web/*.webp`.
- Veröffentlichen: `weiterempfohlen.html` als Artifact **ohne `url`**, damit ein neuer Link entsteht. Bilder als Dateien unter `img/…webp` mit Quelle `img-web/…webp`.
- WordPress-Paket: `python3 website/build_dist.py`. Tests: `node website/tests/perftest.js`, `node website/tests/test_dist.js`.

**Präsentation und Markenbuch (Artifact-Typ „Slides“)**
- Typ: https://claude.ai/artifact/8jTsAFQMFDb2oA8MsPJ2eL. Neues Deck zuerst mit `type_url` anlegen, dann `deck.json` und Folien mit `root` auf `weiterempfohlen-bielefeld/praesentation` bzw. `weiterempfohlen-bielefeld/markenbuch` veröffentlichen.
- Render-Prüfung: `node render/rs.js <folie>` bzw. `node render/rsmb.js <folie>`.
- Fußzeilen-Nummern sind fest eingetragen. Nach dem Einfügen einer Folie neu nummerieren. Die Dokumente nennen Folien deshalb beim Titel, nicht bei der Nummer.

**Logos**
- `python3 marke/make_logos.py` erzeugt Wortmarke, Zeichen und Aufkleber (Ausgabe in `marke/logos/`, Paket in `marke/Logo-Paket/`). Aufkleber-Text: „BIELEFELD EMPFIEHLT“.

**Dokumente**
- Der Text steht als Markdown in `dokumente/markdown/`. Daraus werden neue Claude Docs angelegt, danach die PDFs exportiert.
- Der Umsetzungsplan ist intern (Mail-Vorlagen, Gesprächsleitfaden, Kontakte, Recherchen). Nie an Externe geben.

## Inhaltlicher Stand (Bielefeld)

- **Ansprache:** Mail an Martin Knabenreich (Geschäftsführer Bielefeld Marketing), Jens Siekmann in CC. Die WEGE (City-Managerin Desirée Lukowski) kommt erst nach dem ersten Gespräch dazu. Kontakte mit Quellen im Umsetzungsplan.
- **Hintergrund:** WEGE und Bielefeld Marketing arbeiten ab 2027 unter dem Dach der BBVG zusammen. Ton: eine Chance für ein erstes gemeinsames Projekt, keine Personalfragen.
- **Testphase wie Gütersloh:** vier Monate (Dezember 2026 bis März 2027), 16 teilnehmende Betriebe (einer pro Woche), sechs Drehtage, monatliche Auswertung, kein Ausstieg. 4.850 € netto pro Monat, 19.400 € gesamt, fester Preis.
- **Pro teilnehmenden Betrieb:** fünf Posts (Ankündigung, Neugier-Post, Teaser, Video, Abschluss). Dazu Instagram-Account mit Beiträgen und Betreuung, Website, komplettes Konzept.
- **Rubriken:** „Zu Gast bei …“, „Neu in Bielefeld“, „Wer steckt dahinter?“; als Zusatz „Eine Schicht bei …“, „Wo gibt's das beste …?“ und der Award „Lieblingsort des Jahres“ (Verleihung zum Leineweber-Markt).
- **Kanal:** eigener Serienkanal @weiterempfohlen.bi (Arbeitstitel), Collab-Posts mit @bielefeld.jetzt und dem Betrieb.
- **Kette durch die Stadtteile:** Start in der Altstadt, danach frei. Schlussfrage mit „Gern auch in einem anderen Stadtteil.“ Kettenkarte in Posts, Website und Monatsbericht. Ziel: mindestens fünf der zehn Stadtbezirke, keine Pflicht.
- **Partner:** gleiche Stufen und Preise wie Gütersloh (Presenting 1.200 €/Monat oder 4.800 € einmalig; Serien-Partner 600 €/Monat, bis zu fünf; Aktions-Partner S 1.750 €, M 3.500 €, L 9.000 €, davon 500/1.000/2.000 € in die Serie, höchstens vier Aktionen). Bielefeld Marketing bietet die Pakete zuerst den Bielefeld-Partnern an. Partner zahlen an Bielefeld Marketing, unikat media stellt monatlich 4.850 € in Rechnung. Kein Deckel, keine Garantie.
- **Aktionen:** Weihnachtsmarkt-Spezial (M, Dezember 2026) und „Marktwochen“ (L, Wochenmärkte in den Stadtteilen, Februar/März 2027). Adventskalender erst ab Advent 2027.
- **Zeitplan:** Mail 12. Oktober, Gespräch und Workshop Ende Oktober/Anfang November, Go bis 13. November, erste Drehtage Ende November, Start Do., 3. Dezember 2026 (Weihnachtsmarkt 19.11. bis 30.12.), Abschlussbericht Anfang April 2027, Jahresserie zum Leineweber-Markt (26. bis 30. Mai 2027).
- **@bielefoodies:** lokale Referenz. Der Kanal ist nicht mehr aktiv. Positiv erzählen: Jetzt kommt etwas Neues, größer gedacht.
- **Kontakt:** Stefan Wietfeld, unikat media, 0521 30436986, info@unikat.media.

## Feste Regeln (aus `UEBERGABE.md`, gelten weiter)

- **Inhalt:**
  - Niemand wird bewertet: keine Noten, Sterne oder Superlative.
  - Partner kaufen nie einen Platz in der Empfehlungskette.
  - KI-generierte Bilder als solche kennzeichnen.
  - Fremde Fotos mit Quelle und Lizenz nennen. Für Bielefeld die Commons-Fotos aus `BIELEFELD_ENTSCHEIDUNGEN.md` verwenden.
- **@bielefoodies:** Warum der Kanal endete, nur so sagen: Der Initiator musste sich aus persönlichen Gründen zurückziehen. Keine weiteren Details, auch nicht in internen Unterlagen. Nicht „pausiert“ sagen.
- **Bestehende Kanäle** (etwa @bielefeld_guide.de) nicht schlechtreden. Der Unterschied ist das Modell. Bielefeld Marketing schaltet dort selbst Anzeigen.
- **Gütersloh** wird in Bielefelder Unterlagen nicht erwähnt. Nur der interne Umsetzungsplan hält sachlich fest, dass Gütersloh parallel läuft.
- **Sprache:** Deutsch, kurze klare Sätze, keine Fachsprache. In Unterlagen „Sie“, auf Instagram „du“. Preise immer netto.
- **Git:** Committen und pushen nur, wenn der Nutzer darum bittet.

## Offene Punkte

- **Fotos:** Die zwei Bielefeld-Fotos (Altstadt Bielefeld, BfB Bielefeld; Skyline der Stadt Bielefeld, Hakanneu; beide CC BY-SA 4.0) sind eingesetzt, die Website ist veröffentlicht.
- **Kanalname prüfen:** Ist @weiterempfohlen.bi auf Instagram und TikTok frei?
- **Followerzahlen prüfen:** Die Zahlen der Bielefelder Kanäle und von @bielefoodies sind Näherungswerte. Vor dem Termin in der App prüfen.
- **Adresse von Martin Knabenreich prüfen:** nicht veröffentlicht, vermutlich martin.knabenreich@bielefeld-marketing.de. Vor dem Versand über die Zentrale (0521 55774-555) bestätigen.
- **Docs und PDFs:** Die fünf Bielefeld-Docs anlegen, danach die PDFs neu exportieren und die Links in `dokumente/LINKS_und_LIESMICH.txt` eintragen.
- **Quellen-Links ergänzen:** Radio Bielefeld (23.06.2026) und OWL Journal (04.10.2026) im Umsetzungsplan.
