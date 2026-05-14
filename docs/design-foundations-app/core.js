window.DES001_CORE = (() => {
  function escapeHtml(value) {
    return String(value ?? '')
      .replaceAll('&', '&amp;')
      .replaceAll('<', '&lt;')
      .replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;')
      .replaceAll("'", '&#039;');
  }

  function list(items = []) {
    return `<ul>${items.map((item) => `<li>${escapeHtml(item)}</li>`).join('')}</ul>`;
  }

  function sourceClass(type = '') {
    const lower = type.toLowerCase();
    if (lower.includes('applied')) return 'applied';
    if (lower.includes('cross')) return 'cross';
    if (lower.includes('authority')) return 'authority';
    if (lower.includes('extension')) return 'extension';
    return '';
  }

  function statusLabel(status) {
    if (status === 'partial') return 'Partial digest';
    if (status === 'done') return 'Digested';
    return 'Deep read pending';
  }

  function countByStatus(topics = []) {
    return topics.reduce((acc, topic) => {
      acc[topic.status] = (acc[topic.status] || 0) + 1;
      return acc;
    }, {});
  }

  return {
    escapeHtml,
    list,
    sourceClass,
    statusLabel,
    countByStatus
  };
})();
