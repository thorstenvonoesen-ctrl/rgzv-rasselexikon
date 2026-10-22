// Ohne Browser: dynamische Aktualisierung, Normalisierung und mehrere Anzeigen prüfen.
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
function run(extra = []) {
  const nodes = [{textContent: '…'}, {textContent: '…'}];
  const context = vm.createContext({window: {}, document: {querySelectorAll: () => nodes}});
  vm.runInContext(fs.readFileSync('assets/finder-data.js','utf8'),context);
  const original = context.window.FINDER_BREEDS.length;
  context.window.FINDER_BREEDS.push(...extra);
  for (const file of ['assets/rassen-bestand.js','assets/rassen-gesamt.js']) vm.runInContext(fs.readFileSync(file,'utf8'),context);
  assert.equal(nodes[0].textContent, String(context.window.RASSE_BESTAND.count));
  assert.equal(nodes[1].textContent, nodes[0].textContent);
  return {count: context.window.RASSE_BESTAND.count, original, entries: context.window.FINDER_BREEDS};
}
const base=run();
assert.equal(base.count,base.entries.filter(b=>b.group!=='Dekorationshuhn').length);
const extra={name:'Prüfrasse',url:'pruefrasse.html',description:'Test einer zukünftigen Erweiterung.',group:'Großhuhn',traits:{}};
assert.equal(run([extra]).count,base.count+1);
assert.equal(run([extra,extra]).count,base.count+1);
const original=base.entries.find(b=>b.name==='Zwerg-Kraienköppe');
assert.equal(run([{...original,url:'andere-url.html',name:'Zwerg Kraienkoeppe'}]).count,base.count);
assert.equal(run([{...extra,name:'Ko Gunkei'}]).count,base.count);
for(const invalid of [null,{}, {...extra,url:'../index.html'}, {...extra,url:'https://example.org/rasse.html'}, {...extra,name:' '}, {...extra,group:'Unbekannt'}, {...extra,description:''}]) assert.equal(run([invalid]).count,base.count);
assert.equal(run([{...extra,group:'Dekorationshuhn'}]).count,base.count);
console.log(`${base.count} Rassen; automatische Erhöhung, mehrere Anzeigen, Dubletten und ungültige Einträge geprüft.`);
