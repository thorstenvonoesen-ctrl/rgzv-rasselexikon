const fs = require('node:fs');
const path = require('node:path');

const normalize = value => value.normalize('NFKC').toLocaleLowerCase('de').trim().replace(/\s+/g, ' ');

function generate(inputs, source, previous) {
  if (inputs.aktion === 'Ausstellung deaktivieren') return { ...previous, aktiv: false };
  if (inputs.aktion !== 'Ausstellung veröffentlichen/aktualisieren') throw new Error('Unbekannte Aktion.');
  const match = source.match(/window\.FINDER_BREEDS\s*=\s*(\[[\s\S]*\]);?\s*$/);
  if (!match) throw new Error('Rassenquelle konnte nicht gelesen werden.');
  const breeds = JSON.parse(match[1]);
  const catalog = new Map();
  for (const breed of breeds) {
    const key = normalize(breed.name);
    if (catalog.has(key)) throw new Error('Mehrdeutiger Rassenname: ' + breed.name);
    catalog.set(key, breed);
  }
  const titel = (inputs.titel || '').trim();
  if (!titel) throw new Error('Bitte einen Titel eingeben.');
  const lines = (inputs.rassen || '').split(/\r?\n|;/).map(s => s.trim()).filter(Boolean);
  if (!lines.length) throw new Error('Bitte mindestens eine Rasse mit Käfignummer eingeben.');
  const rassen = lines.map(line => {
    const fields = line.split('|').map(s => s.trim());
    if (fields.length < 2 || fields.length > 3) throw new Error('Ungültige Eingabe: ' + line + '. Erwartet: Rasse | Käfig von | Käfig bis');
    const breed = catalog.get(normalize(fields[0]));
    if (!breed) throw new Error('Rasse nicht im Rasselexikon gefunden: ' + fields[0]);
    const numbers = [fields[1], fields[2] || fields[1]];
    if (!numbers.every(s => /^\d+$/.test(s) && Number.isSafeInteger(Number(s)) && Number(s) > 0)) throw new Error('Ungültige Käfignummer: ' + line);
    const [kaefigVon, kaefigBis] = numbers.map(Number);
    if (kaefigBis < kaefigVon) throw new Error('Käfig bis liegt vor Käfig von: ' + line);
    if (!/^[a-z0-9-]+\.html$/.test(breed.url)) throw new Error('Ungültige Rassenseite: ' + breed.name);
    return { name: breed.name, slug: breed.url, kaefigVon, kaefigBis };
  }).sort((a, b) => a.kaefigVon - b.kaefigVon);
  let total = 0;
  rassen.forEach((r, i) => {
    if (i && r.kaefigVon <= rassen[i - 1].kaefigBis) throw new Error('Käfigbereiche überschneiden sich bei: ' + r.name);
    total += r.kaefigBis - r.kaefigVon + 1;
  });
  if (!Number.isSafeInteger(total)) throw new Error('Zu viele Käfige.');
  return { aktiv: true, titel, ort: (inputs.ort || '').trim(), datum: (inputs.datum || '').trim(), begruessung: (inputs.begruessung || '').trim(), rassen };
}

if (require.main === module) {
  try {
    const root = path.resolve(__dirname, '..');
    const target = path.join(root, 'assets/ausstellung.json');
    const inputs = JSON.parse(fs.readFileSync(process.env.GITHUB_EVENT_PATH, 'utf8')).inputs;
    const result = generate(inputs, fs.readFileSync(path.join(root, 'assets/finder-data.js'), 'utf8'), JSON.parse(fs.readFileSync(target, 'utf8')));
    fs.writeFileSync(target, JSON.stringify(result, null, 2) + '\n');
  } catch (error) {
    console.error('Ausstellung nicht gespeichert: ' + error.message);
    process.exitCode = 1;
  }
}
module.exports = { generate };
