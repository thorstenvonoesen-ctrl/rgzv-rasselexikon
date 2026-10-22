# Erweiterung vom 22. Oktober 2026

188 bisherige Rassekarten + 5 neue Rassen = **193 Rassen** in Übersicht und Rasse-Finder.

Neu: Ko Shamo, Ohiki, Serama, Zwerg-Brakel, Zwerg-Kraienköppe.

Bereits vorhanden: Altsteirer, Andalusier, Appenzeller Barthühner, Appenzeller Spitzhauben,
Bergische Kräher, Bergische Schlotterkämme, Brabanter, Brakel, Breda, Dorking,
Friesenhühner, Holländer Haubenhühner, Houdan, Kastilianer, Kraienköppe, La Flèche,
Minorka, Nackthalshühner, Paduaner, Penedesenca, Bantam, Deutsche Zwerg-Lachshühner,
Federfüßige Zwerghühner, Holländische Zwerghühner und Tuzo.

Tuzo bleibt unter Großhühnern: Die BDRG-Rassetafeln und die Leistungsanforderungen
führen diese kleine Kämpferrasse dort, nicht bei den Zwerghühnern.
Quelle: https://www.bdrg.de/media/docs/Rassetafeln_Huehner.pdf
und https://www.bdrg.de/media/docs/BDRG_Satzung_2024.pdf

Namensprüfung: Groß-/Kleinschreibung, Umlaute und Umschriften, Akzente, Leerzeichen
und Bindestriche wurden normalisiert. Groß- und Zwergformen bleiben getrennte Rassen.
Ko Gunkei bezeichnet Ko Shamo; Twentse Krielen bezeichnet Zwerg-Kraienköppe.
Keine dieser Bezeichnungen erzeugt einen zweiten Eintrag.

Alle bestehenden Detailseiten sind per SHA-256 vor und nach der Ergänzung verglichen
und unverändert. Die vorhandenen Karten wurden unverändert innerhalb der Tiergruppen
alphabetisch angeordnet. Ein bereits zuvor fehlender Finder-Datensatz zum vorhandenen
Hagener Goldhals-Langhuhn wurde mit neutralen Eigenschaften ergänzt. Bestehende
Finder-Datensätze und die Bewertungslogik bleiben erhalten.

Neue Inhalte: `breeds_series4.py`. Ergänzung: `extend_series4.py`.
Prüfung: `check_series4.py` und `browser-series4.cjs`.
Der Ergänzer ist wiederholbar und verweigert das Überschreiben abweichender Detailseiten.
**Nicht den älteren Gesamtgenerator verwenden:** Er bildet den inzwischen erweiterten
Bestand und die aktuelle Startseite nicht vollständig ab.

Die neuen QR-PNGs enthalten ausschließlich die jeweilige vollständige GitHub-Pages-URL;
Zuordnung in `series4-inventory.json`. Neue Druck-PDFs wurden nicht beauftragt.
Die fünf QR-Codes wurden mit ZXing als QR-Code unabhängig decodiert.
Lokale Prüfungen belegen kein erfolgtes GitHub-Pages-Deployment.

Inhaltliche Grenzen sind direkt in den Porträts benannt: Serama-Legezahlen sind
uneinheitliche Schätzungen; ein allgemeingültiger Ohiki-Charakter ist in den benutzten
Standardquellen nicht belegt. Farblisten sind ausdrücklich belegte Beispiele mit
Quellenstand, keine Behauptung einer vollständigen aktuellen Standardliste.
Die neuen Haltungshinweise sind praktische Ableitungen aus Körperbau und Gefieder.
