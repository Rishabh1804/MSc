# HARD_RULES.md — MSc Hard Rules

Twelve standing constraints that govern every change in this repository. They are distilled from `DOCTRINES.md`, `HTML_ARTIFACTS.md`, `CLAUDE.md`, `GITHUB_WORKFLOW.md`, `DATA_POLICY.md`, `RESPONSIBLE_AI.md`, and `QA_CHECKLIST.md`. Those longer source documents remain canonical for nuance and examples; this file is the short reference list a reviewer can hold in their head.

When a rule in this file and a source document disagree, the source document wins and this file should be updated.

## HR-MSc-1 — Charter before build

Make small, reviewable changes. Structural changes are logged in `operations/PROJECT_LOG.md`. New modules update `operations/ROADMAP.md`. Material drift requires an entry in `operations/DECISIONS.md`.

Source: `CLAUDE.md` — Governance Rules, Review Posture.

## HR-MSc-2 — Baseline before model

No ML model is built before a simple baseline exists. The baseline number sits in the experiment report it is compared against.

Source: `DOCTRINES.md` — Doctrine 1.

## HR-MSc-3 — Decision before dashboard

No dashboard is built before the decision it supports is named. A dashboard without a stated decision is decoration.

Source: `DOCTRINES.md` — Doctrine 2.

## HR-MSc-4 — Constraints before optimisation

No optimiser runs before its constraints are written plainly in the experiment or capability card.

Source: `DOCTRINES.md` — Doctrine 3.

## HR-MSc-5 — Evidence before confidence

No strong conclusion without data, experiment, source citation, or an explicitly stated assumption. Claims and evidence stay visibly separated in writing.

Source: `DOCTRINES.md` — Doctrine 4; `RESPONSIBLE_AI.md` — Output Rule.

## HR-MSc-6 — Transfer before reinvention

Before building a new method, check `capabilities/`, `capabilities/patterns/`, `capabilities/anti-patterns/`, and `operations/FAILURE_LOG.md`. Adapt what exists; only build new when nothing fits.

Source: `DOCTRINES.md` — Doctrine 5.

## HR-MSc-7 — Capability before tooling

Free and open-source tools are tried first. A paid tool is justified only when it beats the free option on learning, evidence, reproducibility, transfer, or project capability. Every approved spend leaves an artifact.

Source: `DOCTRINES.md` — Doctrines 6, 7, 8; `BUDGET.md`; `TOOLING.md`.

## HR-MSc-8 — Data classification before use

Every dataset is classified — Public, Synthetic, Internal, Confidential, Sensitive, or Restricted — before use. Synthetic is preferred for practice and prototypes. Sensitive or Restricted data requires explicit approval and documented controls. All datasets register in `operations/DATASETS.md`.

Source: `DATA_POLICY.md`.

## HR-MSc-9 — HTML is never source of truth

Source of truth is Markdown, CSV, JSON, and Python. HTML artifacts — browsers, dashboards, cockpit views, slide decks — are a presentation and review layer. HTML must fetch its content from data files at runtime; it must not hardcode academic claims, numbers, or registers inline.

Presentation HTML is allowed and expected. Slides live in `decks/` as HTML and are exported to `.pptx` by a workflow; the claims they render still come from `operations/*.json` or `datasets/*.csv`. Generated `.pptx` files are build artifacts, not committed source.

Source: `HTML_ARTIFACTS.md`.

## HR-MSc-10 — Decision support is not decision authority

CodeMike outputs assist analysis, scoring, prediction, and recommendation. High-impact decisions — health, finance, legal, employment, personal data, automated ranking or exclusion — require human review and accountability. The boundaries listed in `RESPONSIBLE_AI.md` apply.

Source: `RESPONSIBLE_AI.md` — Core Principle, Boundaries.

## HR-MSc-11 — One commit, one meaningful step

A commit represents a meaningful academic or project step, not a single file. Related changes batch into one commit. Risky changes — file moves, deletions, structural rewrites, large dashboard work — go on a branch with a draft PR.

Source: `GITHUB_WORKFLOW.md` — Standard workflow, Branch rule.

## HR-MSc-12 — No orphan artifacts

Every script, notebook, dataset, capability card, or note belongs to a module, project, experiment, or capability. Meaningful learning updates `operations/SKILL_MAP.md`. New reusable capabilities update `operations/CAPABILITIES.md`. Transfers update `operations/TRANSFER_LOG.md`.

Source: `CLAUDE.md` — Workspace Principles, Governance Rules.

## Rule numbering

The `HR-MSc-N` prefix is stable. New rules append; rules are never silently renumbered. A retired rule keeps its number with a `RETIRED:` note and a pointer to the replacement.
