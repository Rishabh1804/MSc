(() => {
  const config = window.DES001_CONFIG;
  const topics = window.DES001_TOPICS;

  if (!config || !topics || !window.DES001_HOME || !window.DES001_SYNC) {
    throw new Error('DES-001 app failed to initialise: required modules missing.');
  }

  window.DES001_SYNC.report(topics);
  window.DES001_HOME.renderApp(config, topics);
})();
