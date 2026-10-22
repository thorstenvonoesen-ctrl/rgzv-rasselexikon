# Codex-Auftrag: JTL-Wawi 2.1.2 – sieben Druckvorlagen

## Ziel
Aus den sieben beigefügten ORIGINALEN `.vlg`-Dateien kompatible, optisch einheitliche, professionell gestaltete JTL-Wawi-Vorlagen erstellen. Das beigefügte Federlogo verwenden. **Die Originaldateien niemals überschreiben.**

## Dokumente
Rechnung, Rechnungskorrektur, Angebot, Auftrag, Lieferschein, Mahnung, Lieferantenbestellung.

## Gestaltung
Modernes, seriöses Layout für „Geflügelzuchtbedarf – Vom Züchter für den Züchter“, mit grün-goldenem Federlogo. Klare Typografie, ordentliche Abstände, keine überlappenden Elemente, druckbarer DIN-A4-Bereich, keine gelblichen Flächen, keine Musterlogos. Lesbare Artikelpositionen, Summen und Absender-/Empfängerdaten. Dokumentbezeichnung eindeutig.

## Geschäftslogik
Kleinunternehmer nach § 19 UStG: korrekten Hinweis anzeigen; keine gesondert ausgewiesene Umsatzsteuer. Keine unzutreffenden Reverse-Charge-/innergemeinschaftlichen Steuerhinweise. Keine nicht tatsächlich eingerichteten PayPal-/QR-Zahlungsangaben. Bestehende gültige Datenbindungen, Formeln, Platzhalter, Bedingungen und JTL-Funktionen erhalten; keine statischen Testkundendaten in produktive Vorlage übernehmen.

## Technischer Arbeitsablauf
1. `.vlg` als Archive analysieren: Einträge, Encoding, XML/`.lst`, Binärdaten, Bildreferenzen, Checksummen, Größen, Versions-/Designerkompatibilität. Ausgangsstruktur protokollieren.
2. Unveränderte Originale und SHA-256-Prüfsummen sichern.
3. Minimalinvasive Änderungen auf Kopien vornehmen; eingebettete Bilder nur mit verifizierter Referenz- und Formatkonsistenz austauschen. Nicht blind XML/`.lst` mit String-Replacement manipulieren.
4. Für alle sieben Archive ZIP-Integrität, Eintragslisten und referenzierte Ressourcen prüfen; Original-vs-Ergebnis-Diff erstellen.
5. Wenn JTL-Designer/Windows nicht verfügbar ist, ausdrücklich **nicht** behaupten, dass die Vorlagen in JTL getestet wurden. Einen klaren Testplan für Import, Designeröffnung, Vorschau und Ausdruck jedes Dokumenttyps liefern.
6. Fertige `.vlg` in separatem Ordner `output/` bereitstellen, mit Prüfbericht, offenen Risiken und optional PDF-Vorschauen. Keine ungeprüften Dateien als „fertig“ ausgeben.

## Bekannter Fehler
Nach früheren Änderungen trat in JTL „Das Designobjekt konnte nicht bezogen werden“ auf. Ursache bisher nicht gesichert. Frühere ZIP-Arbeitsstände NICHT als Grundlage verwenden; ausschließlich die hier beigefügten Originale.

## Erwartetes Ergebnis
Sieben überarbeitete `.vlg` plus technische Validierung und klare Aussage, welche Tests durchgeführt wurden und welche einen lokalen JTL-Wawi-Test benötigen.
