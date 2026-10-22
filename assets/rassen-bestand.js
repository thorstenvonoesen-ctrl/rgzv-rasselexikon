// Gemeinsamer, validierter Katalog für alle Gesamtanzeigen und den Rasse-Finder.
// Die zugehörigen Dateien und Navigation prüft scripts/check_catalog.py.
(() => {
  'use strict';
  const groups = new Set(['Großhuhn', 'Zwerghuhn', 'Taube', 'Wachtel', 'Gans', 'Ente']);
  const key = value => value.trim().toLocaleLowerCase('de')
    .replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss').replace(/œ/g, 'oe').replace(/æ/g, 'ae')
    .normalize('NFKD').replace(/[\u0300-\u036f]/g, '').replace(/[^a-z0-9]/g, '');
  const aliases = new Map([
    ['kogunkei', 'koshamo'], ['twentsekrielen', 'zwergkraienkoeppe'],
    ['malayen', 'malaien'], ['modernesenglischeskaempferhuhn', 'moderneenglischekaempfer'],
    ['zwergbielefelderkennhuehner', 'bielefelderzwergkennhuehner'],
    ['deutschezwergsperber', 'zwergdeutschesperber'],
    ['hollaendischeweisshauben', 'hollaenderhaubenhuehner'],
    ['faverollesfranzoesischertyp', 'faverolles'], ['franzoesischefaverolles', 'faverolles'],
    ['katalanier', 'prat'], ['araucanas', 'araucana'], ['zwergaraucanas', 'zwergaraucana'],
    ['croadlangshan', 'croadlangschan'], ['deutschelangshan', 'deutschelangschan'],
    ['zwergcroadlangshan', 'zwergcroadlangschan'], ['plymouthrock', 'plymouthrocks'],
    ['jerseygiant', 'jerseygiants'], ['dominique', 'dominikaner'], ['cornish', 'indischekaempfer']
  ]);
  function validEntries(source) {
    const urls = new Set(), names = new Set();
    if (!Array.isArray(source)) return [];
    return source.filter(b => {
      if (!b || typeof b.name !== 'string' || !b.name.trim() ||
          typeof b.description !== 'string' || !b.description.trim() ||
          typeof b.url !== 'string' || !/^[a-z0-9]+(?:-[a-z0-9]+)*\.html$/.test(b.url) ||
          !groups.has(b.group)) return false;
      const normalized = key(b.name), name = aliases.get(normalized) || normalized;
      if (!name || urls.has(b.url) || names.has(name)) return false;
      urls.add(b.url); names.add(name); return true;
    });
  }
  const entries = Object.freeze(validEntries(window.FINDER_BREEDS));
  window.RASSE_BESTAND = Object.freeze({ entries, get count() { return entries.length; }, validEntries });
})();
