// Reine Statusfunktionen werden auch von den Verwaltungs- und Regressionstests genutzt.
((root) => {
  'use strict';
  const today = (date = new Date()) => new Intl.DateTimeFormat('sv-SE', {timeZone:'Europe/Berlin',year:'numeric',month:'2-digit',day:'2-digit'}).format(date);
  const validDate = s => typeof s === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(s) && !isNaN(Date.parse(s)) && new Date(s).toISOString().slice(0,10) === s;
  function current(config, day = today()) {
    if (!config || !Array.isArray(config.veranstaltungen)) return null;
    const matches=config.veranstaltungen.filter(e => e.id === config.aktuelleVeranstaltung);
    if(matches.length!==1) return null;
    const e=matches[0];
    return /^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(e.id) && typeof e.titel==='string' && e.titel.trim() &&
      validDate(e.beginn) && validDate(e.ende) && e.beginn<=e.ende && e.ende>=day &&
      ['angekuendigt','aktuell'].includes(e.status) ? e : null;
  }
  function entries(event, data, catalog) {
    if(!event || event.erkundungFreigegeben!==true || !data || data.veranstaltungId!==event.id || !Array.isArray(data.rassen) || !Array.isArray(catalog)) return [];
    const breeds=new Map(catalog.map(b=>[b.url,b]));
    const seen=new Set(),ranges=[], result=[];
    for(const r of data.rassen){
      if(!r || !breeds.has(r.slug) || seen.has(r.slug)) return [];
      const cages=Array.isArray(r.kaefige)?r.kaefige:[{von:r.kaefigVon,bis:r.kaefigBis}];
      if(!cages.length || !cages.every(k=>k && Number.isSafeInteger(k.von)&&Number.isSafeInteger(k.bis)&&k.von>0&&k.bis>=k.von)) return [];
      seen.add(r.slug); ranges.push(...cages);
      result.push({...r,name:breeds.get(r.slug).name,kaefige:[...cages].sort((a,b)=>a.von-b.von)});
    }
    ranges.sort((a,b)=>a.von-b.von);
    if(ranges.some((r,i)=>i && r.von<=ranges[i-1].bis)) return [];
    return result;
  }
  const api={today,validDate,current,entries};
  root.RGZV_EVENTS=api;
  if(typeof module!=='undefined') module.exports=api;
})(typeof window==='undefined'?globalThis:window);
