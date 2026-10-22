"""Lossless, section-aware LL property editor; originals are read-only inputs."""
from pathlib import Path
import base64, copy, difflib, hashlib, io, json, re, struct, uuid, zipfile, zlib
import xml.etree.ElementTree as ET
from PIL import Image

ROOT=Path(__file__).resolve().parent
NOTICE='"Steuerfrei gemäß § 19 Abs. 1 UStG (Kleinunternehmer)."'

class Section:
    def __init__(self,name,start,parent=None):
        self.name,self.start,self.parent=name,start,parent
        self.props={}; self.children=[]
    def get(self,key): return self.props.get(key,(None,None))[1]
    def descendants(self):
        for c in self.children:
            yield c
            yield from c.descendants()

class Project:
    def __init__(self,data):
        assert data.startswith(b'\xff\xfe'), 'Expected UTF-16LE BOM'
        self.original=data; self.lines=data[2:].decode('utf-16le').splitlines(keepends=True)
        self.nodes=[]; self.roots=[]; self.changes=[]; stack=[]; owner=None
        for i,line in enumerate(self.lines):
            t=line.strip()
            if t.startswith('[') and t.endswith(']'):
                owner=Section(t[1:-1],i,stack[-1] if stack else None)
                (owner.parent.children if owner.parent else self.roots).append(owner)
                self.nodes.append(owner)
            elif t=='{':
                assert owner is not None
                stack.append(owner)
            elif t=='}':
                assert stack, 'Unbalanced project'
                closed=stack.pop()
                owner=stack[-1] if stack else closed
            elif '=' in t and owner is not None:
                key,val=t.split('=',1)
                # Scheme colors intentionally repeat; keep every occurrence separately.
                owner.props[key]=(i,val)
        assert not stack
    def set(self,node,key,value):
        i,old=node.props[key]
        if old==value:return
        prefix=self.lines[i][:len(self.lines[i])-len(self.lines[i].lstrip())]
        self.lines[i]=prefix+key+'='+value+'\r\n'
        node.props[key]=(i,value)
        self.changes.append({'section':node.name,'identifier':node.get('Identifier'),'line':i+1,'property':key,'before':old,'after':value})
    def block(self,node):
        end=next((n.start for n in self.roots if n.start>node.start),len(self.lines))
        return ''.join(self.lines[node.start:end])
    def bytes(self):return b'\xff\xfe'+''.join(self.lines).encode('utf-16le')

def sha(b):return hashlib.sha256(b).hexdigest()
def descriptor(value):
    raw=base64.b64decode(value[3:]); assert raw[4:15]==b'ChK_Packed\0'
    decoded=zlib.decompress(raw[15:]); assert struct.unpack('<I',raw[:4])[0]==len(decoded)
    ET.fromstring(decoded)
    return decoded

def main():
    out=ROOT/'output'; out.mkdir(exist_ok=True)
    reports=ROOT/'pruefung'; reports.mkdir(exist_ok=True)
    logo=Image.open(next((ROOT/'originale').glob('*.png'))).convert('RGBA')
    canvas=Image.new('RGB',logo.size,'white'); canvas.paste(logo,mask=logo.getchannel('A'))
    buf=io.BytesIO(); canvas.save(buf,'JPEG',quality=96,subsampling=0); logo_bytes=buf.getvalue()
    Image.open(io.BytesIO(logo_bytes)).verify()
    all_results=[]; hashes={}
    for src in sorted((ROOT/'originale').glob('*.vlg')):
        original=src.read_bytes(); hashes[src.name]=sha(original)
        with zipfile.ZipFile(io.BytesIO(original)) as z:
            assert z.testzip() is None
            infos=z.infolist(); data={i.filename:z.read(i) for i in infos}
        before=dict(data); index=ET.fromstring(data['index.xml']); original_index=data['index.xml']
        for item in index.findall('.//item'):
            if item.get('Descriptor'): descriptor(item.get('Descriptor'))
        changes=[]; supplier=src.name.startswith('Lieferanten')
        for name,raw in list(data.items()):
            if name.endswith('.image'):
                assert Image.open(io.BytesIO(raw)).format=='JPEG'
                data[name]=logo_bytes
            if not name.endswith('.lst'):continue
            p=Project(raw)
            for n in p.nodes:
                ident=n.get('Identifier') or ''
                if n.name=='UserVariables':
                    for key,(_,v) in list(n.props.items()):
                        if v.startswith('@PositionsColumnWidthVAT;'):p.set(n,key,'@PositionsColumnWidthVAT;0')
                if n.get('Identifier') in ['Vat block','Total block','Note on reverse charge','Note on VAT-exempt outside EU','Payment by PayPal','Payment by sold receivable','USt.Gesamt','Nettogesamt']:
                    p.set(n,'Condition','False')
                if ident=='Note on intra-Community delivery':
                    p.set(n,'Condition','False')
                if n.name=='Object' and ident=='Footer':
                    p.set(n,'Position/Left','20000')
                    p.set(n,'Position/Width','#LL.Device.Page.Size.cx - @BorderLeft - @BorderRight')
                    p.set(n,'Position/Height','#@FooterHeight - 5')
                    p.set(n,'bFrame','0')
                if n.name=='Object' and n.get('ObjectName')=='Bild':
                    p.set(n,'Position/Height','30000')
                if n.name=='Line' and n.get('Text')=='"Ust-IdNr: " +Report.Company.ValueAddedTaxId':
                    p.set(n,'Text',NOTICE); p.set(n,'Condition','True')
                if n.name=='Foreground':
                    indices=[i for i in range(n.start+1,len(p.lines)) if p.lines[i].strip()=='}']
                    end=indices[0]
                    palette=['(30,67,38)','(145,108,35)','(30,67,38)','(64,64,64)','(75,75,75)','(90,90,90)','(120,120,120)','(153,153,153)','(102,102,102)','(204,204,204)']
                    for j,i in enumerate(i for i in range(n.start,end) if p.lines[i].strip().startswith('Color=')):
                        old=p.lines[i].strip().split('=',1)[1]
                        p.lines[i]=p.lines[i][:len(p.lines[i])-len(p.lines[i].lstrip())]+'Color='+palette[j]+'\r\n'
                        p.changes.append({'section':'Foreground','line':i+1,'property':'Color','before':old,'after':palette[j]})
                if n.name=='Background':
                    end=next(i for i in range(n.start+1,len(p.lines)) if p.lines[i].strip()=='}')
                    for i in range(n.start,end):
                        if p.lines[i].strip().startswith('Color='):
                            old=p.lines[i].strip().split('=',1)[1]
                            value='(255,255,255)'
                            p.lines[i]=p.lines[i][:len(p.lines[i])-len(p.lines[i].lstrip())]+'Color='+value+'\r\n'
                            p.changes.append({'section':'Background','line':i+1,'property':'Color','before':old,'after':value})
                text=n.get('Text')
                if supplier and text=='"Bestellung"':p.set(n,'Text','"Lieferantenbestellung"')
                if text and 'JTL_QR_' in text and 'Condition' in n.props:
                    p.set(n,'Condition','False')
                if text and 'Sie können den QR-GiroCode' in text:
                    # Parse quoted formula literals; alter only the one human-readable literal.
                    spans=list(re.finditer(r'"(?:[^"\\]|\\.)*"',text))
                    for m in reversed(spans):
                        if 'Sie können den QR-GiroCode' in m.group():
                            text=text[:m.start()]+'""'+text[m.end():]
                    p.set(n,'Text',text)
                if supplier and n.name=='Object':
                    if ident=='Bestellung':
                        for child in n.descendants():
                            if child.get('Text')=='"Bestellung"':p.set(child,'Text','"Lieferantenbestellung"')
                    if ident=='JTL.WaWi.Firma.Bankverbindung.Bank':
                        for key,value in [('Position/Left','20000'),('Position/Top','281000'),('Position/Width','170000'),('Position/Height','6000')]:p.set(n,key,value)
                    if ident=='JTL.WaWi.Firma.Name':
                        p.set(n,'Position/Height','43000')
                    if ident=='Bestellung':p.set(n,'Position/Width','167000')
                    if n.get('ObjectName')=='Berichtscontainer':p.set(n,'Position/Width','167000')
                if supplier and n.name=='Column' and text in ['Positionen.USt','"USt."']:
                    p.set(n,'Condition','False');p.set(n,'Width','0')
                if supplier and n.name=='Column' and text and 'Gesamt Netto (' in text:
                    p.set(n,'Condition','False')
            if supplier:
                # Reuse a complete original LL image object from this exact bundle.
                base=next((ROOT/'analyse/Rechnung_Neue Vorlage_GlobaleVorgänge').glob('A335*.lst'))
                bp=Project(base.read_bytes()); image_node=next(n for n in bp.roots if n.get('ObjectName')=='Bild')
                image_id=str(uuid.uuid5(uuid.NAMESPACE_URL,'jtl-federlogo-lieferantenbestellung')).upper()
                for key,val in [('LinkUUID','{'+str(uuid.uuid5(uuid.NAMESPACE_URL,'jtl-federlogo-object')).upper()+'}'),('Identifier','Federlogo'),('Position/Left','130000'),('Position/Top','4000'),('Position/Width','60000'),('Position/Height','30000'),('Filename','repository://{'+image_id+'}')]:bp.set(image_node,key,val)
                layout=next(n for n in p.roots if n.name=='Layout');p.set(layout,'ObjectCount',str(int(layout.get('ObjectCount'))+1))
                pos=next(n.start for n in p.roots if n.name=='UserVariables')
                p.lines.insert(pos,bp.block(image_node))
                data[image_id+'.image']=logo_bytes
                # Clone valid original image metadata and change only structured ID nodes.
                source_idx=ET.parse(ROOT/'analyse/Rechnung_Neue Vorlage_GlobaleVorgänge/index.xml')
                image_item=copy.deepcopy(next(n for n in source_idx.findall('.//item') if n.get('Type')=='resource/image'))
                image_item.set('UniqueId',image_id.lower());image_item.set('Name','Federlogo')
                d=ET.fromstring(descriptor(image_item.get('Descriptor')))
                for elem in d.findall('.//item'):
                    if elem.get('name')=='ID':elem.text='repository://{'+image_id+'}'
                    if elem.get('name')=='0':elem.text='Federlogo'
                db=ET.tostring(d,encoding='utf-16',xml_declaration=True)
                image_item.set('Descriptor','@2@'+base64.b64encode(struct.pack('<I',len(db))+b'ChK_Packed\0'+zlib.compress(db)).decode())
                index.find('items').append(image_item)
                # Supplier title is explicit; add the notice to the existing closing paragraph.
                # Apply after reparse since insertion changes line offsets.
                p2=Project(p.bytes())
                for n in p2.nodes:
                    if n.get('Text')=='"Wir danken für eine schnellstmögliche Abwicklung."':
                        p2.set(n,'Text','"Wir danken für eine schnellstmögliche Abwicklung.¶Unser Unternehmen ist Kleinunternehmer gemäß § 19 Abs. 1 UStG."')
                p.lines=p2.lines;p.changes+=p2.changes
            result=p.bytes(); Project(result)
            data[name]=result;changes.extend([dict(entry=name,**c) for c in p.changes])
            diff=''.join(difflib.unified_diff(raw[2:].decode('utf-16le').splitlines(True),result[2:].decode('utf-16le').splitlines(True),fromfile='original/'+name,tofile='output/'+name))
            (reports/(src.stem+'_'+name+'.diff')).write_text(diff,encoding='utf8')
        if supplier:data['index.xml']=ET.tostring(index,encoding='utf-8')
        else:assert data['index.xml']==original_index
        dest=out/(src.name.split('_')[0]+'_Gefluegelzuchtbedarf_PRUEFVERSION.vlg')
        with zipfile.ZipFile(dest,'w') as z:
            for info in infos:z.writestr(info,data[info.filename])
            for name in data.keys()-before.keys():z.writestr(name,data[name],compress_type=zipfile.ZIP_DEFLATED)
        with zipfile.ZipFile(dest) as z:
            assert z.testzip() is None
            assert len(z.namelist())==len(set(z.namelist()))
            payload={n:z.read(n) for n in z.namelist()}
        xmls={n:ET.fromstring(b) for n,b in payload.items() if n.endswith('.xml')}
        ids={n.rsplit('.',1)[0].lower() for n in payload if n!='index.xml'}
        refs=[]
        for name,b in payload.items():
            if name.endswith('.lst'):
                text=b.decode('utf-16');Project(b)
                refs+=re.findall(r'repository://\{([0-9A-Fa-f-]+)\}',text)
                for uid in refs:assert uid.lower() in ids, (name,uid)
            elif name.endswith('.image'):Image.open(io.BytesIO(b)).verify()
        for item in xmls['index.xml'].findall('.//item'):
            assert item.get('UniqueId').lower() in ids
            if item.get('Descriptor'):descriptor(item.get('Descriptor'))
        entries=[{'name':n,'before_bytes':len(before[n]) if n in before else None,'after_bytes':len(b),'sha256_before':sha(before[n]) if n in before else None,'sha256_after':sha(b),'changed':n not in before or before[n]!=b,'crc32':f'{zlib.crc32(b):08x}'} for n,b in payload.items()]
        all_results.append({'original':src.name,'output':dest.name,'sha256_original':sha(original),'sha256_output':sha(dest.read_bytes()),'zip_integrity':'PASS','xml_and_descriptors':'PASS','repository_references':'PASS','lst_structure':'PASS','jtl_import':'NOT_TESTED','jtl_designer':'NOT_TESTED','preview':'NOT_TESTED','print':'NOT_TESTED','entries':entries,'changes':changes,'references':refs})
        assert src.read_bytes()==original
    (reports/'originale-sha256.json').write_text(json.dumps(hashes,indent=2,ensure_ascii=False),encoding='utf8')
    (reports/'validierung.json').write_text(json.dumps(all_results,indent=2,ensure_ascii=False),encoding='utf8')
    print('\n'.join(r['output']+': ZIP/XML/Struktur/Referenzen PASS, '+str(len(r['changes']))+' Property-Änderungen' for r in all_results))

if __name__=='__main__':main()
