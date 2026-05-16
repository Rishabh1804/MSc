// Minimal service worker — caches the cockpit shell on install,
// network-first for everything else so that operational data
// (operations/*.md) is always fresh.

const SHELL_CACHE = 'cockpit-shell-v1';
const SHELL_FILES = [
  './',
  './index.html',
  './manifest.webmanifest',
  './assets/cockpit.css',
  './assets/cockpit.js',
  './views/skill-map.html',
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(SHELL_CACHE).then((cache) => cache.addAll(SHELL_FILES))
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys.filter((k) => k !== SHELL_CACHE).map((k) => caches.delete(k))
      )
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  // Network-first for every request. The shell is cached at install
  // via addAll(SHELL_FILES); on a network failure the cache provides
  // the offline shell. Operational data (operations/*.md) is always
  // fetched fresh — we deliberately do NOT write it to cache here.
  const req = event.request;
  event.respondWith(
    fetch(req).catch(() => caches.match(req))
  );
});
