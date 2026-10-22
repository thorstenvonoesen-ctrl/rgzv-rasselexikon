(() => {
  'use strict';
  const catalog = window.RASSE_BESTAND;
  if (!catalog) return;
  document.querySelectorAll('[data-rassen-anzahl], #rassen-gesamt').forEach(node => {
    node.textContent = String(catalog.count);
  });
})();
