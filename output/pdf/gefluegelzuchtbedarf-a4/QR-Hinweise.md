# Herzblut-Anzeige mit Shop-QR-Code

Die freigegebene Anzeige erhält im unteren rechten Bereich einen QR-Code
mit dem Ziel https://gefluegelzuchtbedarf.myshopify.com.
Das übrige Layout, Foto und Original-Logo bleiben erhalten.

Der QR-Code ist 32 × 32 mm groß, als Vektorflächen in die PDF integriert,
schwarz auf Weiß, mit vier Modulen Ruhezone und Fehlerkorrektur Q.
Die sichtbare vollständige Shopadresse bleibt erhalten.

Die fertige A4-PDF wurde neu bei 300 dpi gerendert und visuell geprüft.
Ein unabhängiger ZXing-Decoder hat den QR-Code aus der gesamten gerenderten
PDF-Seite bei 150 dpi und bei 300 dpi korrekt als die vollständige HTTPS-
Shopadresse ausgelesen. Protokoll: QR-Pruefung.json.
Die technische Prüfung bestätigt den kodierten Link, nicht die Erreichbarkeit
oder Verfügbarkeit des Shopservers.

Druck: A4 hoch, tatsächliche Größe / 100 %.
Quelldateien: anzeige-qr.py, anzeige-v4.py und gestalten.py.
Zusätzlich zu den in Herzblut-Hinweise.md genannten Python-Paketen werden
qrcode und zxing-cpp benötigt. Aufruf: python anzeige-qr.py.

Das Schwarzweißmotiv ist die bereits verwendete KI-generierte Illustration
in fotografischer Darstellung; es wurde für diese QR-Ergänzung nicht neu erzeugt.
