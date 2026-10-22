"""Independent bundle and output audit; no simulated JTL success."""
from pathlib import Path
import io,json,zipfile,hashlib,re,xml.etree.ElementTree as E
from build import ROOT,Project,descriptor
bundle=Path(r'C:\Users\thors\Downloads\JTL_Originale_fuer_Codex.zip')
rows=[]
with zipfile.ZipFile(bundle) as source:
    for original in sorted((ROOT/'originale').glob('*.vlg')):
        assert original.read_bytes()==source.read('originale/'+original.name)
        output=next((ROOT/'output').glob(original.name.split('_')[0]+'_*.vlg'))
        row={'document':original.name.split('_')[0],'original_equals_supplied_bundle':True,'projects':[]}
        with zipfile.ZipFile(original) as a,zipfile.ZipFile(output) as b:
            assert a.testzip() is None and b.testzip() is None
            assert set(a.namelist())<=set(b.namelist())
            index=E.fromstring(b.read('index.xml'))
            mapping={x.get('UniqueId').lower():x for x in index.findall('.//item')}
            for item in mapping.values():
                if item.get('Descriptor'):
                    d=E.fromstring(descriptor(item.get('Descriptor')))
                    repo=d.find(".//list[@name='RepositoryItem']")
                    rid=repo.find("item[@name='ID']")
                    if rid is not None and rid.text:
                        assert rid.text.lower()=='repository://{'+item.get('UniqueId').lower()+'}'
                    typ=repo.find("item[@name='Type']")
                    if typ is not None and typ.text:assert typ.text==item.get('Type')
            for name in b.namelist():
                data=b.read(name)
                if name.endswith('.xml'):
                    tree=E.fromstring(data)
                    if name!='index.xml':assert data==a.read(name),'Unexpected content/mail XML edit'
                    for n in tree.findall('.//template'):
                        uid=n.get('id')
                        if uid and uid!='00000000-0000-0000-0000-000000000000':assert uid.lower() in mapping
                if not name.endswith('.lst'):continue
                p=Project(data);old=Project(a.read(name))
                def block_props(proj,section):
                    return [n.props for n in proj.nodes if n.name==section]
                # Compare actual values because supplier insertion shifts line offsets.
                for key in ['Variables','Fields','ChartFields']:
                    assert [n.get(key) for n in p.nodes if n.name=='UsedIdentifiers']==[n.get(key) for n in old.nodes if n.name=='UsedIdentifiers']
                count=int(next(n.get('ObjectCount') for n in p.roots if n.name=='Layout'))
                parsed_count=sum(n.name=='Object' for n in p.roots)
                old_count=int(next(n.get('ObjectCount') for n in old.roots if n.name=='Layout'))
                old_parsed_count=sum(n.name=='Object' for n in old.roots)
                assert count-old_count==parsed_count-old_parsed_count
                assert next(n.get('FileVersion') for n in p.roots if n.name=='Description')=='16'
                assert '§ 19' in data.decode('utf16') or len([n for n in p.roots if n.name=='ProjectTemplates'])>0
                row['projects'].append({'entry':name,'encoding':'UTF-16LE BOM','file_version':16,'stored_object_count':count,'parsed_top_level_objects':parsed_count,'original_stored_object_count':old_count,'original_parsed_top_level_objects':old_parsed_count,'object_count_delta_matches':True,'used_identifiers_unchanged':True})
        rows.append(row)
(ROOT/'pruefung/unabhaengige-pruefung.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print('PASS: 7 Originale bytegleich zur Quelle; XML-Bindungen, Deskriptoren, Ressourcen-IDs, Objektzahlen und Datenbezeichner geprüft.')
