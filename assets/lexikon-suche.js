(() => {
  const input=document.getElementById('lexikon-suche');
  if(!input)return;
  const cards=[...document.querySelectorAll('.cards .card')];
  const normal=s=>s.toLocaleLowerCase('de').replace(/ä/g,'ae').replace(/ö/g,'oe').replace(/ü/g,'ue').replace(/ß/g,'ss').normalize('NFD').replace(/[\u0300-\u036f]/g,'');
  input.addEventListener('input',()=>{
    const term=normal(input.value.trim());let count=0;
    for(const card of cards){card.hidden=!normal(card.querySelector('h3').textContent).includes(term);if(!card.hidden)count++;}
    document.getElementById('lexikon-suchstatus').textContent=term?count+' passende Einträge':'';
  });
})();
