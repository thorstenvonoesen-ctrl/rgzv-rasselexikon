const fs = require('node:fs');
const path = require('node:path');

const normalize = value => value.normalize('NFKC').toLocaleLowerCase('de').trim().replace(/\s+/g, ' ');

function generate(inputs, source, previous = { aktiv: false, titel: '', ort: '', datum: '', begruessung: '', rassen: [] }) {
  if (inputs.aktion === 'Ausstellung deaktivieren') return { ...previous, aktiv: false };
  if (inputs.aktion === 'Ausstellung anlegen/Grunddaten ändern') {
    const result = { ...previous, aktiv: true };
    for (const key of ['titel', 'ort', 'datum', 'begruessung']) {
      const value = (inputs[key] || '').trim();
      if (value) result[key] = value;
    }
    if (!result.titel) throw new Error('Bitte einen Titel eingeben.');
    return result;
  }
  if (!['Rasse hinzufügen', 'Rasse/Käfige ändern', 'Rasse entfernen'].includes(inputs.aktion)) throw new Error('Unbekannte Aktion.');
  const match = source.match(/window\.FINDER_BREEDS\s*=\s*(\[[\s\S]*\]);?\s*$/);
  if (!match) throw new Error('Rassenquelle konnte nicht gelesen werden.');
  const breeds = JSON.parse(match[1]);
  const catalog = new Map();
  for (const breed of breeds) {
    const key = normalize(breed.name);
    if (catalog.has(key)) throw new Error('Mehrdeutiger Rassenname: ' + breed.name);
    catalog.set(key, breed);
  }
  const name = (inputs.rasse || '').trim();
  if (!name) throw new Error('Bitte eine Rasse eingeben.');
  const breed = catalog.get(normalize(name));
  if (!breed) throw new Error('Rasse nicht im Rasselexikon gefunden: ' + name);
  const matches = previous.rassen.filter(r => r.slug === breed.url);
  if (inputs.aktion === 'Rasse hinzufügen' && matches.length) throw new Error('Rasse bereits vorhanden. Bitte „Rasse/Käfige ändern“ wählen: ' + breed.name);
  if (inputs.aktion !== 'Rasse hinzufügen' && !matches.length) throw new Error('Rasse nicht in der aktuellen Ausstellung vorhanden: ' + breed.name);
  if (inputs.aktion === 'Rasse entfernen') return { ...previous, rassen: previous.rassen.filter(r => r.slug !== breed.url) };
  if (matches.length > 1) throw new Error('Mehrere Käfigbereiche für diese Rasse vorhanden. Bitte die Rasse entfernen und erneut hinzufügen: ' + breed.name);
  const from = (inputs.kaefigVon || '').trim();
  const numbers = [from, (inputs.kaefigBis || '').trim() || from];
  if (!numbers.every(s => /^\d+$/.test(s) && Number.isSafeInteger(Number(s)) && Number(s) > 0)) throw new Error('Bitte gültige positive Käfignummern eingeben.');
  const [kaefigVon, kaefigBis] = numbers.map(Number);
  if (kaefigBis < kaefigVon) throw new Error('Käfig bis liegt vor Käfig von.');
  if (!/^[a-z0-9-]+\.html$/.test(breed.url)) throw new Error('Ungültige Rassenseite: ' + breed.name);
  const rassen = inputs.aktion === 'Rasse hinzufügen'
    ? [...previous.rassen, { name: breed.name, slug: breed.url, kaefigVon, kaefigBis }]
    : previous.rassen.map(r => r.slug === breed.url ? { ...r, kaefigVon, kaefigBis } : r);
  const sorted = [...rassen].sort((a, b) => a.kaefigVon - b.kaefigVon);
  let total = 0;
  sorted.forEach((r, i) => {
    if (i && r.kaefigVon <= sorted[i - 1].kaefigBis) throw new Error('Käfigbereiche überschneiden sich bei: ' + r.name);
    total += r.kaefigBis - r.kaefigVon + 1;
  });
  if (!Number.isSafeInteger(total)) throw new Error('Zu viele Käfige.');
  return { ...previous, rassen };
}

if (require.main === module) {
  try {
    const root = path.resolve(__dirname, '..');
    const target = path.join(root, 'assets/ausstellung.json');
    const inputs = JSON.parse(fs.readFileSync(process.env.GITHUB_EVENT_PATH, 'utf8')).inputs;
    const previous = fs.existsSync(target) ? JSON.parse(fs.readFileSync(target, 'utf8')) : undefined;
    const result = generate(inputs, fs.readFileSync(path.join(root, 'assets/finder-data.js'), 'utf8'), previous);
    fs.writeFileSync(target, JSON.stringify(result, null, 2) + '\n');
  } catch (error) {
    console.error('Ausstellung nicht gespeichert: ' + error.message);
    process.exitCode = 1;
  }
}
module.exports = { generate };
