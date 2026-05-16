# decks/

Slide-deck source. Decks are HTML (reveal.js) that fetch their content from `../operations/` and `../datasets/` the same way cockpit views do (HR-MSc-9).

See `../charter/REPO_STRUCTURE.md` and `../charter/HARD_RULES.md`.

## Layout

After Batch 8 this directory holds:

```text
decks/
├── README.md
├── shared/
│   ├── reveal-theme.css       Cockpit design tokens applied to reveal.js
│   └── deck-data-fetch.js     Fetches operations/*.md into [data-source] sections
└── curriculum/
    └── 00-foundations/        Sample deck
        ├── slides.html        Reveal.js shell; data fetched at runtime
        ├── notes.md           Speaker notes
        └── README.md          Deck charter (intent, audience, evidence links)
```

Subsequent decks follow the same shape — `slides.html`, `notes.md`, `README.md` per deck, grouped under `decks/curriculum/<module-slug>/`, `decks/viva/<capability-slug>/`, or `decks/transfer/<transfer-slug>/` per the migration plan.

## Deck contract

`slides.html` is a reveal.js shell. A data-bearing slide declares its source on the `<section>`:

```html
<section data-source="../../../operations/SKILL_MAP.md">
  <h2>Current skill map</h2>
  <pre class="cm-source-content cm-loading">Loading&hellip;</pre>
  <span class="cm-source-note">source: operations/SKILL_MAP.md</span>
</section>
```

`shared/deck-data-fetch.js` (loaded by every `slides.html`) hydrates these on `Reveal.on('ready')`. The shell HTML carries no copy of the source content — keeping the slide honest about what the file currently says.

## .pptx export

`../.github/workflows/decks-export.yml` runs on push to `main` touching `decks/`, `operations/`, or the workflow/script itself. The workflow:

1. Installs Playwright + python-pptx and a headless Chromium.
2. Runs `../.github/scripts/export_decks.py`, which serves the repo on a free port, walks `decks/**/slides.html`, navigates each slide via `Reveal.slide(i)`, screenshots at 1920×1080, and assembles a `.pptx` per deck (one slide = one full-bleed image).
3. Uploads `build/*.pptx` as a workflow artifact named `decks-pptx`.

No `.pptx` is committed to the repository. The HTML is the source of truth; the export is offered for situations where the HTML deck cannot run.

## Local run

Serve the repo root (e.g. `python -m http.server` from the repo root) and open `http://localhost:8000/decks/curriculum/00-foundations/slides.html`. Direct `file://` opening will not work because the slide fetches sibling-of-repo files.

To produce a `.pptx` locally:

```bash
pip install playwright python-pptx
python -m playwright install --with-deps chromium
python .github/scripts/export_decks.py
ls build/
```
