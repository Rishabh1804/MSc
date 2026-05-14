# DES-001 Modular Dashboard App

This folder contains the modular v2 implementation of the CodeMike DES-001 Design Foundations Study Dashboard.

Primary page:

```text
docs/design-foundations-v2.html
```

Legacy monolithic page:

```text
docs/design-foundations.html
```

## Why this folder exists

The original dashboard stored structure, styles, data, topic notes, source lists, and rendering logic in one large HTML file. That created avoidable friction:

- small content edits required rewriting a large file
- GitHub connector reads could be truncated
- full-file overwrites became risky
- topic notes were mixed with presentation code
- future topic work was harder to review cleanly

The v2 dashboard separates the app into small files so each edit has a clear target.

## File roles

| File | Role | Edit when |
|---|---|---|
| `../design-foundations-v2.html` | Small HTML shell that loads the app modules | Adding/removing top-level containers or changing script order |
| `styles.css` | Visual design, layout, responsive rules, component styling | Changing appearance only |
| `config.js` | Assignment metadata, workflow, rules, synthesis text, version | Changing global assignment framing |
| `data.js` | Topic list, source list, status, summaries, note excerpts, further reading links | Updating topics or source scaffolds |
| `core.js` | Shared utility helpers such as escaping, list rendering, status labels | Adding reusable helper logic |
| `home.js` | Rendering functions for hero, stats, workflow, rules, modules, synthesis | Changing dashboard structure or rendered sections |
| `sync.js` | Validation and consistency checks | Adding quality gates or rubric checks |
| `start.js` | Bootstrap entry point | Changing initialisation order or startup checks |

## Edit rules

1. Do not put long academic notes directly into `design-foundations-v2.html`.
2. Keep the HTML shell small and stable.
3. Put topic metadata, status, and links in `data.js`.
4. Put long topic notes in Markdown under `design/foundations/`.
5. Put appearance-only changes in `styles.css`.
6. Put assignment-wide text in `config.js`.
7. Add validation rules in `sync.js` when the rubric or assignment standard changes.
8. Keep source lists explicit: every completed topic needs multiple source types.

## Required source standard for completed topics

A completed deep-reading topic should include:

- at least 3 sources
- at least 1 primary or high-authority source where possible
- at least 1 practical/applied source
- at least 1 cross-checking or alternative framing source

The current `sync.js` validation checks completed topics for these minimum requirements.

## Topic note pattern

For future topics, prefer this pattern:

```text
design/foundations/topic-02-what-is-ui-design.md
design/foundations/topic-02-what-is-ui-design-further-reading.md
```

Then link those files from `data.js`.

## Topic 1 status

Topic 1 — UI vs UX — has been completed at two levels:

```text
docs/design-foundations-app/data.js
design/foundations/ui-vs-ux-further-reading.md
```

The extension note adds further reading and applied exercises beyond the minimum assignment requirement, including:

- Nielsen Norman Group usability heuristics
- Peter Morville UX Honeycomb
- GOV.UK user-needs discipline
- W3C accessibility, usability, and inclusion framing
- UI inventory exercise
- UX journey-map exercise
- heuristic mini-audit
- UX Honeycomb scoring

## Browser verification notes

The expected GitHub Pages URLs are:

```text
https://rishabh1804.github.io/MSc/docs/design-foundations-v2.html
https://rishabh1804.github.io/MSc/design-foundations-v2.html
```

Use whichever matches the repository's GitHub Pages serving mode.

## Promotion rule

Do not replace `docs/design-foundations.html` with v2 until:

- v2 renders successfully in browser
- CSS loads correctly
- all JS modules load without console errors
- Topic 1 extension link opens correctly
- `sync.js` reports no validation issues for completed topics
- the visual layout is at least equivalent to the legacy dashboard

After verification, the project can either:

1. keep both files and treat v2 as the active artifact, or
2. rename v2 into `docs/design-foundations.html` and archive the old monolithic version.
