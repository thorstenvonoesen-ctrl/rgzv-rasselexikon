# Gesamtauftrag RGZV Hagen – Ergebnisbericht

Stand: 22. Oktober 2026. Die Änderungen sind im lokalen Projekt umgesetzt;
Commit, Push und eine Veröffentlichung wurden in diesem Auftrag nicht ausgeführt.

## Startseite und Veranstaltung

Der bestehende Kopfbereich mit Leitspruch und Vereinsnamen bleibt erhalten.
Darunter folgen die Ankündigung der **1. Offenen Rassetaubenschau 2027** am
**Samstag, 30. Januar 2027**, Rassen entdecken, Rasse-Finder, der gestraffte
Willkommenstext und die Vereinslinks. Anschließend folgt die unveränderte,
alphabetische Rassenübersicht mit einer Namenssuche. Dunkelgrün, weiße Kacheln
und das responsive Grundlayout bleiben erhalten. Ort und Öffnungszeiten der
Taubenschau sind noch nicht bekannt und werden nicht erfunden.

`assets/veranstaltungen.json` ist die zentrale Veranstaltungsverwaltung mit
ausgewählter Veranstaltungs-ID, ISO-Beginn/-Ende, Titel, Datumsanzeige, Ort,
Öffnungszeiten, Beschreibung, Status und ausdrücklicher Erkundungsfreigabe.
Jede Veranstaltung hat eine eigene Belegung unter `assets/ausstellungen/<id>.json`.
Die Taubenschau 2027 startet mit einer leeren Belegung und gesperrter Erkundung.

Ankündigungen verschwinden nach dem letzten Veranstaltungstag in der Zeitzone
Europe/Berlin. Eine geöffnete Seite prüft den Tageswechsel jede Minute und lädt
den neuen Status. Abgesagte, beendete und nicht ausgewählte Veranstaltungen
erscheinen nicht als aktuelle Ausstellung. Eine Erkundung benötigt zusätzlich
eine freigegebene, passende, nicht leere und überschneidungsfreie Käfigbelegung.
Unbekannte Rassenziele, falsche Veranstaltungs-IDs und doppelte Rassenzuordnungen
werden abgewiesen. Der Rundgangsfortschritt ist an die Veranstaltungs-ID gebunden.

Die Lokalschau 2026 wurde deaktiviert; ihre alte öffentliche Belegungsdatei ist
geleert. Die frühere Belegung bleibt in der Git-Historie nachvollziehbar. Es gibt
keine öffentliche Archivnavigation und keinen Erkundungszugang zu vergangenen
Veranstaltungen. Rasseporträts und gedruckte QR-Ziele bleiben davon unabhängig.

Verwaltung: GitHub Actions → **Ausstellung verwalten**. Für eine neue Veranstaltung
eine neue ID, Titel und ISO-Beginn/-Ende eingeben. Grunddaten wählen diese
Veranstaltung aus und sperren zunächst ihre Erkundung. Danach Käfige hinzufügen
und gesondert **Erkundung freigeben** wählen. Änderungen an der Belegung sperren
sie erneut bis zur Freigabe. **Erkundung sperren** belässt die Ankündigung;
**Ausstellung deaktivieren** beendet sie. Textfelder können bei Grunddaten mit
`-` geleert werden. Die Zuordnung bestehender Belegungen wird niemals auf eine
neue Veranstaltungs-ID übertragen.

## Rassebestand und Inhalte

Es sind **192 gültige Rasseeinträge** vorhanden. Die zusätzlich erhaltene
Scherzseite „Hagener Goldhals-Langhuhn“ ist als Dekorationshuhn gekennzeichnet
und wird weder als Rasse gezählt noch im Finder empfohlen.

Alle 30 beauftragten Rassen sind vorhanden:

- Großhühner: Altsteirer, Andalusier, Appenzeller Barthühner, Appenzeller
  Spitzhauben, Bergische Kräher, Bergische Schlotterkämme, Brabanter, Brakel,
  Breda, Dorking, Friesenhühner, Holländer Haubenhühner, Houdan, Kastilianer,
  Kraienköppe, La Flèche, Minorka, Nackthalshühner, Paduaner, Penedesenca.
- Weitere Auftragsrassen: Bantam, Deutsche Zwerg-Lachshühner, Federfüßige
  Zwerghühner, Holländische Zwerghühner, Ko Shamo, Ohiki, Serama, Tuzo,
  Zwerg-Brakel, Zwerg-Kraienköppe. Tuzo bleibt entsprechend der BDRG-Einordnung
  unter Großhühnern; es wurde kein Zwerghuhn-Duplikat erzeugt.

In diesem Gesamtauftrag wurden **keine zusätzlichen Rassen** angelegt.
Die zuvor ergänzten fünf Porträts bleiben erhalten. 25 ältere Porträts der
Auftragsliste wurden um belegte Gewichts-, Legeleistungs- und Eierangaben aus
den BDRG-Originaltafeln ergänzt. Jede Ergänzung verlinkt ihre konkrete PDF-Seite.
Die ursprünglichen Beschreibungstexte bleiben vollständig erhalten. Die Tabellen
sind ausdrücklich ältere Richtwerte, keine aktuellen Leistungsmessungen und
keine Zusicherung individueller Leistungen. Unbelegte Eigenschaften werden
nicht erfunden; die dokumentierten Grenzen bei Serama und Ohiki bleiben sichtbar.

Gesamtanzeigen und Finder verwenden denselben geprüften Katalog aus
`assets/finder-data.js` über `assets/rassen-bestand.js`. Die Anzeige enthält keine
feste Gesamtzahl. URL- und Namensdubletten einschließlich Umlautschreibweisen
und dokumentierter Synonyme werden ausgeschlossen. Die automatischen Prüfungen
gleichen den Katalog mit sämtlichen tatsächlichen Rassedateien und der Navigation ab.

## A7-Schilder und PDF-Ausgaben

Neue Druckauswahl: `schilder-drucken.html`, von der Startseite erreichbar.
Einzelne PDFs können direkt heruntergeladen werden. Ausgewählte Rassen werden
im Browser zu A7-Seiten oder A4-Bögen zusammengestellt. Beide Gesamtausgaben und
ein Beispiel mit acht unterschiedlichen Rassen sind ebenfalls direkt verfügbar.
Die PDF-Bibliothek wird lokal ausgeliefert; es gibt keine CDN-Abhängigkeit.

Erstellt wurden:

- 192 einzelne PDFs unter `output/pdf/a7/`, jeweils exakt **74 × 105 mm**.
- `output/pdf/alle-rasseschilder-a7.pdf`: 192 Seiten im A7-Hochformat.
- `output/pdf/alle-rasseschilder-a4.pdf`: 24 A4-Seiten mit je acht Schildern.
- `output/pdf/beispiel-acht-rasseschilder-a4.pdf`: ein A4-Beispielbogen.

Jedes Schild enthält den vollständigen zentrierten Rassenamen, einen 60 mm großen
QR-Bereich einschließlich vier Modulen Ruhezone sowie die Vereinsbezeichnung.
Schriften sind eingebettet; die QR-Module sind echte Vektorflächen.

Acht A7-Hochformatschilder passen in zwei Spalten und vier Reihen nur dann auf
A4, wenn sie auf dem Bogen um 90° gedreht stehen: 2 × 105 mm = 210 mm,
4 × 74 mm = 296 mm. Es wird **nicht skaliert**. Die verbleibende Millimeterhöhe
verteilt sich auf 0,5 mm oben und unten. Dezente Schnittlinien markieren die
inneren Grenzen. Der Druckdialog ist auf „keine Skalierung“ vorbereitet.
Gedruckt werden muss mit **100 % / tatsächlicher Größe**, ohne Seitenanpassung.
Die A4-Ausgabe benötigt randlosen Druck oder eine geeignete professionelle Ausgabe.

Der neue Workflow **A7-Rasseschilder aktualisieren** erzeugt bei Änderungen am
zentralen Rassenkatalog oder Generator die Einzel- und Gesamt-PDFs erneut und
stößt den bestehenden Branch-Pages-Build an. Er wird erst nach Veröffentlichung
der Workflow-Datei aktiv. Der bisherige Ausstellungs-Verwaltungsworkflow wurde
auf die veranstaltungsbezogenen Dateien umgestellt.

## Durchgeführte Prüfungen

- 192 eindeutige gültige Rassedateien; alle 30 Auftragsrassen vorhanden.
- 194 bestehende Inhaltsseiten mit dem Git-Stand verglichen: alle ursprünglichen
  Texte erhalten; bei 25 Rasseporträts lediglich die dokumentierte Ergänzung.
- 1005 lokale Datei- und Sprungverknüpfungen geprüft.
- Alle **193 bisherigen QR-PNGs** unverändert und unabhängig mit ZXing decodiert,
  einschließlich des QR-Codes zur erhaltenen Scherzseite.
- Alle **188 bisherigen Druckschilder** gerendert und ihre QR-Ziele decodiert.
- Alle **192 neuen A7-Einzel-PDFs** auf exakte Größe, vollständige Namen,
  Vereinsbezeichnung, Druckskalierung und decodierbare QR-Ziele geprüft.
- Alle QR-Codes auf sämtlichen 24 A4-Bögen decodiert; der Beispielbogen zusätzlich
  bei 300 dpi geprüft. Maßstab und Drehung kontrolliert.
- Die tatsächlich vom Browser erzeugten Auswahl-PDFs mit acht Schildern erneut
  geöffnet, vermessen und alle acht QR-Ziele in beiden Formaten decodiert.
- A7-Einzelblatt und A4-Beispiel mit Poppler gerendert und visuell kontrolliert.
- Browserprüfung bei 320, 390, 768 und 1280 Pixeln: kein horizontaler Überlauf,
  keine JavaScript-Seitenfehler. Ankündigung, Ablauf, Freigabe, Käfignummernsuche,
  Namenssuche, Rundgang, Rasse-Finder und PDF-Auswahl erfolgreich getestet.
- Verwaltungsprüfung: neue ID ohne Altbelegung, Freigabe/Sperre, sichere Ablehnung
  überlappender Käfige und Reaktivierung einer beendeten Veranstaltung.
- Automatische Zählererhöhung, mehrere Gesamtanzeigen, ungültige Datensätze,
  Scherzseiten, Dubletten und Namensvarianten getestet. `git diff --check` bestanden.

Maschinenlesbare Nachweise: `scripts/project-results.json`,
`scripts/project-browser-results.json`, `scripts/a7-results.json`,
`scripts/requested-facts-audit.json` und `scripts/a7-layout.json`.

Die Scanprüfung erfolgte technisch anhand gerenderter PDFs. Ein tatsächlicher
Papierausdruck mit Smartphone und die Maße am verwendeten Drucker konnten hier
nicht physisch geprüft werden. Auch die neu angelegten GitHub-Workflows sind
lokal geprüft beziehungsweise vorbereitet, aber noch nicht auf GitHub ausgeführt.
