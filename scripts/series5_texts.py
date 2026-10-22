"""Eigenständig formulierte Porträts; Faktenquellen und Quellenstände stehen am Eintrag.

Haltungshinweise sind praktische Ableitungen aus dem dokumentierten Körperbau.
Fehlende Jahreszahlen und nicht belegte Flug-/Flächenwerte werden nicht geschätzt.
"""
TEXTS={}
def add(name, country, period, short, history, appearance, nature, husbandry, use, colors, sources=()):
    TEXTS[name]=dict(origin=country,period=period,short=short,history=history,appearance=appearance,nature=nature,husbandry=husbandry,use=use,colors=colors,extra_sources=list(sources))

add('Amerikanische Zwerg-Leghorn','USA',None,
 'Weiße kleine Legehühner mit gelben Läufen und großem Einfachkamm.',
 'Die amerikanische Zwergform gehört zur Zuchttradition der Leghorn. Diese geht auf italienische Legehühner zurück, die außerhalb Italiens weiterentwickelt wurden. Im deutschen Verzeichnis ist die amerikanische Zwergform eigenständig aufgeführt; sie wird hier weder mit Zwerg-Italienern noch mit ausländischen Leghorn-Typen zusammengefasst.',
 'Die leichte, gestreckte Figur zeigt einen gut entwickelten Legebauch. Weißes Gefieder, gelbe unbefiederte Läufe, rote Kopfpunkte und weiße Ohrscheiben erzeugen einen deutlichen Kontrast. Der Einfachkamm fällt besonders am Hahn auf; der Schwanz ist gut entwickelt.',
 'Der Legehuhntyp ist kein Nachweis einer bestimmten Zahmheit. Bei der Auswahl einer Zuchtgruppe sollte man die Bewegungsfreude und das Verhalten der konkreten Linie beobachten.',
 'Ein strukturierter Auslauf mit Futtersuchmöglichkeiten passt zur leichten Gestalt. Die Einfriedung sollte erst nach Beobachtung der tatsächlichen Flugfähigkeit festgelegt werden. Kamm und Kehllappen brauchen bei winterlicher Kälte einen trockenen, windgeschützten Rückzugsort.',
 'Die Zwergform erhält den legebetonten Typ der Großrasse in kleinerem Format. Ihre Erhaltung verlangt neben Gefiederfarbe und Körperform auch Aufmerksamkeit für Vitalität und Fortpflanzungsfähigkeit.',
 'Weiß. Die anerkannte amerikanische Zwergform ist nicht mit jeder international als Leghorn bantam bezeichneten Farbvariante gleichzusetzen.')

add('Zwerg-Altsteirer','Deutschland','Zuchtbeginn 1954; BDRG-Anerkennung 1961',
 'Kleine Steirerhühner mit Federschopf und ausgeprägter Landhuhnform.',
 'Heinrich Knöll begann nach dem Zweiten Weltkrieg mit der Verzwergung. Kleine Altsteirer und Zwerg-Welsumer gehörten zum Ausgangsmaterial; Deutsche Zwerghühner kamen hinzu. 1961 wurde der wildbraune Farbenschlag anerkannt. Die Zwergform ist somit wesentlich jünger als die steirische Großrasse.',
 'Ein kleiner Federschopf ergänzt den Einfachkamm. Der längliche, kräftige Körper steht auf unbefiederten Läufen; Brust und Bauch sind gut entwickelt. Beim Hahn heben sich die Behänge und der besichelte Schwanz von der eher schlichten Landhuhnfigur ab.',
 'Der Schopf ist ein Zuchtmerkmal und kein Hinweis auf ein ruhiges Temperament. Die Gewöhnung an Menschen sollte mit langsamem, regelmäßigem Kontakt erfolgen.',
 'Scharrflächen und Deckung bieten Beschäftigung. Der Schopf darf die Sicht nicht einschränken. Bei der Gruppenzusammenstellung sind die tatsächliche Aktivität und Verträglichkeit wichtiger als die geringe Körpergröße.',
 'Ziel war eine kleine Ausgabe des steirischen Nutz- und Ausstellungshuhns. Der Erhalt des Schopfes allein reicht nicht: Körperform, Eierleistung und gesunde Aufzucht gehören ebenfalls zur Zucht.',
 'Wildbraun, weiß und gesperbert sind im ausgewerteten deutschen Verzeichnis aufgeführt.',
 [('SV: Geschichte der Steirerhühner','https://steirerhuehner.jimdofree.com/geschichte/'),('Deutscher SV: Historisches','https://sv-altsteirer-sulmtaler.de/home/historisches-1')])

add('Zwerg-Andalusier','Deutschland und England','In Deutschland 1920 ausgestellt',
 'Blau gesäumte Landhuhnzwerge mit weißem Ohrschmuck.',
 'Die Verzwergung verbindet die europäische Zucht des spanischen Andalusiers mit der Liebhaberzucht kleiner Hühner. Die ältere BDRG-Tafel nennt Deutschland und England und belegt eine deutsche Ausstellung bereits 1920. Diese Angabe bezeichnet eine frühe Präsentation, nicht den exakten Beginn aller Zuchtversuche.',
 'Die schlanke, gestreckte Gestalt trägt einen Einfachkamm, helle Ohrscheiben und unbefiederte, dunkle Läufe. Das Blau des Körpergefieders wird durch eine dunklere Federsäumung gezeichnet. Beim Hahn sind Behänge und Obergefieder dunkler als große Teile des Mantels.',
 'Die elegante Form sollte nicht mit garantierter Zutraulichkeit verwechselt werden. Für die Haltung lohnt der Blick auf die Aufmerksamkeit und das Ausweichverhalten einzelner Tiere.',
 'Auslauf und geeignete Sitzplätze müssen auch beweglichen Tieren sichere Wege bieten. Große Kopfpunkte verdienen Schutz vor nasser Kälte. Bei der Zuchtauswahl sollten saubere Zeichnung und gesunde Körperentwicklung gemeinsam betrachtet werden.',
 'Die Rasse erhält den mediterranen Legehuhntyp in Zwerggröße. Ihr Reiz liegt besonders im Zusammenspiel von Form und Säumung; die Gefiederfarbe allein begründet keine weitere Rasse.',
 'Blau-gesäumt.')

add('Zwerg-Dorking','England',None,
 'Breite, tief stehende Fünfzeher mit englischer Rassegeschichte.',
 'Die Zwergform wurde nach dem Vorbild des englischen Dorking entwickelt. Dessen Geschichte als Fleischhuhn darf nicht mit einem ebenso hohen Alter der Zwergform gleichgesetzt werden. Die ausgewertete BDRG-Tafel belegt England als Herkunft, nennt aber kein gesichertes Entstehungsjahr der kleinen Rasse.',
 'Der langgestreckte, tiefe Körper wirkt von der Seite annähernd rechteckig. Kurze, fleischfarbene Läufe und die zusätzliche fünfte Zehe gehören zu den auffälligen Merkmalen. Die volle Brust und der gut entwickelte Bauch unterscheiden die Rasse von schmalen, hochbeinigen Legehuhnzwergern.',
 'Dorking werden in der Züchterbeschreibung als eher ruhig beschrieben. Auch bei den Zwergen sollte diese Orientierung immer an den konkreten Tieren überprüft werden.',
 'Niedrige, gut erreichbare Sitzstangen und trockene Laufbereiche passen zum tiefen Stand. Die Zehen sollten regelmäßig kontrolliert werden. Eine zusätzliche Zehe ersetzt keine Beurteilung des sicheren Gangs und der gesunden Fußstellung.',
 'Die Zwergzucht bewahrt den charakteristischen englischen Fleischhuhntyp, ohne eine Mastleistung der Großrasse zu versprechen. Die Fünfzehigkeit ist ein Rassemerkmal, nicht automatisch ein Gesundheitsmangel.',
 'Silberhalsig und silber-wildfarbig.',
 [('Züchterin: Dorking und Zwerg-Dorking','https://www.sannes-gluck.de/index.php/rassebeschreibung')])

add('Deutsche Zwerg-Langschan','Deutschland','1910 erstmals ausgestellt',
 'Hoch gestellte Zwerge mit abgerundeter Figur und ansteigender Rückenlinie.',
 'Die deutsche Zwergzucht wurde bereits 1910 öffentlich gezeigt. Ihr Vorbild sind Deutsche Langschan, nicht die gesondert standardisierten Croad-Langschan. Deshalb werden Deutsche Zwerg-Langschan und Zwerg-Croad-Langschan als zwei Rassen geführt und nicht unter dem ungenauen Namen Langschan verdoppelt.',
 'Lange, unbefiederte Läufe heben den vollen Rumpf deutlich an. Der Rücken steigt vom Halsbehang ohne Absatz zum gut geschlossenen Schwanz. Von oben soll die Schwanzpartie an einen Zuckerhut erinnern. Dazu kommen ein kleiner Einfachkamm und eine gleichmäßig gerundete Unterlinie.',
 'Die auffällige Haltung ist ein Formmerkmal. Eine bestimmte Zahmheit oder Flugleistung lässt sich aus der hohen Stellung nicht ableiten.',
 'Sitzplätze und Durchgänge brauchen genügend Höhe für die langen Beine und den aufgerichteten Körper. Ein trockener Boden schützt Füße und Gefieder. Zu knapp bemessene Abteile passen trotz des Zwergnamens nicht zu dieser hohen Figur.',
 'Die Rasse verbindet einen eigenständigen Ausstellungstyp mit Nutzleistung. Für das Bruteier-Mindestgewicht wird der neuere veröffentlichte SV-Standard mit 40 g verwendet, nicht der abweichende Wert der älteren Rassetafel.',
 'Belegt sind unter anderem schwarz, weiß, blau-gesäumt und birkenfarbig.',
 [('Sonderverein: Standard, Stand 2021','https://sv-zwerg-langschan.de/standard/')])

add('Zwerg-Minorka','Deutschland und England',None,
 'Gestreckte Mittelmeerzwerge mit besonders großen weißen Ohrscheiben.',
 'Die kleine Form wurde in England und Deutschland aus dem Minorka-Typ entwickelt. Die historische Bedeutung der Großrasse als Legehuhn gab das Vorbild; die Zwergform ist eine eigene Zuchtrichtung. Ein einziges, allgemein belegtes Gründungsjahr geht aus den hier verwendeten Quellen nicht hervor.',
 'Der Körper ist länglich und wird stolz getragen. Große weiße Ohrscheiben stehen neben roten Kopfpunkten; die Läufe sind dunkel und unbefiedert. Das Gefieder liegt vergleichsweise geschlossen an. Anerkannt sind neben einfachkämmigen auch rosenkämmige Tiere.',
 'Die Rassefamilie wird als lebhaft beschrieben. Daraus folgt weder eine Garantie für Scheu noch für Zahmheit; Erfahrungen mit Menschen beeinflussen den Umgang deutlich.',
 'Kämme, Kehllappen und Ohrscheiben sollten sauber bleiben und vor feuchter Kälte geschützt sein. Raum zum Ausweichen erleichtert ruhiges Einfangen. Eine sichere Einfriedung ist sinnvoll, ohne eine unbewiesene feste Flughöhe zu unterstellen.',
 'Erhalten wird ein mediterraner Legehuhntyp mit auffälligem Ohrschmuck. Weiße Ohrscheiben und weiße Eier sind beide typische Merkmale; das eine ist jedoch kein allgemeines Naturgesetz für alle Hühnerrassen.',
 'Schwarz und weiß; beide im Verzeichnis mit Einfach- oder Rosenkamm.',
 [('GEH: Minorka und Einordnung der Zwergform','https://g-e-h.de/index.php/rassebeschreibungen/55-gefluegelhuhn/503-minorka')])

add('Zwerg-Paduaner','England','Ende des 19. Jahrhunderts; 1910 in Berlin gezeigt',
 'Haubenzwerge mit voller Rundhaube und dichtem Federbart.',
 'Der Sonderverein beschreibt die englische Entwicklung durch William Flamank Entwisle gegen Ende des 19. Jahrhunderts. Weiße Tiere wurden 1910 auf der Nationalen in Berlin vorgestellt. Die Zwergform übernahm die auffällige Kopfgestaltung der Paduaner und wurde zu einer eigenen Ausstellungsrasse.',
 'Eine volle Rundhaube sitzt auf der Schädelerhöhung; ein dichter Kinn- und Backenbart rahmt das Gesicht. Ein regulärer Kamm fehlt. Der leichte Landhuhnkörper wird fast waagerecht getragen, mit anliegenden Flügeln und gut entwickeltem Schwanz.',
 'Der veröffentlichte Standard beschreibt ein ruhiges, zutrauliches Wesen. Das ist ein Rasseideal; Gewöhnung, freie Sicht und passende Gruppen bleiben entscheidend.',
 'Haube und Bart dürfen Augen und Sichtfeld nicht verdecken. Tränken und Futterplätze sollten so angeordnet sein, dass die Kopffedern nicht dauerhaft nass oder verschmutzt werden. Geschützte Auslaufbereiche und ruhiges Annähern erleichtern die Betreuung.',
 'Die züchterische Aufgabe liegt im Gleichgewicht zwischen reichem Kopfgefieder und uneingeschränkter Orientierung. Eine besonders große Haube ist kein Fortschritt, wenn sie die Sicht behindert.',
 'Beispiele sind silber-schwarzgesäumt, gold-schwarzgesäumt, chamois-weißgesäumt, schwarz und weiß.',
 [('Sonderverein: Zwerg-Paduaner mit Standard','https://www.sv-silkiespolands.de/betreute-rassen/zwerg-paduaner/')])

add('Zwerg-Plymouth-Rocks','Deutschland','1914 erstmals gezeigt',
 'Kräftige kleine Nutz- und Ausstellungshühner mit gelben Läufen.',
 'Die deutsche Verzwergung orientierte sich am amerikanischen Plymouth Rock. Die BDRG-Tafel nennt eine erste Vorstellung 1914. Die Zwergform erhält den breiten Nutztyp, ist aber weder mit Zwerg-Amrocks noch mit jeder gestreiften Zwerghuhnrasse gleichzusetzen.',
 'Ein breiter, kräftiger Körper, volle Brust und gut entwickelter Bauch bestimmen die Figur. Der Kopf trägt einen Einfachkamm, die unbefiederten Läufe sind gelb. Bei gestreiften Tieren muss neben der Zeichnung der harmonische Körperbau erkennbar bleiben.',
 'Die Nutzform beschreibt keine individuelle Rangordnung. Wer einen ruhigen Bestand aufbauen möchte, sollte Verhalten und Verträglichkeit der verfügbaren Linie kennenlernen.',
 'Stabile, leicht erreichbare Sitzplätze passen zum kräftigen Körper. Mehrere Futterzugänge vermeiden unnötiges Gedränge. Auslauf mit Scharrmaterial bietet Bewegung, damit eine volle Figur nicht mit übermäßiger Körperfülle verwechselt wird.',
 'Die Rasse verbindet das Erscheinungsbild eines Zweinutzungshuhns mit handlicherer Größe. Erhaltung bedeutet, Körperform und Nutzmerkmale gemeinsam zu berücksichtigen und nicht nur eine bestimmte Federzeichnung zu vermehren.',
 'Unter anderem gestreift, schwarz, weiß und gelb.',
 [('Sonderverein: Plymouth-Rocks-Zucht','https://plymouth-rocks.de/')])

add('Appenzeller Zwerg-Barthühner','Schweiz','1996 anerkannt laut BDRG-Rassetafel',
 'Kleine Schweizer Landhühner mit Rosenkamm und vollem Federbart.',
 'Die Zwergform entstand als kleinere Entsprechung der Appenzeller Barthühner. Die BDRG-Rassetafel nennt die Schweiz und 1996 als Anerkennungsjahr. Der Bezug zum Appenzellerland kennzeichnet das Rassevorbild; die Zwergzucht ist eine jüngere Entwicklung und keine unveränderte alte Landpopulation.',
 'Ein kräftiger, länglicher Rumpf trägt eine volle Brust und einen gut entwickelten Bauch. Rosenkamm und ausgeprägter Bart prägen den Kopf. Beine und Läufe bleiben unbefiedert. Der Bart verdeckt kleine Kopfpunkte, darf aber nicht die Sicht auf die Umgebung nehmen.',
 'Ein Gesicht mit dichtem Bart sagt wenig über den Charakter aus. Die Reaktion auf Pfleger, neue Gegenstände und andere Hühner sollte an der jeweiligen Gruppe beobachtet werden.',
 'Bartfedern brauchen saubere Futter- und Wasserstellen. Ein trockener Stall und Deckung im Auslauf ermöglichen normalen Landhuhnalltag. Bei der Kontrolle sollte unter dem Kopfgefieder auch die tatsächliche Haut- und Federpflege beurteilt werden.',
 'Die kleine Rasse bewahrt den Appenzeller Typ in eigenständiger Zucht. Auch ein kleines Rasseformat braucht ausreichend Bewegung und darf nicht auf die Rolle eines dekorativen Käfigtiers reduziert werden.',
 'Schwarz und rebhuhnhalsig.',
 [('Schweizer Rasseclub: Appenzeller und ihre Zwerge','https://www.appenzeller-und-schweizerhuhn.com/general-9')])

add('Bassetten','Belgien',None,
 'Belgische Zwerghühner mit tiefem Stand und vergleichsweise kräftiger Figur.',
 'Bassetten gehören zur belgischen Zwerghuhnzucht. Sie werden im BDRG eigenständig geführt und nicht als bloßer Farbenschlag anderer Landhuhnzwerge behandelt. Die herangezogenen Tafeln belegen Herkunft und Leistungsrichtwerte, liefern aber keinen eindeutig abgesicherten einzelnen Entstehungstermin.',
 'Der lange, tiefe Rumpf und die eher kurzen Beine geben der Rasse eine bodennahe Silhouette. Der Hahn trägt einen entwickelten Schwanz; auf dem Kopf steht ein Einfachkamm. Die Wachtelzeichnung erzeugt unterschiedliche Gefiederbilder bei Hahn und Henne.',
 'Der tiefe Stand erlaubt keine verlässliche Aussage über Flugfreude. Eine konkrete Linie sollte man beim Futtersuchen, Aufbaumen und Umgang mit Menschen kennenlernen.',
 'Flache Zugänge zu Nestern und niedrige Sitzmöglichkeiten sind praktisch. Einstreu muss trocken bleiben, damit das bodennahe Gefieder nicht verschmutzt. Die geringe Standhöhe darf nicht zu einer unnötig kleinen oder reizarmen Haltung führen.',
 'Die belgische Rasse verbindet Ausstellungstyp und Eiernutzen. Beim Beurteilen ist die Gesamtsilhouette wichtiger als die isolierte Betrachtung einzelner besonders kurzer Beine.',
 'Wachtelfarbig, silber-wachtelfarbig und perlgrau-silberwachtelfarbig.',
 [('Sonderverein: Bassetten','https://www.seltene-zwerghuehner.eu/unsere-rassen/bassetten/')])

add('Bergische Zwerg-Kräher','Deutschland','Anfang des 20. Jahrhunderts; 1926 ausgestellt',
 'Aufgerichtete kleine Langkräher mit goldbrauner Dobbelzeichnung.',
 'Die Verzwergung der Bergischen Kräher erfolgte in Deutschland zu Beginn des 20. Jahrhunderts. Kleine Vertreter der Großrasse und Deutsche Zwerghühner gehörten zur Entwicklung. Bereits 1926 wurden Tiere gezeigt. Die alte Langkrähertradition ist das Vorbild, nicht ein gleich hohes Alter der Zwergform.',
 'Die Rasse zeigt einen schlanken, aufgerichteten Körper, einen Einfachkamm und einen gut besichelten Schwanz. Die goldbraune Dobbelung liegt auf dunklem Grund. Die Zeichnung ist von gewöhnlicher Sprenkelung zu unterscheiden und gehört zum bergischen Rassecharakter.',
 'Der besondere Krähruf ist das namensgebende Merkmal. Seine individuelle Länge und Lautstärke lassen sich nicht aus dem Zwergnamen vorhersagen; vor der Haltung sollte man erwachsene Hähne hören.',
 'Auslauf und Deckung passen zum Landhuhntyp. Bei der Standortwahl ist der Hahnengesang zu berücksichtigen. Eine sichere Einfriedung sollte an der tatsächlichen Aktivität der Tiere ausgerichtet werden.',
 'Die Zucht erhält sowohl die charakteristische Form als auch die Langkrähereigenschaft. Eine rein nach Federfarbe ausgewählte Gruppe würde dem besonderen Zuchtziel nicht vollständig gerecht.',
 'Schwarz-goldbraungedobbelt.',
 [('Sonderverein: Bergische Rassen und Zuchten','https://sv-bergische-huehnerrassen.de/zuchter')])

add('Bergische Zwerg-Schlotterkämme','Deutschland',None,
 'Bergische Landhuhnzwerge mit seitlich fallendem Hennenkamm.',
 'Die Zwergform bewahrt den Typ der Bergischen Schlotterkämme in kleinerer Größe. Sie ist im deutschen Rasseverzeichnis gesondert aufgeführt. Ein bestimmtes Entstehungsjahr ist aus der verwendeten Rassetafel nicht sicher abzuleiten; das hohe Alter der Großrasse wird deshalb nicht auf die Zwerge übertragen.',
 'Der längliche Landhuhnkörper steht vergleichsweise tief. Besonders die Henne zeigt den namengebenden, zur Seite geneigten Einfachkamm. Weiße Zeichnungspartien auf schwarzem Grund bilden die für den anerkannten Farbenschlag charakteristische Dobbelung.',
 'Der Sonderverein beschreibt lebhafte, aufmerksame Tiere, die durch regelmäßigen Kontakt zutraulicher werden können. Das große Kammblatt darf die Orientierung nicht behindern.',
 'Strukturierter Auslauf bietet Beschäftigung und Deckung. Ein trockenes, vor Wind geschütztes Stallklima ist wegen der ausgebildeten Kopfpunkte wichtig. Empfehlungen zu festen Quadratmeterzahlen oder garantierten Flughöhen sind aus den geprüften Standardquellen nicht abzuleiten.',
 'Erhalten wird eine besondere bergische Form mit eigenständigem Kamm- und Zeichnungsbild. Abweichende Angaben zu Farben und Leistung auf Vereinsseiten werden hier zugunsten des belegten BDRG-Verzeichnisstands getrennt behandelt.',
 'Schwarz-weißgedobbelt; nicht mit der goldbraunen Farbe der Zwerg-Kräher verwechseln.',
 [('Sonderverein: Bergische Zwerg-Schlotterkämme','https://sv-bergische-huehnerrassen.de/bergische-zwerg-schlotterkamme')])

add('Brügger Zwerg-Kämpfer','Deutschland',None,
 'Kräftige Kämpferzwerge mit breiten Schultern und dunklen Kopfpunkten.',
 'Die deutsche Zwergzucht nimmt die belgischen Brügger Kämpfer zum Vorbild. Damit sind Herkunft des Rassevorbildes und Entstehungsland der kleinen Form zu unterscheiden. Die ausgewertete BDRG-Tafel nennt Deutschland, aber kein gesichertes Gründungsjahr.',
 'Breite Schultern, starke Beine und ein muskulöser Rumpf prägen die Figur. Der Kopf trägt einen kleinen Erbsenkamm; dunkle Gesichtspartien gehören zum Kämpferausdruck. Das feste Gefieder lässt den Körperbau deutlicher hervortreten als bei weich befiederten Zwergformen.',
 'Eine Kämpferfigur ist keine sichere Vorhersage des Verhaltens gegenüber Menschen. Bei der Vergesellschaftung verdienen Rangordnung und individuelle Verträglichkeit besondere Aufmerksamkeit.',
 'Die kräftigen Tiere benötigen sichere Bewegungsflächen und Rückzugsmöglichkeiten. Für unverträgliche Tiere muss eine Trennung möglich sein. Ein großzügig gegliederter Auslauf ist hilfreicher als die Annahme, der Zwergname erlaube enge Unterbringung.',
 'Heute steht die Erhaltung des historischen Kämpfertyps im Mittelpunkt, nicht die Durchführung von Tierkämpfen. Gesunde Beine und sichere Bewegungen sind wichtiger als übersteigerte Körpermerkmale.',
 'Belegte Beispiele sind schwarz und schwarz-rot.',
 [('Zwergkämpfer-Club: Standards','https://www.xn--zwergkmpferclub-5kb.de/unsere-zwergkaempfer/')])

add('Deutsche Zwerghühner','Deutschland','1917 erstmals ausgestellt',
 'Eigenständige deutsche Landhuhnzwerge mit langem Schmuckgefieder.',
 'Deutsche Zwerghühner entstanden aus kleinen Landhühnern und wurden 1917 erstmals ausgestellt. Sie sind eine eigenständige Zwergrasse und keine verkleinerte Ausgabe einer gleichnamigen Großrasse. Das Zuchtziel verbindet eine elegante Figur mit dem besonderen Schmuckgefieder des Hahns.',
 'Der schlanke Rumpf wird von einem ausgebildeten Schwanz und langem Behang ergänzt. Ein Einfachkamm und unbefiederte Beine halten die Kopf- und Beinsilhouette klar. Die Henne wirkt schlichter, soll aber denselben fein gebauten Landhuhntyp zeigen.',
 'Die elegante, leichte Figur lässt keine pauschale Einstufung als zahm oder scheu zu. Für den Alltag ist es sinnvoll, Tiere zu wählen, die mit ruhiger Annäherung vertraut sind.',
 'Ein abwechslungsreicher Auslauf und gut erreichbare, sichere Sitzplätze ermöglichen Bewegung. Lange Schmuckfedern sollten weder an zu engen Durchgängen scheuern noch durch dauernden Bodenkontakt verschmutzen. Auch kleine Landhuhnzwerge brauchen Rückzugsmöglichkeiten.',
 'Erhalten wird ein deutscher Urzwergtyp mit besonderer Federentwicklung. Der Name Deutsche Zwerghühner ist ein konkreter Rassename und keine Sammelbezeichnung für alle in Deutschland gezüchteten Zwerghühner.',
 'Beispiele sind wildfarbig, goldhalsig, orangehalsig, schwarz und weiß.')

add('Deutsche Zwerg-Reichshühner','Deutschland','Zucht seit den frühen 1930er-Jahren',
 'Kleine Zweinutzungshühner mit gerundetem Rechteckkörper und Rosenkamm.',
 'Die Zwergform wurde in Deutschland zu Beginn der 1930er-Jahre entwickelt. Sie übernahm den Nutztyp der Deutschen Reichshühner. Die Geschichte der großen Rasse und die spätere Verzwergung sind getrennte Schritte; die kleine Form hat einen eigenen Standard.',
 'Ein länglicher, gerundeter Rechteckkörper mit voller Brust und breitem Bauch kennzeichnet die Rasse. Der Rosenkamm liegt flach am Kopf. Die Beine bleiben unbefiedert, der Schwanz geht ohne harten Absatz in die Körperlinie über.',
 'Die abgerundete Figur ist nicht mit garantierter Gemütlichkeit gleichzusetzen. Ob eine Gruppe umgänglich bleibt, hängt auch von Aufzucht, Platzangebot und der Zusammenstellung erwachsener Hähne ab.',
 'Breite Zugänge und mehrere Futterstellen passen zum kräftigen Nutztyp. Auslauf sollte Scharren und Futtersuche ermöglichen. Bei der Zuchtkontrolle ist neben dem dichten Gefieder auch die tatsächliche Körperkondition zu prüfen.',
 'Ziel ist ein kleiner Wirtschaftshuhntyp, bei dem Eierleistung und Form zusammenpassen. Der Rosenkamm ist dabei ebenso Teil des Rassebildes wie Brusttiefe und eine harmonische Rückenlinie.',
 'Belegte Beispiele sind weiß-schwarzcolumbia, schwarz, weiß, rot und gestreift.')

add('Frankfurter Zwerghühner','Deutschland','Zuchtbeginn Ende der 1970er-Jahre; Anerkennung nach Vorstellungen 1994–1997',
 'Weiße, schwarz gezeichnete Urzwerge mit Einfachkamm und kräftigem Rumpf.',
 'Wilhelm Klee entwickelte die Rasse aus einfachkämmigen Nachkommen seiner Zwerg-Wyandotten und kreuzte helle Zwerg-Brahma ein. Der regionale Name wurde nach seinem damaligen Wohnort gewählt. Nach mehrjährigen Vorstellungen als Neuzüchtung wurde daraus eine eigenständig anerkannte Zwerghuhnrasse.',
 'Die volle, abgerundete Figur trägt einen Einfachkamm. Die helle Grundfarbe kontrastiert mit dunkler Zeichnung besonders an Hals und Schwanz. Die Silhouette darf nicht bloß wie ein kleineres Tier einer Ausgangsrasse aussehen; sie muss den festgelegten Frankfurter Typ erkennen lassen.',
 'Die Entstehung aus anderen Zwergrassen liefert keine verlässliche Garantie für ein bestimmtes Temperament. Im Bestand sollten Umgang mit Menschen und Verträglichkeit tatsächlich beobachtet werden.',
 'Gut zugängliche Nester und stabile Sitzgelegenheiten erleichtern den Alltag. Bei heller Grundfarbe sind trockene Einstreu und saubere Ruheplätze hilfreich. Die kompakte Form ersetzt nicht die Möglichkeit zum Scharren und Bewegen.',
 'Die Rasse ist ein Beispiel dafür, wie ein neuer Typ aus gezielter Auswahl und anschließender Standardisierung entstehen kann. Für ihre Erhaltung zählen stabile Merkmale über mehrere Generationen.',
 'Weiß-schwarzcolumbia.',
 [('Sonderverein: Entstehung der Frankfurter Zwerghühner','https://www.sv-frankfurter-zwerghuehner.com/die-entstehung')])

add('Grübbe Bartzwerge','Belgien',None,
 'Belgische Bartzwerge ohne ausgebildeten Schwanz.',
 'Grübbe Bartzwerge gehören zur belgischen Bartzwergzucht und sind als schwanzlose Rasse eigenständig anerkannt. Sie werden deshalb nicht als bloß unvollständig befiederte Antwerpener Bartzwerge eingeordnet. Ein einzelnes, sicher belegtes Entstehungsjahr nennt die herangezogene BDRG-Tafel nicht.',
 'Kinn- und Backenbart, Rosenkamm und ein voller Vorderkörper prägen den Kopf- und Körperausdruck. Der hintere Körperabschluss zeigt keine normale Schwanzpartie. Gerade diese Kombination unterscheidet die Rasse von ähnlich kleinen, aber beschwänzten Bartzwergen.',
 'Der fehlende Schwanz ist kein Charaktermerkmal. Bei der Auswahl sind sichere Bewegung, ungestörte Futteraufnahme und die Reaktion der Tiere auf ihre Umgebung zu beobachten.',
 'Trockene Einstreu und saubere Tränken helfen, den Bart zu pflegen. Die schwanzlose Figur sollte bei der Beobachtung von Gleichgewicht und Fortpflanzung mitbedacht werden. Kleine Tiere brauchen auch in gemischten Gruppen ausreichend geschützte Futterplätze.',
 'Die Zucht bewahrt einen besonderen belgischen Rassetyp. Gesundheit und zuverlässige Fortpflanzung sind dabei mindestens ebenso wichtig wie die eindeutige Ausbildung des schwanzlosen Abschlusses.',
 'Das BDRG-Verzeichnis verweist auf die Farbenschläge der Antwerpener Bartzwerge; Beispiele sind schwarz und gesperbert.')

add('Indische Zwerg-Kämpfer','England','Gegen Ende des 19. Jahrhunderts',
 'Breite, muskulöse Kämpferzwerge mit kurzem, festem Gefieder.',
 'Trotz des Namens entstand die Zwergform in England. Ihr Vorbild ist der dort entwickelte Indische Kämpfer. Die BDRG-Tafel ordnet ihre Entstehung gegen Ende des 19. Jahrhunderts ein. Der Name ist deshalb nicht als Beleg einer unmittelbar indischen Herkunft der Zwergzucht zu lesen.',
 'Eine außerordentlich breite Brust, starke Schultern und kräftige, weit gestellte Beine prägen den Körper. Kurzes, hartes Gefieder verdeckt die Muskulatur nur wenig. Der Kopf trägt einen niedrigen Erbsenkamm; die gesamte Figur wirkt gedrungen und kraftvoll.',
 'Die große Körperbreite sagt nichts Sicheres über Zutraulichkeit aus. Bei Zusammenstellungen erwachsener Tiere sollten mögliche Konflikte früh erkannt und Trennmöglichkeiten bereitgehalten werden.',
 'Niedrige, stabile Einrichtungen passen zur schweren Figur. Rutschfester Boden und trockene Liege- beziehungsweise Ruhebereiche sind wichtig. Das knappe Gefieder verlangt Schutz vor dauernder Nässe und kaltem Wind.',
 'Die heutige Rassezucht erhält einen historischen Kämpfertyp. Die Bezeichnung Zwerg darf nicht dazu verleiten, den Bewegungsraum nach dem Maß besonders leichter Urzwerge zu bemessen.',
 'Fasanenbraun, blau-fasanenbraun, weiß-fasanenbraun und weiß.',
 [('Zwergkämpfer-Club: Indische Zwerg-Kämpfer','https://www.xn--zwergkmpferclub-5kb.de/unsere-zwergkaempfer/')])

add('Lütticher Zwerg-Kämpfer','Belgien',None,
 'Hoch aufgerichtete belgische Kämpferzwerge mit starken Knochen.',
 'Die belgische Zwergform führt den Typ der Lütticher Kämpfer in kleinerem Maßstab weiter. Sie ist vom Brügger Zwerg-Kämpfer zu unterscheiden. Ein genaues Entstehungsjahr wird hier nicht angegeben, weil es aus den herangezogenen Standardquellen nicht zuverlässig hervorgeht.',
 'Der lange, breite Rumpf wird aufgerichtet getragen. Sehr breite Schultern, starke Knochen, lange Läufe und hartes Gefieder sind kennzeichnend. Dunkle Kopfpunkte, kräftige Augenbrauen und ein kleiner Erbsenkamm verstärken den markanten Ausdruck.',
 'Der Standard beschreibt vor allem den kräftigen Kämpferausdruck. Er ist keine Zusage eines bestimmten Verhaltens; Rangordnung und Verträglichkeit müssen im jeweiligen Bestand beurteilt werden.',
 'Die hohen Tiere brauchen ausreichende Kopffreiheit und sichere Wege zwischen Ruhe- und Futterplätzen. Zur Eingliederung neuer Tiere sind getrennte Abteile hilfreich. Nasse, glatte Flächen passen nicht zu einer sicheren Bewegung auf den langen Beinen.',
 'Die Erhaltung betrifft die charakteristische belgische Kämpferfigur. Ein möglichst scharfer Gesichtsausdruck darf nicht mit erwünschter Aggressivität im Umgang oder mit einer Eignung zu Tierkämpfen gleichgesetzt werden.',
 'Belegte Beispiele sind schwarz, schwarz-rot, blau und orangebrüstig.',
 [('Zwergkämpfer-Club: Lütticher Zwerg-Kämpfer','https://www.xn--zwergkmpferclub-5kb.de/unsere-zwergkaempfer/')])

add('Ostfriesische Zwerg-Möwen','Deutschland',None,
 'Leichte Landhuhnzwerge mit feiner Flockenzeichnung.',
 'Die in Deutschland entwickelte Zwergform nimmt die Ostfriesischen Möwen zum Vorbild. Sie erhält deren besonderen Zeichnungstyp in kleiner Größe. Die namensgebende Nähe zur Küstenregion beschreibt die Zuchttradition; es handelt sich selbstverständlich um Haushühner und nicht um Möwenvögel.',
 'Der leichte, gestreckte Körper trägt einen Einfachkamm und einen ausgebildeten Schwanz. Die Henne zeigt eine feine Flockenzeichnung, während der Hahn in großen Teilen gleichmäßiger gefärbt erscheint. Unbefiederte Läufe vervollständigen den klaren Landhuhnumriss.',
 'Für konkrete Aussagen zur Zahmheit oder Flugleistung sind die Tiere der jeweiligen Linie aussagekräftiger als die Zeichnung. Ein ruhiger Umgang erleichtert die Eingewöhnung.',
 'Deckung, unterschiedliche Scharrbereiche und sichere Sitzplätze bieten Abwechslung. Eine Einfriedung sollte beobachtete Flugversuche berücksichtigen. Die kleine Körpergröße rechtfertigt keine reizarme Dauerhaltung in einem engen Ausstellungsabteil.',
 'Die Zwergform verbindet eine regional geprägte Federzeichnung mit dem Nutztyp der Großrasse. Beim Züchten sollten feine Zeichnung und ein kräftiger, gesunder Körper gleichermaßen erhalten werden.',
 'Beispiele sind silber-schwarzgeflockt und gold-schwarzgeflockt.')

add('Ruhlaer Zwerg-Kaulhühner','Deutschland, Thüringen',None,
 'Schwanzlose Thüringer Zwerge mit befiederten Füßen.',
 'Die Rasse entstand im thüringischen Raum um Ruhla. Sie gehört zur eigenständigen deutschen Zwerghuhnzucht und ist nicht einfach die schwanzlose Ausgabe beliebiger Fußfederzwerge. Die Verbindung von Kaulbildung und Fußgefieder gibt ihr einen eigenen Standard und eine gesonderte Rassebezeichnung.',
 'Ein kurzer Körperabschluss ohne normale Schwanzpartie trifft auf deutlich befiederte Beine und Füße. Der Kopf trägt einen Einfachkamm; bärtige Ausführungen sind ebenfalls im Verzeichnis berücksichtigt. Diese Kombination unterscheidet sie von den glattläufigen Zwerg-Kaulhühnern.',
 'Das besondere Federbild beschreibt keine feste Charaktereigenschaft. Für eine passende Gruppe sollte man Aktivität, sicheren Gang und Verhalten an den Futterstellen beobachten.',
 'Trockene, lockere Einstreu ist wegen des Fußgefieders besonders wichtig. Anhaftender Schmutz sollte früh erkannt werden. Niedrige Zugänge und nicht zu enge Durchgänge vermeiden, dass die Fußfedern unnötig beschädigt werden.',
 'Die Zucht erhält einen eigenständigen Thüringer Rassetyp. Bei schwanzlosen Tieren gehören die ungestörte Bewegung und zuverlässige Fortpflanzung ebenso zur Auswahl wie Gefiederzeichnung und Befiederung der Füße.',
 'Beispiele sind gold-porzellanfarbig, isabell-porzellanfarbig und weiß.',
 [('Sonderverein: Ruhlaer Zwerg-Kaulhühner','https://www.seltene-zwerghuehner.eu/unsere-rassen/ruhlaer-zwerg-kaulh%C3%BChner/')])

add('Thüringer Zwerg-Barthühner','Deutschland','Um 1910 in Thüringen erzüchtet',
 'Kleine Landhühner mit vollem Bart und klarer Körperlinie.',
 'Die Zwergzucht entwickelte sich im Thüringer Raum um 1910. Sie überträgt den Typ der Thüringer Barthühner in ein eigenes kleines Rasseformat. Der ältere regionale Hintergrund des großen Barthuhns ist dabei von der späteren Geschichte seiner Zwergform zu unterscheiden.',
 'Ein dichter Kinn- und Backenbart rahmt den Kopf unter dem Einfachkamm. Der längliche Rumpf, der ausgebildete Schwanz und die unbefiederten Läufe ergeben eine schlichte Landhuhnfigur. Die Bartbildung ist deutlicher als die kleinen, teilweise verdeckten Kopflappen.',
 'Der Federbart kann den Gesichtsausdruck verändern, liefert aber keinen sicheren Hinweis auf Temperament. In der Haltung sollte man auf aufmerksame, sicher orientierte Tiere achten.',
 'Futter und Wasser sollten erreichbar sein, ohne den Bart ständig zu durchnässen. Die Augen müssen frei bleiben. Ein gegliederter Auslauf mit Scharrmaterial verbindet Bewegung mit Rückzug und erleichtert die Bildung einer stabilen Gruppe.',
 'Die Rasse erhält einen regionalen deutschen Barthuhntyp. Dabei ist die gesamte Körperform zu bewahren; ein besonders üppiger Bart allein macht noch kein typgerechtes Tier aus.',
 'Beispiele sind schwarz, weiß, blau-gesäumt und rebhuhnhalsig.')

add('Zwerg-Asil','England','Um 1880 ausgestellt',
 'Kompakte Kämpferzwerge mit straffem Körper und markantem Kopf.',
 'Die Zwergform entstand in England und wurde dort bereits um 1880 ausgestellt. Sie bewahrt Merkmale der Asil, deren große Rasse auf südasiatische Kämpfer zurückgeht. Diese historische Verbindung ist nicht mit einer unmittelbaren indischen Entstehung der standardisierten Zwergform gleichzusetzen.',
 'Der kompakte, kräftig bemuskelte Rumpf trägt kurzes, festes Gefieder. Kopf und Schnabel wirken kräftig; der kleine Kamm bleibt eng am Schädel. Die deutlichen Schultern und starken Beine ergeben eine andere Silhouette als bei hochbeinigen oder weich befiederten Zwergen.',
 'Bei Kämpferrassen ist die Verträglichkeit erwachsener Tiere besonders sorgfältig zu prüfen. Ein rassetypischer Kopfausdruck lässt aber keine sichere Aussage über die Beziehung zum Pfleger zu.',
 'Übersichtliche Gruppen und abtrennbare Bereiche erleichtern die Betreuung. Ein trockener, windgeschützter Stall passt zur knappen Befiederung. Sitzmöglichkeiten sollten stabil und so niedrig sein, dass die Tiere sicher auf- und abspringen können.',
 'Heute steht die Erhaltung des historischen Typs im Rahmen der Rassezucht im Vordergrund. Vitalität, Fortpflanzung und gesundes Bewegungsverhalten dürfen dabei nicht hinter auffälligen Körpermerkmalen zurückstehen.',
 'Beispiele sind rotbunt, gelbbunt und weiß.')

add('Zwerg-Augsburger','Deutschland','Zucht um 1970; 1975 anerkannt',
 'Bayerische Landhuhnzwerge mit dem besonderen Becherkamm.',
 'Die Zwerg-Augsburger wurden im Raum Augsburg entwickelt und 1975 anerkannt. Der Sonderverein beschreibt die anschließende Festigung des besonderen Kammes in der Zwergzucht. Die kleine Rasse bewahrt damit ein auffälliges Merkmal der bayerischen Großrasse in eigenständiger Zucht.',
 'Der Körper zeigt eine volle, gestreckte Landhuhnform mit leicht aufgerichteter Haltung. Besonders auffällig ist der Becher- oder Kronenkamm, der aus zwei verbundenen Kammseiten entsteht. Schwarzes Gefieder mit grünlichem Glanz ergänzt die klaren Konturen.',
 'Der markante Kamm ist kein Hinweis auf ein bestimmtes Wesen. Beim Kennenlernen einer Zuchtgruppe sind die Reaktion auf ruhige Annäherung und das Verhalten untereinander wichtiger.',
 'Kamm und Kopfpunkte sollten regelmäßig auf unverletzte Haut kontrolliert werden. Ein trockener Stall und sichere, nicht zu enge Durchgänge sind sinnvoll. Auslauf mit Beschäftigung unterstützt Bewegung statt bloßer Präsentation des besonderen Kopfes.',
 'Die Zucht erhält eine regionale deutsche Besonderheit. Der Sonderverein betont die gefestigte Kammausprägung der Zwerge; für den Liebhaber bleibt die Verbindung von gesundem Körper und typischem Kamm entscheidend.',
 'Schwarz.',
 [('Sonderverein: Geschichte','https://sv-augsburger-huehner.jimdofree.com/geschichte/'),('SV-Flyer mit Zwergstandard','https://s5c0f985d43332428.jimcontent.com/download/version/1676226508/module/16628519824/name/Flyer_SondervereinderZ%C3%BCchterdes%20AugsburgerHuhnesundderZwerg-Augsburger.pdf')])

add('Zwerg-Brabanter','Niederlande',None,
 'Niederländische Haubenzwerge mit Helmhaube, Hörnerkamm und Bart.',
 'Die Zwerg-Brabanter knüpfen an den alten niederländischen Brabantertyp an. Ihre eigene Entstehung ist jünger als die Geschichte der großen Haubenhühner; ein belastbares Einzeljahr wird hier nicht behauptet. Seit 1994 betreut der Brabanter-Sonderverein auch die Zwergform.',
 'Eine nach oben gerichtete Helmhaube, ein kleiner V-förmiger Hörnerkamm und ein gegliederter Bart bilden den charakteristischen Kopfputz. Der Körper bleibt eine gestreckte Landhuhnform. Die Haube ist nicht mit der großen Rundhaube der Zwerg-Paduaner zu verwechseln.',
 'Der Sonderverein beschreibt Brabanter als lebhaft und durch regelmäßigen Umgang durchaus zutraulich. Das kleinere Format ersetzt nicht die individuelle Eingewöhnung.',
 'Der Kopfputz muss die Augen frei lassen. Futterstellen und Tränken sollten Bart und Haube möglichst sauber halten. Strukturierter Auslauf bietet den beweglichen Tieren Beschäftigung; für den Zaun ist die tatsächlich beobachtete Flugfähigkeit maßgeblich.',
 'Züchterisch wichtig ist das Zusammenspiel mehrerer Kopfmerkmale. Eine allein nach besonders großer Haube getroffene Auswahl würde den eigenständigen Brabantertyp verfehlen.',
 'Beispiele sind weiß, schwarz, gold und chamois.',
 [('Sonderverein: Brabanter und Zwerg-Brabanter','https://www.sv-brabanter.de/')])

add('Zwerg-Breda','Niederlande','Um 1935; erneute deutsche Anerkennung 2002 laut SV',
 'Kammlose niederländische Zwerge mit Schopf und Fußbefiederung.',
 'Die Zwergform wurde in den Niederlanden um 1935 entwickelt. Der zuständige Sonderverein beschreibt eine erneute Anerkennung in Deutschland nach der Vorstellung in Erfurt 2002. Diese jüngere deutsche Etappe ist von der wesentlich älteren Entstehung der niederländischen Großrasse zu trennen.',
 'Ein normaler Kamm fehlt; an seiner Stelle liegt eine vertiefte Kopfpartie. Ein kleiner, nach hinten gerichteter Schopf, aufgeworfene Nasenlöcher und die Befiederung an Läufen und Schenkeln machen die Rasse unverwechselbar. Der Rumpf ist länglich mit breiter Brust.',
 'Das ungewöhnliche Gesicht ist kein Ausdruck eines bestimmten Charakters. Bei der Auswahl von Tieren sollte man ihre Orientierung, den sicheren Gang und den Umgang mit Artgenossen beobachten.',
 'Wegen der Fußfedern braucht der Boden trockene, gepflegte Bereiche. Feuchte, verklebte Schenkel- und Laufbefiederung sollte vermieden werden. Schopf und Nasenbereich verdienen bei der regelmäßigen Sichtkontrolle besondere Beachtung.',
 'Erhalten wird ein selten dargestellter niederländischer Typ mit mehreren eigenständigen Merkmalen. Die Vereinsseite enthält unterschiedliche Gewichtsangaben; die Tabelle dieses Porträts kennzeichnet deshalb ausdrücklich die verwendete ältere BDRG-Quelle.',
 'Schwarz, weiß, blau-gesäumt und gesperbert.',
 [('Sonderverein: Zwerg-Breda und Anerkennung','https://www.seltene-zwerghuehner.eu/unsere-rassen/zwerg-breda/')])

add('Zwerg-Crèvecoeur','Deutschland',None,
 'Dunkle Haubenzwerge mit Hörnerkamm und dichtem Bart.',
 'Die Zwergform wurde in Deutschland nach dem Vorbild der französischen Crèvecoeur entwickelt. Ihre Geschichte ist nicht mit dem hohen Alter der normannischen Großrasse gleichzusetzen. In der organisierten Zucht wird sie vom Sonderverein der Seidenhühner und Zwerg-Haubenhühner betreut.',
 'Haube, Bart und kleiner Hörnerkamm prägen den Kopf. Der volle, breite Körper wirkt kräftiger als der vieler leichter Haubenzwerge. Das schwarze Gefieder kann im Licht grünlich glänzen; unbefiederte Läufe vervollständigen den dunklen Gesamteindruck.',
 'Ein dicht befiederter Kopf kann Reaktionen des Tieres schwerer lesbar machen. Verlässliche rasseweite Temperamentsmessungen werden in den benutzten Standardquellen nicht angegeben.',
 'Freie Sicht und saubere Kopffedern sind grundlegende Anforderungen. Tränken sollten den Bart nicht dauerhaft durchnässen. Ein überdachter trockener Bereich hilft, die Haube auch bei nasser Witterung zu pflegen; der Auslauf muss dennoch Bewegung und Futtersuche ermöglichen.',
 'Die Zwergzucht bewahrt den besonderen französischen Kopfputz in kleinerem Format. Für die Typbeurteilung zählen auch Körperbreite und Haltung; die Haube allein unterscheidet die Rasse noch nicht hinreichend von anderen Haubenzwergen.',
 'Schwarz.',
 [('Sonderverein: Zwerg-Crèvecœur mit Standard','https://www.sv-silkiespolands.de/betreute-rassen/zwerg-cr%C3%A8vec%C5%93ur/')])

add('Zwerg-Croad-Langschan','Nordamerika und England',None,
 'Hoch gestellte, vollbrüstige Zwerge mit befiederten Läufen.',
 'Die kleine Form entwickelte sich im nordamerikanischen und englischen Zuchtumfeld der Croad-Langschan. Das chinesische Erbe der Großrasse ist von der Entstehung der Zwergform zu unterscheiden. Sie wird gesondert von den Deutschen Zwerg-Langschan standardisiert und betreut.',
 'Der volle Rumpf steht auf langen Beinen. Zwischen Hals und Schwanz liegt die charakteristisch geschwungene Rückenlinie; die Brust ist breit und gerundet. Eine Befiederung an den Läufen unterscheidet die Rasse deutlich vom glattläufigen Deutschen Zwerg-Langschan.',
 'Die stattliche Erscheinung sagt nichts Sicheres über Flugfreude oder Zahmheit aus. Beim Kennenlernen sind die tatsächlichen Bewegungs- und Ruhegewohnheiten der Gruppe zu beobachten.',
 'Die Kombination aus hohem Stand und Fußbefiederung verlangt sowohl genügend Höhe als auch trockene Bodenflächen. Sitzplätze sollten einen sicheren Anflug erlauben. Verklebte Lauf- und Zehenfedern können den Gang beeinträchtigen und müssen früh bemerkt werden.',
 'Die Zucht erhält einen eigenen Langschantyp. Eine Gleichsetzung aller Langschan-Zwergformen würde sowohl die abweichende Rückenlinie als auch den unterschiedlichen Federsitz der Beine übergehen.',
 'Schwarz, weiß und blau-gesäumt.',
 [('Sonderverein: betreute Langschanrassen','https://www.sv-langschan.de/index.php?pg=verein')])

add('Zwerg-Dominikaner','Deutschland',None,
 'Gesperberte kleine Landhühner mit Rosenkamm.',
 'Die deutsche Verzwergung orientierte sich an den amerikanischen Dominikanern. Deren lange Geschichte in Nordamerika bezeichnet das Rassevorbild, nicht das Alter der Zwergzucht. Die kleine Form erhält den eigenständigen Dominikanertyp und wird nicht mit gestreiften Zwerg-Plymouth-Rocks zusammengefasst.',
 'Der längliche Körper trägt eine breite Brust, einen gut entwickelten Schwanz und einen flach aufliegenden Rosenkamm. Die Läufe sind unbefiedert. Die graue Sperberzeichnung gliedert das Gefieder, ohne die gesamte Körperform verdecken zu sollen.',
 'Die Rassetafel legt keine feste Charakterkategorie fest. Bei einer kleinen Zuchtgruppe sind ruhige Gewöhnung und eine passende Rangordnung aussagekräftiger als die Federzeichnung.',
 'Auslauf mit unterschiedlichen Scharrflächen und sichere Sitzplätze ermöglicht normales Landhuhnverhalten. Mehrere erreichbare Futterstellen helfen, Konkurrenz zu begrenzen. Die Einfriedung ist an den tatsächlichen Flugversuchen der Tiere auszurichten.',
 'Die Rasse bewahrt eine amerikanische Zuchttradition im deutschen Zwergformat. Der Rosenkamm ist ein wichtiges Unterscheidungsmerkmal zu äußerlich ähnlich gezeichneten, aber anders standardisierten Rassen.',
 'Gesperbert.')

add('Zwerg-Dresdner','Deutschland','Zuchtbeginn 1951; 1957 in der DDR anerkannt',
 'Kräftige sächsische Nutzzwerge mit Rosenkamm und gerundetem Körper.',
 'Siegmar Zumpe begann in Dresden-Wilschdorf mit der Zwergzucht, während sein Vater Alfred die Großrasse entwickelte. Kleine Dresdner, Antwerpener Bartzwerge und Zwerg-Wyandotten gehörten zum Ausgangsmaterial. Die Anerkennungswege in den beiden deutschen Staaten verliefen zeitversetzt; 1957 ist für die DDR belegt.',
 'Der kräftige Rumpf zeigt eine volle Brust und einen breiten Legebauch. Der Kopf trägt einen Rosenkamm. Anliegende Flügel und ein nicht übermäßig steil getragener Schwanz ergeben eine gerundete, nutzbetonte Landhuhnform.',
 'Der züchtende Verein Uelsen beschreibt temperamentvolle, oft zutrauliche Tiere. Zugleich können Hähne ihr Revier deutlich verteidigen; die Gruppenzusammenstellung verdient daher Aufmerksamkeit.',
 'Ausweichmöglichkeiten und mehrere Futterzugänge helfen, Konkurrenz zu begrenzen. Ein strukturierter Auslauf bietet Beschäftigung. Der Rosenkamm macht einen trockenen, gut gelüfteten Stall nicht überflüssig.',
 'Die Entstehung war ausdrücklich auf Nutzleistung und Vitalität ausgerichtet. Neuere Leistungsprüfungen zeigen, weshalb historische Standardlegezahlen nicht ungeprüft als aktuelle Messwerte einer beliebigen Linie dargestellt werden sollten.',
 'Braun, braun-blaugezeichnet, schwarz, weiß, gesperbert und rost-rebhuhnfarbig.',
 [('BDRG: Dresdner und Zwerg-Dresdner','https://www.bdrg.de/fuer-sie/rasse-des-jahres/dresdner-zwerg-dresdner-rasse-des-jahres-2025-im-bdrg'),('RGZV Uelsen: eigene Zwerg-Dresdner-Zucht','https://rgzv-uelsen.de/index.php/gefluegel-huehner-enten-tauben-wachteln-rassen-zuechter/153-zwerg-dresdner-huhn-huehner')])

add('Zwerg-Eulenbarthühner','Niederlande','Um 1934; 1996 in den deutschen Standard aufgenommen',
 'Niederländische Landhuhnzwerge mit kleinem Schopf und vollem Bart.',
 'Der zuständige Sonderverein beschreibt die Entstehung der Zwergform in den Niederlanden um 1934 und die Aufnahme in den deutschen Standard 1996. Das ist eine andere Entwicklung als die ältere Zuchtgeschichte der großen Eulenbarthühner.',
 'Kleiner Schopf, Hörnerkamm sowie voller Kinn- und Backenbart bestimmen den Kopf. Der leicht gestreckte Körper trägt eine gerundete Brust. Der Schwanz ist gut befiedert und etwas gefächert; der Gesamttyp bleibt ein mittel hoch stehendes Landhuhn.',
 'Die Vereinsbeschreibung schildert vitale Tiere und berichtet auch von Naturbrut. Eine feste Brutquote oder garantierte Zahmheit ist daraus nicht abzuleiten.',
 'Der dichte Bart benötigt saubere Futter- und Wasserstellen. Auch bei Volierenhaltung müssen Bewegung, Scharren und Deckung möglich sein. Die kleine Schopf- und Bartbildung darf den sicheren Blick auf die Umgebung nicht behindern.',
 'Die Zucht bewahrt eine besondere Verbindung von Landhuhnform und Kopfputz. Ältere Farbbezeichnungen wie Silberlack werden hier nicht ungeprüft als aktuelle deutsche Standardnamen übernommen.',
 'Beispiele sind schwarz, weiß, blau-gesäumt und silber-schwarzgetupft.',
 [('Sonderverein: Zwerg-Eulenbarthühner','https://www.seltene-zwerghuehner.eu/unsere-rassen/zwerg-eulenbarth%C3%BChner/')])

add('Zwerg-Friesenhühner','Niederlande',None,
 'Sehr leichte Friesen mit feiner Flockung und klarer Landhuhnfigur.',
 'Die Zwergform entwickelte sich im niederländischen Zuchtumfeld der Friesenhühner. Ihr Vorbild ist der leichte friesische Landhuhntyp. Die verwendete BDRG-Tafel nennt die Provinz Friesland, liefert aber keine ausreichend genaue Chronik der einzelnen Verzwergungsschritte.',
 'Der kleine Rumpf wirkt leicht und gestreckt. Ein Einfachkamm, unbefiederte Beine und ein gut ausgebildeter Schwanz lassen die Figur klar erkennen. Bei gezeichneten Hennen gliedert eine feine Flockung das Gefieder; Hahn und Henne können farblich deutlich verschieden wirken.',
 'Die leichte Gestalt sollte bei der Beurteilung des Bewegungsbedarfs berücksichtigt werden. Für eine feste Flugdistanz oder eine stets zutrauliche Art fehlt in der Rassetafel ein belastbarer Nachweis.',
 'Ein sicher begrenzter, gegliederter Auslauf bietet den kleinen Tieren Deckung und Beschäftigung. Sitzplätze sollten gut erreichbar und vor Räubern geschützt sein. Freies Umherlaufen ersetzt keine sichere Unterbringung zur Nacht.',
 'Die züchterische Bedeutung liegt im Erhalt eines leichten niederländischen Landhuhntyps. Feine Zeichnung und geringe Größe dürfen nicht zulasten einer kräftigen Konstitution oder normaler Fortpflanzung gehen.',
 'Beispiele sind gelb-weißgeflockt und zitron-schwarzgeflockt.')

add('Zwerg-Holländer-Haubenhühner','Niederlande und Deutschland',None,
 'Lebhafte kleine Haubenhühner mit voller Rundhaube und unbefiederten Läufen.',
 'Die Zwergform entstand im niederländisch-deutschen Zuchtumfeld der Holländer Haubenhühner. Sie ist eine eigenständige kleine Rasse; die Bezeichnung Weißhaube benennt dagegen eine Hauben- und Farbausprägung. Ein zusätzliches Weißhauben-Duplikat wird deshalb nicht angelegt.',
 'Die Rundhaube sitzt auf einer deutlichen Schädelerhöhung. Ein regulärer Kamm fehlt, während Kehllappen und helle Ohrscheiben erkennbar sind. Der Körper ist leicht und länglich; die Läufe sind unbefiedert. Anders als Zwerg-Paduaner tragen sie keinen dichten Federbart.',
 'Der veröffentlichte Standard beschreibt lebhaftes Wesen. Die Haube darf die Sicht nicht einschränken, damit das Tier auf Pfleger und Artgenossen normal reagieren kann.',
 'Haubenkontrolle und eine Tränke, die das Kopfgefieder möglichst trocken hält, gehören zum Alltag. Übersichtliche, geschützte Auslaufbereiche unterstützen die Orientierung. Eine besonders große Haube ist nur dann sinnvoll, wenn Augen und Sichtfeld frei bleiben.',
 'Die Rassezucht erhält den Kontrast zwischen Kopfputz und Landhuhnfigur. Glattfiedrige und im Verzeichnis genannte gestruppte Ausführungen werden nicht als zusätzliche Rassen gezählt.',
 'Beispiele sind Weißhauben schwarz, Weißhauben weiß und Weißhauben blau-gesäumt.',
 [('Sonderverein: Zwerg-Holländer Haubenhühner','https://www.sv-silkiespolands.de/betreute-rassen/zwerg-holl%C3%A4nder-haubenh%C3%BChner/')])

add('Zwerg-Houdan','England',None,
 'Bärtige Haubenzwerge mit Schmetterlingskamm und fünf Zehen.',
 'Die kleine Form wurde in England unter Verwendung großer Houdan und anderer Zwergrassen entwickelt. Die BDRG-Tafel nennt Zwerg-Sussex und Zwerg-Ancona als Kreuzungspartner. Das französische Erbe der Houdan ist somit vom Entstehungsland ihrer Zwergform zu unterscheiden.',
 'Haube und dichter Bart werden von einem besonderen, zweigeteilten Schmetterlingskamm ergänzt. Hinzu kommt die Fünfzehigkeit. Der Rumpf ist länglich und kräftig; die Beine bleiben unbefiedert. Geschecktes Gefieder macht die Konturen der Kopfmerkmale nicht immer auf den ersten Blick erkennbar.',
 'Die auffällige Kopfausstattung ist kein Maß für die Zahmheit. Bei der täglichen Betreuung sind uneingeschränkte Sicht und ein sicherer Gang besonders gut zu beobachten.',
 'Bart und Haube sollten an Futter- und Wasserstellen sauber bleiben. Die zusätzlichen Zehen verdienen regelmäßige Kontrolle. Sitzplätze mit sicheren An- und Abflugwegen helfen, Kopf- und Fußgefieder vor unnötigen Beschädigungen zu schützen.',
 'Die Rasse erhält eine ungewöhnliche Kombination mehrerer Standardmerkmale. Ihre Erhaltung verlangt daher mehr als die Auswahl allein nach Haubengröße oder Weißanteil im Gefieder.',
 'Schwarz-weißgescheckt und weiß.',
 [('Sonderverein: Zwerg-Houdan mit Standard','https://www.sv-silkiespolands.de/betreute-rassen/zwerg-houdan/')])

add('Zwerg-Kastilianer','Deutschland',None,
 'Schwarze kleine Legehühner mit großem Kamm und weißen Ohrscheiben.',
 'Die deutsche Zwergform geht auf den Typ der spanischen Kastilianer zurück. Ihre Entstehung ist von der alten Geschichte des spanischen Landhuhns zu trennen. Die verwendete BDRG-Tafel belegt die deutsche Verzwergung, nennt jedoch kein sicher zuzuordnendes einzelnes Gründungsjahr.',
 'Eine schlanke, gestreckte Landhuhnfigur trägt einen großen Einfachkamm und weiße Ohrscheiben. Schwarzes, im Licht glänzendes Gefieder steht neben roten Kopfpunkten und dunklen, unbefiederten Läufen. Die Gestalt bleibt leichter als die kräftiger gebauten Zwerg-Minorka.',
 'Die ähnliche Färbung verschiedener spanischer Rassetypen erlaubt keinen Rückschluss auf identisches Temperament. Beim Auswählen einer Gruppe sind Reaktionen auf Menschen und Bewegung im Auslauf zu beobachten.',
 'Ausreichend Raum zum Ausweichen erleichtert ruhigen Umgang. Die großen Kopfpunkte brauchen vor allem Schutz vor nasser Kälte und kaltem Wind. Für die Einfriedung sollten beobachtete Flugversuche maßgeblich sein, nicht eine erfundene pauschale Zaunhöhe.',
 'Die Zwergzucht erhält einen klar abgegrenzten mediterranen Legehuhntyp. Ein schwarzes Zwerghuhn mit weißen Ohrscheiben ist deshalb nicht automatisch ein Kastilianer; die gesamte Rasseform muss passen.',
 'Schwarz.')

add('Zwerg-Kaulhühner','Europäische Landhuhnzucht',None,
 'Glattläufige Landhuhnzwerge mit schwanzlosem Körperabschluss.',
 'Schwanzlose kleine Landhühner sind seit langer Zeit bekannt. Die BDRG-Tafel beschreibt ihr Auftreten über mehrere Jahrhunderte, ohne einen einzigen Erzüchter oder ein belastbares Entstehungsjahr festzulegen. Die anerkannte Rasse wird von Ruhlaer Zwerg-Kaulhühnern mit Fußbefiederung getrennt geführt.',
 'Kennzeichnend ist der fehlende normale Schwanzabschluss. Der Körper wirkt dadurch kürzer, als es die Rumpflänge allein erwarten ließe. Einfachkamm und unbefiederte Beine passen zum schlichten Landhuhntyp; das Verzeichnis berücksichtigt auch Ausführungen mit Schopf.',
 'Kaulbildung ist ein Körpermerkmal und keine Aussage über Ruhe oder Scheu. Sichere Fortbewegung und ungestörtes Verhalten in der Gruppe sollten bei jedem Tier beobachtet werden.',
 'Saubere, trockene Böden sowie gut erreichbare Ruheplätze unterstützen den Alltag. In der Zucht sind neben dem Körperabschluss auch die zuverlässige Paarung und der Schlupf zu beurteilen. Gesundheit wird nicht durch ein besonders auffällig kurzes Erscheinungsbild ersetzt.',
 'Die Rasse bewahrt einen eigenständigen schwanzlosen Landhuhntyp. Eine einzelne schwanzlose Nachzucht anderer Rassen ist deshalb noch kein typgerechtes Zwerg-Kaulhuhn.',
 'Beispiele sind goldhalsig, silberhalsig, schwarz und weiß.',
 [('Sonderverein: Zwerg-Kaulhühner','https://www.seltene-zwerghuehner.eu/unsere-rassen/zwerg-kaulh%C3%BChner/')])

add('Zwerg-Krüper','Deutschland',None,
 'Kurzbeinige Landhuhnzwerge mit tiefem, länglichem Körper.',
 'Die deutsche Zwergform bewahrt das besondere Erscheinungsbild der Krüper. Das hohe Alter der Großrasse liefert kein ebenso altes Entstehungsdatum für ihre Zwerge. Die Erhaltung wird vom Sonderverein der Krüper- und Zwerg-Krüperzüchter begleitet.',
 'Kurze Läufe lassen den länglichen Körper dicht über dem Boden erscheinen. Kopf und Schwanz bleiben im Landhuhntyp ausgebildet. Die Rasse darf weder mit einer bloß geduckten Haltung noch mit mangelnder Beweglichkeit verwechselt werden.',
 'Aus dem kurzen Bein lässt sich kein ruhiger Charakter ableiten. Ein sicherer, ungestörter Gang und die normale Teilnahme am Gruppenleben sind wichtige Beobachtungen bei der Auswahl.',
 'Niedrige Stufen, flache Nestzugänge und trockene Einstreu passen zum tiefen Stand. Für Paarungsplanung und Aufzucht sollte die Kurzbeinigkeit mit erfahrenen Züchtern besprochen werden; pauschale Kreuzungsempfehlungen werden hier nicht aus dem Erscheinungsbild abgeleitet.',
 'Die Zucht erhält eine besondere Form der deutschen Landhuhntradition. Im ausgewerteten Verzeichnis sind auch langbeinige Varianten berücksichtigt; diese werden nicht als weitere Rasse mitgezählt.',
 'Weiß und silberhalsig.',
 [('Sonderverein: Krüper und Zwerg-Krüper','https://www.krueperhuhn.de/der-sonderverein/')])

add('Zwerg-La Flèche','Deutschland',None,
 'Schlanke Haubenhuhnverwandte mit markantem V-förmigem Hörnerkamm.',
 'Die deutsche Verzwergung orientierte sich an der französischen Rasse La Flèche. Damit bleiben das französische Rassevorbild und die Entstehung der kleinen Form getrennt. Die verwendete BDRG-Tafel nennt Deutschland; ein genauer Beginn der Zwergzucht wird nicht ohne weiteren Nachweis festgelegt.',
 'Zwei deutlich ausgebildete Kammhörner und weiße Ohrscheiben prägen den Kopf. Die Nasenöffnungen wirken hervorgehoben. Der Körper ist länglich und wird auf unbefiederten Läufen getragen; der Hahn zeigt einen gut entwickelten, hoch getragenen Schwanz.',
 'Die markanten Hörner sind ein Kammmerkmal und kein Ausdruck von Aggressivität. Für die Haltung sind die tatsächliche Scheu beziehungsweise Zutraulichkeit und das Verhalten beim Aufbaumen zu beobachten.',
 'Ein sicherer Auslauf mit Deckung erleichtert die Eingewöhnung. Erhabene Kopfpunkte sollten vor Verletzungen an engen Gittern geschützt sein. Ruhige Annäherung und ausreichend Platz zum Ausweichen sind sinnvoller als häufiges Verfolgen der Tiere.',
 'Die Zwergzucht erhält den besonderen französischen Rassetyp. Die beiden Kammhörner allein reichen zur Bestimmung nicht aus, da auch andere Haubenhuhnrassen Hörnerkämme besitzen.',
 'Schwarz, weiß, blau-gesäumt und gesperbert.',
 [('Sonderverein: Zwerg-La Flèche','https://www.seltene-zwerghuehner.eu/unsere-rassen/zwerg-la-fl%C3%A8che/')])

add('Zwerg-Marans','Frankreich; europäische Zwergzucht',None,
 'Kräftige Maranszwerge mit charakteristisch dunklen Eierschalen.',
 'Die Zwergform orientiert sich an den Marans aus der französischen Atlantikregion. Die knappe ältere BDRG-Tafel nennt vor allem den Ursprung des Rassevorbildes um Marans und La Rochelle; daraus wird hier kein ungesichertes Datum der eigentlichen Verzwergung abgeleitet.',
 'Der längliche, kräftige Körper trägt einen Einfachkamm und fest anliegendes Gefieder. Eine gewisse Laufbefiederung gehört zum Maranstyp. Bei schwarz-kupfernen Hähnen hebt sich der warme Behang vom dunklen Körper ab; Hennen sind zurückhaltender gezeichnet.',
 'Dunkle Eier sind kein Hinweis auf ein bestimmtes Wesen. Ein Bestand sollte nach tatsächlicher Verträglichkeit und ruhigem Umgang mit Menschen beurteilt werden.',
 'Trockene Laufbereiche helfen, die Beinbefiederung sauber zu halten. Die Körperkondition muss unter dem dichten Gefieder kontrolliert werden. In der Zucht sollten Eierschalenfarbe, normale Schalengesundheit und gute Fortpflanzung gemeinsam betrachtet werden.',
 'Die Rasse verbindet einen kompakten Nutztyp mit dem besonderen Schalenpigment. Eine gleichmäßig dunkle Farbe ist bei jedem einzelnen Ei ebenso wenig garantiert wie eine bestimmte Jahreslegezahl.',
 'Schwarz-kupfer und weiß.')

add('Zwerg-Nackthalshühner','Deutschland',None,
 'Landhuhnzwerge mit dem namensgebenden weitgehend unbefiederten Hals.',
 'Die deutsche Zwergzucht übernahm das besondere Halsmerkmal der großen Nackthalshühner. Der Hintergrund dieses Merkmals ist älter und räumlich weiter gefasst als die Zucht der standardisierten Zwergform. Ein genaues Entstehungsjahr der kleinen Rasse ist in der verwendeten Tafel nicht angegeben.',
 'Der weitgehend nackte Hals bildet einen starken Gegensatz zum befiederten Rumpf. Der Körper bleibt ein kräftiges Landhuhn mit gut entwickeltem Bauch und ausgebildetem Schwanz. Das deutsche Verzeichnis berücksichtigt Einfach- und Rosenkamm.',
 'Ein unbefiederter Hals ist keine Krankheit und auch keine Charaktereigenschaft. Temperament und Verträglichkeit sollten wie bei anderen Rassen an den konkreten Tieren beurteilt werden.',
 'Die freiliegende Halshaut sollte regelmäßig auf Verletzungen kontrolliert werden. Schatten, trockene Ruhebereiche und ein windgeschützter Stall gehören zur angemessenen Unterbringung. Eine besondere Kälte- oder Hitzeresistenz wird hier nicht pauschal versprochen.',
 'Züchterisch wird die Kombination aus Halsmerkmal und gesundem Landhuhntyp erhalten. Die nackte Partie allein macht ein beliebiges kleines Huhn noch nicht zum standardgerechten Zwerg-Nackthalshuhn.',
 'Beispiele sind schwarz, weiß, rot und gesperbert.')

add('Zwerg-Rhodeländer','Deutschland',None,
 'Dunkelrote kleine Zweinutzungshühner mit gelben Läufen.',
 'Die deutsche Zwergzucht orientierte sich am amerikanischen Rhodeländertyp. Ihre Geschichte ist von der Entwicklung der großen Rhode Island Red zu trennen. In der heutigen Rassezucht werden neben der kräftigen Nutzform die geschlossene Federstruktur und eine tiefe dunkelrote Farbe besonders beachtet.',
 'Der längliche, volle Rumpf wirkt breit und kräftig. Die gelben, unbefiederten Läufe tragen den Körper mittelhoch. Beim Hahn kontrastiert der dunkel glänzende Schwanz mit dem roten Gefieder. Neben dem Einfachkamm ist auch der Rosenkamm anerkannt.',
 'Ein kräftiger Nutztyp ist nicht automatisch ruhig. Bei der Auswahl sollten Verhalten am Futter, Umgang mit Menschen und die Verträglichkeit erwachsener Hähne tatsächlich beobachtet werden.',
 'Stabile Sitzmöglichkeiten und mehrere Futterzugänge passen zur vollen Figur. Scharrmaterial und Bewegungsraum helfen, die Körperkondition zu erhalten. In der Zucht sollten Eigröße, Fortpflanzung und Vitalität nicht hinter einer besonders dunklen Gefiederfarbe zurückstehen.',
 'Die Rasse bewahrt den legebetonten Zweinutzungstyp in Zwerggröße. Die historische Leistungsangabe ist ein Richtwert; sie darf nicht als Ergebnis einer aktuellen Prüfung jeder verfügbaren Zuchtlinie gelesen werden.',
 'Dunkelrot; mit Einfach- oder Rosenkamm.',
 [('Fachbeitrag: Entwicklung der Zwerg-Rhodeländer','https://www.gefluegelzeitung.de/aktuelles/zwerg-rhodelander/')])

add('Zwerg-Sundheimer','Deutschland',None,
 'Helle Nutzgeflügelzwerge mit dunkler Columbiazeichnung und Fußbefiederung.',
 'Die deutsche Zwergzucht führt den Typ der Sundheimer in kleinerer Form weiter. Die badische Geschichte der Großrasse und die spätere Entwicklung der Zwerge dürfen nicht zeitlich gleichgesetzt werden. Beide Größenformen werden vom Erhaltungsverein der Sundheimer betreut.',
 'Der breite, volle Rumpf steht nicht zu hoch und trägt reichliches Körpergefieder. Ein kleiner Einfachkamm und eine leichte Befiederung der Beine gehören zum Bild. Die dunkle Zeichnung konzentriert sich vor allem auf Hals und Schwanz des ansonsten hellen Gefieders.',
 'Der Verein stellt Sundheimer als Nutz- und Erhaltungsrasse vor. Für die konkrete Zwerggruppe ist die Umgänglichkeit individuell zu beurteilen; die helle Farbe sagt darüber nichts aus.',
 'Trockener, möglichst schlammfreier Boden hilft bei der Pflege der Fußfedern. Breite Zugänge und nicht zu hohe Sitzstangen passen zur vollen Körperform. Auch kleinere Nutzgeflügeltypen benötigen Gelegenheit zu Bewegung und Futtersuche.',
 'Erhalten wird ein regional geprägter Nutztyp mit charakteristischer Zeichnung. Züchterisch zählen gesunde Füße und eine harmonische Figur ebenso wie saubere Columbiazeichnung und Eierleistung.',
 'Weiß-schwarzcolumbia.',
 [('Erhaltungsverein: Zwerg-Sundheimer-Standard, Stand 2018','https://www.sv-sundheimer-huhn.de/media/files/2022-31-10_-rassestandard-zwerg-sundheimer.pdf')])

add('Prat','Spanien','1990 unter Katalanier in Deutschland zugelassen',
 'Katalanische Nutz- und Ausstellungshühner mit hell-goldbraunem Gefieder.',
 'Prat wurden aus spanischen Landhühnern entwickelt und sind mit der katalanischen Zuchttradition verbunden. Die BDRG-Tafel nennt die deutsche Zulassung 1990 unter der Bezeichnung Katalanier. Dieser ältere Name wird deshalb als alternative Bezeichnung behandelt und nicht als weitere Rasse angelegt.',
 'Der kräftige, langgestreckte Rumpf trägt einen Einfachkamm und helle Ohrscheiben. Hell-goldbraunes Gefieder und unbefiederte, bläulich wirkende Läufe ergeben eine eigenständige Kombination. Der Hahn besitzt einen gut entwickelten, gegenüber dem Körper dunkleren Schwanz.',
 'Die Nutzform und der mediterrane Hintergrund reichen nicht für eine garantierte Aussage über Zahmheit. Vor der Anschaffung sollten Aktivität und Verhalten der angebotenen Tiere kennengelernt werden.',
 'Auslauf mit Deckung ermöglicht Futtersuche und Rückzug. Die ausgeprägten Kopfpunkte verdienen Schutz vor nasser Kälte. Für kräftige erwachsene Tiere sind stabile Sitzplätze und gut erreichbare Futterstellen wichtig.',
 'Die Rasse steht für eine spanische Landhuhntradition mit Eier- und Fleischnutzung. Sie ist im ausgewerteten BDRG-Verzeichnis eigenständig aufgeführt und wird nicht mit Penedesenca oder Empordanesa zusammengefasst.',
 'Hell-goldbraun.')

add('Zwerg-Niederrheiner','Deutschland','1954 anerkannt laut züchtendem Verein',
 'Kräftige, farbenreiche Nutzgeflügelzwerge mit gerundeter Form.',
 'Die Verzwergung erfolgte in Deutschland nach dem Vorbild der Niederrheiner. Der züchtende Verein Weidhausen nennt 1954 als Anerkennungsjahr und dokumentiert für seine Tiere den birkenfarbigen Farbenschlag. Die Großrasse und ihre kleine Form haben getrennte Standards.',
 'Ein breiter, voller Körper mit gerundeter Brust kennzeichnet den Nutztyp. Die Beine sind unbefiedert; der Kopf trägt einen Einfachkamm. Anliegendes Gefieder lässt die kräftige Gestalt erkennen, ohne dass die Tiere wie bloße Federbälle wirken sollen.',
 'Die Züchterbeschreibung nennt gesellige, gutmütige, zugleich lebhafte Tiere. Das beschreibt eine Orientierung, nicht das garantierte Verhalten jeder Henne oder jedes Hahns.',
 'Mehrere Futterzugänge und Platz zum Ausweichen passen zu einer geselligen Gruppe. Auslauf mit Scharrmaterial bietet Beschäftigung. Die tatsächliche Körperkondition sollte unter dem vollen Federkleid kontrolliert werden.',
 'Die kleine Rasse verbindet Eiernutzen und den Zweinutzungstyp des Vorbildes. Das Zuchtziel darf nicht allein auf besondere Farben verengt werden; Vitalität und Fortpflanzung gehören ebenso dazu.',
 'Beispiele sind blausperber, kennsperber und birkenfarbig.',
 [('Züchtender Verein: Zwerg-Niederrheiner','https://gzv1891weidhausen.de/zwerg-niederrheiner-birkenfarbig/'),('Sonderverein','https://www.sv-niederrheiner.de/')])

add('Zwerg-Orloff','Deutschland','Versuche seit den 1920ern; Anerkennung in den 1950ern',
 'Bärtige, kräftige Zwerge mit markantem Kopf und aufgerichteter Figur.',
 'Rudolf Barth begann in den 1920er-Jahren mit der Verzwergung; in den 1950ern wurde die Arbeit unter anderem durch Otto Squarr weitergeführt. Der Sonderverein beschreibt getrennte Entwicklungen in Ost- und Westdeutschland. Die Zwergform wurde Mitte der 1950er-Jahre durch eine Musterbeschreibung anerkannt.',
 'Der kräftige Rumpf wird aufgerichtet getragen. Ein breiter Kopf mit Augenbrauen, Wulstkamm und dreigeteiltem Bart bestimmt den Ausdruck. Der Hals ist reich befiedert, der Schwanz verhältnismäßig kurz und gut gefüllt.',
 'Die Kämpferanmutung ist zunächst eine Formbeschreibung. Verträglichkeit und Verhalten gegenüber Pflegern müssen an der jeweiligen Gruppe beurteilt werden.',
 'Der Bart braucht saubere Tränken und Futterstellen. Strukturierter Auslauf und getrennte Rückzugsbereiche erleichtern eine ruhige Gruppenhaltung. Übertreibungen bei Körpergewicht oder Kopfmerkmalen sind für die Gesundheit ebenso wenig hilfreich wie für einen harmonischen Rassetyp.',
 'Der neuere veröffentlichte Sondervereinsstandard nennt 1200 g für den Hahn und 1000 g für die Henne. Diese Angaben werden gegenüber dem abweichenden Hahngewicht der älteren Rassetafel bevorzugt.',
 'Beispiele sind rotbunt, mahagonifarbig, weiß und schwarz.',
 [('Sonderverein: Zwerg-Orloff-Rassestandard','https://www.sv-orloff.com/%C3%BCber-orloffs/zwerg-orloff-rassestandard/')])

add('Zwerg-Spanier','England, Niederlande und Deutschland','Deutscher Neuaufbau ab 1983; Anerkennung 1992',
 'Schwarze Legehuhnzwerge mit auffälliger weißer Gesichtsmaske.',
 'Die Zwergform war in mehreren europäischen Ländern bekannt und musste in Deutschland später erneut aufgebaut werden. Heinrich Kolb nutzte große Spanier und Zwerg-Minorka; englisches Zuchtmaterial unterstützte die Arbeit. Der Fachbeitrag nennt 1992 als Anerkennungsjahr dieser neu gefestigten deutschen Zucht.',
 'Die großflächige weiße Gesichtsmaske ist das auffälligste Merkmal. Dazu kommen ein Einfachkamm, schwarzes Gefieder und dunkle, unbefiederte Läufe. Der längliche Landhuhnkörper wird aufrecht und geschlossen getragen, ohne übermäßig steile Schwanzhaltung.',
 'Die helle Maske ist kein Hinweis auf Zahmheit oder Scheu. Gerade beim Einfangen ist ruhiges Vorgehen sinnvoll, damit die empfindlichen Kopfpunkte nicht an Gittern oder Einrichtungen verletzt werden.',
 'Große Gesichts- und Kammflächen benötigen saubere, trockene Umgebung und Schutz vor feuchter Kälte. Ein sicher gegliederter Auslauf erlaubt Bewegung und Deckung. Für ungesicherte Behauptungen zur Flugdistanz bietet der Standard keine Grundlage.',
 'Die Erhaltung betrifft einen besonders markanten mediterranen Typ. Die Maske muss zusammen mit Körperform und gesunder Entwicklung betrachtet werden, nicht als isoliertes Zuchtziel.',
 'Schwarz.',
 [('Fachbeitrag: Zwerg-Spanier und Zuchtgeschichte','https://www.gefluegelzeitung.de/aktuelles/zwerg-spanier/')])

add('Zwerg-Sulmtaler','Deutschland',None,
 'Kleine Steirer mit Federschopf und vollem, gerundetem Rumpf.',
 'Die in Deutschland entwickelte Zwergform nimmt die österreichischen Sulmtaler zum Vorbild. Die Geschichte des großen steirischen Nutzgeflügels darf nicht unverändert als Chronik der Zwergzucht wiedergegeben werden. Ein exaktes Entstehungsjahr wird aus den hier verwendeten Tafeln nicht behauptet.',
 'Der breite, volle Körper trägt eine tiefe Brust und reichliches Gefieder. Ein kleiner Schopf ergänzt den Einfachkamm. Die unbefiederten Beine und der gut ausgebildete Schwanz lassen den Landhuhncharakter trotz der gerundeten Figur erkennen.',
 'Der kleine Schopf und die weiche Körperwirkung erlauben keine sichere Charakterprognose. Für eine passende Gruppe sollte man Tiere mit ungestörter Orientierung und ausgeglichenem Sozialverhalten auswählen.',
 'Trockene Ruheplätze schützen das volle Gefieder. Nester und Sitzmöglichkeiten sollten ohne schwierige Sprünge erreichbar sein. Der Schopf muss die Augen frei lassen; ein normaler Auslauf bietet Scharren, Deckung und Bewegung.',
 'Die Rasse erhält den steirischen Nutztyp in eigenständiger Zwergzucht. Gefiederfarbe und Schopf sind nur ein Teil des Zuchtbildes; eine volle, gesunde Körperform gehört ebenso dazu.',
 'Beispiele sind gold-weizenfarbig, silber-weizenfarbig und weiß.')

add('Zwerg-Sumatra','Europäische Zwergzucht nach Sumatra-Vorbild','1989 in Deutschland anerkannt',
 'Elegante kleine Langschwanzhühner mit dunklen Kopfpunkten.',
 'Die Zwergform orientiert sich an der alten Sumatra-Rasse mit Bezug zu den Sunda-Inseln. Die BDRG-Tafel nennt 1989 als deutsches Anerkennungsjahr der kleinen Rasse. Das sagt nichts darüber aus, dass sämtliche Schritte der Verzwergung auf Sumatra stattgefunden hätten.',
 'Der längliche Körper geht in eine reich entwickelte Schwanzpartie über. Dunkle Kopfpunkte und ein kleiner Kamm prägen den Kopf. Besonders bei schwarzen Tieren kann das Gefieder stark grünlich glänzen; die Beine sind unbefiedert.',
 'Eine elegante Langschwanzfigur ist kein Beleg für einen ruhigen Charakter. Bei der Auswahl sind Aufmerksamkeit, tatsächliche Flugversuche und Verträglichkeit der Tiere zu beobachten.',
 'Lange Schwanzfedern benötigen ausreichend freie Wege und trockene Ruheplätze. Eine geschützte, sicher begrenzte Voliere kann die Gefiederpflege erleichtern. Bewegung und Futtersuche bleiben auch bei einer aufwendigen Schwanzentwicklung notwendig.',
 'Die Zucht erhält eine besondere asiatisch geprägte Silhouette in Zwerggröße. Glanz und Schwanzlänge dürfen nicht alleinige Auswahlkriterien sein; ein kräftiger Körper und gesunde Aufzucht gehören dazu.',
 'Schwarz, schwarz-rot und wildfarbig.')

add('Zwerg-Yokohama','Deutschland',None,
 'Langschwanzzwerge mit fließender Körperlinie und reichem Schmuckgefieder.',
 'Die deutsche Zwergzucht orientiert sich an den Yokohama. Die japanisch geprägte Geschichte des Rassevorbildes ist von der Entstehung der standardisierten kleinen Form zu trennen. Die verwendete BDRG-Tafel nennt Deutschland, aber kein hinreichend belegtes einzelnes Entstehungsjahr.',
 'Der langgestreckte Rumpf geht ohne harten Absatz in den reich befiederten Schwanz über. Lange Sattel- und Schwanzfedern bestimmen besonders beim Hahn den Eindruck. Der Kopf trägt einen kleinen Kamm, die Beine bleiben unbefiedert.',
 'Das lange Schmuckgefieder ist keine Temperamentsbeschreibung. Im Alltag sollten Bewegungsfreude und tatsächliches Aufbaumverhalten der jeweiligen Tiere beobachtet werden.',
 'Breite, nicht zu enge Durchgänge und trockene Sitzbereiche schützen lange Federn vor Abrieb und Verschmutzung. Die Unterbringung darf das Tier nicht zugunsten schöner Federn an normaler Bewegung hindern. Geschützte Auslaufbereiche erleichtern die Pflege.',
 'Die Rasse bewahrt eine besondere Langschwanzform. Sie wird getrennt von Zwerg-Phönix geführt; ein langer Schwanz allein macht diese beiden Rassetypen nicht identisch.',
 'Weiß-rotgezeichnet und weiß.')

add('Zwerg-Mechelner','Belgien und Deutschland',None,
 'Kräftige kleine Fleischhuhntypen mit befiederten Läufen.',
 'Die belgisch-deutsche Zwergzucht übernahm den Typ der Mechelner. Die lange belgische Geschichte der Großrasse bezeichnet das Rassevorbild, nicht ein ebenso altes Gründungsdatum der kleinen Form. Im deutschen Verzeichnis werden die Zwerge gesondert und mit eigenen Farbenschlägen geführt.',
 'Ein breiter, tiefer Körper, volle Brust und gut entwickelter Bauch lassen den Fleischhuhneinschlag erkennen. Die Beine tragen Federn; der Kopf besitzt einen Einfachkamm. Die gesperberte Zeichnung gliedert das Gefieder, ohne die kräftige Körperform ersetzen zu können.',
 'Der Sonderverein beschreibt die Rassefamilie als ruhig und zutraulich. Für die konkrete Zwerggruppe bleiben Erfahrungen mit Menschen und die individuelle Zusammensetzung entscheidend.',
 'Trockene Laufbereiche helfen bei der Pflege der Beinbefiederung. Nester und Sitzstangen sollten für die kräftigen Tiere gut erreichbar sein. Auch ein Fleischhuhntyp braucht Bewegungsanreize und ausreichend Platz zum Scharren.',
 'Die Zwergform erhält den Mechelner Nutztyp mit handlicherem Körperformat. Der Sonderverein grenzt die deutschen Farbenschläge ausdrücklich von weiteren, nur im Ausland anerkannten Varianten ab.',
 'Gesperbert und perlgrau-gesperbert.',
 [('Sonderverein: Mechelner und Zwerg-Mechelner','https://www.sv-mechelner-huhn.de/')])
