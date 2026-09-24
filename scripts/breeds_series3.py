"""Gezielte Erweiterung vom 24.09.2026; ohne neue A4-Bögen."""
SERIES3 = []

def add(slug, name, origin, short, weights, egg, paragraphs, sources):
    keys = ['history', 'appearance', 'colors', 'nature', 'husbandry', 'use', 'fact']
    texts = paragraphs.strip().split('\n')
    assert len(texts) == len(keys), slug
    SERIES3.append(dict(slug=slug, name=name, origin=origin, short=short,
        group='Großhuhn', weights=weights, egg=egg, sources=sources,
        researched='24. September 2026', **dict(zip(keys, texts))))

add('jersey-giants', 'Jersey Giants', 'USA',
    'Amerikanische Riesenhühner mit breitem Körper und gelassenem Wesen.',
    ('etwa 5,9–6,8 kg nach US-Rasseporträt', 'etwa 4,5–5 kg nach US-Rasseporträt'),
    'Große, cremefarbene bis braune Eier.', '''
Die Brüder John und Thomas Black entwickelten die Rasse im späten 19. Jahrhundert in New Jersey. Ihr Ziel war ein besonders großes Fleischhuhn, das auf dem Markt mit Puten konkurrieren konnte.
Der breite, tiefe Körper trägt einen Einfachkamm. Die Beine sind unbefiedert. Bei schwarzen Tieren fallen die dunklen Läufe mit gelben Fußsohlen auf.
Schwarz, weiß und blau gehören zu den in den USA anerkannten Varianten. Schwarze Federn können im Licht grünlich glänzen.
Jersey Giants gelten als ruhig und freundlich. Ihre Größe ist kein Zeichen besonderer Angriffslust; das einzelne Tier bleibt vom Umgang geprägt.
Große Nester, breite Durchgänge und niedrige, stabile Sitzplätze sind sinnvoll. Das hohe Gewicht muss bei der Stalleinrichtung berücksichtigt werden.
Die Rasse liefert Fleisch und Eier. Bis zur vollen Körperentwicklung braucht sie Zeit; sie ist kein Ersatz für schnell wachsende Masthybriden.
Die hier angegebenen Gewichte stammen aus einem amerikanischen Porträt. Zuchtstandards und einzelne Linien können davon abweichen.
''', [('The Livestock Conservancy: Jersey Giant', 'https://livestockconservancy.org/jersey-giant-chicken/')])

add('plymouth-rocks', 'Plymouth Rocks', 'USA',
    'Kräftige Zweinutzungshühner, besonders bekannt für ihre feine Streifung.',
    ('3–3,5 kg', '2,5–3 kg'), 'Braunschalige Eier.', '''
Plymouth Rocks entstanden im 19. Jahrhundert in den USA. Die nach Plymouth benannte Rasse verbreitete sich als Eier- und Fleischhuhn. In Deutschland betreut sie seit 1901 ein Sonderverein.
Ein breiter, tiefer Körper und eine gerundete Brust prägen den Nutztyp. Gelbe, unbefiederte Beine und ein Einfachkamm ergänzen die Gestalt.
Bekannt ist der gestreifte Farbenschlag. Daneben gibt es etwa weiße, schwarze, gelbe und rebhuhnfarbig-gebänderte Tiere.
Der Sonderverein beschreibt ein ruhiges Wesen und geringes Flugvermögen. Bei regelmäßigem, behutsamem Umgang können die Tiere vertraut werden.
Ein trockener Stall und ein abwechslungsreicher Auslauf bieten gute Grundlagen. Auch wenig flugfreudige Hühner brauchen sichere Begrenzungen und Bewegungsraum.
Eierleistung und Fleischqualität gehören gemeinsam zum Zuchtziel. Körperform und feine Zeichnung machen die Rasse außerdem für Ausstellungen interessant.
Plymouth Rocks und Amrocks sind historisch verwandt, werden im Lexikon aber als eigenständige Rassen vorgestellt.
''', [('Sonderverein Plymouth-Rocks-Züchter', 'https://plymouth-rocks.de/'),
       ('Wikipedia: Plymouth Rock – Gewichtsangaben', 'https://de.wikipedia.org/wiki/Plymouth_Rock_%28Huhn%29')])

add('dominikaner', 'Dominikaner', 'USA',
    'Alte amerikanische Landhühner mit Rosenkamm und Sperberzeichnung.',
    ('2–2,5 kg laut deutschem Sonderverein', '1,75–2,25 kg laut deutschem Sonderverein'),
    'Bräunliche Eier; Bruteier mindestens 58 g laut Sonderverein.', '''
Dominikaner zählen zu den ältesten amerikanischen Hühnerrassen. Ihre genaue Entstehung ist nicht vollständig geklärt. Im 19. Jahrhundert gelangten sie nach Europa und beeinflussten weitere Rassezüchtungen.
Der kräftige, walzenförmige Körper trägt einen niedrigen Rosenkamm. Die gelben Beine sind unbefiedert. Das Gefieder liegt fest an.
Typisch ist die Sperberung mit dunklen und blaugrauen Querzonen. Die Zeichnung ist weniger scharf abgegrenzt als eine klare Streifung.
Der Sonderverein beschreibt temperamentvolle, robuste Tiere. Im Auslauf suchen sie eifrig nach Futter und bleiben aufmerksam in Bewegung.
Ein großer, gegliederter Auslauf kommt ihrem Verhalten entgegen. Deckung, Scharrflächen und ruhiger Umgang erleichtern die Haltung.
Dominikaner verbinden Eier- und Fleischnutzung. Gewichtsangaben unterscheiden sich international; hier stehen die Werte des deutschen Sondervereins.
Der Rosenkamm hilft, sie von ähnlich gezeichneten Plymouth Rocks mit Einfachkamm zu unterscheiden.
''', [('Dominikaner-Sonderverein: Rasse und Standard', 'https://dominikaner-sv.de/dominikaner-sv-de/dominikaner/')])

add('minorka', 'Minorka', 'Spanien / England',
    'Elegante Legehühner mit großen weißen Ohrscheiben.',
    ('2,5–3,5 kg', '2,25–3 kg'), 'Große weiße Eier; häufig etwa 60–65 g.', '''
Die Vorfahren der Minorka kamen von der Baleareninsel Menorca nach England. Dort wurde der Rassetyp weiter gefestigt. In den 1870er Jahren fanden die leistungsfähigen Legehühner auch in Deutschland Verbreitung.
Der kräftige, längliche Körper wirkt stolz aufgerichtet. Besonders auffällig sind die großen, weißen Ohrscheiben. Meist tragen die Tiere einen großen Einfachkamm, daneben gibt es rosenkämmige Varianten.
Schwarze und weiße Minorka sind bekannt. Der Gegensatz zwischen weißer Ohrscheibe und rotem Gesicht ist bei schwarzen Tieren besonders deutlich.
Minorka wirken aufmerksam und lebhaft. Geduldiger, regelmäßiger Kontakt erleichtert die Gewöhnung an Menschen.
Auslauf und Bewegungsraum passen zum Landhuhntyp. Der Stall sollte trocken und geschützt sein; große Kopfpunkte verdienen bei Kälte besondere Aufmerksamkeit.
Die Rasse ist vor allem für große weiße Eier bekannt. Brutlust ist wenig ausgeprägt; die Legeleistung hängt von Linie, Alter und Versorgung ab.
Ohrscheiben sind Hautflächen seitlich am Kopf. Sie sind weder Ohrmuscheln noch weiße Federn.
''', [('BLE: Einheimische Nutztierrassen 2025 (PDF)', 'https://tgrdeu.genres.de/fileadmin/SITE_MASTER/content/Rote_Liste/buch_roteliste_2025_web.pdf')])

add('andalusier', 'Andalusier', 'Spanien / europäische Zucht',
    'Blaue Landhühner, deren Federn dunkel eingefasst sind.',
    ('2,5–3 kg', '2–2,5 kg nach BDRG-Rassetafel'), 'Weiße Eier.', '''
Spanische Landhühner bildeten die Grundlage. Tiere gelangten Mitte des 19. Jahrhunderts nach England; englische und deutsche Züchter formten den heutigen Typ weiter. Der Name erzählt deshalb nur einen Teil der Rassegeschichte.
Andalusier wirken gestreckt und elegant. Ein großer Einfachkamm, weiße Ohrscheiben und dunkle, unbefiederte Beine ergänzen den Landhuhntyp.
Das blaue Federfeld wird von einer dunklen Säumung umrandet. Diese Zeichnung macht die einzelnen Federn gut erkennbar.
Die Tiere sind lebhaft und aufmerksam. Für Beobachter sind besonders ihre Beweglichkeit und die wechselnde Lichtwirkung des Gefieders interessant.
Ein sicherer Auslauf mit Deckung und Beschäftigung passt zu aktiven Hühnern. Trockene, geschützte Ruheplätze bleiben wichtig.
Andalusier wurden als Legehühner genutzt. Heute steht daneben die Erhaltung des besonderen Farb- und Formtyps im Mittelpunkt.
Die blaue Farbe vererbt sich nicht reinerbig. Aus blauen Elterntieren können auch schwarze und sehr helle Nachkommen entstehen.
''', [('Geflügelzeitung: Andalusier', 'https://www.gefluegelzeitung.de/aktuelles/andalusier-einzigartige-zeichnung-mit-langer-geschichte/'),
       ('BDRG: Rassetafeln Hühner (PDF)', 'https://www.bdrg.de/media/docs/Rassetafeln_Huehner.pdf')])

add('kastilianer', 'Kastilianer', 'Spanien',
    'Schwarze spanische Landhühner mit lebhaftem Temperament.',
    ('2–2,5 kg', '1,75–2 kg'), 'Weiße Eier.', '''
Kastilianer gehören zum alten spanischen Landhuhntyp. Sie stehen in enger Beziehung zu weiteren Mittelmeerrassen. In Deutschland wurden sie erst in der Mitte des 20. Jahrhunderts eingeführt.
Der mittelgroße Körper wirkt schlank und aufgerichtet. Ein Einfachkamm, weiße Ohrscheiben und dunkelschieferfarbene Beine prägen das Bild.
Gezüchtet wird schwarzes Gefieder mit grünlichem Glanz. Der Glanz wird besonders sichtbar, wenn Licht schräg auf die Federn fällt.
Kastilianer gelten als lebhaft und neugierig. Trotz ihres Temperaments können sie bei passender Haltung und ruhigem Umgang zutraulich werden.
Bewegungsraum, Deckung und sichere Begrenzungen entsprechen dem aktiven Typ. Eine regelmäßige Versorgung erleichtert die Beobachtung der Gruppe.
Die Rasse wurde vor allem wegen ihrer Eier geschätzt. Frühe Entwicklung und robuste Landhuhneigenschaften gehören zum Nutzgedanken.
Bei der Henne kann sich der hintere Kammteil seitlich neigen. Das Auge soll dabei frei bleiben.
''', [('Rassegeflügelzucht: Kastilianer', 'https://www.rassegefluegelzucht.de/kastilianer')])

add('brakel', 'Brakel', 'Belgien',
    'Belgische Landhühner mit auffälliger Querzeichnung.',
    ('etwa 2–2,75 kg', '1,75–2,25 kg'), 'Weiße Eier.', '''
Brakel, auch Braekel geschrieben, sind eine alte belgische Landhuhnrasse. Sie gehören zum Formenkreis der Sprenkelhühner und wurden lange als leistungsfähige Eierlieferanten gehalten.
Ein länglicher Körper, aufrechter Einfachkamm und unbefiederte Beine prägen die Gestalt. Die Tiere wirken leichtfüßig und aufmerksam.
Bekannt sind silberne und goldene Varianten. Dunkle Querzeichnungen stehen im Kontrast zur hellen oder goldenen Grundfarbe; der Hals wirkt vergleichsweise einfarbig.
Brakel gelten als lebhaft und bewegungsfreudig. Sie nutzen ihren Auslauf aktiv und eignen sich besonders zum Beobachten natürlichen Suchverhaltens.
Ein geräumiger, gut gesicherter Auslauf mit Deckung ist sinnvoll. Die Beweglichkeit sollte bei der Einfriedung berücksichtigt werden.
Traditionell stand die Eierleistung im Vordergrund. Heute trägt die Liebhaberzucht dazu bei, den Landhuhntyp und seine Zeichnung zu erhalten.
Der Name verweist auf Belgien. Die ähnlich geschriebene deutsche Stadt Brakel ist nicht der Ursprung dieser Rasse.
''', [('Oberlausitzer Geflügelzüchterverband: Brakel', 'https://www.rassegefluegel-oberlausitz.de/seite/871049/brakel-huhn.html'),
       ('Wikipedia: Brakel', 'https://de.wikipedia.org/wiki/Brakel_%28Huhn%29')])

add('ostfriesische-moewen', 'Ostfriesische Möwen', 'Deutschland',
    'Bewegliche friesische Landhühner mit Flockenzeichnung.',
    ('2,25–3 kg', '1,75–2,5 kg'), 'Weiße Eier, häufig etwa 50–60 g.', '''
Die Rasse entwickelte sich aus friesischen Landhühnern. Zu Beginn des 20. Jahrhunderts festigten Züchter die typische Flockenzeichnung und einen etwas kräftigeren Körperbau.
Ostfriesische Möwen stehen mittelhoch und wirken robust, aber beweglich. Der Landhuhntyp soll nicht plump erscheinen.
Goldene und silberne Varianten zeigen dunkle Flocken im Gefieder. Die Zeichnung ist ein wesentliches Merkmal der Rasse.
Die GEH beschreibt ausgesprochen agile Tiere und gute Futtersucher. Sie können sich weit vom Stall entfernen und fliegen gern.
Viel Platz und sichere Auslaufgrenzen passen zu ihrem Verhalten. Deckung und abwechslungsreiche Flächen regen die Suche an; vollständiges Futter bleibt trotzdem notwendig.
Die Rasse verbindet Eier- und Fleischnutzung mit Wetterhärte. Brutlust ist meist wenig ausgeprägt, kann aber bei einzelnen Hennen vorkommen.
Trotz ihres Namens sind Ostfriesische Möwen Haushühner. Am Verhalten im Auslauf erkennt man sie als emsige Landbewohner.
''', [('GEH: Ostfriesische Möwen', 'https://g-e-h.de/index.php/rassebeschreibungen/55-gefluegelhuhn/154-ostfriesische-moewe')])

add('bergische-kraeher', 'Bergische Kräher', 'Deutschland',
    'Traditionsreiche Hühner, berühmt für den langen Ruf ihrer Hähne.',
    ('3–3,5 kg', '2–2,5 kg'), 'Weiße Eier.', '''
Bergische Kräher werden seit langer Zeit im Bergischen Land gehalten. Geschichten über ihre Einführung während der Kreuzzüge sind Überlieferungen, keine lückenlos belegte Abstammungsgeschichte.
Der Körper ist kräftig, langgestreckt und aufgerichtet. Die Tiere sollen dabei schlank und nicht gedrungen wirken.
Kennzeichnend ist schwarz-goldbraungedobbelt. Dabei liegen farbige Zeichnungsfelder innerhalb dunkler Federpartien.
Die Hähne fallen vor allem akustisch auf. Während des langen Krährufs schreiten sie nach vorn und senken gegen Ende den Kopf.
Auslauf und Beschäftigung passen zum beweglichen Körper. Vor der Haltung sollte der besondere Hahnengesang bei der Standortwahl berücksichtigt werden.
Neben Eiern und Fleisch spielt die Erhaltung des Krährufs eine besondere Rolle. Krähwettbewerbe trugen dazu bei, diese Eigenschaft züchterisch zu festigen.
Hier ist eine Rasseeigenschaft hörbar: Der langgezogene Ruf unterscheidet sich deutlich vom kurzen Krähen vieler anderer Hühner.
''', [('GEH: Bergische Kräher', 'https://g-e-h.de/index.php/rassebeschreibungen/55-gefluegelhuhn/145-bergischer-kraeher')])

add('bergische-schlotterkaemme', 'Bergische Schlotterkämme', 'Deutschland',
    'Bergische Landhühner mit einem beweglichen Hennenkamm.',
    ('2–2,75 kg', '1,75–2,25 kg'), 'Weiße Eier, als Orientierung etwa 55 g.', '''
Die Rasse gehört zu den alten Hühnern des Bergischen Landes. Vermutlich wirkten Bergische Kräher und spanische Hühner an ihrer Entstehung mit. Eine genaue Kreuzungsfolge ist nicht gesichert.
Der langgestreckte, kastenförmige Körper zeigt den Nutzhuhntyp. Namengebend ist der Einfachkamm der Henne, der locker zur Seite umgelegt wird.
Neben schwarzen Tieren gibt es unter anderem schwarz-weißgedobbelte und schwarz-gelbgedobbelte Varianten. Die Dobbelung bezeichnet besondere Zeichnungsfelder der Federn.
Die Tiere werden als wetterhart und frohwüchsig beschrieben. Sie nutzen einen großen Auslauf gern und zeigen typisches Such- und Scharrverhalten.
Strukturierter Auslauf, trockene Einstreu und geschützte Ruheplätze sind eine geeignete Grundlage. Beim Beobachten lohnt ein Blick auf die Kopfpunkte.
Die Rasse wurde als Nutzhuhn mit weißschaligen Eiern gehalten. Heute kommt der Erhaltung ihrer regionalen Geschichte besondere Bedeutung zu.
„Schlottern“ meint die lockere Lage des Hennenkamms. Es beschreibt weder Zittern noch eine Krankheit des Tieres.
''', [('GEH: Bergische Schlotterkämme', 'https://g-e-h.de/index.php/rassebeschreibungen/55-gefluegelhuhn/147-bergischer-schlotterkamm')])

add('deutsche-langschan', 'Deutsche Langschan', 'Deutschland',
    'Hoch stehende Hühner mit langer, zum Schwanz ansteigender Linie.',
    ('3–4,5 kg', '2,5–3,5 kg'), 'Strohgelbe bis braungelbe Eier.', '''
Deutsche Langschan entstanden im späten 19. Jahrhundert aus eingeführten Croad-Langschan unter Beteiligung weiterer Rassen. Die deutsche Zucht entwickelte einen eigenen, hoch gestellten Typ.
Lange Beine und ein gestreckter Körper bestimmen die Silhouette. Die Rückenlinie steigt zum Schwanz an. Auf dem verhältnismäßig kleinen Kopf sitzt ein kleiner Einfachkamm.
Schwarz, weiß, blau-gesäumt und braunbrüstig gehören zu den beschriebenen Farbenschlägen. Die hohe Stellung bleibt ihr gemeinsames Erkennungsmerkmal.
Die kräftigen Tiere werden als Zweinutzungshühner gehalten. Ihr aufrechtes Erscheinungsbild allein sagt nichts über Angriffslust aus; der Umgang mit der Gruppe bleibt entscheidend.
Stallöffnungen und Sitzplätze müssen zum großen Körper passen. Bei der Aufzucht ist gleichmäßige Entwicklung wichtiger als möglichst schnelle Gewichtszunahme.
Eier- und Fleischnutzung gehören zusammen. Heute ist außerdem die Erhaltung des eigenständigen deutschen Typs ein wichtiges Zuchtziel.
Deutsche Langschan und Croad-Langschan sind verwandt, aber eigenständige Rassen mit unterschiedlichen Körperlinien.
''', [('GEH: Deutsches Langschan', 'https://g-e-h.de/geh-raku/geflueg/gefllangschan2.htm'),
       ('Wikipedia: Deutsches Langschan', 'https://de.wikipedia.org/wiki/Deutsches_Langschan')])

add('croad-langschan', 'Croad-Langschan', 'China / England',
    'Große Hühner mit tiefem Körper, aufrechter Haltung und Fußfedern.',
    ('3,75–4,25 kg', '3–3,5 kg'), 'Dunkelbraune Eier.', '''
Croad-Langschan kamen im 19. Jahrhundert aus China nach England und anschließend nach Deutschland. Aus ihrem Formenkreis gingen mehrere weitere Langschan-Typen hervor.
Der breite, tiefe Körper und die aufrechte Haltung erzeugen einen stattlichen Eindruck. Leicht befiederte Beine und ein Einfachkamm ergänzen die Gestalt.
Schwarze und weiße Tiere sind klassische Varianten. Schwarzes Gefieder kann bei passendem Licht grünlich glänzen.
Die Rasse gilt als ruhig und zutraulich. Hennen können ausgeprägte Brutlust zeigen und als Glucken eingesetzt werden.
Große, gut zugängliche Nester und stabile Sitzplätze sind sinnvoll. Trockene Einstreu hilft, die befiederten Beine sauber zu halten.
Croad-Langschan verbinden Fleischansatz mit dunkelbraunen Eiern. Ihre Vorfahren beeinflussten zahlreiche spätere Zweinutzungsrassen.
Die Größe entsteht nicht allein durch lange Beine. Gerade Rumpftiefe und aufrechte Haltung tragen zum Gesamteindruck bei.
''', [('BLE: Stark gefährdete Hühnerrassen', 'https://www.nutztierhaltung.de/gefluegel/legehennen/oekonomie/einheimische-und-gefaehrdete-huehnerrassen/stark-gefaehrdete-huehnerrassen/'),
       ('Sonderverein der Langschanzüchter', 'https://www.sv-langschan.de/index.php?pg=verein')])

add('cochin', 'Cochin', 'China',
    'Schwere Hühner mit üppigem Federkleid bis zu den Füßen.',
    ('3,5–5,5 kg', '3–4,5 kg'), 'Bruteier mindestens 53 g; braungelbe Schale.', '''
Cochin gelangten im 19. Jahrhundert aus China nach Europa. Ihre Größe und das üppige Gefieder machten sie zu auffälligen Vertretern der damals eingeführten asiatischen Hühner.
Breite, Tiefe und weiche Federn erzeugen eine mächtige, gerundete Gestalt. Beine und Zehen sind befiedert; der Kopf trägt einen Einfachkamm.
Es gibt zahlreiche Farbenschläge, beispielsweise gelb, schwarz, weiß und rebhuhnfarbig-gebändert. Der federreiche Körper verbindet die Varianten.
Cochin gelten als ruhige Hühner. Ihr langsamer wirkendes Auftreten macht eine stressarme Betreuung und genügend Bewegungsangebote nicht weniger wichtig.
Niedrige Sitzplätze, breite Zugänge und trockener Boden passen zu Gewicht und Fußfedern. Nasse, verschmutzte Auslaufbereiche sollten vermieden werden.
Die Rasse hatte Bedeutung als schweres Fleischhuhn und als Ausgangsrasse weiterer Züchtungen. Heute stehen häufig Liebhaber- und Ausstellungszucht im Vordergrund.
Die bereits vorhandenen Zwerg-Cochin sind eine eigenständige Urzwergrasse. Diese Seite behandelt die großen Cochin.
''', [('Sonderverein: Cochin', 'https://sv-cochin-brahma-zwerg-brahma.de/Rassenbeschreibung/Cochin')])

add('houdan', 'Houdan', 'Frankreich',
    'Französische Hühner mit Haube, Bart und fünf Zehen.',
    ('etwa 3,2 kg nach US-Rasseporträt', 'etwa 2,5 kg nach US-Rasseporträt'), 'Weiße Eier.', '''
Houdan tragen den Namen einer französischen Stadt westlich von Paris. Dort waren sie als Fleischhühner bekannt. Später fanden sie auch wegen ihres ungewöhnlichen Aussehens internationale Verbreitung.
Eine Federhaube, Bart und fünf Zehen fallen sofort auf. Unter dem Kopfschmuck liegt ein besonderer, geteilter Kamm. Der Körper bleibt trotz der auffälligen Kopfpartie kräftig.
Besonders bekannt sind schwarz-weißgescheckte Tiere. Es gibt außerdem weiße Houdan; die anerkannten Varianten unterscheiden sich zwischen Ländern.
Die Livestock Conservancy beschreibt Houdan als ruhig und ausgesprochen sanft. Gute Sicht und ruhiger Umgang helfen, Schreckreaktionen zu vermeiden.
Die Haube darf die Sicht nicht einschränken. Trockene, geschützte Bereiche sowie saubere Futter- und Wasserstellen sind für die Kopffedern wichtig.
Ursprünglich wurde die Fleischqualität geschätzt. Eier und die Erhaltung des charakteristischen Haubenhuhns ergänzen heute die Nutzung.
Fünf Zehen sind bei Houdan ein Rassemerkmal. Die meisten anderen Haushühner besitzen vier Zehen pro Fuß.
''', [('The Livestock Conservancy: Houdan', 'https://livestockconservancy.org/houdan-chicken/')])

add('faverolles', 'Faverolles', 'Frankreich',
    'Der französische Rassetyp mit Bart, fünf Zehen und leicht befiederten Beinen.',
    ('3,5–4 kg nach französischer Übersicht', '2,8–3,5 kg nach französischer Übersicht'), 'Helle Eier.', '''
Faverolles entstanden im französischen Eure-et-Loir als Fleischhühner für den Markt. Verschiedene Rassen wirkten an ihrer Entwicklung mit. Dieses Porträt beschreibt die französische Form, aus der sich auch Deutsche Lachshühner entwickelten.
Der kräftige Körper trägt einen Vollbart und einen Einfachkamm. Die Beine sind leicht befiedert. Fünf Zehen an jedem Fuß gehören zu den auffälligen Merkmalen.
Bekannt ist der helle lachsfarbene Typ, im französischen Standard als froment argenté bezeichnet. Hahn und Henne unterscheiden sich deutlich in ihrer Gefiederzeichnung.
Faverolles werden als ruhige, gutmütige Hühner geschätzt. Behutsamer Umgang unterstützt die Gewöhnung an Menschen.
Saubere Tränken und trockene Einstreu helfen, Bart und Fußfedern zu pflegen. Sitzplätze und Nester sollten für den schweren Körper gut erreichbar sein.
Die ursprüngliche Fleischnutzung erklärt den breiten Körper. Heute kommen Eier, Liebhaberzucht und die Erhaltung der französischen Rasseform hinzu.
Faverolles und Deutsche Lachshühner sind eng verwandt. Die getrennten Seiten machen ihre unterschiedliche züchterische Entwicklung sichtbar.
''', [('Club des volailles françaises: Geschichte der Faverolles (PDF)', 'https://www.volailles-francaises.ch/Files/la_faverolles.pdf'),
       ('Französischer Geflügelverband: Rasseübersicht (PDF)', 'https://avifede.com/wp-content/uploads/2019/11/2019_annuaire_federation_NPDC_picardie-c.pdf')])

add('dorking', 'Dorking', 'England',
    'Alte englische Fleischhühner mit langem Körper und fünf Zehen.',
    ('etwa 4,1 kg nach US-Rasseporträt', 'etwa 3,2 kg nach US-Rasseporträt'), 'Weiße bis cremefarbene Eier.', '''
Dorking sind nach einer Marktstadt in Surrey benannt. Die südenglische Region war für hochwertiges Tafelgeflügel bekannt. Verbindungen zu Hühnern der Römerzeit werden diskutiert, sind aber nicht lückenlos belegt.
Ein langer, tiefer Körper und relativ kurze Beine prägen die Gestalt. Fünf Zehen unterscheiden Dorking von vielen anderen Fleischhühnern.
Bekannt sind unter anderem weiße, silbergraue und weitere farbige Varianten. Größe und Einzelheiten können sich nach Farbenschlag und Standard unterscheiden.
Die Rasse gilt als ruhig und sanft. Zugleich sind die Tiere gute Futtersucher, wenn ihnen geeigneter Auslauf zur Verfügung steht.
Niedrige, stabile Sitzplätze und trockene Bodenbereiche passen zum tiefen Körper. Genügend Bewegungsraum hilft, die Tiere in guter Kondition zu halten.
Besonders die Fleischqualität begründete ihren Ruf. Hennen liefern außerdem helle Eier und können auch in kühleren Jahreszeiten legen.
Die zusätzliche Zehe ist ein altes Erkennungsmerkmal. Sie allein beweist jedoch keine bestimmte Abstammungsgeschichte.
''', [('The Livestock Conservancy: Dorking', 'https://livestockconservancy.org/dorking-chicken/')])

add('sussex', 'Sussex', 'England',
    'Ruhige englische Zweinutzungshühner mit rechteckigem Körperprofil.',
    ('3–4 kg', '2,5–3 kg'), 'Bruteier mindestens 60 g; gelbbraune bis hellbraune Schale.', '''
Sussex entstanden in Südengland, wo Geflügel für den Londoner Markt gemästet wurde. Anfang des 20. Jahrhunderts wurde der Rassetyp standardisiert und fand auch in Deutschland Verbreitung.
Der breite, tiefe Körper wirkt von der Seite rechteckig. Ein Einfachkamm und helle, unbefiederte Beine ergänzen den kräftigen Nutztyp.
Bekannt sind weiß-schwarzcolumbia, gelb-schwarzcolumbia und braun-porzellanfarbig. Bei der Columbiazeichnung konzentrieren sich dunkle Partien auf Hals und Schwanz.
Der Sonderverein beschreibt Sussex als ruhig und zutraulich. Regelmäßiger, behutsamer Kontakt fördert ein vertrautes Verhalten.
Gut zugängliche Nester, stabile Sitzplätze und ein abwechslungsreicher Auslauf passen zum Körperbau. Bewegung bleibt auch bei gemütlichen Hühnern wichtig.
Sussex sind klassische Zweinutzungshühner für Eier und Fleisch. Körperfülle und brauchbare Legeleistung gehören gemeinsam zum Zuchtziel.
Die Großrasse erhält eine eigene Seite. Der bereits vorhandene Eintrag Zwerg-Sussex bleibt davon getrennt.
''', [('Sonderverein: Beschreibung der Sussex', 'https://sussex-sv.de/beschreibung/')])

add('paduaner', 'Paduaner', 'Europa',
    'Leichte Haubenhühner mit Rundhaube und dichtem Bart.',
    ('2–2,5 kg nach verlinktem Züchterporträt', '1,5–2 kg'), 'Weiße Eier; Bruteier mindestens 48 g.', '''
Der Name erinnert an Padua, doch die ältere Herkunft lässt sich nicht eindeutig einem Land zuordnen. Haubenhühner dieses Formenkreises sind seit Jahrhunderten in Europa bekannt.
Eine volle Rundhaube und ein dichter Bart bestimmen den Kopf. Ein sichtbarer Kamm fehlt. Der Körper ist eher leicht und zeigt eine aufrechte Landhuhnform.
Beispiele sind schwarz, weiß, silber-schwarzgesäumt, gold-schwarzgesäumt und chamois-weißgesäumt. Bei gesäumten Varianten werden die einzelnen Federn optisch betont.
Paduaner können zutraulich werden. Freie Sicht ist für ihr Verhalten entscheidend: Ein Tier mit verdeckten Augen kann leichter erschrecken.
Haube und Bart sollten trocken und sauber bleiben. Geschützte Auslaufbereiche und ein uneingeschränktes Sichtfeld verdienen besondere Aufmerksamkeit.
Heute stehen Liebhaberzucht und die Erhaltung des Haubentyps im Vordergrund. Daneben liefern die Hennen weiße Eier; Brutlust ist meist gering.
Haube und Bart bestehen aus Federn. Ihre Pflege gehört ebenso zur Haltung wie Futter, Wasser und ein sauberer Stall.
''', [('Paduaner Österreich: Rasseporträt und Haltung', 'https://www.paduaner.at/paduaner-allgemein/')])

add('appenzeller-spitzhauben', 'Appenzeller Spitzhauben', 'Schweiz',
    'Leichte, lebhafte Schweizer Hühner mit nach vorn gerichteter Spitzhaube.',
    ('1,5–1,8 kg', '1,2–1,5 kg'), 'Helle Eier.', '''
Die ältere Geschichte der Spitzhauben ist nicht vollständig geklärt. Lange wurden sie vor allem im Appenzellerland gehalten. Seit 1983 unterstützt ProSpecieRara die Erhaltung dieser Schweizer Rasse.
Der leichte Körper trägt eine schmale, nach vorn gerichtete Federhaube. Der ungewöhnliche Kopfschmuck unterscheidet sich deutlich von einer großen Rundhaube.
Besonders bekannt sind silber-schwarzgetupfte Tiere. Daneben gibt es unter anderem gold-schwarzgetupfte, schwarze und weitere Farbvarianten.
Spitzhauben sind lebhaft, ausdauernde Futtersucher und geschickte Kletterer. Ihr zierliches Aussehen täuscht über ihre Widerstandsfähigkeit hinweg.
Ein gut gesicherter, strukturierter Auslauf passt zur Beweglichkeit. Deckung und geschützte Ruheplätze ergänzen den trockenen Stall.
Die Rasse wird als Legehuhn und zur Erhaltung eines regionalen Kulturguts gezüchtet. Gesundheit und Vitalität gehören dabei zu den wichtigen Zuchtzielen.
In ihrer Heimat werden Spitzhauben auch liebevoll „Tschüpperli“ genannt. Trotz ihres kleinen Körpers sind sie keine Zwergrasse.
''', [('ProSpecieRara: Appenzeller Spitzhaubenhuhn', 'https://www.prospecierara.ch/tiere/rassenportr%C3%A4ts/gefl%C3%BCgel/appenzeller-spitzhaubenhuhn')])

add('appenzeller-barthuehner', 'Appenzeller Barthühner', 'Schweiz',
    'Widerstandsfähige Schweizer Landhühner mit Bart und Rosenkamm.',
    ('2–2,3 kg', '1,6–1,8 kg'), 'Etwa 55 g je Ei als Rasseorientierung.', '''
Appenzeller Barthühner entstanden Mitte des 19. Jahrhunderts in der Ostschweiz. Italiener wurden mit bart- und rosenkämmigen Hühnern verbunden. Seit 1985 unterstützt ProSpecieRara ihre Erhaltung.
Kinn- und Backenbart bilden eine geschlossene Gesichtsbefiederung. Darüber sitzt ein breiter Rosenkamm. Sichtbare Kehllappen sind im Zuchtbild nicht erwünscht.
Schwarze, rebhuhnhalsige und blaue Tiere sind bekannt. Der Bart ist bei beiden Geschlechtern vorhanden und gehört nicht nur zum Hahn.
Die Rasse wird als aufgeweckt, wetterfest und widerstandsfähig beschrieben. Regelmäßiger ruhiger Umgang erleichtert die Betreuung.
Auslauf und Beschäftigung passen zum Landhuhntyp. Tränken und Futterstellen sollten so gestaltet sein, dass der Bart sauber bleibt.
Die Eierleistung stand bei der Entwicklung im Mittelpunkt. ProSpecieRara nennt rund 120 Eier jährlich als Orientierung; tatsächliche Leistungen schwanken.
Appenzeller Barthühner und Appenzeller Spitzhauben sind unterschiedliche Rassen. Ihr Kopfschmuck macht den Unterschied schon auf den ersten Blick sichtbar.
''', [('ProSpecieRara: Appenzeller Barthuhn', 'https://www.prospecierara.ch/tiere/rassenportr%C3%A4ts/gefl%C3%BCgel/appenzeller-barthuhn')])
