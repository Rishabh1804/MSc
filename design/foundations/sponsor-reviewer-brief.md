# Sponsor Reviewer Brief — Destination Master Browser

Status: **v2** of the Sponsor Reviewer recruitment + onboarding framework. v1 created 2026-05-18 to close NEXT_ACTIONS priority 9 (recruitment infrastructure) and unblock Lab 05 F-PRIN-1 / F-EVAL-1 / Lab 06 Fix #5b. v2 (this revision) adds **source-citation completeness** and **unknown-field discipline** as first-class evaluation criteria — added in the governance-debt PR following the §19 policy adoption (no-assumption + live-data rule). The Sponsor Reviewer session is now also the human-grade evaluation gate for the v2 source-backed enrichment service when it ships (P21).

Owner: CodeMike (workspace) — coordinated with Rishabh.

v2 revision history: §9 added; §3 Part 2 + §4 unchanged; §5 closure-path table extended with two new rows; §3 Part 3 debrief Q-list unchanged (the new criteria are evaluated *across* the existing tasks, not via new tasks).

---

## 1. Why this role exists

Two labs depend on a real reviewer's input:

- **Lab 05 (HCD audit)** identified that v1.1 has *no human-grade evaluation*. Principle 2 of ISO 9241-210 (Users involved throughout) is the only outright **Fail** in the audit (F-PRIN-1, High severity). Closure requires at least one real reviewer testing v1.1's behaviour against the 14 acceptance criteria — not a substitute, a prerequisite.
- **Lab 06 (Gestalt audit)** identified F-GES-5 as a false-positive grouping between the toolbar's search input and its filter selects (different interaction grammars — live-update vs commit-on-change — that the visual treatment groups together). Fix #5a (visual separation) shipped in the v1.1.x polish PR; Fix #5b (grammar unification: would the workspace make selects live-update too?) is deferred to v1.2 because the right answer depends on what a real reviewer expects after working with the tool for a session.

Neither problem can be solved by the single-person workspace. Both need a person who actually does the QA-review work the tool is built for.

This brief defines who that person should be, what we'd ask them to do, what format their feedback should take, and how their feedback feeds into v1.2.

## 2. Who the Sponsor Reviewer should be

Required profile:

- **Domain experience**: has done dataset-QA review work in the past — checking records for verification status, deciding which records are ready for downstream consumption (a "Planner-ready" decision in this domain). Specific tools they've used don't matter; the *shape of the work* does.
- **Real reviewer time**: willing to spend ~2–3 hours in a single session walking through v1.1 against a representative subset of the 359-row `destinations_master_v2.csv` reference dataset. Not a focus-group sweep — a real review session.
- **Articulate failure-mode reporting**: can describe what surprised them, what they expected and didn't get, where they had to re-read or re-derive context, where they almost made a wrong promote-decision. Comfortable saying "I don't know what this means" when the trust signal is unclear.

Preferred profile:

- **Two reviewers** rather than one — Topic 5 §3 Principle 6 (Multidisciplinary team) is the most-stretched principle for solo workspaces, and two reviewers approach this from independent angles. If two is not feasible, one is acceptable with the limitation named in the v1.2 closure write-up.
- **At least one reviewer using assistive technology** (screen reader, keyboard-only navigation, low-vision magnifier) — closes Lab 05 F-W3C-1 (Accessibility lens Partial). If not available, accessibility re-testing is queued for v2.x and named honestly.
- **Inclusion lens** — at least one reviewer whose first language is not English, OR who uses the tool on a low-bandwidth connection, OR on mobile, OR with a different cultural framing of QA work. Each adds an inclusion-sub-dimension that Lab 05 F-REQ-2 / F-W3C-1 named as a Fail. Not all required for v1.2; at least one closes one sub-dimension.

Not required:

- Software engineering background — the reviewer doesn't need to read code
- Familiarity with the DES-001 curriculum — irrelevant to the review task
- Investment in the workspace's design discipline — fresh-eye is the value

Time budget: ~3 hours of the reviewer's time per session. One review session pre-v1.2; one follow-up session post-v1.2 ship to verify closures (Audit 2 cycle per NEXT_ACTIONS priority 11).

Compensation: per workspace tooling budget (`charter/BUDGET.md`); requires Rishabh approval if a paid compensation rate is chosen. Default is an informal exchange (reciprocal review, peer-time trade) but a paid hour-rate is the cleaner option if the reviewer's time is genuinely scarce.

## 3. What we'd ask them to do

A reviewer session has three parts, totalling ~3 hours.

### Part 1 — Orient (30 min)

The reviewer opens `docs/destination-master-browser.html` on their own machine (or via the GitHub Pages deployment). They are given:

- The seven-step reviewer journey from `design/foundations/topic-03-ux-design.md` §7 (arrive → understand → narrow → compare → inspect → recover → leave) as the orientation frame
- The 14 v1.1 acceptance criteria from `design/foundations/ux-acceptance-criteria.md` §2 as the things-to-check list
- *No* implementation context: not what we built, not what we expect, not what failed in v1
- *No* prompting on Lab 05 / Lab 06 findings (the findings are our hypotheses; the reviewer is the test)

They're asked to read the trust banner + page header + stats banner, then narrate (out loud or in writing) their initial impression of:

- What the tool is for
- Who it's for
- What state the data is in
- What they'd be cautious about before acting on the data

### Part 2 — Task (90 min)

The reviewer is given two concrete scoped tasks:

**Task A — Find candidates for promotion** (45 min):
> "Find five records in this dataset that are not yet Planner-ready but could be promoted with light verification. Tell us *which records* and *why* you'd promote each one."

This exercises: narrowing (filters + search), comparing (sortable columns + cards toggle), inspecting (drawer), trust evaluation (badge + verification field + Planner status), and recovery (clear-all, back-out).

**Task B — Find records to flag for caution** (45 min):
> "Find any records that you would *not* want to promote — anything that looks unverified, blocked, missing fields, or has a caution tag. Tell us *what's wrong* and *what evidence* led you to flag each one."

This exercises: trust-signal recognition at multiple depths, anti-pattern detection (over-trust), caution-chip noticing, and the "what's wrong" articulation.

Both tasks are timed loosely (45 min target) but the reviewer can take longer if needed; the *time* is data (Topic 3's cost budgets), not a hard limit.

### Part 3 — Debrief (60 min)

The reviewer answers structured questions (recorded in writing OR transcribed from a recording):

1. **Trust signal**: at any moment did the trust signal disappear, contradict itself, or feel ambiguous? Where? What did you do about it?
2. **Narrowing**: did the search input + filter selects feel like one group of narrowing controls, or two different control categories? (Lab 06 F-GES-5 falsification — this is the question that adjudicates Fix #5b.)
3. **Card vs table**: which view did you prefer for which task? Did the table's verification column elevation (the pill, post-polish) actually help, or felt like noise?
4. **Empty / loading / error**: did you encounter any of these? If yes, did the state tell you enough to recover?
5. **Drawer**: did you read the drawer-trust banner, or skip past it? Were the body sections in the right order?
6. **Surprises**: anything that surprised you, where you expected one behaviour and got another?
7. **Missing**: anything the tool *should* have done that it didn't?
8. **Confidence**: on a scale of 1–10, how confident would you be promoting your five Task-A picks to Planner-ready? What would raise that score?

The eight questions map back to specific Lab 04/05/06 findings — but the reviewer doesn't see that mapping; they answer the question, we do the mapping.

## 4. Format of their feedback

Three deliverables per session:

1. **Annotated screenshot bundle** — the reviewer captures screenshots (any platform) of the moments when something surprised them, confused them, or worked particularly well. Each screenshot is annotated with one sentence: "I expected X; the tool did Y."
2. **Debrief responses** — written or transcribed answers to the eight Part-3 questions. Free-form length; one paragraph per question is the target minimum.
3. **Confidence-rating table** — a simple table:

   | Task | Records picked | Confidence (1–10) | What would raise confidence |
   |---|---|---:|---|
   | A (promote) | 5 records | _ | _ |
   | B (flag) | N records | _ | _ |

Storage location for received feedback: `curriculum/courses/des-001-design-foundations/feedback/sponsor-reviewer-N/` (one folder per reviewer session; N=1 for the first session). The session folder contains the screenshot bundle + debrief responses + confidence table + any session-recording (if recorded).

## 5. How feedback feeds into v1.2

The Sponsor Reviewer feedback is treated as **Audit 1.5** — a real-user evaluation grade running between Audit 1 (Lab 05 + Lab 06 introspective audits) and Audit 2 (post-v1.2 closure verification).

Specific closure paths:

| Lab finding | Sponsor Reviewer input that closes it |
|---|---|
| **Lab 05 F-PRIN-1** (High; Principle 2: Users involved throughout) | One real reviewer session = closure. Two = clean closure. |
| **Lab 05 F-EVAL-1** (High; human-grade evaluation absent) | Same session closes this. |
| **Lab 05 F-W3C-1** (High; Inclusion lens Fail) | One reviewer per inclusion sub-dimension (≥1 partial closure); five sub-dimensions = full closure (probably v2.x not v1.2). |
| **Lab 06 Fix #5b** (search-vs-select grammar unification) | Debrief Q2 answer adjudicates: if reviewers expect live-update, do it; if reviewers expect commit-on-change, leave it; if reviewers don't notice, leave it (no behaviour change). |
| **Lab 04 Loop 1 U-CONF-1..4** (now landed in `ux-acceptance-criteria.md`) | When the v1.2 batch-promote feature lands, the Sponsor Reviewer evaluates the confirm-modal anatomy against the four criteria. |
| **Audit 2 trigger** (NEXT_ACTIONS priority 11) | Post-v1.2 Sponsor Reviewer session re-tests against the same eight debrief questions; differences vs Audit 1.5 are the audit's findings. |
| **§9 source-citation completeness criterion** (v2, added 2026-05-18 — for v2 source-backed builds, P21) | When P21 ships, the Sponsor Reviewer evaluates the per-field source-citation surface — can they trace any visible enriched value to its source, source-tier, and fetch date in ≤2 interactions? Pass = yes; partial = yes for stable-derived, not live-volatile (or vice versa); fail = source provenance is not surface-visible. |
| **§9 unknown-field discipline criterion** (v2, added 2026-05-18 — for v2 source-backed builds, P21) | When P21 ships, the Sponsor Reviewer evaluates the unknown-discipline surface — does the tool clearly distinguish `known` (source-cited) from `unknown_pending_research` from "not applicable"? Pass = three states visibly distinct; partial = two of three states distinguished; fail = unknowns presented as blanks / defaults / dashes indistinguishable from "not applicable". |

Each feedback item gets classified per the Topic 3 framework: **user need** (→ adds to backlog with GOV.UK form), **user request** (→ rewritten to a need, then evaluated), or **solution-shape** (→ rejected unless it sharpens a need).

## 6. Recruitment process

CodeMike doesn't recruit directly — Rishabh decides whether to recruit and from where. This brief gives the recruitment decision a concrete shape so it can happen quickly when authorised.

Recruitment sources to consider (Rishabh decides):

1. **Internal network** — colleagues, former teammates, classmates who've done data-QA work
2. **Codex network** — the broader workspace has connections; this is the natural first ask
3. **Hire** — a paid hour-rate recruitment if the network doesn't produce a fit (requires `charter/BUDGET.md` update + Rishabh approval per workspace tooling rule)
4. **Self-as-Sponsor (interim)** — Rishabh does the review session in lieu of a third party. *Honestly named limitation*: this is still single-person work; it closes F-PRIN-1 only partially. Better than nothing; not as good as a real third party.

The recruitment ask (one-paragraph version for forwarding):

> *"I'm building a data-QA review tool for an internal reference dataset. I have a design audit that found six findings I think a real reviewer's eye would either confirm or refute — and one specific question (does the search input vs filter selects feel like one group or two?) that I can't answer without a real reviewer's session. The ask is ~3 hours of your time: 30 min orient, 90 min two scoped review tasks against the live build, 60 min structured debrief. You don't need any prep or context; the value is your fresh-eye honesty. Are you up for it?"*

## 7. Honest limitations of this brief

Three limitations to name (Topic 5 discipline — name limitations explicitly):

1. **One reviewer is not enough for inclusion-lens closure.** F-W3C-1 has five sub-dimensions (language, bandwidth, device, cultural context, terminology). A single reviewer closes at most one sub-dimension; the rest stay open. Full closure is a v2.x problem, not v1.2.
2. **Self-as-Sponsor is a fallback, not a closure.** If no third-party Sponsor Reviewer is recruited and Rishabh does the session himself, F-PRIN-1 is *partially* closed (better than nothing; still single-person evaluation). Audit 2 should not pretend self-as-Sponsor is equivalent to third-party.
3. **The brief itself is single-person work.** This brief was authored by the workspace, not co-authored with a target reviewer or evaluated by an HCD practitioner. A future iteration of this brief (post-Sponsor-Reviewer feedback) should incorporate the reviewer's own observations on what the session should have asked.

These limitations are *named* per the HCD discipline. The brief is HCD-substantial because the limitations are visible and queued for closure, not silenced.

## 8. Status

- **v1 of this brief**: landed 2026-05-18 in PR #26
- **v2 of this brief**: landed 2026-05-19 in the governance-debt PR (this revision) — §9 source-citation + unknown-field discipline criteria added
- **First recruitment ask**: pending Rishabh's decision on source (network / hire / self-as-Sponsor)
- **First reviewer session**: scheduled after recruitment lands
- **Audit 1.5 closure cycle**: after the first session — produces a new feedback file, updates the v1.2 backlog, and re-grades the Lab 05 + Lab 06 findings
- **Audit 2 trigger**: after v1.2 ships, re-run the same session to verify closures
- **Audit 3 trigger** (v2 addition): after P21 ships — full cycle definition lives in §9.4 (criteria + closure paths + skill-row promotion gates)

## 9. v2 evaluation criteria — source-citation completeness + unknown-field discipline

Added 2026-05-19 in the governance-debt PR following workspace adoption of the no-assumption + live-data + free-tier-only policy (strategy doc §19) and two-tier architecture decision (§19.6). The criteria are *forward-looking*: they apply to the v2 source-backed builds (P21) and cannot be meaningfully scored against the v1.0 heuristic baseline (which by design does not carry per-field source citations). For v1.x sessions before P21 ships, §9 is a *pre-recorded* part of the brief that the reviewer can read for context; for post-P21 sessions, §9 becomes a required evaluation surface alongside §3's tasks.

### 9.1 Why these criteria are first-class

The §19 policy revision moved the workspace from "every enriched field is heuristic-derived" to "every enriched field is either source-backed (with citation) or `unknown_pending_research`". That is a category change in what a reviewer needs to evaluate — not just *whether the field looks right*, but *whether the field tells the truth about its own provenance*. A field that looks right but cannot be traced to its source is not v2-ready, regardless of how plausible the value seems. A field that says "unknown" honestly is more trustworthy than a field that looks specific but lacks citation. The Sponsor Reviewer's fresh-eye is the right instrument for this evaluation because the workspace's own judgement on its own data is the kind of judgement the §19 policy explicitly distrusts.

### 9.2 Source-citation completeness — evaluation surface

The reviewer evaluates: **for any visible enriched field, can I trace this value to its source (source name + source tier + fetch date) in ≤2 interactions from where I see it?**

- **Pass** — every visible field on the card / table / drawer has a source affordance (icon / inline citation / drawer-section) that reveals source + tier + fetch date in one click (or one expand). Tier-stable and tier-live fields both satisfy this.
- **Partial** — only some fields satisfy the trace test. Common partial: stable-derived layer fields cite sources cleanly; live-volatile fields show the value but not the "fetched at" timestamp.
- **Fail** — at least one visible field has no traceable source surface, OR the surface exists but reveals only the source *name* and not the tier / fetch date.

Reviewer instruction (added to Part 2 of the session for P21+ tools):
> *"Pick three enriched fields from any record — **including at least one tier-stable field (e.g. route distance, baseline climatology, altitude) and at least one tier-live field (e.g. current flight, current weather, current permit)**. For each, find the source citation. If you can't, tell us where you looked first and what you expected to find."*

The tier-stable + tier-live requirement is deliberate: §19.6's two-tier architecture means the source-citation surface has *two* failure modes (stable-derived layer cites cleanly but live-volatile doesn't carry `fetched_at`, or vice versa). A reviewer left to sample purely by visual salience would tend to pick the easy-to-cite fields and miss the harder layer. The three picked fields + their source-trace verdicts feed Audit 3.

### 9.3 Unknown-field discipline — evaluation surface

The reviewer evaluates: **does the tool visibly distinguish three states — `known` (source-cited), `unknown_pending_research` (source checked, value missing, manual research needed), and not-applicable (this field does not apply to this destination type)?**

- **Pass** — all three states have distinct visual treatments (e.g. value text vs `Unknown — research pending` chip with research-status link vs `—` or `n/a` dimmed). No confusion between the three.
- **Partial** — two of three states are distinct; the third collapses into one of the other two (commonly: `unknown_pending_research` collapses into not-applicable, both rendered as blanks).
- **Fail** — unknowns and not-applicables both render as blank / dash / default — the reviewer cannot tell from the surface whether the field was checked-and-missing or never-applicable. This silently violates the §19.5 unknown-discipline rule even when the underlying data is correct.

Reviewer instruction (added to Part 2 of the session for P21+ tools):
> *"Find a record that has at least one field you can tell is 'unknown'. Tell us whether you can also tell — without opening the source dataset — whether the field was checked-and-missing or doesn't apply to this destination type."*

The reviewer's answer adjudicates the unknown-discipline verdict.

### 9.4 Audit 3 — when v2 ships (P21)

After P21 ships, the Sponsor Reviewer session repeats Parts 1–3 from §3 with §9's §9.2 + §9.3 evaluation surfaces added to Part 2. The session output becomes Audit 3 (parallel to Audit 1.5 + Audit 2). Audit 3's findings feed:

- Final closure of Lab 05 F-PRIN-1 / F-EVAL-1 for the v2 build (separate from the v1.1 closure already credited)
- Promotion decision on the calibration-cycle capability (currently maturity 2; second worked example via P20 + P21 promotes to maturity 3 — see `operations/CAPABILITIES.md`)
- Big Data Analytics + Data Engineering skill rows promotion from level 2 to level 3 in `operations/SKILL_MAP.md`

### 9.5 Honest limitations of the v2 criteria

Three to name (HCD discipline — name limitations explicitly):

1. **The criteria don't apply pre-P21.** v1.0 heuristic baseline cannot pass §9.2 because the v1.0 design explicitly does not carry per-field source citations. Running §9.2 against v1.0 would always return *fail* by construction; that's a category-mismatch, not a finding. Use §9 *only* for v2 source-backed surfaces.
2. **§9.2 evaluates the *tool*, not the *source registry*.** A tool can satisfy §9.2 (every field traceable) while its underlying source registry contains errors. Source-registry correctness is a separate audit, owned by the data-engineering workstream (not the Sponsor Reviewer).
3. **§9.3 evaluates the *surface*, not the *honesty of the underlying classification*.** The tool can render three distinct states correctly while incorrectly classifying which field falls into which state. Classification correctness is again the data-engineering workstream's audit, not the reviewer's.

These limitations are *named* per the §19.9 honest-limitations discipline.
