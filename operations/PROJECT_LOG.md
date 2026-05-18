# PROJECT_LOG.md — CodeMike Project Log

This file records material progress, decisions, setup work, and milestone changes for the MSc CodeMike workspace.

## Log Rules

Add an entry when:

- a root governance file changes materially
- a new module or folder is created
- a capability becomes reusable
- an experiment produces evidence
- a skill maturity level changes
- a paid tool is proposed or approved
- a capability transfers to another project
- a risk, failure, or important limitation is identified

## Entry Template

```md
## YYYY-MM-DD — Title

Type: setup / learning / experiment / capability / transfer / review / risk / budget

Summary:

Files changed:

Evidence produced:

Next action:
```

## 2026-05-18 — Browser v1.1.x polish: six Lab 06 Gestalt fixes shipped (visual-treatment only)

Type: transfer / capability / review-followup

Summary:

Closes the v1.1.x polish PR queued at NEXT_ACTIONS priority 8. All six Lab 06 fixes shipped as visual-treatment-only changes to `docs/destination-master-browser.html` (zero behavioural changes; 19/19 walk-through pass with no regression). Closes six Gestalt findings (F-GES-1 through F-GES-6 except the v1.2-deferred F-GES-5 behaviour half) and upgrades the R1 caution-chip Trade-off to Pass.

Fixes shipped:

- **Fix #1** — `.verif-pill` component added; renderCards meta-grid + renderTable column 6 use it; verification signal now elevated to a coloured pill at both card + table depths, no longer collapsing into surrounding metadata via similarity (closes F-GES-1 + F-GES-2)
- **Fix #2** — view-toggle separated from narrowing-controls common-region via `margin-left + padding-left + border-left` (closes F-GES-4)
- **Fix #3** — active-filter summary moved 20px below toolbar with stronger tint differential (background `#eef2f7`, border solid `#cbd5e1`) (closes F-GES-6)
- **Fix #4** — sortable column headers get a faint ` ↕` glyph in the unsorted state via `aria-sort="none"::after` (closes F-GES-3)
- **Fix #5a** — search field gets `padding-right + border-right` to visually separate it from the selects (closes F-GES-5 visual half)
- **Fix #6** — caution-chip divider via `.card-chips .chip.warn:first-of-type::before` (R1 Trade-off → Pass upgrade)

Plus two Lyra missed-opportunity closures from PR #18:

- Computed leverage scores per fix added to the audit doc; Fix #1's score (2.8) confirms its #1 rank
- Five after-screenshots captured via Playwright (`curriculum/courses/des-001-design-foundations/verification/v1.1.x-polish/capture-fixes.js`) and indexed in the audit doc

Files changed:

- `docs/destination-master-browser.html` — six CSS additions + two helper-function rewires (`renderCards` + `renderTable`) + one new helper (`verifPill`)
- `design/foundations/topic-06-gestalt-audit.md` — addendum with computed leverage scores + screenshot index + walk-through regression result
- `curriculum/courses/des-001-design-foundations/verification/v1.1.x-polish/` (new) — capture script + five after-screenshots

Evidence produced:

- Six Gestalt findings closed at visual-treatment scope (one v1.2-deferred — F-GES-5 behaviour half pending Sponsor Reviewer)
- 19/19 walk-through pass on polished build (zero regression)
- Five annotated after-screenshots in the audit doc
- Leverage-score formula computed per fix; ranking confirmed

Next action:

End-of-polish closure: Lyra + Aurelius graded reviews on this PR. Merge. Then the v1.1.x polish queue is empty; v1.2 implementation is the next implementation move (NEXT_ACTIONS priority 10) once Sponsor Reviewer recruitment lands.

## 2026-05-17 — DES-001 three-topic push complete (Topics 4 + 5 + 6 closed; grade report v3 next)

Type: learning / assignment / milestone / governance

Summary:

Closes the ratified three-topic push (Topics 4 → 5 → 6) in a single working window across two days. Six PRs merged (Topic 4 PR A #13 + PR B #14; Topic 5 PR A #15 + PR B #16; Topic 6 PR A #17 + PR B #18). The DES-001 12-topic curriculum is now half-closed (6 / 12 topics done; 6 / 12 still in stub state at `Fitts' law`, `Button states`, `Typography`, `Color theory`, `Web design / grid layout`, `Design systems`).

The push established the **canonical design hierarchy** as a workspace constant:

```
Topic 5 — HCD (umbrella; ISO 9241-210 + W3C triad)
   ├─ Topic 4 — Design thinking (the loop, when problem isn't well-framed)
   ├─ Topic 3 — UX design (the criteria + journey)
   ├─ Topic 2 — UI design (the components)
   └─ Topic 6 — Gestalt (the perceptual constraint layer underneath visual treatment)
```

Three audit-shapes are now reusable workspace patterns (Lab 04 design-thinking loop, Lab 05 HCD audit, Lab 06 Gestalt audit). Lyra + Aurelius graded reviews on PR B for each topic confirmed each lab's discipline.

Three labs' worth of v1.2 work is now inherited by the v1.2 implementation PR (Lab 04 Loop 1 batch-promote-confirm + Lab 05 6-item HCD list led by Sponsor Reviewer recruitment + Lab 06 6-item Gestalt list with 5 v1.1.x + 1 v1.2). The v1.1.x polish PR has its own scope (Lab 06's 5 v1.1.x visual-treatment fixes that close 6 findings).

Files changed (cumulative across the six PRs; see per-topic entries below for details):

- Three deep-reading docs: `design/foundations/topic-04-design-thinking.md`, `topic-05-hcd.md`, `topic-06-gestalt.md`
- Three lab outputs: `topic-04-design-thinking-loop.md`, `topic-05-hcd-audit.md`, `topic-06-gestalt-audit.md`
- Six lecture + reading-pack + quiz × 3 + lab-brief files per topic across `curriculum/courses/des-001-design-foundations/`
- Three Lab submissions in `submissions/`
- Master-browser checklist sections §23..§31 (9 new sections across the three topics)
- `docs/design-foundations-app/data.js` — three topics promoted from stub to full done modules (12 modules total; 6 done; Cipher-verified zero errors)
- All tracking files updated per topic (competency-map, weekly-plan, learning-log, submission, viva)
- Operations governance catch-up this PR: SKILL_MAP, CAPABILITIES, PROJECT_LOG (this entry + 3 per-topic entries), NEXT_ACTIONS, TRANSFER_LOG

Evidence produced:

- Six PRs merged cleanly into main with consistent stacked-PR shape (PR A reading branch → PR B lab branch cut from PR A)
- 12 DES-001 dashboard modules; 6 done with full notes; 6 in stub state with consistent shape
- Three workspace-grade audit-shape templates ready for re-use
- Eleven reusable capabilities now at maturity 4 (six pre-existing from Topics 2 + 3 + Browser v1.1 ship; five added by Topics 4 + 5 + 6)
- Lab 05's anticipated-violations list refuted *and* confirmed where the audit found counter-evidence vs alignment-evidence
- Lab 06's anticipated-violations list confirmed at five-of-six rate (one softened from Violation to Trade-off) — falsifiability the deep-reading docs earned by writing the anticipations down up-front
- Cross-topic validation: Lab 06 confirms Topic 2's four-depth trust signal spec is intact at 3/4 depths and that the findings are *implementation* failures rather than *specification* failures

Next action:

Write **grade-report v3** at `feedback/DES-001-grade-report-v3.md` — cumulative DES-001 grade after Topics 1–6 (HCD compliance from Topic 5 + Gestalt compliance from Topic 6 + scope-incompleteness adjustment scaled down from −6 toward 0 as 6/12 topics now closed). After v3 lands, **STOP** per the ratified three-topic push goal.

## 2026-05-17 — DES-001 Topic 6 closed (Gestalt principles + Lab 06 + master-browser checklist §29..§31)

Type: learning / assignment / capability

Summary:

Closed DES-001 Topic 6 — Gestalt principles. Two PRs land the topic: PR A (#17) produces the deep-reading evidence (`design/foundations/topic-06-gestalt.md`, 15 sections) + the lecture, reading pack (4 required sources: Wertheimer/Koffka/Köhler via secondary, IxDF, NN/g, Smashing + 5 extension), quiz with worked answers, lab brief, eight viva questions + worked answers, and the data.js promotion (status `done`, 5 sources, full notes). PR B (#18) executes Lab 06 — a Gestalt audit of v1.1 (`design/foundations/topic-06-gestalt-audit.md`, Audit 1) across six regions × six principles (36 cells: 22 Pass + 5 Trade-off + 7 Violation + 4 N/A) + four conflict adjudications (zero left unresolved) + density-vs-grouping audit + 6-item prioritised v1.1.x / v1.2 fix list — and appends master-browser checklist §29 (three Gestalt gates) + §30 (three anti-patterns) + §31 (canonical pointer).

Key insight: Gestalt sits *underneath* Topic 2 as the perceptual constraint layer. A design can satisfy Topic 2 (correct components) and Topic 3 (correct acceptance criteria) and still violate Gestalt (wrong perceived grouping). Lab 06 confirms this by surfacing F-GES-1 + F-GES-2: the trust badge is correctly elevated per Topic 2 §6.2 four-depth spec, but the *verification text* duplicated inside the card meta-grid + table column at equivalent visual weight to non-trust fields partially undoes the badge's elevation via similarity-collapse. Single visual-treatment fix closes both occurrences.

The perceptual-constraint vs aesthetic-rule distinction is the topic's most operationally important discipline. Style-reading: "use whitespace generously" is unfalsifiable. Constraint-reading: every visual choice defends itself against what the visual system *will* do — falsifiable per region.

Files changed:

- `design/foundations/topic-06-gestalt.md` (new — 15-section deep-reading doc)
- `design/foundations/topic-06-gestalt-audit.md` (new — Audit 1; six regions × six principles + conflict adjudication + density-vs-grouping + prioritised fix list)
- `curriculum/courses/des-001-design-foundations/lectures/lecture-06-gestalt-principles.md` (new)
- `curriculum/courses/des-001-design-foundations/readings/topic-06-gestalt-principles-reading-pack.md` (new)
- `curriculum/courses/des-001-design-foundations/quizzes/quiz-06-gestalt-principles.md` + `-answer-key.md` + `-answers.md` (new — ten worked answers)
- `curriculum/courses/des-001-design-foundations/labs/lab-06-gestalt-audit.md` (new — six-step brief)
- `curriculum/courses/des-001-design-foundations/viva/DES-001-viva-questions.md` + `-answers.md` (Topic 6 questions + answers appended)
- `curriculum/courses/des-001-design-foundations/submissions/lab-06-gestalt-audit-results.md` (new — formal Lab 06 submission)
- `design/checklists/master-browser-design-checklist.md` (§29 + §30 + §31 appended)
- `docs/design-foundations-app/data.js` (Gestalt principles flipped to `done`; five sources; full notes object attached; Cipher-verified)
- All tracking files updated (competency-map, weekly-plan, learning-log, DES-001-submission)

Evidence produced:

- Six audited regions × six principles = 36-cell perceptual matrix
- 6 findings (F-GES-1..6) + 1 meta-finding (F-GES-7)
- 4 cross-principle conflicts adjudicated (zero unresolved)
- 6-item prioritised fix list (5 v1.1.x + 1 v1.2)
- Three Gestalt anti-patterns for data-review tools (silent density collapse, decorative motion, too many similarity signals)
- Three reusable CodeMike capabilities (Gestalt audit template; violation taxonomy diagnostic vocabulary; density-vs-grouping audit pattern)
- Canonical hierarchy extension (Gestalt as perceptual constraint layer underneath Topic 2)
- Cross-audit validation of Topic 2's four-depth trust signal

Next action:

End-of-three-topic-push closure (this PR): governance catch-up complete; write grade-report v3 next.

## 2026-05-17 — DES-001 Topic 5 closed (HCD + Lab 05 + master-browser checklist §26..§28)

Type: learning / assignment / capability

Summary:

Closed DES-001 Topic 5 — Human-centred design. Two PRs land the topic: PR A (#15) produces the deep-reading evidence (`design/foundations/topic-05-hcd.md`, 16 sections) + lecture, reading pack (4 required sources: ISO 9241-210, IDEO Field Guide HCD chapters, Don Norman HCD essays, W3C accessibility/usability/inclusion + 6 extension), quiz with worked answers, lab brief, eight viva questions + worked answers, and the data.js promotion. PR B (#16) executes Lab 05 — a full HCD audit of v1.1 + Lab 04 Loop 1 against ISO 9241-210's four activities + six principles + the W3C triad (`design/foundations/topic-05-hcd-audit.md`, Audit 1) — and appends master-browser checklist §26 (four HCD gates) + §27 (four anti-patterns) + §28 (canonical pointer).

Verdict: v1.1 is *HCD-substantial but incomplete*. Six principles graded 2 Pass + 3 Partial + 1 Fail (Principle 2: Users involved throughout — the workspace has no real users yet). W3C triad: Usability Pass, Accessibility Partial, Inclusion Fail. Seven findings; six-item prioritised v1.2 HCD list led by Sponsor Reviewer recruitment.

Key insight: HCD is the **umbrella** over Topics 2 / 3 / 4 in the canonical hierarchy. HCD doesn't produce *new artifacts*; it provides the *audit-shape* (every artifact maps to at least one of the four ISO activities). Norman's *HCD Considered Harmful?* critique is addressed by doing the context-of-use activity at the **systems** level (not just the individual user level) — and Audit 1 surfaces that systems-level context-of-use is exactly the gap v1.1 needs to close in v1.2 (F-CTX-1).

Files changed:

- `design/foundations/topic-05-hcd.md` (new — 16-section deep-reading doc)
- `design/foundations/topic-05-hcd-audit.md` (new — Audit 1)
- `curriculum/courses/des-001-design-foundations/lectures/lecture-05-human-centered-design.md` (new)
- `curriculum/courses/des-001-design-foundations/readings/topic-05-human-centered-design-reading-pack.md` (new)
- `curriculum/courses/des-001-design-foundations/quizzes/quiz-05-human-centered-design.md` + `-answer-key.md` + `-answers.md` (new)
- `curriculum/courses/des-001-design-foundations/labs/lab-05-hcd-audit.md` (new)
- `curriculum/courses/des-001-design-foundations/viva/DES-001-viva-questions.md` + `-answers.md` (Topic 5 Q+A appended)
- `curriculum/courses/des-001-design-foundations/submissions/lab-05-hcd-audit-results.md` (new)
- `design/checklists/master-browser-design-checklist.md` (§26 + §27 + §28 appended)
- `docs/design-foundations-app/data.js` (Topic 5 flipped to `done`)
- All tracking files updated

Evidence produced:

- Audit Steps 1–4: per-activity evidence with three-persona context-of-use table + systems-level context-of-use table + documented requirements table + design solutions table + evaluation evidence table
- Audit Step 5: 2 Pass + 3 Partial + 1 Fail across the six ISO principles
- Audit Step 6: W3C triad audit (1 Pass + 1 Partial + 1 Fail)
- 7 findings (4 High + 2 Medium + 1 lower) + 6-item prioritised v1.2 HCD list ordered by leverage
- Four HCD anti-patterns for single-person workspaces
- Honest naming of limitations as the workspace discipline (Topic 5's most important pattern)

Next action:

Start Topic 6 (Gestalt principles) — final topic in the ratified three-topic push.

## 2026-05-17 — DES-001 Topic 4 closed (Design thinking + Lab 04 + master-browser checklist §23..§25)

Type: learning / assignment / capability

Summary:

Closed DES-001 Topic 4 — Design thinking. Two PRs land the topic: PR A (#13) produces the deep-reading evidence (`design/foundations/topic-04-design-thinking.md`) + lecture, reading pack (4 required sources: Stanford d.school Bootleg, IBM Design Thinking, Tim Brown HBR + *Change by Design*, NN/g "Design Thinking 101" + 5 extension including Norman's *Design Thinking: A Useful Myth* critique), quiz with worked answers, lab brief, eight viva questions + worked answers, and the data.js promotion. PR B (#14) executes Lab 04 — Loop 1 on the batch-promote-confirm modal (`design/foundations/topic-04-design-thinking-loop.md`) with eight steps (Pick → Empathize → Define → Ideate ≥3 candidates → Three-constraint triage → Prototype-spec → Test-spec with falsification criteria → Decision; Candidate B chosen via comparative reasoning vs A/C/D) — and appends master-browser checklist §23 (four design-thinking gates) + §24 (five anti-patterns) + §25 (canonical loop-output pointer).

Key insight: design thinking is the *iteration mechanism* inside HCD's lifecycle, not a substitute for it. The Topic 4 / Topic 3 routing rule (well-framed → Topic 3 criteria directly; not well-framed → Topic 4 loop first) is the operational discipline.

Three reusable capabilities extracted: the 8-step loop template, the three-constraint triage frame, the problem-framing decision tree (Topic 4 first vs Topic 3 first).

Files changed:

- `design/foundations/topic-04-design-thinking.md` (new — deep-reading doc)
- `design/foundations/topic-04-design-thinking-loop.md` (new — Loop 1 worked example)
- `curriculum/courses/des-001-design-foundations/lectures/lecture-04-design-thinking.md` (new)
- `curriculum/courses/des-001-design-foundations/readings/topic-04-design-thinking-reading-pack.md` (new)
- `curriculum/courses/des-001-design-foundations/quizzes/quiz-04-design-thinking.md` + `-answer-key.md` + `-answers.md` (new)
- `curriculum/courses/des-001-design-foundations/labs/lab-04-design-thinking-loop.md` (new)
- `curriculum/courses/des-001-design-foundations/viva/DES-001-viva-questions.md` + `-answers.md` (Topic 4 Q+A appended)
- `curriculum/courses/des-001-design-foundations/submissions/lab-04-design-thinking-loop-results.md` (new)
- `design/checklists/master-browser-design-checklist.md` (§23 + §24 + §25 appended)
- `docs/design-foundations-app/data.js` (Topic 4 flipped to `done`)
- All tracking files updated

Evidence produced:

- Loop 1: full 8-step worked example for batch-promote-confirm modal
- Three-persona synthesis (first-time / power / accessibility-need) as the solo-workspace Empathize translation
- Four candidates with three-constraint triage and comparative selection (B chosen)
- Topic 4 / Topic 3 routing decision tree
- Five design-thinking anti-patterns (skipping Ideate, single-pass design thinking, empathy-by-introspection, workshop theatre, triage by taste) with sourced mitigations
- Three reusable design-thinking capabilities

Next action:

Start Topic 5 (HCD) — second of the three topics in the ratified push.

## 2026-05-17 — v1.1 polish follow-up: walk-through script committed, four polish items behaviourally tested, governance freshness restored

Type: review-followup / governance

Summary:

Closes the Lyra and Aurelius missed opportunities from the PR #11 review. The work is small but each item closes a real loose end:

**Walk-through script committed (Lyra + Aurelius).** Previously orphaned at `/tmp/walkthrough-v1.1.js`. Now at `curriculum/courses/des-001-design-foundations/verification/v1.1-walkthrough/walkthrough.js` with screenshot output paths anchored via `__dirname` + a `path.join` helper so it can be run from anywhere and writes screenshots back into the verification folder. Reproducibility is now a property of the repo, not the container.

**Four new behavioural gate-tests added** (Lyra observation 3-4 + missed a11y coverage): POLISH-1 (focus restoration on drawer close → asserts `document.activeElement` is the opener row), POLISH-2 (count-flash CSS class fires on filter change), POLISH-3 (drawer `aria-describedby` resolves to the trust-state line), POLISH-4 (taxonomy-drift `console.warn` fires on a synthetic unmapped `verification_status` row + the row still renders via the safe-default fallback). Walk-through now produces **19/19 pass** (15 original + 4 new). The polish items shipped in PR #11 are now defended against regression.

One small bug found and fixed during the polish-test additions: POLISH-1 initially failed because U-LEA-1 left the page in cards view, and `.focus()` on a hidden TR silently fails. Test switches back to table view before asserting; implementation was correct.

**Tracking-file freshness (Aurelius observations 2 + 5).** `README.md` "Active artifacts" split into v1.1 (canonical) + v1.0 (archived) rows. `NEXT_ACTIONS.md` priority 3 rewritten to name the canonical URL and the archive URL explicitly, dated to the 2026-05-16 ship.

**TRANSFER_LOG template aligned (Aurelius observation 4).** Updated the template at the top of TRANSFER_LOG.md to match the `### Transfer N — <source> → <target>` form Transfer 1 used, with the eight standard fields. Future transfer entries follow the same shape.

**First formal capability card written (Aurelius observation 3).** `capabilities/seven-step-reviewer-journey.md` — the canonical statement of the highest-leverage DES-001-derived design capability, with method, current maturity (4), evidence, limitations, reusable-in list, transfer history, and next action. Mirrors the format of the existing capability cards (`dashboard-insight-design.md` etc). Sets the template for future cards as the remaining five capabilities promote to maturity 5.

Files changed:

- `curriculum/courses/des-001-design-foundations/verification/v1.1-walkthrough/walkthrough.js` (new — committed from /tmp; extended with four polish gates; paths anchored to __dirname)
- `curriculum/courses/des-001-design-foundations/verification/v1.1-walkthrough/walkthrough-results.json` (refreshed; 19 entries)
- `curriculum/courses/des-001-design-foundations/verification/v1.1-walkthrough/walkthrough-*.png` (refreshed)
- `curriculum/courses/des-001-design-foundations/verification/v1.1-walkthrough/v1.1-walkthrough-verification-2026-05-16.md` (updated: 15/15 → 19/19; script-path note)
- `capabilities/seven-step-reviewer-journey.md` (new — first canonical card)
- `README.md` (active-artifacts split)
- `operations/NEXT_ACTIONS.md` (priority 3 refreshed for v1.1 vs v1.0)
- `operations/TRANSFER_LOG.md` (template aligned with Transfer 1 form)

Evidence produced:

- 19/19 walk-through pass with zero console errors — including the four behavioural tests Lyra flagged as missing
- A canonical capability card other future cards can mirror
- Reproducibility of the walk-through preserved across container restarts
- Workspace tracking files refreshed to reflect post-v1.1 state

Operating-loop implication: the *Improve* step of the CodeMike loop is genuinely closing now — review caught real misses, the misses were fixed, the fixes were verified. The loop's last step is not ceremonial.

Next action:

Start DES-001 Topic 4 — Design thinking — per the ratified execution plan §3. User can also verify the production GitHub Pages render of v1.1 at convenience (NEXT_ACTIONS priority 3).

## 2026-05-16 — Destination Master Browser v1.1 shipped (polish + walk-through + transfer)

Type: capability / transfer / governance

Summary:

Closes the v1.1 implementation. This PR ships the polish items Lyra flagged on PR #10, runs the full 13-gate Playwright walk-through against the live build (**15/15 pass** including the cross-cutting CONSOLE check; zero console errors), and promotes the workspace's UI/UX skill and design capabilities per CLAUDE.md governance.

Walk-through coverage: every one of the 13 v1.1 UX gate-criteria in `design/foundations/ux-acceptance-criteria.md` has an explicit machine-evaluated pass/fail test. The deferred-but-implemented U-INS-3 (drawer Prev/Next) is also verified. The CONSOLE check confirms no `console.error`, `pageerror`, or `requestfailed` events across the full walk-through. Two evaluators running the same script against the same build reach the same 15 verdicts — that is the reproducibility property the acceptance-criteria sheet was designed to deliver.

Polish edits (every Lyra observation from PR #10 closed):

- Drawer ARIA: kept `role="dialog"` + `aria-modal="false"` per WAI-ARIA APG's non-modal-dialog pattern; added `aria-describedby="drawerTrustText"` so screen readers announce the trust state when the dialog gains focus; HTML comment documents the choice.
- Focus restoration on drawer close: `state.lastOpener` captures the row/card on first open; `closeDrawer` calls `opener.focus()` after the slide-out completes. Keyboard users resume at their journey position rather than at the document body.
- Result-count perceptibility (U-NAR-1 "perceptible" requirement): added `#resultCount.flash` with a brief `--accent-soft` background flash; reflow-forced so the transition restarts cleanly on every count change.
- CSV URL override: `?csv=<url>` query-param overrides the default GitHub raw URL. Production loads unchanged; staging / offline URLs supported without code changes.
- Taxonomy-drift detection: `console.warn` (deduped via `_warnedTrustValues` set) fires on any unmapped `verification_status` / `planner_use_status` combination so QA spots master-CSV drift.

Governance promotions (per CLAUDE.md "New reusable skills require updates to SKILL_MAP.md", "New reusable capabilities require updates to CAPABILITIES.md", "Transfers require updates to TRANSFER_LOG.md"):

- `operations/SKILL_MAP.md` — "UI / UX design for data-review tools" promoted from level 4 (Applied to real project) → level 5 (Reusable / teachable / template-ready). Evidence: the v1.1 walk-through demonstrates the pattern is reproducible and the transfer is complete.
- `operations/CAPABILITIES.md` — all six DES-001-derived design capabilities promoted from maturity 3 (Reusable pattern) → maturity 4 (Transferred to project). Each row's evidence column now cites the v1.1 walk-through.
- `operations/TRANSFER_LOG.md` — new "Transfer 1" entry recording the full DES-001 → Browser v1.1 transfer with date, source capabilities, target project, problem solved, artifact transferred, evidence, outcome, limitations, and next action.
- `operations/NEXT_ACTIONS.md` — priority 4 (Implement Destination Master Browser v1.1) flipped from `doing` to `done`.

Files changed:

- `docs/destination-master-browser.html` (polish edits — drawer focus restoration, count-flash CSS + JS, CSV override, console-warn taxonomy guard, drawer aria-describedby + HTML comment)
- `curriculum/courses/des-001-design-foundations/verification/v1.1-walkthrough/` (new — verification report + 4 screenshots + raw JSON results)
- `operations/SKILL_MAP.md` — UI/UX skill row updated to level 5 with v1.1 evidence
- `operations/CAPABILITIES.md` — six capability rows promoted to maturity 4 with transfer evidence
- `operations/TRANSFER_LOG.md` — Transfer 1 recorded
- `operations/NEXT_ACTIONS.md` — priority 4 marked `done`

Evidence produced:

- 15/15 walk-through pass against the v1.1 build (machine-evidenced)
- Four screenshots (table / cards / empty / drawer) capturing the implementation in each major state
- Raw JSON walk-through results for reproducibility
- The Destination Master Browser as the workspace's first real applied-design transfer
- The CodeMike operating loop completes for the design-discipline domain: Orient → Learn → Prove → Package → **Transfer (this PR)** → Improve (future v1.2 if needed)

Next action:

User to verify production GitHub Pages render at convenience (NEXT_ACTIONS.md priority 3). Then start DES-001 Topic 4 (Design thinking) per the ratified execution plan §3.

## 2026-05-16 — Destination Master Browser v1.1 core implementation

Type: capability / transfer

Summary:

First PR of the v1.1 implementation work. Ships the core build of the Destination Master Browser at the canonical path `docs/destination-master-browser.html`, against the DES-001 Topic 2 component rule sheet (`design/foundations/ui-design-component-rules.md`) and Topic 3 UX acceptance-criteria sheet (`design/foundations/ux-acceptance-criteria.md`). The v1 build is archived at `docs/destination-master-browser-v1.0.html`.

v1.1 implements the seven-step reviewer journey at component level: sticky dataset-trust banner at the top of every screen; toolbar with search + 5 selects + accent-indicator on non-default fields; active-filter summary chip-row above the result list with per-filter removal and a Clear-all action; table-by-default with sortable columns; card view as a secondary toggle; record-detail drawer that opens on row/card click with persistent trust banner in the drawer header, Prev/Next navigation, close-on-click-outside + close-on-Esc; trust-badge component used at four depths (top banner, list row, card top-right, drawer header) with seven defined states (`verified`, `planner-ready`, `unverified`, `blocked`, `missing-fields`, `conflict`, `unassigned`) each carrying icon + colour + text; distinct components for loading (skeleton), empty (content-rich, with active-filter summary + Clear-all + suggestion), and error (inline notification with Retry + Report-issue actions); responsive layout collapsing to single-column on narrow viewports; `prefers-reduced-motion` honoured.

Playwright smoke test against an in-memory CSV stub passed 26/26 checks: trust banner visible; correct row count; trust badges in every row; sortable headers; view toggle; active-filter chip appears on filter change; Clear-all visible; empty state renders with filter list + recovery action; drawer opens with correct name + trust state, navigates with Prev/Next, closes on Esc with proper state cleanup; cards view renders all records. Zero console errors. Initial defects found during smoke testing and fixed in the same PR: sticky table-header was intercepting row clicks (removed); `.drawer { display: grid }` was overriding `[hidden] { display: none }` (added explicit `.drawer[hidden] { display: none !important }` override).

Reference-path discipline: historical references (Lab 01 / Lab 02 / Lab 03 evidence, lecture-02, design/foundations/ docs) point at `destination-master-browser-v1.0.html` to preserve historical accuracy (those labs were executed against v1); active references (README.md, docs/index.html, docs/repo-map.html, operations/NEXT_ACTIONS.md, operations/ARTIFACT_INDEX.md) point at the canonical `destination-master-browser.html`.

Files changed:

- `docs/destination-master-browser.html` (new — canonical v1.1 build, ~1000 lines)
- `docs/destination-master-browser-v1.0.html` (renamed from `-v1.html`)
- `curriculum/courses/des-001-design-foundations/verification/v1.1-core/` (new — Playwright smoke-test screenshots)
- All references across the repo updated to the correct historical-vs-active path
- `operations/NEXT_ACTIONS.md` priority 4 moved to `doing` (full walk-through verification + TRANSFER_LOG entry land in PR B)

Evidence produced:

- A working v1.1 build at the canonical path, smoke-tested
- Two Playwright screenshots (above-the-fold and full-page) saved as verification evidence
- Reference-path discipline established for future versions (historical = explicit version suffix; active = canonical)
- Two real defects found and fixed during smoke testing (sticky-header click interception; [hidden] specificity)

Next action:

Open PR B — full 13-gate walk-through verification against the live build; promote `SKILL_MAP.md` skill to level 5 (transferred); promote `CAPABILITIES.md` capabilities to maturity 4 (transferred to project); add a `TRANSFER_LOG.md` entry recording the DES-001 → Browser v1.1 capability transfer; polish items (refined focus rings, animation perceptibility tuning, accessibility audit). After PR B merges, NEXT_ACTIONS priority 4 moves to `done`.

## 2026-05-16 — DES-001 Topic 3 closed (UX design + Lab 03 + acceptance-criteria sheet)

Type: learning / assignment / capability

Summary:

Closed DES-001 Topic 3 — UX design. Two PRs land the topic: PR A (#8) produces the deep-reading evidence (source-by-source notes across Don Norman / NN/g / IDEO / GOV.UK Service Manual / IxDF; source comparison; CodeMike interpretation; browser application; anti-patterns; v1.1 UX-implementation impact; checklist updates). PR B (this entry) executes Lab 03 (full reviewer-journey map + 14 UX acceptance criteria + user-need audit + Lab 01 → Lab 03 gap analysis) and appends Topic 3 sections to the master-browser checklist (§20 four UX gates + §21 four UX anti-patterns + §22 canonical pointer to the acceptance-criteria sheet).

The seven-step reviewer journey (arrive / understand / narrow / compare / inspect / recover / leave) has goal / cost-budget / failure-mode / trust-check per step. v1's verdict: 0 of 7 cleanly Pass; 3 Partial; 1 Partial-to-fail; 3 Fail (Compare, Inspect, Recover). The 14 UX acceptance criteria (13 gate-tests, 12 marked as v1.1 must-pass gates) close all three Fail steps and all 11 tracked Lab 01 findings.

The single most operationally important discipline introduced is **GOV.UK's user-need form** applied as a backlog gate. Every v1.1 item now has a *need* (no UI mechanism named) and an *acceptance-criterion ID*. Items that cannot produce both are refused. The other four sources (Norman, NN/g, IDEO, IxDF) allow loose user-need language that lets solution-shape thinking drift in; GOV.UK alone enforces the discipline that catches it.

**Browser v1.1 is now unblocked.** Per the ratified execution plan §3 (gate 1), v1.1 implementation begins between Lab 03 close and Topic 4 open. The complete v1.1 specification = Topic 2 component rule sheet + Topic 3 UX acceptance-criteria sheet + master-browser checklist §3 + §18 + §20.

Files changed:

- `design/foundations/topic-03-ux-design.md` (new — 16-section deep-reading doc; PR A)
- `design/foundations/topic-03-ux-design-journey-map.md` (new — Lab 03 Steps 1–4; PR B)
- `design/foundations/ux-acceptance-criteria.md` (new — Lab 03 Step 5; Browser v1.1's UX gate; PR B)
- `curriculum/courses/des-001-design-foundations/lectures/lecture-03-ux-design.md` (new; PR A)
- `curriculum/courses/des-001-design-foundations/readings/topic-03-ux-design-reading-pack.md` (new; PR A)
- `curriculum/courses/des-001-design-foundations/quizzes/quiz-03-ux-design.md` + `-answer-key.md` + `-answers.md` (new; PR A)
- `curriculum/courses/des-001-design-foundations/labs/lab-03-ux-design-journey-map.md` (new; PR A)
- `curriculum/courses/des-001-design-foundations/submissions/lab-03-ux-design-journey-map-results.md` (new; PR B)
- `curriculum/courses/des-001-design-foundations/viva/DES-001-viva-questions.md` + `-answers.md` (Topic 3 questions and answers appended; PR A)
- `design/checklists/master-browser-design-checklist.md` (§20 + §21 + §22 appended; PR B)
- `docs/design-foundations-app/data.js` (Topic 3 module flipped to `done`; three of twelve now `done`; PR A)
- Tracking files: `competency-map.md`, `weekly-plan.md`, `learning-log.md`, `submissions/DES-001-submission.md`, `revisions/DES-001-revision-plan-v1.md`

Evidence produced:

- Seven-step reviewer-journey map for the Destination Master Browser
- 14 UX acceptance criteria with 13 gate-tests
- 9 v1 features + 13 v1.1 backlog items audited as need / request / solution-shape; all produce clean user needs
- Lab 01 → Lab 03 gap-closure trail (11 findings, all closeable by v1.1)
- Four UX gates and four UX anti-patterns appended to the master-browser checklist
- Three more reusable CodeMike design capabilities (seven-step reviewer-journey template; UX acceptance-criterion form; user-need triage). Combined with Topic 2's three, the workspace now has six reusable design capabilities — threshold for promoting to formal capability cards.

Next action:

Implement Browser v1.1 against the consolidated specification (rule sheet + acceptance-criteria sheet + checklist gates). Then start Topic 4 — Design thinking.

## 2026-05-16 — DES-001 grade report v2 (Topic 1 + Topic 2 milestone)

Type: assessment / review

Summary:

Issued grade report v2 for DES-001 after Topic 1 and Topic 2 both closed. Cumulative grade is **87/100 — Excellent (rubric) / Distinction (course policy)**, up from v1's 82/100 (+5). Topic 2 *as a topic* scores 96/100 (Benchmark band), but promotion of the whole assignment to benchmark requires Topics 3–12 to close.

The Lyra review caught an arithmetic-integrity issue: v1's subscores summed to 89 (with the academic-discipline cap), yet v1 reported total 82 — a hidden 7-mark scope-incompleteness deduction below the line. v2 surfaces that discipline explicitly with a `−6` adjustment in the table (proportional to 10/12 vs 11/12 scaffolded), so v3 (after Topic 6) and v4 (after Topic 12) can scale honestly. The adjustment reaches 0 only at full course closure.

Subscore changes vs v1:

- Source comparison and bias awareness: 13 → 14 (Topic 2 added the agreement / difference-by-emphasis / per-source-omissions structure)
- Application to CodeMike/browser: 18 → 19 (Topic 2's rule sheet is the strongest browser-application artifact in the course)
- HTML usability and clarity: 8 → 9 (live visual verification closed; Topic 2 module digested)
- Checklist/actionability: 9 → 10 (Topic 2 added six sourced gates plus the canonical rule-sheet pointer)

All six v1 required revisions are now closed or partially closed. New v2 required revisions are forward progress only: continue Topic 3 → implement Browser v1.1 → continue Topics 4–12.

Files changed:

- `curriculum/courses/des-001-design-foundations/feedback/DES-001-grade-report-v2.md` (new — supersedes v1 as the current provisional grade)
- `curriculum/courses/des-001-design-foundations/competency-map.md` (current-grade-status banner updated)
- `curriculum/courses/des-001-design-foundations/revisions/DES-001-revision-plan-v1.md` (revision log row added)
- `curriculum/courses/des-001-design-foundations/submissions/DES-001-submission.md` (grade pointer updated)

Evidence produced:

- Per-criterion v2 grade with explicit Δ vs v1
- Topic 2 standalone per-topic grade (96/100)
- Named-and-closed status for every v1 required revision
- New v2 required-revisions list (forward-progress only)
- Reaffirmed next-action: Topic 3, then Browser v1.1

Next action:

Start Topic 3 — UX design.

## 2026-05-16 — DES-001 Topic 2 closed (deep reading + Lab 02 + rule sheet)

Type: learning / assignment / capability

Summary:

Closed DES-001 Topic 2 — What is UI design. Two PRs land the topic: PR A produces the deep-reading evidence (source-by-source notes across Material Design 3, Apple HIG, IBM Carbon, GOV.UK Design System, Don Norman; source comparison; CodeMike interpretation; browser application; anti-patterns; v1.1 implementation backlog; checklist updates). PR B executes Lab 02 (20-pattern inventory + state-coverage matrix + affordance/signifier/feedback audit + container-selection rules + filter-UI rules + consolidated rule sheet) and appends six Topic 2 component gates to the master-browser checklist.

Structural insight from the topic: the Destination Master Browser is a *master-detail data-review tool with faceted filtering* (Carbon pattern vocabulary). Naming the pattern fixes most v1.1 component choices: table by default with cards as secondary, drawer for detail (never modal), filter chips + dropdowns + search for narrowing, content-rich empty state with Clear-all recovery, skeleton loading, inline error notification, and a four-depth trust signal (top banner + list row + drawer header + future confirm-modal).

The five required sources differ less on definition than on emphasis — modality (Material permissive vs HIG/Carbon/GOV.UK restrictive), data-table prominence (Carbon first-class vs others light), and "when not to use" discipline (GOV.UK explicit vs others implicit). For this product, the HIG/Carbon/GOV.UK majority position wins on modality; Carbon's table-and-pattern vocabulary wins on the central reviewer task; GOV.UK's negative-space discipline becomes a checklist gate.

Files changed:

- `design/foundations/topic-02-what-is-ui-design.md` (new — 13-section deep-reading doc)
- `design/foundations/topic-02-ui-design-component-inventory.md` (new — Lab 02 Steps 1–3)
- `design/foundations/ui-design-component-rules.md` (new — Lab 02 Steps 4–6; Browser v1.1's input)
- `curriculum/courses/des-001-design-foundations/quizzes/quiz-02-what-is-ui-design-answers.md` (new — ten worked answers)
- `curriculum/courses/des-001-design-foundations/viva/DES-001-viva-questions.md` + `-answers.md` (Topic 2 questions and answers appended)
- `curriculum/courses/des-001-design-foundations/submissions/lab-02-ui-design-component-inventory-results.md` (new — formal Lab 02 submission)
- `design/checklists/master-browser-design-checklist.md` (§18 six Topic 2 gates + §19 canonical rule-sheet pointer)
- `docs/design-foundations-app/data.js` (Topic 2 module flipped to `done`; sources expanded from three to six; full notes object attached; Playwright re-verified)
- `curriculum/courses/des-001-design-foundations/competency-map.md`, `weekly-plan.md`, `learning-log.md`, `submissions/DES-001-submission.md`, `revisions/DES-001-revision-plan-v1.md`, `feedback/DES-001-grade-report-v1.md` (tracking files updated; Topic 2 marked closed; revision item 5 closed)

Evidence produced:

- 20-pattern v1 component inventory with element-category classification
- 12-pattern missing-pattern list (the v1.1 backlog)
- 20 × 9 state-coverage matrix with severity-ranked findings (3 HIGH + 4 MEDIUM)
- Affordance / signifier / feedback audit per interactive pattern; three cross-cutting findings (F1 active-state, F2 trust-signal depth, F3 three-states-one-component)
- Container-selection rule sheet (card / table / list / drawer / modal) with when-to-use + when-not-to-use + sources + decision tree
- Filter-UI rule sheet (search / chip / dropdown / faceted panel) with decision tree
- Four-depth trust-signal specification with seven trust states
- Six Topic 2 checklist gates appended to the master-browser checklist
- Three reusable CodeMike design capabilities extracted from the topic (master-detail-with-faceted-search pattern card; nine-state interactive checklist; affordance-signifier-feedback triple-check)

Next action:

Start Topic 3 — UX design. Browser v1.1 implementation remains gated on Topic 3 closing per the ratified execution plan.

## 2026-05-16 — DES-001 execution plan ratified and Topic 1 close-out

Type: learning / assignment / assessment / governance

Summary:

Ratified the DES-001 execution plan (all four §1 decisions confirmed as the recommended option: full 12-topic scope, per-topic sequencing, Browser v1.1 implementation after Topic 3, dashboard rename). Closed four of the six required revisions from the Topic 1 grade report.

Live visual verification of the modular dashboard ran under Playwright/Chromium against `file://` URLs in the remote execution container. All six promotion-rule conditions from `docs/design-foundations-app/README.md` passed: rendering, CSS, zero console errors, Topic 1 extension link, sync.js validation, layout equivalence with the legacy single-file dashboard. The rename then executed: `docs/design-foundations-v2.html` → `docs/design-foundations.html` (canonical, matching the assignment brief); `docs/design-foundations.html` (the 418-line monolithic predecessor) → `docs/design-foundations-v1.html` (archived). A second Playwright run against the canonical filename confirmed the rename did not break the relative `design-foundations-app/` script paths. Topic 1 quiz answers and viva answers were written to round out the close-out.

Files changed:

- `docs/design-foundations.html` (formerly `design-foundations-v2.html`)
- `docs/design-foundations-v1.html` (formerly `design-foundations.html`)
- `docs/design-foundations-app/config.js` (primaryArtifact and legacyArtifact paths swapped; version label updated)
- `docs/design-foundations-app/README.md` (Promotion rule section closed; verification result recorded)
- `curriculum/courses/des-001-design-foundations/verification/` (new — verification report and screenshots)
- `curriculum/courses/des-001-design-foundations/quizzes/quiz-01-ui-vs-ux-answers.md` (new)
- `curriculum/courses/des-001-design-foundations/viva/DES-001-viva-answers.md` (new)
- `curriculum/courses/des-001-design-foundations/feedback/DES-001-grade-report-v1.md` (items 1–4 of Required revisions marked closed)
- `curriculum/courses/des-001-design-foundations/revisions/DES-001-revision-plan-v1.md` (items 1–3 closed; revision-log rows added)
- `README.md`, `docs/repo-map.html`, `curriculum/courses/README.md`, course-level `README.md`/`syllabus.md`/`learning-log.md`/`submissions/DES-001-submission.md` (all `design-foundations-v2.html` references updated to the canonical filename)

Evidence produced:

- Playwright verification report at `curriculum/courses/des-001-design-foundations/verification/dashboard-visual-verification-2026-05-16.md`
- Three full-page screenshots (pre-rename v2, pre-rename above-the-fold, post-rename canonical) in `curriculum/courses/des-001-design-foundations/verification/`
- Defensible viva answers covering all eight Topic 1 questions with examiner-push follow-ups
- Self-marked quiz answers grounded in the Destination Master Browser

Next action:

Open the PR for this close-out work. After it merges, execute Topic 2 (the scaffold landed in PR #3): five-source deep reading, source comparison, and Lab 02 — producing the component rule sheet that becomes Browser v1.1's input.

## 2026-05-12 — DES-001 assignment and rubric created

Type: learning / assignment / assessment

Summary:

Formalised the Design Foundations Study Dashboard as CodeMike's first graded assignment: DES-001. The assignment frames `docs/design-foundations.html` as a reviewable university-style submission with multi-source deep reading, notes generation, further reading suggestions, grading, resubmission rules, and benchmark-promotion criteria.

Files changed:

- `assignments/DES-001-design-foundations-study-dashboard.md`
- `assignments/rubrics/design-foundations-rubric.md`
- `ARTIFACT_INDEX.md`

Evidence produced:

- DES-001 assignment brief
- 100-mark marking rubric
- grading bands: Fail, Pass, Good, Excellent, Benchmark
- automatic cap rules for weak source comparison or unsafe claims
- benchmark eligibility criteria
- resubmission rules

Next action:

Begin DES-001 deep reading with Topic 1: UI vs UX. Update `docs/design-foundations.html` with notes, source comparison, browser implications, anti-patterns, and further reading.

## 2026-05-12 — Seed compatibility cleanup completed

Type: taxonomy / validation / QA

Summary:

Updated the destination tag dictionary and master validator to accept legitimate legacy seed concepts found in the original 134-row seed dataset. These values are now treated as seed-compatible vocabulary: structurally valid for master ingestion, but still subject to future enrichment and normalization review.

Files changed:

- `datasets/reference/destination_tag_dictionary.md`
- `src/codemike/data/destination_master_validation.py`
- `NEXT_ACTIONS.md`
- `trackers/destination-database-build-tracker.md`

Evidence produced:

- accepted seed-compatible location types including `beach_city`, `culture_hill_town`, `desert_beach_emirate`, `heritage_capital`, `hill_heritage_city`, `island_heritage_city`, `island_resort_district`, `lake_mountain_city`, `mountain_capital`, `mountain_valley`, `northern_city`, and `wildlife_region`
- accepted seed-compatible vibe tags including `city`, `limestone`, `monsoon`, `museums`, `relaxation`, `stopover`, and `villa`

Next action:

Rerun `python src/codemike/data/destination_master_validation.py` in Termux and commit the regenerated clean validation report.

## 2026-05-12 — Destinations master v2 validation utility created

Type: dataset / validation / QA

Summary:

Created the master validation utility for `destinations_master_v2.csv`. The validator checks row count, required columns, unique master IDs, source lineage keys, duplicate name keys, critical blanks, controlled statuses, destination scales, location types, vibe tags, trip-style tags, context tags, caution tags, and source-confidence values.

Files changed:

- `src/codemike/data/destination_master_validation.py`
- `reports/evidence/destination-master-v2-validation-report.md`
- `ARTIFACT_INDEX.md`
- `NEXT_ACTIONS.md`
- `trackers/destination-database-build-tracker.md`

Evidence produced:

- reusable master validation script
- validation report scaffold
- Termux command path for computed validation

Next action:

Run the master validation script in Termux and commit the computed validation report. If structurally clean, create a master HTML browser.

## 2026-05-12 — Destinations master v2 promotion script created

Type: dataset / script / promotion

Summary:

Created the master promotion utility that will combine the 134-row seed dataset and 225-row clean normalized candidate backlog into `destinations_master_v2.csv`. The script maps both sources into the master schema, assigns stable `DST2-*` IDs, preserves source lineage, infers destination scale, and writes a promotion report.

Files changed:

- `src/codemike/data/destination_master_promotion.py`
- `ARTIFACT_INDEX.md`
- `NEXT_ACTIONS.md`
- `trackers/destination-database-build-tracker.md`

Evidence produced:

- reusable master promotion script
- generated-output plan for `datasets/reference/destinations_master_v2.csv`
- generated-output plan for `reports/evidence/destination-master-v2-promotion-report.md`

Next action:

Run the master promotion script in Termux and commit the generated master CSV and promotion report.

## 2026-05-12 — Destinations master v2 schema created

Type: dataset / schema / promotion

Summary:

Created the canonical master schema for consolidating the 134-row seed dataset and 225-row clean normalized candidate backlog into `destinations_master_v2.csv`. The schema defines stable master IDs, lineage fields, destination scale, taxonomy fields, workflow statuses, verification placeholders, Planner-use status, and promotion rules.

Files changed:

- `datasets/reference/destinations_master_v2_schema.md`
- `ARTIFACT_INDEX.md`
- `NEXT_ACTIONS.md`
- `trackers/destination-database-build-tracker.md`

Evidence produced:

- master field definition
- seed-to-master mapping
- normalized-candidate-to-master mapping
- initial deduplication and safety rules
- promotion script requirements

Next action:

Create `src/codemike/data/destination_master_promotion.py`, then generate `datasets/reference/destinations_master_v2.csv` from Termux.

## 2026-05-12 — Artifact-management layer created

Type: artifact / tracker / governance

Summary:

Created a lightweight artifact-management layer for the CodeMike destination database work. This adds a central artifact index, operational next-actions tracker, decision log, destination database build tracker, and a work-done checkpoint report.

Files changed:

- `ARTIFACT_INDEX.md`
- `NEXT_ACTIONS.md`
- `DECISIONS.md`
- `trackers/destination-database-build-tracker.md`
- `reports/work-done/code-mike-destination-database-work-done-v1.md`

Evidence produced:

- central map of source data, generated data, scripts, reports, trackers, and HTML review artifacts
- decision rationale for layered data architecture, taxonomy-first build, unverified-data handling, and Termux execution
- operational queue for the next validation and master-schema steps
- checkpoint report summarising the destination database work completed so far

Next action:

Run the clean normalized backlog validation in Termux, then proceed to `datasets/reference/destinations_master_v2_schema.md`.

## 2026-05-12 — Remaining destination taxonomy cleanup completed

Type: taxonomy / validation / QA

Summary:

Added the six remaining normalized backlog concepts to the destination taxonomy and normalized backlog validator so the next validation run can reach zero invalid destination types and zero invalid vibe tags.

Files changed:

- `datasets/reference/destination_tag_dictionary.md`
- `src/codemike/data/destination_normalized_validation.py`

Evidence produced:

- accepted destination types: `culture_town`, `lake_hill_station`, `mountain_resort`
- accepted vibe tags: `monastery`, `rain`, `rock_carving`

Next action:

Run `python src/codemike/data/destination_normalized_validation.py` and commit the regenerated computed validation report. If clean, proceed to `datasets/reference/destinations_master_v2_schema.md`.

## 2026-05-12 — Normalized destination backlog validation utility created

Type: dataset / QA / validation

Summary:

Created a validation utility for the normalized 225-row India destination backlog. The validator checks required columns, duplicate keys, normalized destination types, normalized vibes, trip-style tags, context tags, and promotion statuses before master schema design.

Files changed:

- `src/codemike/data/destination_normalized_validation.py`
- `reports/evidence/destination-normalized-backlog-validation-v1.md`

Evidence produced:

- normalized backlog validation readiness rule
- report scaffold for computed validation output

Next action:

Run the validator and commit the regenerated computed report if it changes. Then create `datasets/reference/destinations_master_v2_schema.md`.

## 2026-05-12 — Destination backlog normalisation utility created

Type: dataset / QA / normalisation

Summary:

Created the destination backlog normalisation utility for converting the raw 225-row India expansion backlog into a cleaner intermediate file before master promotion. The utility separates true vibes from trip-style tags, context tags, caution tags, and destination-scale hints.

Files changed:

- `src/codemike/data/destination_backlog_normalization.py`
- `reports/evidence/destination-candidate-backlog-normalisation-v1.md`

Evidence produced:

- normalisation rules for raw candidate values such as `fort`, `temple`, `weekend`, `gateway`, `remote`, and `border`
- report documenting the expected output and next execution artifact

Next action:

Run the normalisation script and commit `datasets/reference/destination_expansion_backlog_india_v1_normalized.csv`.

## 2026-05-12 — Destination candidate backlog taxonomy QA created

Type: dataset / QA / taxonomy

Summary:

Created the first taxonomy validation utility and QA report for the 225-row India destination candidate backlog. The pass checks candidate IDs, duplicate name keys, destination types, vibe tags, priority tiers, and verification statuses against Destination Tag Dictionary v2.

Files changed:

- `src/codemike/data/destination_taxonomy_validation.py`
- `reports/evidence/destination-candidate-backlog-taxonomy-qa-v1.md`

Evidence produced:

- first candidate backlog taxonomy QA report
- identified tag normalisation issues before master promotion
- confirmed candidate ID uniqueness and no exact name-country/name-state duplicates in the first pass

Next action:

Create `datasets/reference/destination_expansion_backlog_india_v1_normalized.csv` before building `destinations_master_v2.csv`.

## 2026-05-12 — Destination tag dictionary v2 and HTML browser created

Type: taxonomy / artifact / interface

Summary:

Expanded the destination tag dictionary into v2 and created a GitHub Pages HTML browser for taxonomy review. The taxonomy now covers destination scale, destination types, vibes, traveller fit, trip styles, caution tags, source confidence, source types, and workflow statuses.

Files changed:

- `datasets/reference/destination_tag_dictionary.md`
- `docs/destination-tag-dictionary.html`
- `docs/index.html`

Evidence produced:

- expanded controlled vocabulary for destination database v2
- interactive taxonomy browser
- Pages landing page link for tag dictionary review

Next action:

Use the tag dictionary to validate the 225-row India candidate backlog and identify non-standard tags before promotion.

## 2026-05-12 — Destination database v2 massive expansion setup

Type: dataset / reference / strategy

Summary:

Started the destination database v2 scale-up. Added a strategy document for building a massive Planner-ready destination database, a controlled tag dictionary, and a 225-row India-only expansion backlog. The system now separates seed destinations from candidate backlog entries so the database can grow without contaminating Planner-ready records.

Files changed:

- `datasets/reference/destination_database_v2_strategy.md`
- `datasets/reference/destination_tag_dictionary.md`
- `datasets/reference/destination_expansion_backlog_india_v1.csv`
- `DATASETS.md`

Evidence produced:

- target scale strategy from 250 rows to 5,000+ rows
- controlled destination vocabulary
- 225 India expansion candidates
- dataset registry scale snapshot showing 359 total seed + candidate records

Next action:

Create a QA/deduplication and promotion pipeline that converts selected backlog candidates into enriched destination records.

## 2026-05-12 — Destination browser v2 and QA report created

Type: artifact / evidence / interface

Summary:

Created a destination database QA report and a GitHub Pages-compatible enriched destination browser v2. Browser v2 loads the 134-row destination seed CSV and applies client-side heuristic enrichment for Planner-style review.

Files changed:

- `reports/evidence/destination-database-qa-v1.md`
- `docs/destination-browser-v2.html`
- `docs/index.html`

Evidence produced:

- destination database QA v1 report
- enriched browser with origin-fit, infant-suitability, fatigue, planning-complexity, medical-access, and Planner-readiness filters
- Pages landing page updated with v2 link

Next action:

Stabilise enrichment rules into a committed enriched CSV or add destination scoring v1 using the v2 enrichment fields.

## 2026-05-05 — HTML artifact layer and destination browser created

Type: artifact / interface

Summary:

Added CodeMike's HTML artifact layer and created the first standalone HTML review artifact: a filterable destination browser for the India and near-India seed database.

Files changed:

- `HTML_ARTIFACTS.md`
- `artifacts/html/README.md`
- `artifacts/html/destination-browser-v1.html`

Evidence produced:

- HTML artifact operating guide
- standalone interactive browser for destination seed review
- visual inspection layer for region, country, type, budget, family suitability, and access complexity

Next action:

Create an enriched destination dataset and update the browser to use enrichment fields such as origin fit, infant suitability, travel fatigue, and planner use status.

## 2026-05-05 — Destination reference database seed created

Type: dataset / reference

Summary:

Started expanding CodeMike's destination database beyond the synthetic trip-options experiment. Added a reference dataset area, schema, and a 134-row seed database covering India and nearby/regionally relevant international destinations.

Files changed:

- `datasets/reference/README.md`
- `datasets/reference/india_region_destinations_schema.md`
- `datasets/reference/india_region_destinations_seed.csv`
- `DATASETS.md`

Evidence produced:

- reference destination schema
- 134-row India and near-India destination seed dataset
- dataset registry entry

Next action:

Create a destination database QA/enrichment pass: region coverage check, duplicate check, schema validation, and fields for nearest airport, origin fit, infant suitability, and verification sources.

## 2026-05-05 — Recommendation scoring source module extracted

Type: productisation / capability

Summary:

Converted the trip-options scoring logic from EXP-001 and EXP-002 into a reusable Python module under `src/codemike/recommendation/`. This begins the productisation path from experiment to reusable source code.

Files changed:

- `src/codemike/__init__.py`
- `src/codemike/recommendation/__init__.py`
- `src/codemike/recommendation/trip_scoring.py`
- `src/codemike/recommendation/README.md`
- `EVIDENCE.md`

Evidence produced:

- reusable source module for scoring and sensitivity ranking
- module documentation
- evidence entry for module extraction

Next action:

Add unit tests and a small CLI/example runner before Planner transfer.

## 2026-05-05 — Recommendation sensitivity analysis v1.1 completed

Type: experiment / evidence

Summary:

Completed sensitivity analysis for the trip-options recommendation scoring experiment. Tested five priority scenarios and identified stable versus preference-sensitive recommendations.

Files changed:

- `datasets/processed/trip_options_sensitivity_v1_1.csv`
- `reports/experiment-reports/trip-options-sensitivity-v1-1.md`
- `EXPERIMENTS.md`
- `EVIDENCE.md`

Evidence produced:

- EXP-002 sensitivity analysis
- scenario-ranked dataset
- stable top recommendation set
- preference-sensitive premium option insight

Next action:

Create a Planner transfer candidate or convert scoring logic into a reusable module under `src/`.

## 2026-05-05 — Recommendation scoring v1 completed

Type: experiment / capability

Summary:

Completed the first recommendation-scoring experiment on the synthetic Planner-style trip options dataset. Produced a scored dataset, experiment report, experiment register entry, evidence register entry, and moved Recommendation Scoring from Level 1 to Level 2.

Files changed:

- `datasets/processed/trip_options_scored_v1.csv`
- `reports/experiment-reports/trip-options-recommendation-scoring-v1.md`
- `EXPERIMENTS.md`
- `EVIDENCE.md`
- `capabilities/recommendation-scoring.md`

Evidence produced:

- EXP-001 recommendation scoring experiment
- ranked dataset of 21 scoreable options
- documented weighted formula and penalty rules
- capability maturity update to Level 2 for Recommendation Scoring

Next action:

Run sensitivity analysis as v1.1 before considering transfer to Planner.

## 2026-05-05 — Computed trip-options EDA completed

Type: evidence / capability

Summary:

Completed the first computed evidence pass on the synthetic Planner-style trip options dataset. Created a processed flagged dataset, an evidence report, updated the evidence register, and moved Data Cleaning plus Exploratory Analysis from Level 1 to Level 2.

Files changed:

- `datasets/processed/README.md`
- `datasets/processed/trip_options_flagged.csv`
- `reports/evidence/trip-options-eda-report.md`
- `EVIDENCE.md`
- `capabilities/data-cleaning.md`
- `capabilities/exploratory-analysis.md`

Evidence produced:

- computed data quality checks
- processed flagged dataset
- EDA evidence report
- capability maturity update to Level 2 for Data Cleaning and Exploratory Analysis

Next action:

Create the first recommendation scoring experiment using the scoreable trip options.

## 2026-05-05 — First synthetic evidence path set up

Type: setup / evidence

Summary:

Created the first concrete evidence path for CodeMike using a synthetic Planner-style trip options dataset. This path is designed to exercise data cleaning, exploratory analysis, recommendation scoring readiness, and dashboard KPI thinking.

Files changed:

- `datasets/synthetic/README.md`
- `datasets/synthetic/trip_options_sample.csv`
- `synthetic-data/trip_options_generator.py`
- `notebooks/00-foundations/README.md`
- `notebooks/00-foundations/trip-options-eda.md`
- `DATASETS.md`
- `EVIDENCE.md`

Evidence produced:

- synthetic dataset generator
- synthetic CSV sample
- EDA scaffold
- dataset registry entry
- evidence register entry

Next action:

Run or write the first computed EDA and cleaning analysis, then update capability maturity where justified.

## 2026-05-05 — First capability cards created

Type: setup / capability

Summary:

Created CodeMike's first eight capability cards and linked them to the reusable pattern library. Each card starts at maturity Level 1 because the method exists but evidence has not yet been produced.

Files changed:

- `capabilities/data-cleaning.md`
- `capabilities/exploratory-analysis.md`
- `capabilities/research-synthesis.md`
- `capabilities/recommendation-scoring.md`
- `capabilities/optimisation-modelling.md`
- `capabilities/model-evaluation.md`
- `capabilities/dashboard-insight-design.md`
- `capabilities/project-transfer.md`
- `capabilities/README.md`

Evidence produced:

- first capability catalogue
- pattern-to-capability mapping
- maturity and evidence requirements for each capability

Next action:

Produce the first evidence artifact using a synthetic dataset and update capability maturity where justified.

## 2026-05-05 — First reusable pattern library created

Type: setup / pattern

Summary:

Created CodeMike's first reusable pattern library. These patterns cover the initial working pipeline from data cleaning and exploratory analysis through research summary, recommendation scoring, optimisation framing, model evaluation, dashboard KPI design, and project transfer planning.

Files changed:

- `patterns/data-cleaning-checklist.md`
- `patterns/eda-notebook-template.md`
- `patterns/research-paper-summary-template.md`
- `patterns/recommendation-scoring-pattern.md`
- `patterns/optimisation-problem-template.md`
- `patterns/model-evaluation-template.md`
- `patterns/dashboard-kpi-pattern.md`
- `patterns/transfer-plan-template.md`
- `patterns/README.md`

Evidence produced:

- first reusable method library
- pattern index
- future candidate pattern list

Next action:

Create first capability cards that reference the pattern library.

## 2026-05-05 — Orientation induction pack created

Type: setup / orientation

Summary:

Created CodeMike's student-life and university induction layer. This gives the AI Postgraduate a non-technical foundation covering academic culture, integrity, conduct, legal/compliance awareness, wellbeing, employability, international context, inclusion, research ethics, professional behaviour, HR readiness, and city/culture awareness.

Files changed:

- `orientation/university-life.md`
- `orientation/academic-integrity.md`
- `orientation/student-conduct.md`
- `orientation/legal-and-compliance.md`
- `orientation/wellbeing-and-support.md`
- `orientation/careers-and-employability.md`
- `orientation/international-student-context.md`
- `orientation/equality-diversity-inclusion.md`
- `orientation/research-ethics.md`
- `orientation/professional-behaviour.md`
- `orientation/hr-and-workplace-readiness.md`
- `orientation/city-and-culture.md`

Evidence produced:

- complete first-pass orientation framework
- cross-links to policy, evidence, responsible AI, supervision, QA, portfolio, and transfer files

Next action:

Begin first capability cards or first reusable patterns.

## 2026-05-05 — Milestone 0 started

Type: setup

Summary:

Initialised CodeMike as the AI Postgraduate capability system for the MSc workspace. Established the repository direction: hybrid now, institutional later.

Files changed:

- `README.md`
- `CLAUDE.md`
- `CODEMIKE.md`
- `STUDENT_LIFE.md`
- `ROADMAP.md`

Evidence produced:

- repository identity and operating model
- six-month roadmap direction

Next action:

Create active capability files and scaffold folders.
