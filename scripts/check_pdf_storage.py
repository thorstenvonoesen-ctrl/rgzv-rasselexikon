"""Dauerhafte zentrale Sammlung prüfen; veraltete Ausgabeordner verhindern."""
from pathlib import Path
import json
from check_catalog import ROOT,GROUPS

def check(root=ROOT):
    raw=(root/'assets/finder-data.js').read_text(encoding='utf-8')
    breeds=json.loads(raw.split('window.FINDER_BREEDS = ',1)[1].strip().rstrip(';'))
    names={b['url'].replace('.html','.pdf') for b in breeds if b['group'] in GROUPS}
    assert len(names)==sum(b['group'] in GROUPS for b in breeds),'Doppelte Schilder'
    actual={p.name for p in (root/'output/pdf/a7').glob('*.pdf')}
    assert actual==names,('A7-Sammlung unvollständig',names.symmetric_difference(actual))
    for name in ['alle-rasseschilder-a7.pdf','alle-rasseschilder-a4.pdf']:
        assert (root/'output/pdf'/name).is_file(),name
    for name in ['schilder','druckboegen']:
        assert not (root/name).exists(),'Veralteter Ausgabeordner: '+name
    print(f'{len(names)} A7-Schilder zentral; Gesamtausgaben vorhanden; keine alten Ausgabeordner.')
    return len(names)

if __name__=='__main__':check()
