# DES-001 Topic 3 — UX design

Status: deep reading executed; source comparison and browser application complete; ready as input to Lab 03 and to Destination Master Browser v1.1.

Lecture: `curriculum/courses/des-001-design-foundations/lectures/lecture-03-ux-design.md`
Reading pack: `curriculum/courses/des-001-design-foundations/readings/topic-03-ux-design-reading-pack.md`
Lab to be executed against this doc: `curriculum/courses/des-001-design-foundations/labs/lab-03-ux-design-journey-map.md`
Companion topic (UI design): `design/foundations/topic-02-what-is-ui-design.md` and `design/foundations/ui-design-component-rules.md`
Primary assignment artifact: `docs/design-foundations.html`

## 1. Topic definition

UX design is the discipline of **understanding** the user's task, **modelling** the journey they take through it, **designing** the interactions that make the journey succeed, and **evaluating** whether the design actually produces success for real users.

Three deliberate moves in this definition:

1. It uses four verbs (*understand, model, design, evaluate*) so UX design is decision work, not opinion work.
2. It names *modelling* — most explicitly as journey maps — because the model is what makes UI decisions defensible.
3. It anchors quality to *real users succeeding at the task*, not to "feels right" or "looks modern". A UX design without a verifiable outcome is decoration plus opinion.

UX design is distinct from:

- **UI design** — the substrate (Topic 2). UI design is the *what is built*; UX design is the *why and whether-it-worked*.
- **Usability evaluation** — one phase of UX design (the *evaluate* activity), not the whole.
- **User research alone** — research is an input. UX design uses research to model and decide.

## 2. The four canonical UX activities

Every source in this topic — even those that use different vocabulary — converges on a four-activity model:

| Activity | What it asks | Artifact it produces |
|---|---|---|
| **Research** | Who is the user? What is the task? Where does it happen? Why does it matter? | Personas, contexts of use, user-need statements |
| **Modelling** | What is the structure of the task as the user experiences it? | Task analysis, journey maps, mental models |
| **Design** | What sequence of interactions makes the task succeed? | Wireframes, flows, prototypes, interaction specs |
| **Evaluation** | Does the design actually let the user complete the task? | Usability studies, heuristic audits, task-success metrics |

DES-001 Topic 3 sits squarely in the **modelling** activity (journey mapping) and produces the bridge from modelling to **design** (acceptance criteria). Topic 1's heuristic audit was a basic **evaluation** pass. Topics 4–5 (design thinking, HCD) will deepen **research**.

## 3. Source list and type classification

| # | Source | Type | Why it was chosen |
|---|---|---|---|
| S1 | Don Norman — *The Design of Everyday Things* (introduction + user-centred-design chapter) | P (Primary / conceptual) | The conceptual foundation: fit the design to the user, not the user to the design. Source of the seven-stage action model that all journey-mapping traditions inherit. |
| S2 | Nielsen Norman Group — Definition of UX + *10 Usability Heuristics* | P (High-authority) | The broadest UX definition ("all aspects of the end-user's interaction with the company, services, and products") plus the most-cited evaluation framework. |
| S3 | IDEO — *The Field Guide to Human-Centered Design* (Methods section) | A (Applied / methods-heavy) | Practical synthesis techniques: how-might-we statements, journey mapping, insight clustering. The strongest source on *operationalising* research into design moves. |
| S4 | GOV.UK Service Manual — *Learning about users* + *Map a user's journey* | A (Applied / public-service-strict) | The strictest source on user-need form, on "do not start with the solution", and on what a journey map must contain to be useful. Research-evidence links per chapter. |
| S5 | Interaction Design Foundation — *UX Design* (foundations course summary) | X (Cross-check / educational) | A neutral cross-check on the discipline's scope, vocabulary, and method. Useful for checking that an idiosyncratic source isn't being taken as the field consensus. |

| # | Extension source | Type | Why |
|---|---|---|---|
| E1 | Kim Goodwin — *Designing for the Digital Age* (personas + scenarios) | X | The bridge from research artifacts to design artifacts |
| E2 | Indi Young — *Mental Models* | X | Aligning system structure to the user's existing mental model |
| E3 | Peter Morville — UX Honeycomb | X (revisited from Topic 1) | UX quality facets as a journey-level audit lens |
| E4 | Jeff Patton — *User Story Mapping* | X | A story-shaped journey representation; complements GOV.UK |
| E5 | ISO 9241-210 — Human-centred design lifecycle | X (preview of Topic 5) | Standards-grade UX process to cross-check completeness |

This selection covers four traditions (cognitive ergonomics — Norman; usability research — NN/g; design-thinking practice — IDEO; public-service rigour — GOV.UK) plus an educational cross-check. The rubric's minimum is three sources with ≥ 1 primary and ≥ 1 applied; this topic uses five required (two primary, two applied, one cross-check) plus five extension.

## 4. Source-by-source notes

### 4.1 Don Norman — DOET (S1)

**What it teaches.** Norman's central UX claim is the seven-stage action model: a user goes from *goal* → *plan* → *specify* → *perform* → *perceive* → *interpret* → *compare-with-goal* and loops. A design that doesn't support every stage fails at the stage it skips. The book introduces the term "human-centred design" and frames it as fitting the design to the human, not training the human to the design.

**Key claims that carry weight.**

- The two "gulfs": the *gulf of execution* (how does the user act on the system?) and the *gulf of evaluation* (how does the user know what the system did?). Every interaction crosses both. Most UX failures live in one of them.
- *Discoverability* and *understanding* are the user's evaluation. If the user can't see what the system can do or can't tell what just happened, the system has failed regardless of how cleverly it works internally.
- Errors are not the user's fault. A system that produces high error rates has a UX failure, not a user-training problem. The design must make the *correct path the easy path*.

**What it omits or under-emphasises.** Norman's examples are everyday objects (doors, kettles, stoves). The translation to data-review tools requires work; the seven-stage model still applies but the modelling artifacts (personas, journey maps) are not in DOET — they come from later research traditions.

**Strongest takeaway for this topic.** Every reviewer interaction with the browser crosses both gulfs. UX design must close both at every journey step — not just at the showpiece moments. v1's loading/empty/error pane (Lab 02 finding F3) is a gulf-of-evaluation failure: the reviewer perceives the same visual region with the same styling regardless of which of the three states is active.

### 4.2 Nielsen Norman Group (S2)

**What it teaches.** NN/g's definition of UX is the broadest in the field: *"User experience encompasses all aspects of the end-user's interaction with the company, its services, and its products."* This intentional breadth is paired with Nielsen's 10 usability heuristics, which are the most-cited UX evaluation framework on the web.

**Key claims that carry weight.**

- UX is not just the screen. It includes the surrounding service, the support, the recovery from errors, the data quality the user encounters, and the user's confidence at the end.
- Heuristic evaluation is fast, cheap, and reliable for catching *categories* of UX problems. It does not replace user testing for catching *specific* problems.
- Severity ratings matter: a heuristic finding is not a fix-list; it is an input to prioritisation.

**What it omits or under-emphasises.** The breadth is also a weakness: if everything is UX, nothing diagnoses what to fix. NN/g's articles are typically findings or framings, not full process documents — they don't replace IDEO's or GOV.UK's process artifacts.

**Strongest takeaway for this topic.** The breadth matters for the Destination Master Browser because the reviewer's UX includes the *outcome* — did they leave with the correct mental model about data trust? That isn't a screen property; it is a journey property. Topic 1 already used this framing; Topic 3 turns it into testable journey criteria.

### 4.3 IDEO — Field Guide to HCD (S3)

**What it teaches.** IDEO's Field Guide is the most practical source on *how to do UX work*. It is organised by methods: how to plan research, how to recruit, how to conduct interviews, how to synthesise insights, how to construct journey maps, how to generate "how might we" statements, how to prototype, how to iterate. Every method has step-by-step instructions, time estimates, and example outputs.

**Key claims that carry weight.**

- The *Inspiration → Ideation → Implementation* loop is iterative, not sequential. Each phase produces inputs to the next, and the loop is meant to run multiple times per project.
- Synthesis (turning raw research into insights) is the hardest skill in UX and the most under-taught. The Field Guide gives explicit techniques: insight clustering, theme cards, "how might we" reframing.
- Journey maps in IDEO's tradition emphasise *emotional* state alongside actions — what the user feels at each step, not just what they do. This is a deliberate counterweight to purely-functional task analyses.

**What it omits or under-emphasises.** IDEO's framing is consumer-product- and service-shaped. Internal data-review tools (the Destination Master Browser's category) are not a central case. Emotional-state mapping is less directly applicable; the reviewer's "delight" matters less than their cognitive load and trust accuracy.

**Strongest takeaway for this topic.** The journey-map method itself is the most transferable artifact: a seven-step browser journey with goal / cost / failure-mode / trust-check per step is the IDEO journey-map shape adapted to the reviewer task. Emotional state is replaced by trust state.

### 4.4 GOV.UK Service Manual (S4)

**What it teaches.** GOV.UK's Service Manual is the strictest source on UX discipline. Two chapters carry the topic's weight:

- *Learning about users* — defines what user research is and is not. Insists on real users, not stakeholders. Insists on observation alongside interview. Insists on user-need form: `As a [user], I need [outcome], so that [goal]` — *with no UI mechanism named*.
- *Map a user's journey through a service* — defines what a journey map must contain (user, goal, touch-points, pain-points, opportunities) and what it must not contain (the team's preferred solution dressed up as a journey).

**Key claims that carry weight.**

- *User need ≠ user request ≠ solution-shape.* This is the single most important UX discipline GOV.UK enforces. A user who says "I want a reset button" has issued a request that names a UI mechanism (solution-shape). The underlying need is "recover from over-filtering without losing orientation". Designing for the request locks the design; designing for the need keeps options open.
- *Start with the user, not the service.* Many UX failures happen because the team starts with what the service can do and works backward to fit the user. GOV.UK insists on starting with what the user needs to accomplish and working forward.
- *Research evidence per design decision.* Every recommendation in the manual links to research; design choices are defensible by evidence, not by taste.

**What it omits or under-emphasises.** GOV.UK is for transactional public services — applying for a benefit, paying tax, registering for something. It is not for dense reviewer-facing data tools. Its journey-map vocabulary translates well, but its persona work is shaped around citizen archetypes that don't map directly to internal reviewer personas.

**Strongest takeaway for this topic.** The *user-need form* — `As a [reviewer], I need [outcome], so that [goal]` — becomes the canonical statement form for Lab 03. Every browser feature must be defensible against a user need in this form. Features that can't produce one are findings (probably solution-shaped needs in disguise).

### 4.5 Interaction Design Foundation — UX Design (S5)

**What it teaches.** IxDF's UX Design topic course is a neutral cross-check on the discipline. It cites Norman, NN/g, IDEO, and other tradition leaders, and produces an integrated picture of UX as *user research + interaction design + information architecture + usability + accessibility*.

**Key claims that carry weight.**

- UX is multi-disciplinary by construction. Interaction design, information architecture, usability, and accessibility are sub-disciplines, not separate fields.
- The UX designer's primary skill is *translating* between research and design — neither pure research nor pure design.
- The most common UX failure mode is the *implementation-first* trap: starting with "what can we build" rather than "what does the user need to do".

**What it omits or under-emphasises.** As an educational summary, IxDF does not break new ground. It is useful as a sanity-check that the integrated picture from the other four sources is not idiosyncratic.

**Strongest takeaway for this topic.** UX design is *translation*. The acceptance-criteria sheet that Lab 03 produces is exactly a translation: from research-level user needs and journey models to design-level criteria the UI must produce.

## 5. Source comparison

### 5.1 Where the five required sources agree

- UX is broader than UI. Fixing UX requires understanding the user and the task, not just the screen.
- The activities cluster as research / modelling / design / evaluation (vocabulary varies; structure does not).
- Research evidence (real users, real tasks) must back design decisions. Speculation is not UX work.
- Journey maps are the canonical modelling artifact for bridging research to design.
- Designing the happy path only is a failure mode; the empty / failure / recovery paths are where most UX work lives.

### 5.2 Where they differ — by emphasis

| Question | Norman | NN/g | IDEO | GOV.UK | IxDF |
|---|---|---|---|---|---|
| Unit of analysis | The action (seven-stage model) | The whole experience including service | The journey + the emotion at each step | The user-need statement | The full UX-design discipline |
| How strict is "user need vs request"? | Conceptual; not strict | Moderate; named but not enforced | Moderate | **Very strict** (separate chapter; explicit forbidden patterns) | Educational; not enforced |
| Emotional dimension | Implicit (frustration as design failure) | Implicit | **Explicit** (emotion mapped per step) | Mostly absent (task-shaped) | Educational summary |
| Process formality | Loose (book of essays) | Loose | **High** (methods with steps, times, outputs) | **High** (manual with rules) | Educational |
| Public-service rigour | n/a | n/a | n/a | **Maximum** | n/a |
| Reading-age / content discipline | Loose | Moderate | Moderate | **Very strict** (plain English, short sentences) | Educational |
| Coverage of data-review tools | Conceptually applicable | Conceptually applicable | Light (consumer-shaped) | Light (transactional-shaped) | Coverage by inference |

### 5.3 Where they diverge in ways that matter for the browser

- **User-need discipline.** Only GOV.UK enforces the `As a [user], I need [outcome], so that [goal]` form with the *no-UI-mechanism* rule. For an internal tool that has historically been built feature-first ("add a sort control", "add a chip filter"), GOV.UK's discipline is the corrective. Without it, v1.1 risks shipping more solution-shaped features.
- **Emotional state.** IDEO maps emotion per journey step; the other sources do not. For the Destination Master Browser, emotion is replaced by *trust state* — does the reviewer feel safe about the data? IDEO's structure transfers; the content varies.
- **Process formality.** IDEO and GOV.UK provide step-by-step methods; Norman and NN/g provide concepts. A team executing UX work needs both: concepts to know what they're aiming for, methods to know how to get there.
- **Journey-map content.** IDEO's journey-map shape is broader (actions + touchpoints + emotions); GOV.UK's is narrower (user + goal + touch-points + pain-points + opportunities). For the browser, the narrower GOV.UK shape with the *trust state* column added is the right fit.

### 5.4 What each source omits explicitly

- **Norman**: modern web/digital vocabulary; specific patterns; data-trust modelling
- **NN/g**: process artifacts (it has findings but not full method packs)
- **IDEO**: internal-tool framing; the strict user-need form
- **GOV.UK**: emotion / delight; complex enterprise data tools; charts; drawers
- **IxDF**: original framings (it is a summary)

No single source is sufficient. The five together cover the topic.

## 6. User need vs user request vs solution-shape

The most operationally useful Topic 3 distinction — sourced primarily from GOV.UK with reinforcement from Norman (designing for the user, not for the team's assumptions) — is the three-way classification:

| Class | Form | Test | Example |
|---|---|---|---|
| **User need** | `As a [user], I need [outcome], so that [goal]` | Names no UI mechanism; testable as a behaviour | "As a reviewer, I need to recover from over-filtering, so that I can keep working efficiently" |
| **User request** | A user actually said this, but it names a mechanism | Came from a real user; names a UI mechanism | "I want a Reset button" |
| **Solution-shape** | The team's assumption framed as a need | No user evidence; names a mechanism | "Users probably need a sort dropdown" |

The discipline: every v1.1 feature must be defensible against a user need in the GOV.UK form. Requests and solution-shapes are *inputs* to the need-extraction process, not substitutes for it.

Three browser-specific examples:

1. **"I want a Reset button"** (request) → need: *"As a reviewer, I need to recover from over-filtering without losing orientation."* The Reset button is one valid implementation; a Clear-all action in the empty state is another; chip-by-chip removal is another. The need leaves the design open.
2. **"Users probably want a card view"** (solution-shape; assumed by the original v1 design) → need: *"As a reviewer, I need to browse rich-record information one record at a time."* This is a valid need but only for one of the seven journey steps (Inspect-like browsing). Topic 2 already showed Cards-only fails the Compare step; the underlying need wasn't isolated.
3. **"Show the trust state on every record"** (a Lab 01 finding) → need: *"As a reviewer, I need to know each record's trust state at every depth of the journey, so that I do not over-trust or under-trust records."* Topic 2's four-depth trust signal implements this need without naming a specific signifier.

## 7. The reviewer journey (seven steps)

The canonical Destination Master Browser reviewer journey. Each step has *goal / cost / failure mode / trust check*. These are derived from Lab 01 Exercise B (heuristic-level) but specified at the behavioural level required by Topic 3's acceptance criteria.

| # | Step | Goal (user-need form) | Cost budget | Failure mode | Trust check |
|---|---|---|---|---|---|
| 1 | **Arrive** | *As a reviewer, I need to orient to the tool and the dataset within seconds.* | ≤ 5s; no interactions | Reviewer can't tell what tool / what dataset / what state | Top-of-page dataset-trust banner visible |
| 2 | **Understand** | *As a reviewer, I need to read the dataset's overall trust state, so that I treat it appropriately.* | ≤ 10s; no interactions | Over-trust ("Planner-ready") or under-trust ("avoid this tool") | Dataset banner is unambiguous (text + colour + icon) |
| 3 | **Narrow** | *As a reviewer, I need to constrain the result set along any facet, so that I focus on the records I want to review.* | ≤ 3 interactions per facet; ≤ 30s total | Filter applied but reviewer cannot tell which / cannot remove individually | Trust badge present in result list after narrowing |
| 4 | **Compare** | *As a reviewer, I need to scan many records along common attributes, so that I find outliers or candidates.* | ≤ 60s for first comparison pass | Cards-only forces serial reading; sort missing; reviewer loses track | Trust badge in first column of any table mode |
| 5 | **Inspect** | *As a reviewer, I need to read a record's full detail while keeping list context, so that I do not lose my place.* | ≤ 2 interactions; ≤ 5s open | Modal blocks list; back-button breaks context | Trust banner persistent in drawer header |
| 6 | **Recover** | *As a reviewer, I need to escape an over-filtered state and adjust filters individually, so that I keep working efficiently.* | ≤ 1 interaction to clear all; ≤ 1 interaction per filter to remove individually | Reset hidden; no active-filter summary; reviewer restarts | Trust badge survives recovery (still shown after narrow → empty → recover) |
| 7 | **Leave** | *As a reviewer, I need to leave with an accurate mental model of which records I reviewed and their trust state, so that downstream decisions are correct.* | n/a (journey end) | Reviewer over-confident; trust state was lost during inspection | Final trust state seen during the journey was honest |

Each step's failure mode names a real v1 limitation or a Lab 02 finding. The trust-check column makes the four-depth trust signal (Topic 2 §6.2 / rule sheet §7) operational *journey-step-by-step*.

## 8. UX acceptance criteria — form and examples

A UX acceptance criterion is a *testable, behavioural* statement of what the reviewer must be able to do, expressed independently of the UI mechanism. The standard form:

```text
The reviewer can [behaviour], in [cost budget], with [feedback requirement].
```

Three worked examples:

**Criterion U-NAR-1 (Narrow):** *The reviewer can apply, combine, and remove filters along any facet without leaving the result-list view. Every applied filter is visible without scrolling and is individually removable. The result-count updates within 300ms of each interaction and the change is perceptible.* — Closes Lab 01 finding on "no active-filter summary"; cross-refs Topic 2 rule sheet §4 and §8 (active-filter summary row).

**Criterion U-INS-1 (Inspect):** *The reviewer can open a record's full detail in ≤ 2 interactions (≤ 1 from a list row), keeping the list visible behind the detail. The detail closes in 1 interaction (button, Esc key, or click outside) and returns the reviewer to the list at the same scroll position.* — Closes Lab 01 finding on "no drawer"; cross-refs Topic 2 rule sheet §3.4 (drawer) and §8 (record-detail drawer row).

**Criterion U-REC-1 (Recover):** *From any empty-result state, the reviewer can return to a non-empty result set in ≤ 1 interaction. The active filters are listed in the empty state and are individually removable. A "Clear all" action is the explicit recovery affordance.* — Closes Lab 01 finding on "no reset / no recovery"; cross-refs Topic 2 rule sheet §3 (containers) and §8 (empty state row).

Lab 03 will produce the full set of criteria — at least one per journey step, with the priority subset marked as v1.1 UX gates.

## 9. CodeMike interpretation

For the CodeMike workspace, UX design is the discipline that converts research and modelling into *testable behavioural criteria the UI must produce*. Two stricter framings come out of the five-source synthesis:

1. **Every feature has a user-need statement in the GOV.UK form.** A feature that can't be defended against a user need (no UI mechanism named) is solution-shape and is refused. Topic 2's rule sheet specifies *what to build*; Topic 3 specifies *why and for whom*.
2. **Every journey step has at least one acceptance criterion.** Without criteria, the journey is a story rather than a specification. With criteria, two evaluators reach the same verdict on the same design.

The CodeMike-shaped working definition:

> UX design = (extract user needs in GOV.UK form) + (model the journey with goal / cost / failure / trust per step) + (write testable acceptance criteria per step) + (verify the design produces those criteria) + (audit the design against UX anti-patterns)

Anything outside this — visual treatment that doesn't change behaviour, copy changes that don't affect comprehension, additions unmotivated by a user need — is downstream or out of scope.

## 10. Application to the Destination Master Browser

### 10.1 Pattern decisions that follow from the topic

Topic 2 named the master-browser pattern (master-detail with faceted filtering) at the *component* level. Topic 3 specifies the *journey* through that pattern.

| Decision | Choice | Justification | Sources |
|---|---|---|---|
| Journey shape | Seven steps: arrive / understand / narrow / compare / inspect / recover / leave | GOV.UK journey-map structure with trust-check column added | S4, S2 |
| User-need form | `As a [reviewer], I need [outcome], so that [goal]` — UI mechanism not named | GOV.UK strict form | S4 |
| Trust check per step | Every step has a defined trust signal that must be visible at that depth | Topic 1 finding + Topic 2 §6.2 four-depth spec, operationalised per step | S2, Topic 2 |
| Cost budget per step | Interactions / time / cognitive cost named per step | IDEO process formality + Norman gulfs | S1, S3 |
| Failure mode per step | Each step has a named failure mode the design must prevent | Norman gulfs + NN/g heuristic-style framing | S1, S2 |
| Acceptance criteria | 1–3 per step, behavioural, testable | IxDF translation framing + GOV.UK form | S5, S4 |
| Need-vs-request audit | Every browser feature must produce a user need (GOV.UK form) | GOV.UK discipline | S4 |
| Empty / loading / error as first-class journey states | Designed for the empty / loading / error path — not the happy path only | Norman gulf-of-evaluation; Topic 2 finding F3 | S1, Topic 2 |

### 10.2 v1.1 UX gates — the criteria that must pass

The full set lives in `design/foundations/ux-acceptance-criteria.md` (Lab 03 output). The high-priority subset, scoped here for the deep-reading layer:

1. **Arrive** within 5s, dataset trust state visible without interaction.
2. **Narrow** with active-filter summary visible, individually removable, ≤ 3 interactions per facet.
3. **Compare** in table mode with sortable columns; cards-only is no longer the default.
4. **Inspect** opens a drawer in ≤ 2 interactions, list context preserved, trust banner in drawer header.
5. **Recover** from any empty-result state in ≤ 1 interaction; active-filter summary lists the current narrowing.
6. **Trust signal survives every depth** — list row, table row, drawer header — with the seven-state trust badge from Topic 2 rule sheet §7.

These are the *journey-level companion* to Topic 2's component rule sheet. Both sheets are required before v1.1 ships.

### 10.3 Gap closure against Lab 01

| Lab 01 finding | Topic 3 treatment | Closed by v1.1? |
|---|---|---|
| No reset / no recovery affordance | Criterion U-REC-1 (recover ≤ 1 interaction) + need extraction | Yes |
| No active-filter summary | Criterion U-NAR-1 (narrow with visible active filters) | Yes |
| No detail inspection | Criterion U-INS-1 (drawer ≤ 2 interactions) | Yes |
| Cards-only for compare task | Topic 2 §3.2 (table as default) + criterion U-COM-1 (compare task) | Yes |
| Trust signal not preserved in deeper contexts | Trust-check column in journey map + Topic 2 §6.2 four-depth spec | Yes |
| Empty state silent / loading silent / error silent | Topic 2 finding F3 + criterion at each journey step | Yes |
| Modal-vs-drawer for inspect | Topic 2 §3.4 + criterion U-INS-1 (non-modal) | Yes |

All seven Lab 01 findings are closeable by v1.1 once both Topic 2's rule sheet and Topic 3's acceptance-criteria sheet are implemented.

## 11. Anti-patterns to refuse

Topic 3 identifies four UX anti-patterns specific to data-review tools. The v1.1 redesign and any subsequent design work must refuse each:

1. **Designing the happy path only.** Data-review tools spend most reviewer-time in non-happy paths (empty results, conflicts, missing fields, blocked statuses). A design that fully specifies "browse → find → open" and treats empty / error / loading as edge cases is a UX failure for a tool where the edge cases are the work. (Norman gulfs; Lab 02 finding F3.)
2. **Confusing user request with user need.** Designing for what users said (mechanism-named) instead of what they need (outcome-named) locks the design unnecessarily and ships solution-shape features. (GOV.UK discipline.)
3. **Skipping evaluation.** Shipping a journey that was never tested against real reviewer behaviour. The acceptance-criteria sheet is the *minimum* evaluation gate; user testing is the next step. (NN/g + Norman.)
4. **Ignoring the trust check at depth.** Topic 1's finding carried forward: trust state must survive every journey step, not just the list. A design that signals trust on the list and silently drops it in the detail or after-filter is a journey UX failure. (Lab 01 + Topic 2 §6.2.)

Each is sourced from ≥ 2 of the five required Topic 3 sources or carries forward from prior topics.

## 12. Implementation implications for Browser v1.1

The Lab 03 output at `design/foundations/ux-acceptance-criteria.md` will be the canonical UX gate. Together with Topic 2's `ui-design-component-rules.md`, it forms Browser v1.1's full specification. Implementation work that Topic 3 adds to the v1.1 commitment (beyond Topic 2's component work):

1. **Add a Need column to the v1.1 backlog** — every backlog item has a user need in GOV.UK form. Items without one are refused.
2. **Add an Acceptance-criterion column to the v1.1 backlog** — every backlog item has at least one acceptance criterion drawn from `ux-acceptance-criteria.md`.
3. **Add a reviewer-walk-through test** before any v1.1 PR merges — for each of the seven journey steps, a reviewer (real or simulated) walks the v1.1 build and the design passes only if every criterion is satisfied.
4. **Add an empty / loading / error verification** — each of the three non-happy-path states must be intentionally triggered and verified against its acceptance criterion.
5. **Defer all v1.1 features not justified by an acceptance criterion** — including visual polish, additional filter facets, batch actions, and analytic dashboards.

## 13. Further reading and exercise tasks

The reading pack lists five extension sources. The applied exercises Lab 03 will execute against this topic:

- **Full journey map** — seven steps × five columns (goal / cost / failure / trust / current-v1).
- **Acceptance-criteria sheet** — 7–15 criteria, each cross-referenced to journey step + Topic 2 rule-sheet component + Lab 01 finding.
- **User-need extraction** — every browser feature audited as need / request / solution-shape.
- **Lab 01 → Lab 03 gap analysis** — table mapping every Lab 01 finding to its Topic 3 criterion + Lab 02 component.
- **Topic 3 anti-pattern check** against the checklist at master-browser-design-checklist.md (Lab 03 will append a Topic 3 section).

Lab 03's decision gate is *reproducibility*: a second evaluator applying the acceptance-criteria sheet to v1 must reach the same pass/fail verdicts.

## 14. Reusable CodeMike capability extracted from this topic

Three reusable capabilities the workspace gains from Topic 3:

1. **Seven-step reviewer-journey template** — applicable to any data-review tool (datasets browser, validator review, Planner review). Combines GOV.UK journey-map structure with a trust-check column. Lives in `capabilities/` once promoted.
2. **UX acceptance-criterion form** — *"The reviewer can [behaviour], in [cost budget], with [feedback requirement]"* — applicable to any UX work across the workspace. The form is testable and reproducible by construction.
3. **User-need vs request vs solution-shape triage** — applicable to any product-decision intake. GOV.UK-derived classification that prevents solution-shape features from passing as user needs.

Combined with Topic 2's three capabilities (master-detail pattern, nine-state checklist, affordance triple-check), the workspace now has six reusable design capabilities — close to the threshold where a formal capability-card template makes sense.

## 15. Reflection on the source set

The reading was honest in one specific way: no two sources said the same thing. Norman supplied the conceptual ground (gulfs, action stages, errors as design failures). NN/g supplied the breadth of UX scope and the most-cited evaluation framework. IDEO supplied the methods and the synthesis techniques. GOV.UK supplied the user-need discipline that none of the others enforce. IxDF supplied the integrated picture as a cross-check.

A single-source stop would have cost differently per source. Stopping at Norman: no journey-map artifact, no user-need form. Stopping at NN/g: no method packs, no user-need discipline. Stopping at IDEO: no public-service strictness, weaker user-need form. Stopping at GOV.UK: no emotional dimension, weaker on consumer products. The five together produce a working UX vocabulary for the Destination Master Browser that none alone could.

The most operationally significant lesson is GOV.UK's user-need discipline. The other four sources are conceptually rigorous about UX but permit the team to drift into solution-shape language; GOV.UK alone enforces the discipline that prevents this drift. For an internal tool with a history of feature-first thinking, this is the single most important corrective the topic introduces.

## 16. Open work

- Run **Lab 03** against this topic (`labs/lab-03-ux-design-journey-map.md`).
- Produce the **consolidated UX acceptance-criteria sheet** at `design/foundations/ux-acceptance-criteria.md`.
- After Lab 03 closes, implement **Browser v1.1** against (Topic 2's component rule sheet) + (Topic 3's UX acceptance-criteria sheet) + the master-browser checklist (Topic 1 §3 + Topic 2 §18 + Topic 3 §20).
- Topics 4–5 (Design thinking; HCD) will deepen the research/modelling activities.
