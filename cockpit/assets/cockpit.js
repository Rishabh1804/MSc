// CodeMike Cockpit — minimal runtime.
//
// Contract (HR-MSc-9): cockpit HTML must not hardcode academic claims.
// This module fetches the markdown source listed on a `[data-source]`
// element and renders it as a preformatted block (no client-side
// markdown parser — keeps the bundle dependency-free and the rendering
// honest about the source).

(function () {
  function escapeHtml(s) {
    return s
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  async function loadView(viewEl) {
    const source = viewEl.getAttribute('data-source');
    if (!source) {
      viewEl.innerHTML = '<p class="cm-error">No data-source attribute set on this view.</p>';
      return;
    }
    try {
      const res = await fetch(source, { cache: 'no-cache' });
      if (!res.ok) {
        throw new Error('HTTP ' + res.status);
      }
      const text = await res.text();
      viewEl.innerHTML = '<pre>' + escapeHtml(text) + '</pre>';
    } catch (err) {
      viewEl.innerHTML =
        '<p class="cm-error">Failed to load <code>' +
        escapeHtml(source) +
        '</code>: ' +
        escapeHtml(String(err)) +
        '</p>' +
        '<p class="cm-error">Check that the source file exists and that the deploy workflow staged it.</p>';
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[data-source]').forEach(function (el) {
      if (el.tagName === 'MAIN' || el.classList.contains('cm-view')) {
        loadView(el);
      }
    });
  });
})();
