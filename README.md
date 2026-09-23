# Digitales Rasselexikon – RGZV Hagen

Statische Erweiterung des bestehenden GitHub-Pages-Projekts. Die vorhandene
`ayam-cemani.html` ist unverändert. Keine Änderung an der Pages-Konfiguration.

## Umfang

- 21 Rasseseiten: 7 Großhühner, 12 Zwerghühner, 1 Taubenrasse, 1 Wachtel.
- 21 QR-Codes in `qr-codes/` (PNG, schwarz/weiß, Fehlerkorrektur Q,
  vier Module Ruhezone). Jeder enthält ausschließlich seine vollständige URL.
- 21 Einzel-PDFs in `schilder/`, jeweils **90 × 60 mm**.
- 3 A4-Druckbögen in `druckboegen/`, mit 8 / 8 / 5 Schildern und Schnittmarken.

Basis: https://thorstenvonoesen-ctrl.github.io/rgzv-rasselexikon/
Die vollständige URL-Zuordnung steht in `scripts/layout.json`.
Neue URLs sind erst nach Veröffentlichung der Dateien über das bestehende
GitHub-Pages-Verfahren öffentlich erreichbar. Ein lokaler Linktest ist kein
Nachweis eines bereits erfolgten Deployments.

## Drucken

Die A4-Bögen bei **Tatsächliche Größe / 100 %** ausdrucken.
„An Seite anpassen“, Verkleinerung und randlose Vergrößerung ausschalten.
Die Schnittmarken begrenzen 90 × 60 mm; der abgerundete Rahmen liegt
1,5 mm innerhalb der Schnittkante. Der QR-Bereich misst einschließlich
Ruhezone 35 × 35 mm. Die QR-Module sind echte Vektorflächen im PDF.

Die neu erstellte Ayam-Cemani-Vorlage folgt der ergänzenden Vorgabe:
weißer Hintergrund, schwarze Typografie, dünner abgerundeter Rahmen,
Text links, QR rechts. Alle anderen Schilder nutzen dieselbe Vorlage.
Ein Probedruck mit Lineal und Smartphone ist vor einer großen Druckauflage sinnvoll.

## Inhalte und Wartung

Die neuen Besuchertexte stehen mit zugeordneten Quellen in `scripts/breeds.py`.
Jede neue Rasseseite nennt ihre Quellen. Exakte Leistungsversprechen und
unklare Entstehungsdaten wurden bewusst vermieden. Farbenschläge sind Beispiele.
Die Texte ersetzen keinen vollständigen Rassestandard.

```powershell
python -m pip install -r scripts/requirements.txt
python scripts/build.py
python scripts/check.py
```

Der PDF-Generator verwendet Arial aus `C:/Windows/Fonts` und bettet die Schrift
ein. Für andere Betriebssysteme muss der Schriftpfad angepasst werden.
`build.py --reference-only` erzeugt ausschließlich die Ayam-Cemani-Vorlage.
Die erzeugten HTML-Dateien, PNGs und PDFs werden direkt von GitHub Pages
ausgeliefert; auf dem Server sind weder Python noch JavaScript erforderlich.

## Durchgeführte Prüfungen

Maschinenlesbare Ergebnisse: `scripts/qa-results.json` und
`scripts/browser-results.json`.

- Jede Rasse genau einmal in der Startseitenübersicht; alle 153 internen
  Datei- und Sprunglinks auf Existenz geprüft.
- Alle 21 PNGs mit dem unabhängigen Decoder ZXing ausgelesen und exakt mit
  der vorgesehenen URL verglichen.
- Alle 21 Einzel-PDFs bei 150 und 300 dpi gerendert und QR-Codes decodiert.
- Alle 21 QR-Codes aus den drei A4-Bögen bei 300 dpi decodiert.
- PDF-Seitengrößen gemessen; vollständige Rassenamen per Textextraktion geprüft.
- Alle PDF-Wörter innerhalb des linken Textbereichs, mit Abstand zum QR-Code.
- Alle Textpositionen und Schriftgrößen auf A4 mit den Einzel-PDFs verglichen:
  nur Verschiebung, keine Skalierung.
- Alle 22 HTML-Seiten in Microsoft Edge bei 320, 390, 768 und 1280 Pixeln
  geprüft: kein horizontaler Überlauf, keine JavaScript-Seitenfehler.
- 21 Navigationen von der Übersicht zur Rasse und zurück erfolgreich.
- Gerenderte Schilderübersicht, A4-Bögen und mobile Seiten visuell kontrolliert.
- `git diff --check` ohne Fehler; Ayam-Cemani-HTML unverändert.

Browserprüfung: `scripts/browser-check.cjs` benötigt Playwright und installiertes
Microsoft Edge. Optional bezeichnet `PLAYWRIGHT_MODULE` den absoluten Pfad
zur Playwright-Installation. Die Prüfung arbeitet lokal über Datei-URLs.
Temporäre Prüfbilder und lokal installierte Hilfspakete sind von Git ausgeschlossen.
