window.DES001_SYNC = (() => {
  function validateTopicSources(topic) {
    if (topic.status !== 'done') return [];
    const issues = [];
    if (!topic.sources || topic.sources.length < 3) issues.push(`${topic.title}: fewer than 3 sources.`);
    const types = (topic.sources || []).map((source) => String(source[0]).toLowerCase());
    if (!types.some((type) => type.includes('primary') || type.includes('authority'))) issues.push(`${topic.title}: missing primary/authority source.`);
    if (!types.some((type) => type.includes('applied'))) issues.push(`${topic.title}: missing applied source.`);
    if (!types.some((type) => type.includes('cross') || type.includes('extension'))) issues.push(`${topic.title}: missing cross-check/extension source.`);
    return issues;
  }

  function validate(topics = []) {
    return topics.flatMap(validateTopicSources);
  }

  function report(topics = []) {
    const issues = validate(topics);
    if (issues.length) {
      console.warn('DES-001 validation issues:', issues);
    } else {
      console.info('DES-001 validation passed for completed topics.');
    }
    return issues;
  }

  return { validate, report };
})();
