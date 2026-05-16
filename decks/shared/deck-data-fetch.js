// Deck data fetcher — companion to cockpit.js, with the same contract:
// HR-MSc-9 forbids hardcoding academic claims in HTML. A deck slide that
// shows operational state must fetch the source file at runtime.
//
// Usage in a slide:
//   <section data-source="../../operations/SKILL_MAP.md">
//     <h2>Skill map</h2>
//     <pre class="cm-source-content">Loading...</pre>
//     <span class="cm-source-note">source: operations/SKILL_MAP.md</span>
//   </section>
//
// On reveal:ready, every section with [data-source] gets its
// <pre class="cm-source-content"> populated with the fetched file.

(function () {
  function escapeHtml(s) {
    return s
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  async function hydrate(section) {
    const source = section.getAttribute('data-source');
    const target = section.querySelector('.cm-source-content');
    if (!source || !target) return;
    try {
      const res = await fetch(source, { cache: 'no-cache' });
      if (!res.ok) throw new Error('HTTP ' + res.status);
      const text = await res.text();
      target.innerHTML = escapeHtml(text);
    } catch (err) {
      target.classList.add('cm-error');
      target.textContent = 'Failed to load ' + source + ': ' + String(err);
    }
  }

  function hydrateAll() {
    document.querySelectorAll('section[data-source]').forEach(hydrate);
  }

  if (window.Reveal && typeof window.Reveal.on === 'function') {
    window.Reveal.on('ready', hydrateAll);
  } else {
    document.addEventListener('DOMContentLoaded', hydrateAll);
  }
})();
