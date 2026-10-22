# Fehlermeldung beim Angebot – 4. Oktober 2026

Der Nutzer meldet „Das Designobjekt konnte nicht bezogen werden“ beim Angebot. Der Screenshot belegt die Fehlermeldung, aber nicht ihre Ursache. Ob die Originalvorlage funktioniert und ob im aktuellen Mandanten ein Angebotsdatensatz vorhanden bzw. ausgewählt ist, ist noch nicht bekannt.

Erneute unabhängige Archivprüfung: bestanden. Die Originale sind unverändert; die geprüften Referenzen und Metadaten sind konsistent. Dies bestätigt keine Designerkompatibilität.

Ein Designobjekt ist in JTL der Datensatz des jeweiligen Belegtyps für die Designer-Vorschau. Der JTL-Guide beschreibt die Auswahl über den Pfeil neben „Bearbeiten“ → „Designobjekt wählen…“. Im JTL-Supportforum wird die konkrete Fehlermeldung mit einem fehlenden passenden Vorgang in Verbindung gebracht. Deshalb ist zuerst ein vorhandenes **Angebot** im gleichen Mandanten als Designobjekt auszuwählen. Ein Auftrag allein ist kein Nachweis, dass ein Angebotsdatensatz vorliegt.

Diagnosefolge:

1. Vorhandenes Angebot im aktuellen Mandanten prüfen und für die Vorlage über „Designobjekt wählen…“ auswählen.
2. Designer mit diesem Datensatz öffnen.
3. Wenn kein Angebot vorhanden ist: einen geeigneten Testdatensatz ausschließlich in einer Testmandantenkopie anlegen; keine erfundenen Daten in die Vorlagendatei schreiben.
4. Falls der Fehler mit ausgewähltem Angebot bleibt: dieselbe Belegauswahl mit der unveränderten Originalvorlage vergleichen. Tritt er nur mit der Prüfversion auf, Änderungen an Hauptprojekt, Baustein und Bild einzeln isolieren. Tritt er auch mit dem Original auf, zuerst Datenobjekt-/Mandantenkontext untersuchen.

Bis zum erfolgreichen Vergleich werden weder eine Dateibeschädigung noch eine gelöste Ursache behauptet. Die Prüfversionen wurden in diesem Diagnoseschritt nicht geändert.

Quellen:
- https://guide.jtl-software.com/jtl-wawi/vorlagen-ausgabe-1-0/druck-e-mail-exportvorlagen-verwalten/
- https://forum.jtl-software.de/threads/fehler-beim-bearbeiten-einer-vorlage.126925/
