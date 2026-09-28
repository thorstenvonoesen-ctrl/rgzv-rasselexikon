(() => { const count = document.getElementById('rassen-gesamt'); if (count && Array.isArray(window.FINDER_BREEDS)) count.textContent = new Set(window.FINDER_BREEDS.map(b => b.url)).size; })();
