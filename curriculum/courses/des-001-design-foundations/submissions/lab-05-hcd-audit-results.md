# Lab 05 — Submission

Lab brief: `curriculum/courses/des-001-design-foundations/labs/lab-05-hcd-audit.md`
Source topic: `design/foundations/topic-05-hcd.md`
Audit output: `design/foundations/topic-05-hcd-audit.md`
Target artifacts: Destination Master Browser v1.1 (post-PR #12) + Lab 04 Loop 1

## Executive summary

Lab 05 ran a full HCD audit against v1.1 + Lab 04 Loop 1, evaluating the workspace against ISO 9241-210's four activities, six principles, and the W3C accessibility/usability/inclusion triad. The audit produced evidence per activity, a Pass/Partial/Fail verdict per principle, lens-by-lens W3C findings, and a six-item prioritised v1.2 HCD list.

**Overall verdict**: v1.1 is *HCD-substantial but incomplete*. The audit-shape is intact; machine-grade discipline is strong. The single outright **Fail** (Principle 2: Users involved throughout) and the four **High**-severity findings (systems-context-of-use under-documented; inclusion-lens requirements absent; human-grade evaluation absent; inclusion lens fails five sub-dimensions) are all closable in v1.2 with Sponsor Reviewer recruitment plus four targeted specification efforts.

## Steps executed

| Step | Output | File / section |
|---|---|---|
| 1 — Context of use | Three-persona context-of-use table + systems-level context-of-use table (4 layers) | Audit doc §Step 1 |
| 2 — User requirements | Documented requirements table (15 rows) + gap analysis (2 findings) | Audit doc §Step 2 |
| 3 — Design solutions | Solutions table (12 rows) with chosen-vs-defaulted column | Audit doc §Step 3 |
| 4 — Evaluation | Evaluation evidence table (6 rows) + human-grade gap analysis | Audit doc §Step 4 |
| 5 — Six-principle audit | Per-principle verdict with evidence + mitigation (2 Pass, 3 Partial, 1 Fail) | Audit doc §Step 5 |
| 6 — W3C triad audit | Per-lens verdict (1 Pass, 1 Partial, 1 Fail) with sub-dimension findings | Audit doc §Step 6 |
| 7 — Findings + prioritised list | 7 findings; 6-item prioritised v1.2 HCD list | Audit doc §Step 7 |

## Key findings

### Activity-level findings

- **F-CTX-1 (High)**: Systems-level context-of-use under-documented. Norman's *HCD Considered Harmful?* critique applies — v1.1 centred the individual reviewer; the downstream Planner consumer and lateral handoff layers are not yet designed objects.
- **F-REQ-1 (Medium)**: Lab 04 §8 U-CONF-1..4 acceptance criteria are described in prose but not landed in `ux-acceptance-criteria.md`. The v1.2 implementation PR will need to either re-derive them or discover they're missing.
- **F-REQ-2 (High)**: Inclusion-lens user requirements entirely absent from the canonical criteria sheet. Five sub-dimensions (language, bandwidth, device, cultural context, terminology) each need at least one explicit requirement.
- **F-EVAL-1 (High)**: Human-grade evaluation is absent. Only the machine-grade 19-gate Playwright walkthrough exists. No real reviewer has used v1.1. This is the largest single HCD gap.
- **F-EVAL-2 (Medium)**: v1.1 has no heuristic-grade evaluation that uses the post-Topics-2-5 discipline. Topic 1's Lab 01 audit was of v1; the walkthrough is machine-grade only.

### Principle-level finding

- **F-PRIN-1 (High)**: Principle 2 (Users involved throughout) is the only outright Fail. Closure requires Sponsor Reviewer recruitment in v1.2 — not just a polish item, a prerequisite.

### W3C-lens finding

- **F-W3C-1 (High)**: Inclusion lens fails on five sub-dimensions. v1.1 works for an English-speaking desktop reviewer with prior context; it fails for any reviewer outside that profile.

### Strengths

- **Audit-shape is intact**: every major artifact maps to at least one ISO activity. The discipline of naming what each artifact serves is visible across the workspace.
- **Seven-step journey + four-depth trust signal + 14 acceptance criteria** satisfy Activities 1–2 at the per-persona level and the usability + accessibility lenses.
- **Topic 4 Loop 1 is HCD-compliant**: every loop stage produced an artifact; the three-persona synthesis satisfies the explicit-understanding principle's solo translation.
- **Iteration is structural** by construction (PR cadence + design-thinking loop).
- **Honest naming of limitations** runs through the workspace.

## Prioritised v1.2 HCD list

| # | Action | Closes |
|---:|---|---|
| 1 | Recruit at least one Sponsor Reviewer | F-EVAL-1, F-PRIN-1, partially F-EVAL-2 |
| 2 | Land U-CONF-1..4 in `ux-acceptance-criteria.md` | F-REQ-1 |
| 3 | Produce systems-context-of-use document | F-CTX-1 |
| 4 | Specify inclusion-lens requirements (≥ 1 per sub-dimension) | F-REQ-2, F-W3C-1 |
| 5 | Include screen-reader test in Sponsor Reviewer recruitment | Accessibility lens partial → pass |
| 6 | Re-audit v1.1 at heuristic-grade with post-Topics-2-5 discipline | F-EVAL-2 |

Items 1, 2, 3, 4 close the high-severity findings. Bundleable with the v1.2 implementation work.

## Repository outputs

| Output | Path | Status |
|---|---|---|
| Full HCD audit (Steps 1–7 evidence) | `design/foundations/topic-05-hcd-audit.md` | Complete |
| Lab submission (this file) | `submissions/lab-05-hcd-audit-results.md` | Complete |
| Master-browser checklist Topic 5 gates + anti-patterns + canonical pointer | `design/checklists/master-browser-design-checklist.md` §26 + §27 + §28 | Complete |

## Submission checklist (per the lab brief)

- [x] All four ISO activities audited with evidence (Steps 1–4)
- [x] All six ISO principles graded Pass/Partial/Fail with evidence (Step 5)
- [x] All three W3C triad lenses applied to v1.1 (Step 6)
- [x] Prioritised v1.2 HCD findings list produced (Step 7)
- [x] Master-browser checklist Topic 5 section appended (Step 8)

## Decision-gate satisfaction (per the lab brief)

The brief's gate: *"All four ISO activities have evidence; all six principles are graded; all three W3C lenses have findings; the v1.2 HCD findings list is prioritised; each finding is tagged with the ISO activity it serves."*

All five conditions satisfied:

1. ✓ Activities 1–4 each have at least one piece of evidence
2. ✓ Six principles graded (2 Pass, 3 Partial, 1 Fail)
3. ✓ Three W3C lenses have explicit findings (1 Pass, 1 Partial, 1 Fail)
4. ✓ v1.2 HCD list prioritised (6 items, ordered by leverage)
5. ✓ Each of the 7 findings tagged with the ISO activity / principle / lens it serves

Decision-gate satisfied.

## What this lab produces beyond the rubric minimum

- A **systems-context-of-use specification format** as a reusable template
- An **HCD self-audit gate** that catches missing activities at the per-item level
- An **HCD-audit template** other workspaces can mirror
- A **prioritised list** ordered by leverage, not enumeration order — every item closes ≥ 1 high-severity finding

## Open work after Lab 05

- Start **Topic 6 (Gestalt principles)** — final topic in the ratified three-topic push
- **Grade report v3** lands after Topic 6 closure (covers cumulative DES-001 grade after Topics 1–6, including Lab 05's HCD compliance verdict)
- v1.2 implementation begins with the six-item prioritised HCD list as inherited work alongside the existing v1.2 backlog

## Lab 05 status

**Complete.** Lab evidence is sufficient for Topic 5 to be marked Closed. PR B (this submission) closes Topic 5. After PR B merges, Topic 5 is fully closed and Topic 6 (Gestalt principles) begins.
