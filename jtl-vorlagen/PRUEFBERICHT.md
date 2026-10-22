# JTL-Wawi 2.1.2 – sieben überarbeitete Druckvorlagen

Stand: 4. Oktober 2026. **Status: technisch geprüfte Prüfversionen; keine Produktionsfreigabe.**

Die sieben `.vlg` liegen in `output/`. Nur diese Dateien importieren, keine entpackten `.lst`. Die gelieferten Originale wurden ausschließlich gelesen und unter `originale/` unverändert gesichert. `verify.py` hat alle sieben Archive byteweise gegen das gelieferte ZIP geprüft. Die SHA-256-Werte stehen in `pruefung/originale-sha256.json`; Ergebnisprüfsummen und Eintragsprüfsummen in `pruefung/validierung.json`.

## Änderungen

- Alle sieben Dokumente verwenden das gelieferte grün-goldene Federlogo. Sechs vorhandene JPEG-Ressourcen behalten ihre IDs und das JPEG-Format. Das PNG wurde auf weißem Hintergrund als JPEG in voller Auflösung 1774 × 887 eingebettet. Es wurde kein Musterlogo verwendet. Die vorhandenen Bildfelder sind auf 60 × 30 mm angepasst und behalten die proportionale Darstellung.
- Die vorhandenen Farbschemata erhalten dunkles Grün, zurückhaltendes Gold und weiße Hintergründe. Der gemeinsame Fußbereich der sechs neueren Vorlagen bleibt innerhalb der seitlichen Ränder und endet vor dem unteren Seitenrand. Arial und bestehende Größen bleiben erhalten, um keine unkontrollierten Umbrüche einzuführen.
- Die sechs neueren Vorlagen zeigen im bestehenden Fußbereich „Steuerfrei gemäß § 19 Abs. 1 UStG (Kleinunternehmer).“ Der Hinweis ersetzt dort die bisherige USt-IdNr.-Zeile. Die Gläubiger-ID-Bindung bleibt erhalten. Die Lieferantenbestellung erhält in ihrem bestehenden Schlussabsatz einen Hinweis auf die Kleinunternehmereigenschaft des bestellenden Unternehmens.
- Steuerpositionsspalten werden ausgeblendet. Netto-Zwischensummenblöcke und gesonderte Umsatzsteuerblöcke werden deaktiviert. Bestehende Gesamtbetrags- und Preisberechnungen bleiben erhalten. Das gilt ausdrücklich auch für die Einkaufsberechnung: Die Vorlage verändert keine tatsächlich vom Lieferanten berechneten Steuern oder Einkaufswerte.
- Die vorhandenen Hinweise auf innergemeinschaftliche Lieferung, Reverse Charge und steuerfreie Drittlandslieferung werden für diesen Vorlagensatz deaktiviert. Die PayPal- und PayPal-Factoring-Blöcke sowie die Zahlungs-QR-Spalten sind deaktiviert. Der GiroCode-Werbetext ist aus den Überweisungsabsätzen entfernt; Bank-, Fälligkeits- und Skontobindungen bleiben erhalten.
- Die Lieferantenbestellung heißt ausdrücklich „Lieferantenbestellung“. Sie erhält einen zusätzlichen Bildgegenstand mit eigener stabiler Ressourcen-ID, einen engeren rechten Adressbereich und Anpassungen an Titel-, Tabellen- und Fußbereich. Der alte Datenraum `Vorgang.*` bleibt erhalten; es wurden keine `Report.*`-Bindings aus anderen Dokumenten übernommen.

## Aufbau der Originale und Änderungsverfahren

Alle sieben `.vlg` sind ZIP-Archive. Sechs bestehen aus `index.xml`, einem E-Mail-XML, einem Inhalts-/Aktions-XML, einem Hauptprojekt `.lst`, einem gemeinsamen Baustein `.lst` und einer JPEG-Ressource `.image`. Der Lieferschein enthält zusätzlich eine binäre `.printerconfig`. Die Lieferantenbestellung enthält ursprünglich fünf XML-Einträge und ein `.lst`, aber kein eingebettetes Bild.

XML-Dateien sind UTF-8; `.lst` sind UTF-16LE mit BOM und CRLF, `FileVersion=16`. Die Dateien behalten dieses Format. Die Eintragslisten enthalten je nach Dokument sechs oder sieben Einträge; die Lieferantenbestellung erhält genau einen neuen `.image`-Eintrag. ZIP-Kompressionsverfahren, Zeitstempel und sonstige Metadaten vorhandener Einträge werden beim Schreiben übernommen. Größen, CRC-32 und SHA-256 jedes Original-/Ergebniseintrags sind in `validierung.json` dokumentiert.

Die JTL-Deskriptoren verwenden `@2@`, Base64, eine 4-Byte-Little-Endian-Längenangabe, `ChK_Packed` und zlib-komprimierte UTF-16-XML-Profile. Alle wurden dekomprimiert, auf korrekte Längen geprüft und als XML gelesen. Sie enthalten Repository-Metadaten; in den analysierten Bilddeskriptoren stehen keine Bildabmessungen oder Inhaltsprüfsummen. ZIP-CRC und Größen werden beim Erstellen neu berechnet. Für sechs Vorlagen bleibt `index.xml` bytegleich. Nur die Lieferantenbestellung erhält einen strukturiert erzeugten zusätzlichen Bildeintrag mit konsistentem ID-/Typ-Profil.

`build.py` liest LL-Abschnitte, Klammerstruktur und Eigenschaften. Änderungen erfolgen an konkret erkannten Eigenschaftsfeldern. Es gibt kein globales blindes Ersetzen von XML oder `.lst`. Unveränderte Zeilen bleiben erhalten. Die vollständigen UTF-8-Diffs der `.lst` liegen in `pruefung/*.diff`; das JSON-Protokoll listet jeweils alte und neue Eigenschaftswerte. Bildänderungen sind über Format, Abmessungen und Hashes nachvollziehbar. Es werden keine Kundentestdaten eingesetzt.

## Durchgeführte Prüfungen

| Prüfung | Ergebnis |
|---|---|
| Originale bytegleich zum gelieferten ZIP | bestanden, 7/7 |
| Original- und Ergebnis-ZIP vollständig lesbar, CRC-Test | bestanden, 7/7 |
| Keine doppelten ZIP-Einträge; vorhandene Einträge erhalten | bestanden, 7/7 |
| XML syntaktisch lesbar und Vorlagenverknüpfungen auflösbar | bestanden, 7/7 |
| Komprimierte Deskriptoren: Header, Länge, XML, IDs/Typen | bestanden, 7/7 |
| LL-BOM, Encoding, Klammerstruktur, Version 16 | bestanden, 7/7 |
| Repository-Verweise und Bilddateien auflösbar/decodierbar | bestanden, 7/7 |
| Inhalts-/Aktions- und E-Mail-XML bytegleich | bestanden, 7/7 |
| `UsedIdentifiers`-Variablen und Felder unverändert | bestanden, alle 13 Projekte |
| Änderungen an gespeicherter Objektzahl passend zu hinzugefügten Objekten | bestanden |
| JTL-Import, Designeröffnung, Datenvorschau, PDF-Export, Ausdruck | **nicht bestätigt / nicht durchgeführt** |

Die gespeicherten LL-Objektzahlen stimmen in einigen Originalen bereits nicht mit der Zahl sichtbarer oberster `[Object]`-Abschnitte überein. Diese Ausgangseigenschaft wurde nicht „repariert“. Geprüft wurde die Übereinstimmung des Änderungsdeltas; bei der Lieferantenbestellung jeweils +1. Einzelwerte stehen in `unabhaengige-pruefung.json`.

JTL-Wawi 2.1.2 und List & Label 30 sind installiert. Die Vorlagenverwaltung wurde per Computer Use gelesen. Bedienversuche meldeten „foreground window did not report a process id“ und „coordinate input geometry is unavailable“. Es wurde kein erfolgreicher Import der Prüfversionen oder eine Designeröffnung beobachtet. Der separate native Lesetest `runtime_check.py` blieb schon beim ersten Originalprojekt ohne Ergebnis hängen und wurde abgebrochen. **Daraus lässt sich weder eine erfolgreiche Kompatibilität noch ein Defekt der Ergebnisdateien ableiten.** Ein vollständiger Formelauswertungstest mit dem JTL-Datenprovider fand nicht statt.

## Offene Risiken

1. Der frühere Fehler „Das Designobjekt konnte nicht bezogen werden“ ist nicht reproduziert und seine Ursache nicht gesichert. ZIP-/XML-Konsistenz allein schließt diesen Fehler nicht aus.
2. Die Kompatibilität mit dem JTL-Designer, Repository-Import und dessen tatsächlicher Formelauswertung ist offen. Vorhandene GUIDs bleiben erhalten. Beim Import können bestehende gleichnamige Vorlagen bzw. Repository-Objekte kollidieren; deshalb zuerst in einer separaten Testmandantenkopie prüfen.
3. Überlappungen, lange Inhalte, Tabellenumbrüche, Fußzeilenhöhe und Logo-Lesbarkeit benötigen die echte JTL-Vorschau. Die Eigenschaften sind angepasst, aber nicht gerendert. Es gibt bewusst keine als echte Vorschau ausgegebenen Mockup-PDFs.
4. Steuerspalten auszublenden korrigiert keine falsche Wawi-Steuerkonfiguration. Ausgangsbelege müssen im System tatsächlich als Kleinunternehmerumsätze korrekt berechnet werden. Gesamtbeträge, Zahlungsinformationen und frei eingegebene Texte können weiterhin falsche Inhalte liefern; sie sind nicht durch statische Werte ersetzt.
5. Lieferantenbestellungen sind Eingangs-/Einkaufsprozesse. Die Kleinunternehmereigenschaft des Bestellers beseitigt keine Steuerpflicht eines Lieferanten. Der separate Steuerausweis ist auftragsgemäß in der Druckvorlage verborgen, Einkaufsbeträge bleiben erhalten. Die Netto-Einkaufspreise und der Gesamtwert müssen fachlich miteinander abgestimmt geprüft werden.
6. E-Mail-HTML, CSV-/ZUGFeRD-Aktionen und Druckerkonfiguration sind unverändert. Dieser Auftrag bearbeitet die Druckprojekte. Bestehende E-Mail-Texte und freie Wawi-Textfelder können eigene Steuer- oder Zahlungsangaben enthalten.

## Lokaler Testplan und Freigabekriterien

Zuerst eine Testkopie des Mandanten verwenden. Die vorhandenen Vorlagen exportieren. Keine Prüfversion als Standard aktivieren und keine vorhandene Vorlage ersetzen. Jede Datei dem passenden Dokumenttyp zuordnen, importieren und unter einem eindeutig erkennbaren Testnamen speichern. Falls JTL ein Überschreiben vorhandener Objekte anbietet, den Test abbrechen und ausschließlich in einer isolierten Mandantenkopie fortfahren.

Für **jeden** der sieben Dokumenttypen: Import protokollieren; Designer öffnen; Hauptprojekt und eingebundenen Baustein prüfen; Formelfehlerliste prüfen; speichern und erneut öffnen; mit echten passenden Belegdaten Vorschau erstellen; PDF exportieren; einen A4-Ausdruck bzw. Druckertest erzeugen. Importerfolg allein ist keine Freigabe. Die Prüffelder unten sind absichtlich offen.

| Dokument | Zusätzliche Datenfälle | Import | Designer | Vorschau/PDF | A4-Druck |
|---|---|---|---|---|---|
| Rechnung | 1 und 40 Positionen; lange Namen; Rabatt; Teilzahlung; Skonto; bezahlt/unbezahlt; Storno/Proforma falls genutzt | offen | offen | offen | offen |
| Rechnungskorrektur | Teil-/Vollkorrektur; negative Werte; mehrseitig; mit/ohne Rechnungsbezug | offen | offen | offen | offen |
| Angebot | lange Adresse; 40 Positionen; Rabatte; optionale Artikel/Varianten falls genutzt | offen | offen | offen | offen |
| Auftrag | abweichende Lieferadresse; Varianten/Konfigurationen; Teillieferung/Teilzahlung falls genutzt | offen | offen | offen | offen |
| Lieferschein | abweichende Adresse; 40 Positionen; Chargen/Seriennummern falls genutzt; keine ungewollten Preise | offen | offen | offen | offen |
| Mahnung | jede verwendete Mahnstufe; Teilzahlung; mehrere offene Rechnungen; Mahngebühren | offen | offen | offen | offen |
| Lieferantenbestellung | Lieferantenartikelnummer; VPE; lange Liefer-/Rechnungsadresse; lange Druckanmerkung; mehrseitig; Einkaufswerte mit Steuer | offen | offen | offen | offen |

In jeder Vorschau prüfen: richtige Dokumentbezeichnung, Logo und Firmendaten; alle Positionen lesbar; Gesamtbetrag identisch zur Wawi; sichtbarer §-19-Hinweis; keine separate Umsatzsteuerzeile/-spalte; keine sichtbaren Reverse-Charge-/IGL-Hinweise oder PayPal-/QR-Zahlungsangebote; Seitenzählung und Fußbereich korrekt; keine abgeschnittenen oder überlappenden Elemente. Bei optional fehlenden Daten dürfen keine leeren Bank-/Zahlungsversprechen entstehen. Bankdaten und Fälligkeiten müssen zu den tatsächlich eingerichteten Zahlungsarten passen. Erst nach vollständiger dokumentierter Prüfung produktiv übernehmen.

## Quellen für die Prüfgrenzen

- [§ 19 UStG](https://www.gesetze-im-internet.de/ustg_1980/__19.html): aktuelle Steuerbefreiung für Kleinunternehmer; Grundlage des Hinweises.
- [combit: Repository-Modus](https://docu.combit.net/net/en/Using%20the%20Repository-Mode.html): Ressourcen werden über Repository-IDs statt Dateipfade geladen.
- [combit: LlProjectOpen](https://docu.combit.net/progref/en/Documents/llprojectopen.htm): Öffnen mit ignorierten Formelproblemen ersetzt keine Prüfung mit bekannten Datenstrukturen. Der abgebrochene native Versuch wäre daher selbst bei Erfolg nur ein Strukturtest gewesen.

## Dateien

`output/`: sieben Prüfversionen. `originale/`: gesicherte Quelle inklusive PNG. `pruefung/`: JSON-Prüfprotokolle und Projektdiffs. `build.py` und `verify.py`: nachvollziehbare Erstellung und unabhängige Prüfung. `runtime_check.py`: nicht erfolgreich abgeschlossener nativer Prüfversuch; nicht automatisch erneut starten. `analyse/`: entpackte Originalstruktur, ausschließlich zur Analyse.
