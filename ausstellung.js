const ausstellung = {
  aktiv: false,
  titel: "Unsere Ausstellung",
  ort: "Bürgerhalle Hagen-Dahl",
  datum: "",
  rassen: []
};

(() => {
  'use strict';
  const teaser = document.getElementById('ausstellung-start');
  if (teaser) teaser.hidden = ausstellung.aktiv !== true;
  const host = document.getElementById('ausstellung-inhalt');
  if (!host) return;
  const node = (tag, text, cls) => {
    const el = document.createElement(tag);
    if (text) el.textContent = text;
    if (cls) el.className = cls;
    return el;
  };
  if (ausstellung.aktiv !== true) {
    host.append(node('p','Derzeit ist keine Ausstellung aktiviert.'));
    const back = node('a','Zurück zum Rasselexikon','button'); back.href='index.html'; host.append(back);
    return;
  }
  // Only explicitly configured entries are used. Reject invalid ranges and non-local URLs.
  const entries = ausstellung.rassen.filter(r => r && typeof r.name === 'string' && /^[a-z0-9-]+\.html$/.test(r.slug) && Number.isSafeInteger(r.kaefigVon) && Number.isSafeInteger(r.kaefigBis) && r.kaefigVon > 0 && r.kaefigBis >= r.kaefigVon);
  const slugs = [...new Set(entries.map(r=>r.slug))];
  const ranges = entries.map(r=>[r.kaefigVon,r.kaefigBis]).sort((a,b)=>a[0]-b[0]);
  let occupied=0, end=0;
  for (const [from,to] of ranges) { if (to>end) occupied+=to-Math.max(end,from-1); end=Math.max(end,to); }
  const key='rgzv-ausstellung:'+JSON.stringify([ausstellung.titel,ausstellung.ort,ausstellung.datum,entries.map(r=>[r.slug,r.kaefigVon,r.kaefigBis]).sort()]);
  let discovered=new Set(), storageOK=true;
  try { const stored=JSON.parse(localStorage.getItem(key)||'[]'); if(Array.isArray(stored)) discovered=new Set(stored.filter(s=>slugs.includes(s))); } catch { storageOK=false; }
  host.append(node('h2',ausstellung.titel));
  host.append(node('p',[ausstellung.ort,ausstellung.datum].filter(Boolean).join(' · ')));
  host.append(node('p',slugs.length+' ausgestellte Rassen · '+occupied+' belegte Käfige','highlight'));
  const tour=node('section'); tour.append(node('h3','Dein Ausstellungsrundgang'));
  const status=node('p');status.setAttribute('role','status');
  const bar=node('progress');bar.max=Math.max(1,slugs.length);bar.setAttribute('aria-label','Entdeckte Rassen');
  const reset=node('button','Fortschritt zurücksetzen','ausstellung-secondary');reset.type='button';
  const storageNote=node('p','Der Fortschritt kann hier nicht dauerhaft gespeichert werden und gilt nur bis zum Neuladen.');storageNote.hidden=storageOK;
  tour.append(status,bar,reset,storageNote);host.append(tour);
  function save(){try{localStorage.setItem(key,JSON.stringify([...discovered]));}catch{storageNote.hidden=false;}}
  function update(){status.textContent=discovered.size+' von '+slugs.length+' Rassen entdeckt';bar.value=discovered.size;reset.disabled=discovered.size===0;}
  function field(label,placeholder,id){const wrap=node('div');const caption=node('label',label);caption.htmlFor=id;const input=node('input');input.id=id;input.type='search';input.placeholder=placeholder;wrap.append(caption,input);return [wrap,input];}
  const search=node('div','','ausstellung-search');
  const [nameWrap,nameInput]=field('Rasse suchen','Rasse suchen …','rasse-suche');
  const [cageWrap,cageInput]=field('Käfignummer suchen','Käfignummer eingeben','kaefig-suche');cageInput.inputMode='numeric';
  search.append(nameWrap,cageWrap);host.append(search,node('h2','Ausgestellte Rassen'));
  const message=node('p');message.setAttribute('role','status');const list=node('div','','ausstellung-cards');host.append(message,list);
  const normal=s=>s.toLocaleLowerCase('de').normalize('NFD').replace(/[\u0300-\u036f]/g,'').trim();
  function render(){
    const term=normal(nameInput.value), query=cageInput.value.trim();
    const number=/^\d+$/.test(query)?Number(query):NaN;
    const matches=entries.filter(r=>(!term||normal(r.name).includes(term))&&(!query||(r.kaefigVon<=number&&number<=r.kaefigBis)));
    list.replaceChildren();
    message.textContent=matches.length ? (query?'Käfig '+number+' · ':'')+matches.length+' passende Einträge' : query?'Für diese Käfignummer wurde keine Rasse gefunden.':'Keine passende ausgestellte Rasse gefunden.';
    for(const r of matches){
      const card=node('article','','card');card.append(node('h3',r.name),node('p',r.kaefigVon===r.kaefigBis?'Käfig '+r.kaefigVon:'Käfige '+r.kaefigVon+'–'+r.kaefigBis,'ausstellung-cage'));
      const link=node('a','Rasse entdecken','button');link.href=r.slug;card.append(link);
      const label=node('label','','ausstellung-discovered');const checkbox=node('input');checkbox.type='checkbox';checkbox.checked=discovered.has(r.slug);
      checkbox.addEventListener('change',()=>{checkbox.checked?discovered.add(r.slug):discovered.delete(r.slug);save();update();list.querySelectorAll('input[type=checkbox]').forEach(c=>{if(c.dataset.slug===r.slug)c.checked=checkbox.checked;});});
      checkbox.dataset.slug=r.slug;label.append(checkbox,document.createTextNode('✓ Rasse entdeckt'));card.append(label);list.append(card);
    }
  }
  nameInput.addEventListener('input',render);cageInput.addEventListener('input',render);
  reset.addEventListener('click',()=>{discovered.clear();save();update();render();});
  update();render();
})();
