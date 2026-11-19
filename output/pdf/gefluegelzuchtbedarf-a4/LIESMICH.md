# Geflügelzuchtbedarf · A4-Werbeschild

## Fertige Druckdatei

`Werbeschild-A4.pdf` ist eine einseitige Anzeige im Endformat 210 × 297 mm.
Zum Ausdrucken A4, Hochformat, tatsächliche Größe / 100 % wählen.
Alle wesentlichen Elemente liegen mindestens 12 mm vom Blattrand entfernt.
Die cremefarbene Hintergrundfläche reicht bis zum Seitenrand; ein normaler
Bürodrucker kann hier einen schmalen weißen Rand lassen.
Die Datei ist für den direkten A4-Ausdruck ausgelegt, ohne Schnittmarken und
ohne zusätzliche Beschnittzugabe. Es wird keine PDF/X-Zertifizierung behauptet.

## Gestaltung und Auswahl

Drei eigenständige Entwürfe sind im dreiseitigen Dokument
`Drei-Designkonzepte.pdf` enthalten. Die Reihenfolge entspricht der Tabelle.
Bewertungen sind gestalterische Einschätzungen auf einer Skala von 1 bis 5,
keine Ergebnisse einer Publikumsbefragung.

| Konzept | Eleganz | Werbewirkung | Lesbarkeit | Glaubwürdigkeit |
| --- | ---: | ---: | ---: | ---: |
| 1 · Fachhandelsanzeige | 5 | 5 | 5 | 5 |
| 2 · Editorial | 5 | 3 | 4 | 5 |
| 3 · Markenanzeige | 4 | 4 | 4 | 5 |

**Auswahl: Konzept 1.** Die groß gesetzte, dreiteilige Aussage bildet einen
klaren Blickfang auf Dunkelgrün. Das Original-Logo ist auf Creme gut erkennbar,
die beiden Sortimentszeilen machen die Spezialisierung deutlich, und die
vollständige Shopadresse schließt die Anzeige mit einem eigenen Schwerpunkt ab.
Die Mischung aus Baskerville und Gill Sans verbindet ruhige Wertigkeit mit
klarer Gebrauchstypografie. Gold wird außerhalb des Original-Logos nur für
dezente Linien und kleine Akzente verwendet.

Konzept 2 setzt auf einen asymmetrischen Satzspiegel und eine vertikale grüne
Achse. Der redaktionelle Charakter wirkt kultiviert, erreicht aus der Ferne
aber weniger Aufmerksamkeit; die Sortimentszeilen beanspruchen mehr Lesezeit.

Konzept 3 verwendet einen zentrierten Markenauftritt und einen dunkelgrünen
Abschluss mit Sortiment und Adresse. Es wirkt ruhig und glaubwürdig, seine
zentrierte Hierarchie ist jedoch konventioneller und weniger prägnant als 1.

## Technische Kontrolle

- Endformat der PDF maschinell überprüft: 210 × 297 mm, eine Seite.
- Finale PDF tatsächlich bei 300 dpi gerendert und visuell kontrolliert.
- PNG-Vorschau: 2481 × 3508 Pixel, mit 300-dpi-Metadaten.
- Original-Logo: unveränderte transparente PNG-Datei, 1774 × 887 Pixel.
- Platzierte Logobreite: 148 mm; effektive Auflösung: 304,5 dpi.
- Alle neu gesetzten Texte und Linien bleiben in der PDF Vektoren.
- Verwendete TrueType-Schriften sind als Teilmengen in der PDF eingebettet.
- Vollständige Shopadresse in der PDF-Textebene überprüft.
- Kein QR-Code Bestandteil dieser Gestaltung.
- Keine KI-generierten Tiere, Produktbilder oder Änderungen am Logo.

## Bearbeiten und erneut erzeugen

`gestalten.py` ist die bearbeitbare, reproduzierbare Layoutquelle.
`original-logo.png` ist eine unveränderte Kopie der vorgefundenen Originaldatei
aus `jtl-vorlagen/originale/Elegantes Geflügelzuchtbedarf-Logo mit Feder(1).png`.

Benötigt werden Python und die Pakete reportlab, pypdfium2, Pillow und pypdf.
Die verwendeten Schriftdateien werden aus `C:/Windows/Fonts` geladen:
`BASKVILL.TTF`, `GIL_____.TTF`, `GILB____.TTF`.
Schriftdateien werden nicht mitgeliefert. Die bereits erzeugte PDF lässt sich
ohne diese lokal installierten Schriften drucken.

Aufruf: `python gestalten.py`

Farben, Texte und Positionen sind direkt im Skript benannt und bearbeitbar.
Das Quellenpaket enthält die Layoutquelle, das Original-Logo und diese Hinweise.
