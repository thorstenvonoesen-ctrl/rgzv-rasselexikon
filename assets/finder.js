(() => {
  'use strict';
  const breeds = window.FINDER_BREEDS.filter(b => b.url !== 'hagener-goldhals-langhuhn.html');
  const questions = [
    ['Welche Geflügelart interessiert Sie?', [['Großhuhn','Hühner'],['Zwerghuhn','Zwerghühner'],['Ente','Enten'],['Gans','Gänse'],['Taube','Tauben'],['Wachtel','Wachteln'],['any','Ich bin offen für alles']]],
    ['Wie viel Platz steht zur Verfügung?', [['small','Eher wenig'],['garden','Normaler Garten'],['large','Viel Platz'],['any','Spielt keine Rolle']]],
    ['Was ist Ihnen besonders wichtig?', [['calm','Ruhiges Wesen'],['utility','Eier / Nutzen'],['looks','Außergewöhnliches Aussehen'],['tradition','Ursprüngliche oder traditionelle Rassen'],['show','Ausstellung und Zucht'],['discover','Einfach eine interessante Rasse entdecken']]],
    ['Wie viel Erfahrung haben Sie?', [['beginner','Ich fange gerade erst an'],['some','Etwas Erfahrung'],['expert','Viel Erfahrung']]],
    ['Welche Tiergröße bevorzugen Sie?', [['small','Lieber kleinere Tiere'],['medium','Mittlere Größe'],['large','Große Tiere'],['any','Egal']]],
    ['Wie aktiv dürfen die Tiere sein?', [['calm','Lieber ruhig'],['active','Gerne etwas lebhafter'],['any','Aktivität spielt keine Rolle']]],
    ['Ist Flugfreudigkeit für Sie ein Problem?', [['low','Ja, möglichst wenig flugfreudig'],['no','Nein'],['any','Egal']]],
    ['Was möchten Sie mit den Tieren hauptsächlich?', [['garden','Tiere im Garten halten'],['utility','Eier / Nutzwert'],['breed','Rassegeflügelzucht'],['show','Ausstellen'],['discover','Erst einmal kennenlernen'],['any','Keine bestimmte Richtung']]]
  ];
  let answers = Array(8).fill(null), step = 0;
  const host = document.getElementById('finder-content');
  const progressArea = document.getElementById('progress-area');
  function element(tag, text, cls) {
    const node = document.createElement(tag);
    if (text) node.textContent = text;
    if (cls) node.className = cls;
    return node;
  }
  function button(text, cls, action) {
    const node = element('button', text, cls); node.type = 'button'; node.addEventListener('click', action); return node;
  }
  function score(b, a) {
    let points = 0; const reasons = [], cautions = [], t = b.traits;
    const add = (value, reason) => { points += value; if (reason) reasons.push(reason); };
    if (a[0] === b.group) add(20, 'Gehört zu Ihrer gewählten Geflügelgruppe.');
    if (a[4] !== 'any' && t.size) {
      if (a[4] === t.size) add(5, 'Die grobe Größenklasse entspricht Ihrem Wunsch.'); else points -= 3;
    }
    if (a[1] === 'small' && t.space === 'high') { points -= 7; cautions.push('Der Platzwunsch passt möglicherweise nicht: Auslauf und gegebenenfalls Wasserfläche genau prüfen.'); }
    if (a[1] === 'large' && t.space === 'high') add(2, 'Ihr großzügiges Platzangebot ist für diese Tiergruppe hilfreich.');
    const interests = a[2] || [];
    if (interests.includes('calm') && t.activity === 'calm') add(4, 'Der Lexikon-Kurztext beschreibt ein ruhiges Wesen.');
    if (interests.includes('calm') && t.activity === 'active') points -= 2;
    for (const [key, reason] of [['utility','Der Kurztext betont Eier oder Nutzwert.'],['looks','Die beschriebenen äußeren Merkmale passen zu Ihrem Interesse an besonderem Aussehen.'],['tradition','Der Kurztext verweist auf Tradition, Geschichte oder einen Landhuhntyp.']]) {
      if (interests.includes(key) && t[key]) add(4, reason);
    }
    if (a[5] !== 'any' && t.activity) {
      if (a[5] === t.activity) add(4, a[5] === 'calm' ? 'Die beschriebene ruhige Art entspricht Ihrer Aktivitätsvorliebe.' : 'Die beschriebene lebhafte Art entspricht Ihrer Aktivitätsvorliebe.'); else points -= 3;
    }
    if (a[6] === 'low' && t.flight === 'high') { points -= 6; cautions.push('Flugfreudigkeit kann Ihrem Wunsch widersprechen; eine passende Sicherung ist nötig.'); }
    if (a[7] === 'utility' && t.utility) add(5, 'Der beschriebene Nutzwert passt zu Ihrem hauptsächlichen Interesse.');
    if (b.specialist) {
      if (a[3] === 'beginner') points -= 15;
      if (a[7] === 'garden') points -= 15;
      cautions.push('Eiderenten sind eine Wildart mit besonderen Haltungsansprüchen, keine Hausentenrasse.');
    }
    // Unknown experience, flight, space and exhibition suitability stay neutral.
    if (interests.includes('show') || ['show','breed'].includes(a[7])) reasons.push('Das Rasseporträt bietet einen Einstieg für Ihr Interesse an Zucht und Ausstellung; Eignung bitte gesondert klären.');
    if (interests.includes('discover') || a[7] === 'discover') reasons.push('Das vorhandene Porträt passt zu Ihrem Wunsch, eine Rasse zunächst kennenzulernen.');
    return {breed:b, points, reasons:[...new Set(reasons)], cautions};
  }
  function rank(a) {
    const sorted = breeds.map(b => ({...score(b,a), tie:Math.random()})).sort((x,y) => y.points-x.points || x.tie-y.tie);
    const preferred = a[0] === 'any' ? sorted : sorted.filter(x => x.breed.group === a[0]);
    const chosen = preferred.slice(0,3);
    // Some groups contain fewer than three entries. Label cross-group suggestions honestly.
    if (chosen.length < 3) chosen.push(...sorted.filter(x => x.breed.group !== a[0]).slice(0,3-chosen.length).map(x => ({...x, alternative:true})));
    return chosen;
  }
  function randomBreed() { return breeds[Math.floor(Math.random()*breeds.length)]; }
  function animateAndFocus() {
    host.classList.remove('finder-enter'); void host.offsetWidth; host.classList.add('finder-enter');
    const title = host.querySelector('h2'); title.tabIndex = -1; title.focus({preventScroll:true});
    if (document.querySelector('.finder').getBoundingClientRect().top < 0) document.querySelector('.finder').scrollIntoView({block:'start'});
  }
  function render() {
    host.replaceChildren(); progressArea.hidden = false;
    document.getElementById('progress-text').textContent = 'Frage '+(step+1)+' von 8';
    document.getElementById('progress').value = step+1;
    const [title, options] = questions[step], multi = step === 2;
    host.append(element('h2', title));
    if (multi) host.append(element('p', 'Mehrere Antworten möglich. Wählen Sie mindestens eine und dann „Weiter“.'));
    const choices = element('div', '', 'finder-options');
    const actions = element('div', '', 'finder-actions');
    const back = button('Zurück', 'finder-secondary', () => { step--; render(); }); back.disabled = step === 0;
    const next = button('Weiter', 'button', () => { step++; render(); });
    next.disabled = !(answers[2] || []).length;
    for (const [value,label] of options) {
      const selected = multi ? (answers[step] || []).includes(value) : answers[step] === value;
      const choice = button(label, 'finder-choice', () => {
        if (multi) {
          const set = new Set(answers[step] || []); set.has(value) ? set.delete(value) : set.add(value);
          answers[step] = [...set]; choice.setAttribute('aria-pressed', String(set.has(value))); next.disabled = !set.size;
        } else {
          answers[step] = value; if (step === 7) results(); else { step++; render(); }
        }
      });
      choice.setAttribute('aria-pressed', String(selected)); choices.append(choice);
    }
    actions.append(back); if (multi) actions.append(next);
    host.append(choices,actions); animateAndFocus();
  }
  function results() {
    host.replaceChildren(); progressArea.hidden = false;
    document.getElementById('progress-text').textContent = '8 von 8 Fragen beantwortet';
    document.getElementById('progress').value = 8;
    host.append(element('h2', 'Diese Rassen könnten zu Ihnen passen'));
    host.append(element('p', 'Aufgrund Ihrer Auswahl könnten diese Rassen interessant sein. Unbekannte Eigenschaften wurden neutral gewertet.'));
    const selection = rank(answers);
    if (selection.some(x => x.alternative)) host.append(element('p', 'In Ihrer gewählten Gruppe sind weniger als drei Einträge vorhanden. Die zusätzlichen Vorschläge aus anderen Gruppen sind als Alternativen gekennzeichnet.', 'highlight'));
    const cards = element('div', '', 'finder-results');
    for (const result of selection) {
      const b = result.breed, card = element('article', '', 'card');
      card.append(element('span', result.alternative ? 'Alternative aus einer anderen Gruppe · '+b.group : b.group, 'badge'), element('h3', b.name));
      const reasons = result.reasons.slice(0,3);
      const fillers = [b.description, 'Ein weiteres Porträt zum Vergleichen und Entdecken; unbekannte Eigenschaften sind keine bestätigte Übereinstimmung.', 'Die Detailseite unterstützt Sie dabei, die Anforderungen vor einer Entscheidung näher kennenzulernen.'];
      for (const text of fillers) { if (reasons.length === 3) break; if (!reasons.includes(text)) reasons.push(text); }
      const list = element('ul'); reasons.forEach(text => list.append(element('li',text))); card.append(list);
      result.cautions.forEach(text => card.append(element('p',text,'finder-note')));
      const link = element('a','Rasse entdecken','button'); link.href = b.url; card.append(link); cards.append(card);
    }
    host.append(cards);
    let note = 'Die Zuordnung nutzt grobe Hinweise aus den Lexikon-Kurztexten. Sie bestätigt weder Anfänger- noch Haltungseignung. Wenig Flugfreude und geringer Platzbedarf sind bei fehlenden Angaben nicht zugesichert.';
    if (answers[3] === 'beginner') note += ' Für den Einstieg sollten Sie die konkrete Haltung mit erfahrenen Züchtern besprechen.';
    host.append(element('p',note,'finder-note'));
    const actions = element('div','','finder-actions');
    actions.append(button('Zurück','finder-secondary',()=>{step=7;render();}),button('Andere Antworten ausprobieren','button',()=>{answers=Array(8).fill(null);step=0;render();}),button('🎲 Zufällige Rasse entdecken','finder-secondary',()=>{window.location.href=randomBreed().url;}));
    host.append(actions); animateAndFocus();
  }
  render();
})();
