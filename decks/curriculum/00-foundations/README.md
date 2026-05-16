# decks/curriculum/00-foundations/

Deck for curriculum module `00-foundations`. Sample deck for the Batch-8 pipeline scaffold.

## Intent

A walking demonstration that:

1. A deck is HTML, not PowerPoint.
2. Every data-bearing slide fetches its source file at runtime — no academic claim hardcoded in the slide HTML (HR-MSc-9).
3. The same source markdown drives the cockpit views, so the deck and the cockpit cannot disagree.
4. A `.pptx` export is available on demand (workflow artifact) for situations where a HTML deck cannot run.

## Audience

The capability workspace itself — Aurelius for chronicling, Cipher for QA, CodeMike for the operating walk-through.

## Evidence links

- `../../../operations/SKILL_MAP.md`
- `../../../operations/ROADMAP.md`
- `../../../operations/NEXT_ACTIONS.md`

These paths are exactly what `slides.html` fetches; changing the deck means changing the source markdown, not the slide HTML.

## How to run

- **HTML:** open `slides.html` in a browser; cross-bucket fetches require the repo to be served (any static server pointed at the repo root works, e.g. `python -m http.server` from the repo root, then visit `http://localhost:8000/decks/curriculum/00-foundations/slides.html`).
- **.pptx:** push to `main` touching this directory or any of the source files; download the `decks-pptx` artifact from the run of `decks-export` in `.github/workflows/`.
