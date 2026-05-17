# Topic 5 — HCD Audit (v1.1 + Lab 04 Loop 1)

Lab brief: `curriculum/courses/des-001-design-foundations/labs/lab-05-hcd-audit.md`
Source topic: `design/foundations/topic-05-hcd.md`
Audit number: **Audit 1** (the first formal HCD audit run against the workspace).
Date: 2026-05-17.
Subject: Destination Master Browser v1.1 (post-PR #12) + Lab 04 Loop 1 (batch-promote-confirm).

This audit grades the design work against ISO 9241-210's four activities + six principles + the W3C accessibility/usability/inclusion triad. Each cell cites a specific source artifact in the workspace. Cells that cannot cite an artifact are *findings*.

---

## Step 1 — Activity 1: Context of use

### Per-persona context-of-use

| Field | First-time reviewer | Power reviewer | Accessibility-need reviewer |
|---|---|---|---|
| **User** | A reviewer encountering the browser for the first time; given < 5 minutes of orientation | A reviewer who has used the browser regularly for weeks; has built a mental model of trust states and filter behaviour | A reviewer using assistive technology (screen reader: VoiceOver / NVDA / JAWS), keyboard-only navigation, or magnification |
| **Tasks** | Understand what the dataset is; learn the seven-step journey; complete a single record review | Promote N records to Planner per session; recover from over-filtering; switch view modes | Same tasks as power-reviewer but via keyboard + screen-reader + (where applicable) magnification |
| **Environment** | Desktop browser (Chromium-family); typical office network; English-language UI | Same environment; assumed familiarity with reviewer terminology ("Planner-ready", "verified", "candidate") | Same environment + assistive technology stack; may include screen-reader-only or screen-reader+magnification combinations |
| **Equipment** | Modern desktop with mouse + keyboard | Same | Same hardware + AT (NVDA on Windows / VoiceOver on macOS most common; refreshable braille uncommon but supported) |
| **Constraints** | Reviewer may abandon if orientation > 5min; cost asymmetric (wrong promotion >> friction); no upstream training | Speed matters; flow interruptions are costly; trust signals must survive at every depth | Accessibility regressions are non-negotiable; aria-* attributes must be authoritative; focus management must survive every interaction |

Evidence sources: Lab 04 §Step 2 (three-persona Empathize synthesis); Topic 3 §6 reviewer-journey user-need extraction; Topic 2 §6.2 trust-signal four-depth spec.

### Systems-level context-of-use (Norman's critique territory)

| Layer | What it is | Documented? |
|---|---|---|
| **Upstream** — Data-engineering pipeline | The 359-row `destinations_master_v2.csv` is produced by a validation + promotion pipeline (operations/trackers + datasets/reference). Reviewer doesn't see this layer but the trust states encode its outputs. | **Partial** — pipeline tracked in `datasets/reference/destinations_master_v2_schema.md` + the validation/promotion reports. Reviewer-facing browser doesn't reference upstream provenance per record beyond `source_layer` and `source_id`. |
| **Downstream** — Planner consumer | Records marked `planner_ready` are consumed downstream by the Planner tool (separate project). The reviewer's promotion decision affects what Planner sees. | **Fail** — no documentation in the workspace of what Planner does with promoted records, what failure modes Planner has when consuming bad data, or how the reviewer's promotion decision constrains Planner's behaviour. This is the systems-level gap Norman's critique anticipates. |
| **Lateral** — Other reviewers / handoff | Multi-reviewer coordination is implicit ("we have reviewers"); there is no documented handoff between reviewers or any provenance for who promoted what when. | **Fail** — no audit trail in v1.1. Multi-reviewer workflow is not designed yet. |
| **Regulatory / organisational** — Internal QA standards for the records | The `master_structurally_valid_not_planner_ready` validation report names the structural-validity bar but not the *editorial* standard reviewers apply. | **Partial** — structural validation documented; editorial standards implicit in reviewer training (which doesn't exist as documentation). |

### Activity 1 verdict

**Per-persona context: well-documented** (Lab 04 §2 + Topic 3 §6 cover the three personas with task / environment / constraint detail).

**Systems-level context: under-documented** (downstream Planner consumer is the largest gap; Norman's critique applies). The v1.1 work centred the reviewer as an individual; the system the reviewer is embedded in is not yet a designed object. **Finding F-CTX-1**: produce a systems-context-of-use document in v1.2 covering upstream + downstream + lateral + regulatory layers.

---

## Step 2 — Activity 2: User requirements

### Documented user requirements (per workspace evidence)

| Requirement | Form | W3C lens served | Source artifact |
|---|---|---|---|
| Reviewer orients within 5s; no scroll, no interaction (U-ARR-1) | Acceptance criterion | Usability | `ux-acceptance-criteria.md` §2 |
| Trust state persistent on scroll (U-ARR-2) | Acceptance criterion | Usability + Accessibility | `ux-acceptance-criteria.md` §2 |
| Trust state via text + colour + icon — never colour alone (U-UND-1) | Acceptance criterion + checklist gate | Accessibility | `ux-acceptance-criteria.md` §2; checklist §18 colour-plus-text rule |
| Filters reversible without leaving result list; ≤300ms feedback (U-NAR-1) | Acceptance criterion | Usability | `ux-acceptance-criteria.md` §2 |
| Filter controls visibly distinguish default vs applied (U-NAR-2) | Acceptance criterion | Usability + Accessibility | `ux-acceptance-criteria.md` §2 |
| Trust badge across the result list (U-NAR-3) | Acceptance criterion | Usability | `ux-acceptance-criteria.md` §2 |
| Sortable columns; comparison pass <60s (U-COM-1) | Acceptance criterion | Usability | `ux-acceptance-criteria.md` §2 |
| Card/table toggle; table default (U-COM-2) | Acceptance criterion | Usability | `ux-acceptance-criteria.md` §2 |
| Drawer ≤2 to open, 1 to close, scroll preserved (U-INS-1) | Acceptance criterion | Usability + Accessibility | `ux-acceptance-criteria.md` §2 |
| Trust banner persistent in drawer header (U-INS-2) | Acceptance criterion | Usability + Accessibility | `ux-acceptance-criteria.md` §2 |
| Prev/Next navigation in drawer (U-INS-3) | Acceptance criterion | Usability + Accessibility | `ux-acceptance-criteria.md` §2 |
| Recovery from empty state in ≤1 interaction (U-REC-1) | Acceptance criterion | Usability | `ux-acceptance-criteria.md` §2 |
| Empty / loading / error are distinct components (U-REC-2) | Acceptance criterion | Usability + Accessibility | `ux-acceptance-criteria.md` §2 |
| Trust signal consistent across the journey (U-LEA-1) | Acceptance criterion | Usability + Accessibility | `ux-acceptance-criteria.md` §2 |
| Container-selection rules + state coverage + affordance/signifier/feedback (P-* via rule sheet) | Component-level requirements | Usability + Accessibility | `ui-design-component-rules.md` |
| Future v1.2: U-CONF-1..4 (batch-promote-confirm modal) | Acceptance criterion (specified in Lab 04 §8; not yet in canonical sheet) | Usability + Accessibility | Lab 04 §Step 8 — **finding**: not yet landed in `ux-acceptance-criteria.md` |

### Gap analysis

**Implicit requirements not explicitly captured:**

- **Inclusion**: no requirements addressing multi-language UI, low-bandwidth contexts, non-Western reviewer contexts, mobile-as-primary use case. All inclusion-lens requirements are absent from the canonical criteria sheet.
- **Systems-level**: no requirements covering reviewer-to-reviewer handoff, audit trail for promotion decisions, or downstream Planner-consumer contract.
- **Power-reviewer flow**: implicit in Lab 04 ("modal must work for any-N") but no canonical criterion captures the "session efficiency for power users" need.

**Finding F-REQ-1**: Lab 04 §8 U-CONF-1..4 acceptance criteria are described in prose but not landed in `ux-acceptance-criteria.md`. The v1.2 implementation PR will need to either (a) re-derive them or (b) discover they were never properly landed. **Recommend**: add the four criteria to `ux-acceptance-criteria.md` §2 as a deferred-v1.2 block alongside the existing U-INS-3 deferred row.

**Finding F-REQ-2**: Inclusion-lens requirements are entirely absent. **Recommend**: add a v1.2 backlog item to specify at least one requirement per inclusion sub-dimension (language, bandwidth, device, cultural context).

### Activity 2 verdict

**Usability + Accessibility requirements: well-documented** (14 criteria covering the seven-step journey, each behavioural + testable + mechanism-independent).

**Inclusion requirements: under-documented** (entirely absent from the canonical sheet). **Finding F-REQ-2 above.**

**Lab 04 follow-through: incomplete** (U-CONF-1..4 in prose only, not in sheet). **Finding F-REQ-1 above.**

---

## Step 3 — Activity 3: Design solutions

### Documented design solutions (per workspace evidence)

| Solution | Satisfies requirement(s) | Topic 4 loop produced it? | Chosen or defaulted? |
|---|---|---|---|
| Sticky trust banner (top-of-page) | U-ARR-1, U-ARR-2, U-UND-1, U-LEA-1 | No (predates Lab 04) | Chosen (Topic 2 §6.2 + Topic 3) |
| Trust badge component (7 states; used at top banner + list row + card top-right + drawer header) | U-NAR-3, U-INS-2, U-LEA-1 | No | Chosen (Topic 2 §7) |
| Toolbar with search + 5 selects + accent-dot indicator on non-default | U-NAR-1, U-NAR-2 | No | Chosen (Topic 2 §4 + §8) |
| Active-filter summary chip-row + Clear-all + result count | U-NAR-1, U-REC-1 | No | Chosen (Topic 2 §8) |
| Table view (default) with sortable columns + sticky header | U-COM-1, U-COM-2 | No | Chosen (Topic 2 §3.2 + §8) |
| Cards view (secondary; toggle) | U-COM-2 | No | Carried forward from v1 + Topic 2 §3.1 rules |
| Record-detail drawer (non-modal side panel) | U-INS-1, U-INS-2, U-INS-3 | No | Chosen (Topic 2 §3.4 + HIG/Carbon majority position) |
| Distinct skeleton (loading) / content-rich empty / inline-error components | U-REC-2 | No | Chosen (Topic 2 §6 anti-pattern 5/6 + §8) |
| Focus restoration on drawer close | (polish item) | No | Chosen (PR #12 polish) |
| Result-count flash animation on filter change | U-NAR-1 perceptibility | No | Chosen (PR #12 polish) |
| Taxonomy-drift `console.warn` for unmapped trust states | (defensive engineering) | No | Chosen (PR #12 polish) |
| **Future v1.2**: Batch-promote-with-confirm modal (Candidate B) | U-CONF-1..4 (deferred) | **Yes** — Lab 04 Loop 1 | Chosen via three-constraint triage |

### Activity 3 verdict

**Design solutions: well-documented** (every major solution maps to ≥ 1 user requirement; most solutions cite the source artifact that constrained them).

The "Chosen vs Defaulted" column shows most solutions were **chosen** rather than defaulted — that's the discipline Topic 4 introduces (the three-constraint triage forces explicit choice). The exception is the cards view, which is *carried forward from v1* rather than chosen for v1.1 — defensible because v1.1 was a transformation of v1, not a greenfield design.

No findings at the activity level; all major solutions trace to requirements.

---

## Step 4 — Activity 4: Evaluation

### Evaluation evidence in the workspace

| Evaluation | Type | What it verifies | Limitation |
|---|---|---|---|
| 19-gate Playwright walkthrough | Machine-grade | All 14 v1.1 UX acceptance criteria + U-INS-3 + 4 polish behavioural tests + CONSOLE meta-check | No human user has run this; verifies the *implementation matches the criteria*, not that the *criteria are right for real users* |
| Topic 2 component inventory + state matrix + affordance audit (Lab 02) | Heuristic-grade | v1's component coverage and state gaps | Audit of v1, not v1.1; superseded by walkthrough for v1.1 |
| Topic 1 Lab 01 heuristic audit (Nielsen + UX Honeycomb) | Heuristic-grade | v1's general usability + UX quality | Audit of v1, not v1.1; superseded by Topic 3 acceptance criteria |
| Topic 3 Lab 03 journey map + acceptance criteria | Specification-grade | v1.1 design *intentions*; what success looks like | Pre-implementation; specifies what to test against |
| Topic 4 Lab 04 falsification criteria (Step 7) | Specification-grade | What would change our mind about Candidate B (batch-promote-confirm modal) | Specification only; not run with real users |
| Defect-found-and-fixed in PRs (sticky-thead, [hidden] specificity, U-NAR-2 test logic) | Diagnostic | Cases where the test caught implementation or test bugs | Suggests the walkthrough has bite, but no real-user signal |

### Gap analysis: what *human-grade* evaluation exists?

**None.** No real reviewer has used v1.1; no Sponsor Reviewer has been recruited; the falsification criteria from Lab 04 §7 are *specifications*, not *results*.

**Finding F-EVAL-1**: human-grade evaluation is the largest single gap in the HCD audit. Closure requires recruiting at least one Sponsor Reviewer in v1.2 and running a test against the six Lab 04 falsification criteria + the 13 v1.1 UX gates.

**Finding F-EVAL-2**: evaluation evidence from Topic 1/2 audits is of *v1*, not *v1.1*. The walkthrough is the v1.1-specific evaluation, but it's machine-grade only. No artifact in the workspace re-audits v1.1 at the heuristic level *with the design discipline updates Topics 2–5 introduced*. **Recommend**: a v1.2 Sponsor Reviewer session can serve double duty — verifying acceptance criteria *and* providing heuristic-grade observations the walkthrough can't.

### Activity 4 verdict

**Machine-grade evaluation: strong** (the 19-gate walkthrough is reproducible, behavioural, and runs in seconds).

**Human-grade evaluation: absent.** Largest single HCD gap. Closure: Sponsor Reviewer in v1.2.

---

## Step 5 — Six-principle audit

| # | Principle | Verdict | Evidence + mitigation |
|---:|---|:---:|---|
| 1 | Explicit understanding of users, tasks, environments | **Partial** | Three-persona synthesis (Lab 04 §2) + Topic 3 §6 user-need extraction document understanding at the persona level. Limitation: no real users have been involved; understanding is designer-synthesised. **Honest naming + Sponsor Reviewer recruitment in v1.2** closes the principle. |
| 2 | Users involved throughout design and development | **Fail** | No real users have been involved in any v1.1 phase. The three-persona synthesis is a substitute, not a satisfaction. **Honest naming + Sponsor Reviewer recruitment in v1.2** is the only closure path. |
| 3 | Design driven and refined by user-centred evaluation | **Partial** | Machine-grade walkthrough satisfies the lower bound; Topic 4's falsification criteria specify the user-grade evaluation; no real users have evaluated yet. **Sponsor Reviewer testing in v1.2** closes the principle. |
| 4 | Process is iterative | **Pass** | The PR cadence (PRs #3 → #15) is iterative by construction; Topic 4 explicitly introduces the design-thinking loop; Lab 04 names Loop 2 trigger conditions. |
| 5 | Design addresses the whole user experience | **Pass** | Topic 1 framing (UX is the whole journey, not just the screen) + seven-step journey + four-depth trust signal + per-journey-step acceptance criteria explicitly address the whole experience. |
| 6 | Multidisciplinary team includes skills + perspectives | **Partial** | Solo workspace; same person plays all roles. Mitigation via conscious multi-lens adoption (three-persona synthesis; Lyra + Aurelius + Cipher + CodeMike review modes). **Honest naming** is the only closure path in a solo context; principle is structurally constrained, not closeable until team-size grows. |

**Two principles Pass, three Partial, one Fail.** All three Partial + the Fail are closable by Sponsor Reviewer recruitment in v1.2 except Principle 6, which is structurally constrained by team size.

### Activity-5 verdict

**Principles 2 + 3 are the closure path for v1.2.** Principle 6 is honest-naming-only in solo workspace. **Finding F-PRIN-1**: Principle 2 (Users involved throughout) is the only outright Fail; recruitment of Sponsor Reviewer becomes a v1.2 prerequisite, not just a polish item.

---

## Step 6 — W3C triad audit

| Lens | Verdict | Evidence + gaps |
|---|:---:|---|
| **Usability** | **Pass** | 19-gate walkthrough covers the seven-step journey end-to-end; zero console errors; all 14 acceptance criteria + U-INS-3 + 4 polish tests pass. Lab 04's any-N requirement (anticipating v1.2) extends the discipline. |
| **Accessibility** | **Partial** | Substantial: focus rings (PR #12), aria-describedby (PR #12), focus restoration on drawer close (PR #12), keyboard nav through table/cards/drawer, screen-reader-friendly aria attributes, colour-plus-text/icon rule (Topic 2 §5 anti-pattern 4). Gap: no real assistive-tech testing yet; ARIA correctness verified by inspection + Playwright but not by NVDA/VoiceOver/JAWS run. **Closure**: include a screen-reader test in v1.2 Sponsor Reviewer recruitment criteria. |
| **Inclusion** | **Fail** | English-only copy; assumes reviewer knows domain terms ("Planner-ready", "verified", "candidate") without inline definitions; no low-bandwidth consideration (CSV fetched from raw.githubusercontent.com without compression discussion); mobile layout exists but tested only as a secondary case; no consideration of non-Western reviewer cultural contexts; no language-switching capability. **Closure**: produce explicit inclusion-lens requirements in v1.2 (per Activity 2 finding F-REQ-2); scope inclusion fixes for v1.2 vs v2.x with rationale per item. |

### Activity-6 verdict

**Usability strong; Accessibility substantial-but-needs-AT-testing; Inclusion fail.**

**Finding F-W3C-1**: Inclusion is the worst-served W3C lens. Five distinct sub-dimensions (language, bandwidth, device, cultural context, terminology) all need attention. The scoping decision (v1.2 vs v2.x per item) should be explicit, not silent.

---

## Step 7 — Findings and prioritised v1.2 HCD list

### Strengths

- **Audit-shape is intact**: every major artifact maps to at least one ISO activity. The discipline of *naming what each artifact serves* is visible across the workspace.
- **The seven-step journey + four-depth trust signal + 14 acceptance criteria** satisfy Activities 1–2 for the *per-persona* context-of-use and the *usability + accessibility* W3C lenses.
- **Topic 4 Loop 1 is HCD-compliant**: every loop stage produced an artifact (evidence rule); the three-persona synthesis satisfies the explicit-understanding principle's solo translation.
- **Iteration is structural**, not aspirational — the PR cadence + the design-thinking loop together satisfy Principle 4 by construction.
- **Honest naming of limitations** runs through the workspace: the v1.1 implementation references missing Sponsor Reviewer; Lab 04 names Loop 2 trigger conditions; the polish PRs (#12) name what isn't yet covered.

### Gaps (consolidated from Steps 1–6)

| ID | Finding | Activity / lens | Severity |
|---|---|---|:---:|
| **F-CTX-1** | Systems-level context-of-use under-documented (downstream Planner consumer; lateral handoff; regulatory) | Activity 1 | **High** |
| **F-REQ-1** | Lab 04 §8 U-CONF-1..4 criteria are in prose but not landed in `ux-acceptance-criteria.md` | Activity 2 | Medium |
| **F-REQ-2** | Inclusion-lens user requirements entirely absent from the canonical criteria sheet | Activity 2 + Inclusion lens | **High** |
| **F-EVAL-1** | Human-grade evaluation absent; only machine-grade walkthrough exists | Activity 4 + Principle 2 + Principle 3 | **High** |
| **F-EVAL-2** | v1.1 has no heuristic-grade evaluation that uses the post-Topics-2-5 discipline (Topic 1's Lab 01 audit is of v1) | Activity 4 | Medium |
| **F-PRIN-1** | Principle 2 (Users involved throughout) is the only outright Fail; closure requires Sponsor Reviewer recruitment | Principle 2 | **High** |
| **F-W3C-1** | Inclusion lens fails on five sub-dimensions (language, bandwidth, device, cultural context, terminology) | W3C inclusion | **High** |

### Prioritised v1.2 HCD list (ordered by leverage)

| Priority | Action | Closes findings |
|---:|---|---|
| **1** | Recruit at least one Sponsor Reviewer | F-EVAL-1, F-PRIN-1, partially F-EVAL-2 |
| **2** | Land U-CONF-1..4 acceptance criteria in `ux-acceptance-criteria.md` as a deferred-v1.2 block | F-REQ-1 |
| **3** | Produce a systems-context-of-use document (one page covering upstream pipeline + downstream Planner + lateral handoff + regulatory) | F-CTX-1 |
| **4** | Specify inclusion-lens requirements (≥ 1 per sub-dimension); scope each as v1.2 vs v2.x | F-REQ-2, F-W3C-1 |
| **5** | Include assistive-tech (screen-reader) test in Sponsor Reviewer recruitment | Accessibility partial → pass |
| **6** | Re-audit v1.1 at heuristic-grade with the post-Topics-2-5 discipline (likely as part of Sponsor Reviewer session) | F-EVAL-2 |

Items 1, 2, 3, 4 close the *high-severity* findings. Item 5 upgrades accessibility from partial to pass. Item 6 is bundleable with Item 1.

### What this audit does NOT do

- It does not run the Sponsor Reviewer recruitment. Recruitment is the v1.2 prerequisite, not an audit deliverable.
- It does not write the inclusion-lens requirements. Specifying them is the v1.2 work, not the audit's.
- It does not produce the systems-context-of-use document. That's a v1.2 deliverable that the audit identifies as needed.

The audit's job is to *find the gaps* and *prioritise the closures*. The closures themselves are v1.2 work.

---

## Audit summary

- **4 of 4 ISO activities audited** with evidence per activity
- **6 of 6 ISO principles graded** (2 Pass, 3 Partial, 1 Fail)
- **3 of 3 W3C triad lenses applied** (1 Pass, 1 Partial, 1 Fail)
- **7 findings identified**, 4 high-severity, 2 medium, 1 lower
- **6-item prioritised v1.2 HCD list** produced

**Overall HCD compliance verdict for v1.1**: *Substantial but incomplete.* The audit-shape itself is intact, and machine-grade discipline is strong. The Fail (Principle 2: Users involved throughout) and the High-severity gaps (F-CTX-1, F-REQ-2, F-EVAL-1, F-W3C-1) are all closable in v1.2 with Sponsor Reviewer recruitment + four targeted documentation+specification efforts.

**Decision**: Pass v1.1 as *HCD-substantial*; queue v1.2 with the six-item prioritised list as inherited HCD work.

## Capabilities extracted from this audit

Three reusable capabilities the workspace gains from running Audit 1:

1. **HCD-audit template** (four-activity rows + six-principle table + W3C-triad table + findings + prioritised list) — applicable to any product the workspace builds.
2. **HCD self-audit gate** (the four-cell check from Topic 5 quiz Q10) — applicable to every backlog item before implementation.
3. **Systems-context-of-use specification format** (upstream + downstream + lateral + regulatory layers) — applicable to any data-review tool with a wider workflow.

These three (combined with Topic 5 §14's three) take the workspace's reusable design-capability count further. Capability promotion (per `capabilities/README.md`) gets easier as the catalogue grows.
