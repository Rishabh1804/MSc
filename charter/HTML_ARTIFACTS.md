# HTML_ARTIFACTS.md — CodeMike HTML Artifact Layer

CodeMike's source of truth remains Markdown, CSV, Python, reports, and versioned data files.

HTML artifacts are a review and interaction layer: single-file interfaces that make complex information easier to inspect, compare, explain, and transfer.

## Core Rule

Use Markdown when the artifact is mostly linear.

Use HTML when the artifact benefits from:

- filters
- tabs
- sorting
- cards
- diagrams
- timelines
- sliders
- dashboards
- comparison views
- visual scanning
- interactive review

## Architecture

```text
Markdown / CSV / Python = source of truth
HTML artifacts = review and interaction layer
PWA = eventual operating cockpit
```

## Appropriate HTML Artifact Uses

- destination database browser
- recommendation ranking explorer
- sensitivity analysis dashboard
- capability browser
- pattern library gallery
- roadmap timeline
- orientation portal
- experiment report viewer
- project transfer review
- Planner OptionCard prototype

## Rules

- HTML artifacts should be self-contained when practical.
- Do not make HTML the only source of truth.
- Link back to the data, report, or source file that generated the artifact.
- Include limitations and verification status.
- Avoid hidden logic that is not represented in Python, Markdown, or data files.
- If an artifact becomes product-critical, graduate it into a proper app/PWA component later.

## Folder

HTML artifacts live in:

```text
artifacts/html/
```

## First Target Artifact

`artifacts/html/destination-browser-v1.html`

Purpose:

- inspect the India + near-India destination database
- filter by region, budget, family suitability, and access complexity
- visually check database coverage
- prepare for Planner transfer and PWA design
