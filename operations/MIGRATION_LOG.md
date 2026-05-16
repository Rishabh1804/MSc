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

## Register

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
Commit: (pending — backfilled next batch)  
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
