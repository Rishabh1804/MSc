# cockpit/

PWA source for the CodeMike operating cockpit. Each cockpit view is an HTML shell that fetches data from `../operations/*.md` (and, where applicable, `../datasets/*.csv`) at runtime. No academic claim is hardcoded in cockpit HTML — that is HR-MSc-9 made operational.

See `../charter/REPO_STRUCTURE.md` and `../charter/HARD_RULES.md` for the rules that bind this directory.

## Layout

```text
cockpit/
├── index.html                Landing page; links to views; registers sw.js
├── manifest.webmanifest      PWA manifest
├── sw.js                     Service worker — shell cached, data network-first
├── assets/
│   ├── cockpit.css           Design tokens + minimal layout
│   └── cockpit.js            Fetch + escape helpers (no markdown parser)
└── views/
    └── skill-map.html        Reference view: fetches operations/SKILL_MAP.md
```

## View contract

Every view follows the same shape:

1. The HTML shell has a `<main class="cm-view" data-source="<relative path>">` element.
2. `cockpit.js` reads `data-source` on `DOMContentLoaded`, fetches the file, and renders the response inside the element as escaped preformatted text. There is no client-side markdown renderer — the view is honest about what the source actually says.
3. No content is duplicated from the source in the shell. The shell holds the chrome (title, links, footer); the body comes from the fetched file.

A new view is added by copying `views/skill-map.html`, changing the `<title>`, the heading, and the `data-source` value.

## Deploy

`.github/workflows/cockpit-build.yml` runs on push to `main` when `cockpit/`, `operations/`, or `datasets/` change. It assembles a Pages bundle (`cockpit/` plus the specific `operations/` and `datasets/` files the cockpit reads) and publishes to GitHub Pages via `actions/deploy-pages`. No build output is committed back to the repository.

Locally, the cockpit can be served with any static server pointed at the repo root, e.g. `python -m http.server` from the repo root; navigate to `http://localhost:8000/cockpit/`.

## Why dependency-free

The cockpit is a learning-evidence tool, not a product. Pulling in a markdown library or a UI framework would add review surface for no learning benefit. If a future view needs richer rendering, prefer adding a small per-view helper to `assets/cockpit.js` over importing a dependency.
