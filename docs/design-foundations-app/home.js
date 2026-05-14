window.DES001_HOME = (() => {
  const { escapeHtml, list, sourceClass, statusLabel, countByStatus } = window.DES001_CORE;

  function renderHero(config) {
    document.getElementById('app-hero').innerHTML = `
      <div class="eyebrow">${escapeHtml(config.eyebrow)}</div>
      <h1>${escapeHtml(config.title)}</h1>
      <p class="lead">A modular learning dashboard for the UI/UX foundations CodeMike must digest before upgrading the destination master browser. Long notes now live outside the HTML shell to avoid fragile large-file updates.</p>
      <div class="notice"><strong>Rule:</strong> ${escapeHtml(config.sourcePolicy)}</div>
    `;
  }

  function renderStats(config, topics) {
    const counts = countByStatus(topics);
    document.getElementById('app-stats').innerHTML = [
      ['Total modules', topics.length],
      ['Digested modules', counts.done || 0],
      ['Minimum sources/module', 3],
      ['Current artifact', config.version]
    ].map(([label, value]) => `
      <div class="stat"><small>${escapeHtml(label)}</small><strong>${escapeHtml(value)}</strong></div>
    `).join('');
  }

  function renderWorkflow(config) {
    document.getElementById('app-workflow').innerHTML = config.workflow.map(([title, body]) => `
      <div class="step"><strong>${escapeHtml(title)}</strong><span>${escapeHtml(body)}</span></div>
    `).join('');
  }

  function renderRules(config) {
    document.getElementById('app-rules').innerHTML = config.rules.map((rule) => `
      <article class="rule">
        <h3>${escapeHtml(rule.title)}</h3>
        ${list(rule.items)}
      </article>
    `).join('');
  }

  function renderSources(sources = []) {
    if (!sources.length) return '<p>Source scaffold pending.</p>';
    return `<div class="source-list">${sources.map(([type, label, href, why]) => `
      <div class="source-row">
        <span class="source-type ${sourceClass(type)}">${escapeHtml(type)}</span>
        <div>
          <a href="${escapeHtml(href)}" target="_blank" rel="noreferrer">${escapeHtml(label)}</a>
          <small>${escapeHtml(why)}</small>
        </div>
      </div>
    `).join('')}</div>`;
  }

  function renderTopic(topic, index) {
    return `
      <article class="module">
        <div class="module-head">
          <div class="num">${index + 1}</div>
          <div>
            <h3>${escapeHtml(topic.title)}</h3>
            <p class="summary">${escapeHtml(topic.summary)}</p>
          </div>
          <span class="status ${escapeHtml(topic.status)}">${statusLabel(topic.status)}</span>
        </div>
        <div class="module-grid">
          <div>
            <div class="panel"><h4>Sources consulted / queued</h4>${renderSources(topic.sources)}</div>
            <div class="panel"><h4>Topic summary</h4><p>${escapeHtml(topic.notes.summary)}</p></div>
            <div class="panel"><h4>Key principles</h4>${list(topic.notes.principles)}</div>
            <div class="panel"><h4>Source comparison</h4><p>${escapeHtml(topic.notes.comparison)}</p></div>
            <div class="panel"><h4>Disagreements / emphasis differences</h4><p>${escapeHtml(topic.notes.disagreements)}</p></div>
          </div>
          <div>
            <div class="panel"><h4>CodeMike interpretation</h4><p>${escapeHtml(topic.notes.interpretation)}</p></div>
            <div class="panel"><h4>Application to destination master browser</h4><p>${escapeHtml(topic.notes.application)}</p></div>
            <div class="panel"><h4>Anti-patterns</h4>${list(topic.notes.antiPatterns)}</div>
            <div class="panel"><h4>Implementation implications</h4>${list(topic.notes.implementation)}</div>
            <div class="panel"><h4>Checklist updates</h4>${list(topic.notes.checklist)}</div>
            <div class="further"><h4>Further reading suggestions</h4>${list(topic.further)}</div>
          </div>
        </div>
      </article>
    `;
  }

  function renderModules(config, topics) {
    document.getElementById('app-curriculum-note').textContent = config.curriculumNote;
    document.getElementById('app-modules').innerHTML = topics.map(renderTopic).join('');
  }

  function renderSynthesis(config) {
    document.getElementById('app-synthesis').innerHTML = `
      <h2>${escapeHtml(config.synthesis.title)}</h2>
      ${config.synthesis.paragraphs.map((paragraph) => `<p>${paragraph}</p>`).join('')}
    `;
  }

  function renderApp(config, topics) {
    renderHero(config);
    renderStats(config, topics);
    renderWorkflow(config);
    renderRules(config);
    renderModules(config, topics);
    renderSynthesis(config);
  }

  return { renderApp };
})();
