# MIGRATION_LOG.md — Repository Migration Log

Chronological record of migration batches as they commit. The frozen target state lives in `MIGRATION_PLAN.md`; this file records what has actually happened.

All batches stack as commits on branch `claude/review-msc-sproutlab-docs-HzsrJ` and ship under PR #1. Batches merge into `main` together at PR close.

## Entry template

~~~md
## Batch <N> — <short title>

Date:
PR: #1
Commit: <short SHA>
Scope: <one sentence>
Files added:
Files moved:
Files deleted:
Verification: <link-check status, build status, manual smoke check>
Notes:
~~~

A batch's own commit SHA is backfilled by the next batch's log update (since a commit cannot know its own SHA at write time). The most recent batch's `Commit` field will read `(pending — backfilled next batch)` until then.

## Plan revisions

### 2026-05-15 — Stacked-commit cadence

PR: #1  
Commit: `ee68591`  
Affects: All batches from Batch 1 onward; Batch 0 retroactively reclassified from "draft PR per batch" to "first commit on PR #1".  
Change: Migration plan now describes the cadence as stacked commits on a single branch / single PR, not one PR per batch.  
Reason: Aligns with the session's designated working branch and reduces PR overhead. Per-commit review preserves batch-level reviewability.

### 2026-05-15 — Add `artifacts/` to the directory table; expand Batch 6 row

PR: #1  
Commit: `82596a7`  
Affects: Batch 6.  
Change: Adds a new row to the root-directory-targets table in `MIGRATION_PLAN.md`: `artifacts/` → `operations/artifacts/`. Updates the Batch 6 row in the Batches table to enumerate all five directories now in scope (`trackers`, `benchmarks`, `orientation`, `synthetic-data`, `artifacts`). Updates the "Why" paragraph from "22 directories" to "23 directories" with a note about the audit miss.  
Reason: `artifacts/` was discovered at the repo root during Batch 4 staging — the original audit missed it. The migration plan must reflect actual state before the batch that moves it. Target chosen: `operations/artifacts/` because the directory contains operational evidence outputs (HTML, exports) that are governed by `charter/HTML_ARTIFACTS.md` and catalogued by `operations/ARTIFACT_INDEX.md`. Also clarifies that the `synthetic-data/` → `datasets/synthetic/` move is a merge (target already exists with `trip_options_sample.csv`), not a rename.


### Batch 0 — Foundation

Date: 2026-05-15  
PR: #1  
Commit: `32cd4f3`  
Scope: Added the four foundation files that make subsequent batches reviewable and idempotent.  
Files added:
  - `charter/HARD_RULES.md`
  - `charter/REPO_STRUCTURE.md` (rewritten version of the pre-existing root `REPO_STRUCTURE.md`; the stale root copy was inadvertently left behind and is removed in Batch 2)
  - `operations/MIGRATION_PLAN.md`
  - `operations/MIGRATION_LOG.md`  

Files moved: none  
Files deleted: none  
Verification: PR #1 opened as draft; `mergeable_state: clean`; no review threads; 0 check runs (no workflows configured yet).  
Notes: First commit on the migration branch. Citations in `HARD_RULES.md` to `charter/...` and `operations/...` paths intentionally do not resolve until Batches 2 and 3 land. Batch 0 corrected by Batch 2: the original root `REPO_STRUCTURE.md` was not deleted when the rewritten copy was added at `charter/REPO_STRUCTURE.md`; the duplicate is removed in Batch 2.

### Batch 1 — Stub READMEs for new top-level buckets

Date: 2026-05-15  
PR: #1  
Commit: `e877e38`  
Scope: Added README files to the new top-level buckets so they exist in git and explain their purpose to anyone landing there.  
Files added:
  - `charter/README.md`
  - `operations/README.md`
  - `curriculum/README.md`
  - `cockpit/README.md`
  - `decks/README.md`  

Files modified:
  - `operations/MIGRATION_LOG.md` (this entry)

Files moved: none  
Files deleted: none  
Verification: Five new files, none overwriting existing content. `capabilities/README.md` deliberately NOT touched — the directory already exists with nine capability cards indexed (`dashboard-insight-design`, `data-cleaning`, `exploratory-analysis`, `model-evaluation`, `optimisation-modelling`, `project-transfer`, `recommendation-scoring`, `research-synthesis`, plus the existing README). It will be updated in Batch 5 when `patterns/`, `anti-patterns/`, `case-studies/`, `decision-science/` land underneath it.  
Notes: `curriculum/`, `cockpit/`, `decks/` are entirely new directories created by this commit. `charter/` and `operations/` already existed from Batch 0; their READMEs document the bucket's purpose for anyone landing there.

### Batch 2 — Move charter docs

Date: 2026-05-15  
PR: #1  
Commit: `37add23`  
Scope: Moved 13 policy docs from the repository root into `charter/`, where the bucket README declares them to live.  
Files moved (via `git mv`, rename detection: yes):
  - `BUDGET.md` → `charter/BUDGET.md`
  - `CODEMIKE.md` → `charter/CODEMIKE.md`
  - `DATA_POLICY.md` → `charter/DATA_POLICY.md`
  - `DOCTRINES.md` → `charter/DOCTRINES.md`
  - `DOMAIN_MAP.md` → `charter/DOMAIN_MAP.md`
  - `GITHUB_WORKFLOW.md` → `charter/GITHUB_WORKFLOW.md`
  - `HTML_ARTIFACTS.md` → `charter/HTML_ARTIFACTS.md`
  - `PRODUCTISATION.md` → `charter/PRODUCTISATION.md`
  - `QA_CHECKLIST.md` → `charter/QA_CHECKLIST.md`
  - `RESPONSIBLE_AI.md` → `charter/RESPONSIBLE_AI.md`
  - `STUDENT_LIFE.md` → `charter/STUDENT_LIFE.md`
  - `SUPERVISION.md` → `charter/SUPERVISION.md`
  - `TOOLING.md` → `charter/TOOLING.md`

Files modified:
  - `charter/README.md` — rewritten with the post-Batch-2 contents table.
  - `operations/MIGRATION_LOG.md` — backfilled Batch 1's commit SHA (`e877e38`); appended this entry.

Files added: none  
Files deleted:
  - `REPO_STRUCTURE.md` (root) — stale pre-rewrite duplicate of `charter/REPO_STRUCTURE.md`; left behind by Batch 0. Diff before deletion: 112 lines (root) vs 114 lines (charter); root version used the pre-migration framing without the cross-links to `operations/MIGRATION_PLAN.md`. Removing the root copy makes `charter/REPO_STRUCTURE.md` the single source of truth.

Verification: No content changes to the 13 moved files — moves only. `git status --short` shows 13 `R` (rename) entries, 1 `D` (delete) entry, plus 2 `M` (modified) entries for `charter/README.md` and this log file. Root `.md` count before Batch 2: 32 (31 original + `REPO_STRUCTURE.md` carried over). After Batch 2: 18 (`CLAUDE.md`, `README.md`, and 16 operations docs awaiting Batch 3). After Batch 3 it drops to 2 — the target.  
Notes: Tracked internal links from `CLAUDE.md` and from the moved files themselves (e.g. references like `[BUDGET.md](BUDGET.md)`) will break until Batch 9 (internal link sweep). This is intentional and documented in `MIGRATION_PLAN.md`. `CLAUDE.md` stays at root per `REPO_STRUCTURE.md` (root inventory) and is rewritten in Batch 9.

### Batch 3 — Move operations docs

Date: 2026-05-15  
PR: #1  
Commit: `61f92d1`  
Scope: Moved 16 register/log docs from the repository root into `operations/`, completing the root cleanup that brings root `.md` count to its target of 2 (`CLAUDE.md`, `README.md`).  
Files moved (via `git mv`, rename detection: 100% similarity on all 16):
  - `ARTIFACT_INDEX.md` → `operations/ARTIFACT_INDEX.md`
  - `CAPABILITIES.md` → `operations/CAPABILITIES.md`
  - `DATASETS.md` → `operations/DATASETS.md`
  - `DECISIONS.md` → `operations/DECISIONS.md`
  - `EVIDENCE.md` → `operations/EVIDENCE.md`
  - `EXPERIMENTS.md` → `operations/EXPERIMENTS.md`
  - `FAILURE_LOG.md` → `operations/FAILURE_LOG.md`
  - `LIBRARY.md` → `operations/LIBRARY.md`
  - `NEXT_ACTIONS.md` → `operations/NEXT_ACTIONS.md`
  - `PORTFOLIO.md` → `operations/PORTFOLIO.md`
  - `PROJECT_LOG.md` → `operations/PROJECT_LOG.md`
  - `RISK_REGISTER.md` → `operations/RISK_REGISTER.md`
  - `ROADMAP.md` → `operations/ROADMAP.md`
  - `SKILL_MAP.md` → `operations/SKILL_MAP.md`
  - `TRANSFER_LOG.md` → `operations/TRANSFER_LOG.md`
  - `VIVA.md` → `operations/VIVA.md`

Files modified:
  - `operations/README.md` — rewritten with the post-Batch-3 contents table.
  - `operations/MIGRATION_LOG.md` — backfilled Batch 2's commit SHA (`37add23`); appended this entry.

Files added: none  
Files deleted: none  
Verification: No content changes to the 16 moved files. Root `.md` count: 18 → 2 (`CLAUDE.md`, `README.md`) — matches the target inventory in `MIGRATION_PLAN.md`. `git status --short` shows 16 `R` entries plus 2 `M` entries for the README and this log file.  
Notes: Internal references from `CLAUDE.md` to `SKILL_MAP.md`, `PROJECT_LOG.md`, `TRANSFER_LOG.md`, `CAPABILITIES.md`, `BUDGET.md`, `TOOLING.md`, etc., now all break (the previous referenced root locations no longer exist). All such links are fixed in Batch 9 (internal link sweep). The remaining 14 root directories move in Batches 4-6.

### Batch 4 — Curriculum merge

Date: 2026-05-15  
PR: #1  
Commit: `49d95e2`  
Scope: Moved four root directories — `assignments/`, `courses/`, `modules/`, `thesis/` — into `curriculum/`, giving academic work a single parent.  
Directories moved (via `git mv`, 33 file renames in total, all 100% similarity):
  - `assignments/` → `curriculum/assignments/` (3 entries: 1 brief, 1 README, `rubrics/`)
  - `courses/` → `curriculum/courses/` (`des-001-design-foundations/` plus README)
  - `modules/` → `curriculum/modules/` (10 numbered module dirs: `00-foundations` … `09-capstone`)
  - `thesis/` → `curriculum/thesis/` (README only at present)

Files modified:
  - `curriculum/README.md` — rewritten with the post-Batch-4 contents table.
  - `operations/MIGRATION_LOG.md` — backfilled Batch 3's commit SHA (`61f92d1`); appended this entry.

Files added: none  
Files deleted: none  
Verification: No content changes to the 33 moved files. Root directory count: 24 → 20 (assignments, courses, modules, thesis no longer at root).  
Notes: Discovered an unplanned root directory during this batch — `artifacts/` (containing `artifacts/html/destination-browser-v1.html` + README). It is not in the `MIGRATION_PLAN.md` directory table. A plan revision will follow before Batch 6, targeting `artifacts/` → `operations/artifacts/` (operational evidence outputs, governed by `charter/HTML_ARTIFACTS.md` and indexed by `operations/ARTIFACT_INDEX.md`). `artifacts/` is not touched in Batch 4. Cross-references in moved files to root-level filenames (e.g. links to `PROJECT_LOG.md`) remain broken until Batch 9.

### Batch 5 — Capability consolidation

Date: 2026-05-15  
PR: #1  
Commit: `2f9d0ff`  
Scope: Moved four root directories — `anti-patterns/`, `case-studies/`, `decision-science/`, `patterns/` — into `capabilities/`, putting reusable-knowledge sub-buckets under their parent.  
Directories moved (via `git mv`, 12 file renames in total, all 100% similarity):
  - `anti-patterns/` → `capabilities/anti-patterns/` (1 README; populated as anti-patterns are documented)
  - `case-studies/` → `capabilities/case-studies/` (1 README; populated as case studies are written)
  - `decision-science/` → `capabilities/decision-science/` (1 README; populated as decision-science methods land)
  - `patterns/` → `capabilities/patterns/` (1 README + 8 pattern files)

Files modified:
  - `capabilities/README.md` — added a "Layout" section showing the new sub-buckets; refreshed the cross-bucket reference paths in the "Maturity Rule" section from bare filenames (`EVIDENCE.md`) to the post-migration paths (`../operations/EVIDENCE.md`). Original capability-card table preserved unchanged.
  - `operations/MIGRATION_LOG.md` — backfilled Batch 4's commit SHA (`49d95e2`); appended this entry.

Files added: none  
Files deleted: none  
Verification: No content changes to the 12 moved files. Pattern links in the existing `capabilities/README.md` table (e.g. `patterns/data-cleaning-checklist.md`) — broken before this batch because `/patterns/` was a root sibling, not a child of `capabilities/` — now resolve correctly. Root directory count: 20 → 16.  
Notes: The pre-Batch-5 README was authored expecting `patterns/` to already live inside `capabilities/`; the original repo had it at root, so those links were broken before any migration ran. This batch makes the README correct. Cross-bucket references to `../operations/...` files are written assuming Batches 2-3 (operations moves) have already landed.

### Batch 6 — Trackers, benchmarks, orientation, synthetic-data, artifacts

Date: 2026-05-15  
PR: #1  
Commit: `19cf2f1`  
Scope: Moved the remaining four planned root directories plus the `artifacts/` directory added by the preceding plan revision (`82596a7`). Post-Batch-6 root holds 15 directories — the target inventory minus `.github/`, which Batches 7-8 add.  
Directories moved (via `git mv`, all 100% similarity):
  - `trackers/` → `operations/trackers/`
  - `benchmarks/` → `operations/benchmarks/`
  - `orientation/` → `charter/orientation/` (13 files, the student-life policy bucket)
  - `artifacts/` → `operations/artifacts/` (1 subdir + 1 HTML artifact)

Merge — `synthetic-data/` → `datasets/synthetic/`:
  - Source `synthetic-data/trip_options_generator.py` moved into `datasets/synthetic/` alongside the existing `trip_options_sample.csv`.
  - Source `synthetic-data/README.md` removed; its useful content (generator purpose, candidate list) merged into `datasets/synthetic/README.md`. The generator reference path was corrected from `synthetic-data/trip_options_generator.py` to `trip_options_generator.py` (now a sibling), and `DATASETS.md` reference was rewritten to `../../operations/DATASETS.md`.
  - The `synthetic-data/` directory is removed (git does not track empty directories).

Files modified:
  - `datasets/synthetic/README.md` — merged in the deleted README's content, fixed generator and `DATASETS.md` paths.
  - `operations/MIGRATION_LOG.md` — backfilled Batch 5's commit SHA (`2f9d0ff`); backfilled the Batch-6 plan revision's commit SHA (`82596a7`); appended this entry.

Files added: none  
Files deleted:
  - `synthetic-data/README.md` — content merged into `datasets/synthetic/README.md`.

Verification: Root directory inventory after Batch 6: `capabilities/`, `charter/`, `cockpit/`, `curriculum/`, `datasets/`, `decks/`, `design/`, `docs/`, `notebooks/`, `operations/`, `projects/`, `prompts/`, `references/`, `reports/`, `src/`. That is 15 directories — exactly the post-migration target minus `.github/`, which is created by Batches 7-8.  
Notes: With `orientation/` now living at `charter/orientation/`, any reference in `STUDENT_LIFE.md` (now `charter/STUDENT_LIFE.md`) or in `CLAUDE.md` to `orientation/` as a root sibling is broken — caught by Batch 9. Internal references inside `orientation/` documents to root-level filenames remain broken until Batch 9 as well.

### Batch 7 — Cockpit PWA scaffold

Date: 2026-05-15  
PR: #1  
Commit: `ff38e96`  
Scope: Scaffolded the CodeMike Cockpit — a dependency-free PWA whose views fetch markdown from `operations/` at runtime and render it as escaped preformatted text, honouring HR-MSc-9 ("no academic claim hardcoded in cockpit HTML").  
Files added:
  - `cockpit/index.html` — landing page; lists views; registers the service worker.
  - `cockpit/views/skill-map.html` — reference view; fetches `../../operations/SKILL_MAP.md` via `data-source`.
  - `cockpit/assets/cockpit.css` — design tokens (cm-bg, cm-surface, cm-text, cm-accent, cm-rule) + minimal layout (max-width 70ch, sans-system stack).
  - `cockpit/assets/cockpit.js` — fetch + HTML-escape helpers; no markdown parser. Reads `data-source` on `[data-source].cm-view` elements, fetches with `cache: 'no-cache'`, escapes the body, wraps in `<pre>`.
  - `cockpit/manifest.webmanifest` — PWA manifest (theme `#0f172a`, standalone).
  - `cockpit/sw.js` — service worker; shell cached on install (`cockpit-shell-v1`), network-first for everything else so operations data is always fresh.
  - `.github/workflows/cockpit-build.yml` — Pages deploy workflow. Trigger: pushes to `main` touching `cockpit/**`, `operations/**`, `datasets/**`. Stages the cockpit, a curated subset of operations files (`SKILL_MAP.md`, `PROJECT_LOG.md`, `NEXT_ACTIONS.md`, `ROADMAP.md`, `CAPABILITIES.md`), and `datasets/synthetic/` into `_site/`, then deploys via `actions/deploy-pages@v4`.

Files modified:
  - `cockpit/README.md` — rewritten with the post-Batch-7 layout, view contract, deploy model, and dependency-free rationale.
  - `operations/MIGRATION_LOG.md` — backfilled Batch 6's commit SHA (`19cf2f1`); appended this entry.

Files moved: none  
Files deleted: none  
Verification: Cockpit served locally from the repo root via `python -m http.server` resolves `http://localhost:8000/cockpit/`, the skill-map view fetches `../../operations/SKILL_MAP.md` and renders the file contents. Workflow file lints (yaml structure verified in commit); first deployment will occur when this branch merges to `main` and triggers `cockpit-build`. New root directory: `.github/`.  
Notes: No view duplicates any content from the source markdown. The choice to render as `<pre>` rather than parsed markdown is deliberate — it keeps the contract honest ("what you see is what the file says") and avoids a runtime dependency. A future view can add per-view parsing helpers if needed.

### Batch 8 — Deck pipeline scaffold

Date: 2026-05-15  
PR: #1  
Commit: `1bd74aa` (with fixup `4739f14` adding `.gitignore` and untracking a stray `.pyc`)  
Scope: Scaffolded the deck pipeline. Decks are reveal.js HTML with the same fetch-at-runtime contract as cockpit views; a workflow renders every `decks/**/slides.html` to `.pptx` via headless Chromium + python-pptx and uploads the bundle as a workflow artifact.  
Files added:
  - `decks/shared/reveal-theme.css` — reveal.js theme using the same design tokens as `cockpit/assets/cockpit.css` (cm-bg, cm-surface, cm-text, cm-accent, cm-rule). A deck looks like the same product as the cockpit.
  - `decks/shared/deck-data-fetch.js` — hydrates `<section data-source="…">` slides with the fetched markdown, escaped, into a sibling `<pre class="cm-source-content">`. Hooked into `Reveal.on('ready')` when available, falls back to `DOMContentLoaded`.
  - `decks/curriculum/00-foundations/slides.html` — sample deck. Loads reveal.js v5 from jsdelivr, applies `shared/reveal-theme.css`, three data-bearing slides fetching `operations/SKILL_MAP.md`, `operations/ROADMAP.md`, `operations/NEXT_ACTIONS.md`.
  - `decks/curriculum/00-foundations/notes.md` — speaker notes for the sample deck. Walks slide-by-slide and explains how to add a new data slide.
  - `decks/curriculum/00-foundations/README.md` — deck charter: intent, audience, evidence links, how to run (HTML + .pptx).
  - `.github/scripts/export_decks.py` — Python exporter. Serves the repo via `http.server` on a free port, walks `decks/**/slides.html`, navigates each slide via `Reveal.slide(i)`, screenshots at 1920×1080, assembles a `.pptx` per deck (one full-bleed image per slide). Attaches `notes.md` (if present) to the first slide's notes.
  - `.github/workflows/decks-export.yml` — workflow. Triggers: push to `main` touching `decks/`, `operations/`, the workflow, or the script. Installs Playwright + python-pptx + Chromium, runs `export_decks.py`, uploads `build/*.pptx` as the `decks-pptx` artifact. Output not committed.

Files modified:
  - `decks/README.md` — rewritten with the post-Batch-8 layout, deck contract, export model, and local-run instructions.
  - `operations/MIGRATION_LOG.md` — backfilled Batch 7's commit SHA (`ff38e96`); appended this entry.

Files moved: none  
Files deleted: none  
Verification: `python -m py_compile .github/scripts/export_decks.py` succeeds (verified locally before commit — see commit notes). Sample deck served locally via `python -m http.server` resolves at `http://localhost:8000/decks/curriculum/00-foundations/slides.html`, reveal.js initialises, and the three data slides populate from `operations/`. The workflow's first execution will occur when this branch merges to `main`.  
Notes: The deck pipeline's "no .pptx in the repo" stance is intentional — the HTML is the source of truth, the .pptx is a transport artifact. The same fetch contract used in `cockpit/` and `decks/` means a future "what does the workspace currently say?" view in either channel renders the same thing.

### Batch 9 — Internal link sweep

Date: 2026-05-15  
PR: #1  
Commit: (pending — last commit in the migration)  
Scope: Final batch. Updated cross-bucket references in `CLAUDE.md` and `README.md` to point at the post-migration locations, and added a reproducible link-sweep script for future migrations. Verified that no Markdown link targets `](FILE.md)` to moved bare-filename docs remain anywhere in the tree.  
Files added:
  - `.github/scripts/link_sweep.py` — reproducible link-sweep. Walks every `.md` file (excluding `MIGRATION_LOG.md`, `MIGRATION_PLAN.md`, and itself), parses Markdown inline-link `](target)` and reference-style `[id]: target` definitions, and rewrites targets that match moved files or moved root directories using `os.path.relpath` from the file containing the link. Idempotent; preserves anchors and query strings.

Files modified:
  - `CLAUDE.md` — prose references rewritten from bare filenames to the post-migration paths:
    - `SKILL_MAP.md` → `operations/SKILL_MAP.md` (3 occurrences)
    - `PROJECT_LOG.md` → `operations/PROJECT_LOG.md` (2 occurrences)
    - `STUDENT_LIFE.md` → `charter/STUDENT_LIFE.md`
    - `orientation/` → `charter/orientation/`
    - `TRANSFER_LOG.md` → `operations/TRANSFER_LOG.md` (2 occurrences)
    - `BUDGET.md` → `charter/BUDGET.md` (2 occurrences)
    - `TOOLING.md` → `charter/TOOLING.md` (2 occurrences)
    - `CAPABILITIES.md` → `operations/CAPABILITIES.md` (2 occurrences)
    - `ROADMAP.md` → `operations/ROADMAP.md`
  - `README.md` — "Primary locations" table rewritten to reflect the post-migration top-level inventory (`charter/`, `operations/`, `capabilities/`, `curriculum/courses/`, `curriculum/assignments/`, `curriculum/modules/`, `curriculum/thesis/`, `cockpit/`, `decks/`, etc.). DES-001 course-folder path updated to `curriculum/courses/des-001-design-foundations/`. Cockpit row added to the Active Artifacts table. Reference to `GITHUB_WORKFLOW.md` updated to `charter/GITHUB_WORKFLOW.md`.
  - `operations/MIGRATION_LOG.md` — backfilled Batch 8's commit SHA (`1bd74aa`) and the follow-up fixup SHA (`4739f14`); appended this entry.

Files moved: none  
Files deleted: none  
Verification: `python3 .github/scripts/link_sweep.py` reports `0 file(s) changed, 0 link(s) rewritten` — confirming no broken Markdown link targets remain. Spot-checks of `grep -rIn --include="*.md" -E '\]\((BUDGET|...|VIVA)\.md'` and `\]\((anti-patterns|...|trackers)/'` return only matches inside `operations/MIGRATION_LOG.md` (intentional historical citations) and `link_sweep.py` itself (the script's regex).  
Notes: The migration plan and its "internal link sweep" Batch 9 commitment proved larger in label than in scope — most cross-references in the original repo were prose backtick mentions (`` `SKILL_MAP.md` ``) rather than Markdown hyperlinks. The script catches the hyperlink case; the prose case was handled file-by-file in `CLAUDE.md` and `README.md`. Moved docs (under `charter/`, `operations/`, etc.) that reference other moved docs as siblings did not need rewriting since their relative positions are preserved.

---

End of migration. Root state matches `MIGRATION_PLAN.md` target: 2 `.md` files (`CLAUDE.md`, `README.md`) and 16 directories including `.github/` (`capabilities/`, `charter/`, `cockpit/`, `curriculum/`, `datasets/`, `decks/`, `design/`, `docs/`, `notebooks/`, `operations/`, `projects/`, `prompts/`, `references/`, `reports/`, `src/`, `.github/`).
