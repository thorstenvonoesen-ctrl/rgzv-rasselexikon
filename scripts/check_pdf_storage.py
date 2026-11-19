"""Dauerhafte zentrale Sammlung prüfen; veraltete Ausgabeordner verhindern."""
from pathlib import Path
import json
import sys
from check_catalog import ROOT,GROUPS

def check(root=ROOT, snapshot=False):
    raw=(root/'assets/finder-data.js').read_text(encoding='utf-8')
    breeds=json.loads(raw.split('window.FINDER_BREEDS = ',1)[1].strip().rstrip(';'))
    names={b['url'].replace('.html','.pdf') for b in breeds if b['group'] in GROUPS}
    assert len(names)==sum(b['group'] in GROUPS for b in breeds),'Doppelte Schilder'
    if snapshot:
        # Katalogänderungen können vor den automatisch erzeugten PDFs eintreffen.
        layout=json.loads((root/'scripts/a7-layout.json').read_text(encoding='utf-8'))
        names={url.replace('.html','.pdf') for url in layout['entries']}
        assert len(names)==layout['count']
    central=root/'A7-Rasseschilder'
    legacy=root/'output/pdf'
    collections={'alle-rasseschilder-a7.pdf','alle-rasseschilder-a4.pdf',
                 'beispiel-acht-rasseschilder-a4.pdf','erweiterung-50-a7.pdf','erweiterung-50-a4.pdf'}
    actual={p.name for p in central.glob('*.pdf')}-collections
    assert actual==names,('A7-Sammlung unvollständig',names.symmetric_difference(actual))
    assert {p.name for p in (legacy/'a7').glob('*.pdf')}==names
    for name in names | collections:
        alias=(legacy/'a7' if name in names else legacy)/name
        assert (central/name).read_bytes()==alias.read_bytes(),name
    for name in ['schilder','druckboegen']:
        assert not (root/name).exists(),'Veralteter Ausgabeordner: '+name
    print(f'{len(names)} A7-Schilder zentral; Gesamtausgaben vorhanden; keine alten Ausgabeordner.')
    return len(names)

if __name__=='__main__':check(snapshot='--snapshot' in sys.argv)
