"""Bestandsschutz, Vollständigkeit, Verlinkung, Sortierung und unabhängiger QR-Decoder."""
import hashlib, json, re, sys
from urllib.parse import urlsplit, unquote
from html.parser import HTMLParser
from extend_series4 import ROOT, SERIES4, BASE, cards, name, normalized, sortkey
from PIL import Image
import zxingcpp

report=json.loads((ROOT/'scripts/series4-inventory.json').read_text(encoding='utf-8'))
for filename,digest in report['preserved_pages'].items():
    assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==digest,filename
index=(ROOT/'index.html').read_text(encoding='utf-8')
allcards=cards(index)
assert len(allcards)==report['after']==193
assert len({normalized(name(c)) for c in allcards})==193
urls=[re.search(r'href="([^"]+)"',c)[1] for c in allcards]
assert len(set(urls))==193
assert all((ROOT/u).is_file() for u in urls)
for content in re.findall(r'<div class="cards">(.*?)</div>',index,re.S):
    keys=[sortkey(name(c)) for c in cards(content)]
    assert keys==sorted(keys)
finder=json.loads((ROOT/'assets/finder-data.js').read_text(encoding='utf-8').split('window.FINDER_BREEDS = ',1)[1].strip().rstrip(';'))
assert len(finder)==len({b['url'] for b in finder})==193
assert set(urls)=={b['url'] for b in finder}
class Links(HTMLParser):
    def handle_starttag(self,tag,attrs):
        for key,value in attrs:
            if key not in ('href','src') or not value: continue
            parts=urlsplit(value)
            if parts.scheme or parts.netloc or not parts.path: continue
            assert (ROOT/unquote(parts.path)).exists(),value
for b in SERIES4:
    text=(ROOT/(b['slug']+'.html')).read_text(encoding='utf-8')
    Links().feed(text)
    assert urls.count(b['slug']+'.html')==1
    for key in ['history','appearance','colors','nature','husbandry','use','fact','laying','egg']:
        assert b[key] and __import__('html').escape(b[key]) in text,(b['slug'],key)
    assert '<strong>Tiergruppe</strong>Zwerghuhn' in text
    qr=Image.open(ROOT/'qr-codes'/f'{b["slug"]}.png').convert('RGB')
    assert [r.text for r in zxingcpp.read_barcodes(qr,formats=zxingcpp.BarcodeFormat.QRCode)]==[BASE+b['slug']+'.html']
Links().feed(index)
result=dict(total=193,added=5,requested_already_present=25,preserved_pages=len(report['preserved_pages']),qr_decoded=5,unique_names=True,unique_urls=True,finder_complete=True,alphabetical_groups=True,local_links=True,all_new_fields=True)
(ROOT/'scripts/series4-results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
