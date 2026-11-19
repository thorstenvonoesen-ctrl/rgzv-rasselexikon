# Herzblut-Faltbroschüre

## Drucken

Die Datei Herzblut-Wickelfalz-A4-Duplex.pdf enthält genau zwei A4-Querformatseiten:

1. Außenseite: links Einschlaglasche, mittig Rückseite, rechts Titel.
2. Innenseite: links Tränken/Fütterung, mittig Brut/Aufzucht, rechts Stallzubehör.

Beide Seiten auf **ein Blatt A4**, **Querformat**, **beidseitig**,
**tatsächliche Größe / 100 %**, **an der kurzen Kante wenden** drucken.
Keinen Broschüren-/Heftdruck, keine zwei Seiten pro Blatt und keine zusätzliche
Verkleinerung aktivieren. Duplex und unveränderte Skalierung sind außerdem als
PDF-Druckpräferenzen hinterlegt; maßgeblich bleiben die Druckertreibereinstellungen.

Die Hintergrundfläche reicht bis zum Blattrand. Ein Bürodrucker darf einen
schmalen weißen Rand lassen; alle relevanten Inhalte halten mindestens etwa
7 mm Abstand zum Blatt- und Falzrand. Die Datei ist eine A4-Ausgabe ohne
zusätzlichen Beschnitt, Schnittmarken oder sichtbare Falzlinien. Es wird keine
PDF/X-Zertifizierung behauptet. Eine Druckerei kann andere Beschnitt- oder
Farbprofilvorgaben verlangen.

## Zweimal falten: Wickelfalz

Das Blatt mit der geöffneten **Innenseite nach oben** hinlegen.
Die **rechte schmale Lasche (97 mm)** nach links auf das mittlere Feld falten.
Danach das **linke Feld (100 mm)** nach rechts darüber schließen.
So liegt die Titelseite oben; Endformat ungefähr **100 × 210 mm**.

Falzpositionen ab linker Blattkante:

| Ansicht | Felder von links nach rechts | Falze |
| --- | --- | --- |
| Außenseite | 97 / 100 / 100 mm | 97 und 197 mm |
| Innenseite | 100 / 100 / 97 mm | 100 und 200 mm |

Die verkürzte Lasche berücksichtigt die Papierlagen im Wickelfalz. Vor einer
größeren Auflage einen Duplex-Probedruck falten. Bei starkem Papier die
Falzbreiten mit dem ausführenden Druckbetrieb abstimmen und bei Bedarf rillen.
Die separate Datei Druck-und-Falzplan.pdf dient als Anleitung und gehört
nicht mit in den Duplex-Druckauftrag der Broschüre.

## Gestaltung und Prüfung

Der freigegebene Anzeigenstil wurde auf sechs Inhaltsseiten übertragen:
kräftige Franklin-Gothic-Schrift, warmes Weiß, Anthrazit, Rostrot, unverändertes
Original-Logo und das bereits verwendete KI-generierte Schwarzweißmotiv.
Das Motiv ist keine Originalaufnahme eines bestimmten tatsächlichen Züchters.
Es wurde für die Broschüre nicht neu erzeugt oder verändert.

HERZBLUT10 mit 10 % Rabatt wurde entsprechend der Bestätigung des Nutzers
übernommen. Beide QR-Codes führen zur vollständigen Shop-Startseite;
der Code wird beim Bezahlen manuell eingegeben. Keine zusätzlichen Bedingungen
oder Laufzeiten wurden erfunden; die Shopkonfiguration wurde nicht geändert.

- Zwei Seiten A4 quer, je 297 × 210 mm, maschinell geprüft.
- Unterschiedliche Breiten der Lasche auf Vorder- und Rückseite gespiegelt.
- Beide PDF-Seiten bei 300 dpi tatsächlich gerendert und visuell kontrolliert.
- Beide QR-Codes mit unabhängigen ZXing-Scans bei 150 und 300 dpi überprüft.
- QR-Codes als Vektoren, Ruhezone von vier Modulen, Fehlerkorrektur Q.
- Foto effektiv über 430 dpi, Original-Logo über 540 dpi.
- Neu gesetzte Schriften als TrueType-Teilmengen in der PDF eingebettet.
- Hochauflösende PNGs: je 3508 × 2481 Pixel mit 300-dpi-Metadaten.
- Keine Freigabe der Farbwiedergabe auf einem bestimmten Drucker behauptet.

## Bearbeitbare Quelle

Die Datei broschuere.py und die beiden PNG-Bilddateien zusammen in einem
Ordner halten. Benötigt werden Python mit reportlab, pypdfium2, pypdf,
Pillow, qrcode und zxing-cpp. Die Windows-Schriften Franklin Gothic Book,
Heavy und Medium müssen unter C:/Windows/Fonts verfügbar sein; sie werden
nicht mitgeliefert. Aufruf: python broschuere.py.

Das Quellenpaket enthält außerdem das technische Prüfprotokoll.
