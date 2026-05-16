# DES-001 Topic 2 — What is UI design

Status: Deep reading executed; source comparison and browser application complete; ready as input to Lab 02 and to Destination Master Browser v1.1.

Lecture: `curriculum/courses/des-001-design-foundations/lectures/lecture-02-what-is-ui-design.md`
Reading pack: `curriculum/courses/des-001-design-foundations/readings/topic-02-what-is-ui-design-reading-pack.md`
Lab to be executed against this doc: `curriculum/courses/des-001-design-foundations/labs/lab-02-ui-design-component-inventory.md`
Primary assignment artifact: `docs/design-foundations.html`

## 1. Topic definition

UI design is the discipline of **choosing** which interface elements appear, **arranging** them in space and hierarchy, **specifying their behaviour across all states**, and **visually treating** them — so that a user can complete a task with low cognitive cost and unambiguous feedback. Visual design (colour, typography, illustration, mood) is a sub-skill inside UI design; it is not the discipline itself.

This definition makes three deliberate moves:

1. It uses verbs (*choose, arrange, specify, treat*) so that UI design is decision work, not decoration work.
2. It names *state* as first-class, alongside arrangement and treatment, because every interactive element is a small state machine and ignoring state is the most common failure mode in production UIs.
3. It anchors quality to *task completion* and *unambiguous feedback*, so a UI's success is testable rather than aesthetic.

## 2. Source list and type classification

| # | Source | Type | Why it was chosen |
|---|---|---|---|
| S1 | Material Design 3 — *Foundations* and *Components* | A (Applied design system) | The most widely deployed component library on the web. Strong decomposition of foundations (motion, layout, typography, color) versus components, and explicit per-component state guidance. |
| S2 | Apple Human Interface Guidelines — *Foundations* and *Components* | A (Applied design system, platform-led) | The dominant native-platform component vocabulary. Strong on behaviour rules ("a primary action belongs in this position", "use confirmation only when X"). Useful counterweight to web-first systems. |
| S3 | IBM Carbon — *Component patterns* and *Usage guidelines* | A (Applied, enterprise-grade) | Carbon is built for enterprise data interfaces — tables, drawers, filters, structured pages — which is exactly the genre the Destination Master Browser lives in. Accessibility is baked in rather than retrofitted. |
| S4 | GOV.UK Design System — *Components* and *Patterns* | A (Applied, public-sector, content-first) | The most disciplined system on what *not* to add. Each component lists "when to use this", "when not to use this", and "research evidence". Accessibility-first; minimalist by default. |
| S5 | Don Norman — *The Design of Everyday Things* (chapter on affordances, signifiers, feedback) | P (Primary / conceptual foundation) | The conceptual ground all four design systems silently inherit from. Without this layer the systems read like style guides rather than ergonomics. |

| # | Extension source | Type | Why |
|---|---|---|---|
| E1 | Schoger & Wathan — *Refactoring UI* | X (Cross-check) | Visual treatment as a sub-skill within UI design; useful corrective when "UI design = visual design" creeps back in. |
| E2 | Nielsen Norman Group — card / table / modal pattern articles | X | Pattern-specific deep dives for the container-selection question. |
| E3 | Brad Frost — *Atomic Design* | X | Hierarchical decomposition (atoms → molecules → organisms) for thinking about reuse. |
| E4 | WCAG 2.2 / W3C ARIA Authoring Practices (APG) | X (Standards) | Accessibility patterns for interactive components — buttons, dialogs, menus, tabs, listbox. Forms the bridge between UI design and disability access. |
| E5 | Smashing Magazine — "When to use cards vs tables" essays | X | Practitioner essays on container-selection trade-offs; useful applied counter-perspective. |

This selection covers four different design-system traditions (Google web, Apple platform, IBM enterprise, GOV.UK public-sector) plus the primary conceptual foundation. The rubric's minimum is three sources with at least one primary and one applied; this topic uses five required sources (one primary, four applied across different traditions) plus five extension sources.

## 3. Source-by-source notes

### 3.1 Material Design 3 (S1)

**What it teaches.** Material splits the discipline into *foundations* (layout, typography, color, motion, elevation, accessibility, density, sound) and *components* (action chips, buttons, cards, dialogs, drawers, menus, navigation drawer/bar/rail, snackbars, sliders, tabs, text fields, tooltips, top app bar, etc.). Every component page lists: anatomy, behaviour, states, accessibility notes, and dos/don'ts. States are first-class — `enabled`, `disabled`, `hovered`, `focused`, `pressed`, `dragged`, plus loading and error where applicable.

**Key claims that carry weight.**

- Components are *systems*, not just shapes — a "button" is a state machine plus content rules plus a density choice.
- *Density* (compact, default, comfortable) is a global design property, not a per-screen choice; making it global keeps interfaces predictable.
- *Elevation* (the z-axis hierarchy) is a *meaning* tool. Higher elevation = more transient or more interactive. Misuse breaks the user's mental model.
- *Motion* is informational — transitions show *where things came from* and *where they go*. Decorative animation degrades meaning.

**What it omits or under-emphasises.** Material is opinionated about *how* a component should look once you've chosen it, but quieter on *which* component is right for a given task. The "when to use a card vs a list vs a table" question is mostly answered by examples rather than rules. Material also tilts toward consumer product surfaces; data-heavy enterprise screens get less attention than dashboards-with-charts do.

**Strongest takeaway for this topic.** State coverage is a checklist, not an aspiration. Every interactive deserves explicit `default / hover / focus / active / disabled / loading / empty / error / success`, and "the design doesn't show this state" is a finding, not an omission.

### 3.2 Apple Human Interface Guidelines (S2)

**What it teaches.** HIG organises around platforms (iOS, iPadOS, macOS, watchOS, tvOS, visionOS) and then around principles: clarity, deference, depth. The *Components* section covers controls, content views, modalities (alerts, sheets, popovers), navigation, status, and system experiences. HIG is unusually firm on placement and behaviour rules — primary actions on the right (iOS) or bottom (macOS sheets); destructive actions distinguished from cancel; modal scope tightly limited.

**Key claims that carry weight.**

- Consistency with the platform is itself a usability feature. Custom controls cost the user re-learning effort and almost never pay back.
- Modality has a high cost. A modal that blocks the user must be earned — used for a confirm, a destructive choice, or a task that *must* finish before the user can continue. Modal as a default container is anti-pattern.
- The user's *focus* should be on the content, not on the chrome. Chrome that doesn't disappear when content is the point of the screen breaks deference.

**What it omits or under-emphasises.** HIG presumes a native platform. Mapping its rules to a web context (which is the Destination Master Browser's context) requires translation. HIG also under-discusses dense tabular data — Apple's typical user surfaces are consumer-shaped (mail, photos, settings), not data-engineering shaped.

**Strongest takeaway for this topic.** Modal-as-default is a smell. A modal earns its place by blocking the user for something the user must finish or cancel before continuing — not because the designer needed a place to put a form. For the Destination Master Browser, this means inspect-a-record should be a *drawer* (peripheral context preserved), not a *modal* (peripheral context blocked).

### 3.3 IBM Carbon (S3)

**What it teaches.** Carbon is explicit that it is for enterprise applications. Its component set is heavy on patterns the Destination Master Browser actually needs: data tables (with sortable, expandable, batch-actions, sticky-header variants), data lists, filter panels, side panels (drawers), pagination, tag, status indicator, toast notification, breadcrumb, and the *Empty State* component as a first-class citizen.

**Key claims that carry weight.**

- The data table is *the* enterprise primitive. It has its own behavioural language: sort, filter, expand, batch-select, pagination, sticky columns, sticky header, virtualization.
- Empty states are content, not chrome. They include a primary message, a recovery action, and (when relevant) the next step. An empty state is a *constrained success state*, not a failure.
- Accessibility is built into every component spec rather than appearing as a separate section. Keyboard focus order, semantic role, ARIA where required, and contrast minimums are part of "this is the component".
- Pattern beats primitive. Carbon publishes *patterns* (login, dashboard, side-panel detail, master-detail) alongside components; patterns are the unit of decision because they solve a task, not just a slot.

**What it omits or under-emphasises.** Carbon's visual language is corporate. Some surfaces (consumer-facing landing screens, marketing pages, product onboarding) sit awkwardly inside it.

**Strongest takeaway for this topic.** The right unit of design is the *pattern* — master-detail, faceted-search, table-with-batch-actions — not the individual component. The Destination Master Browser is a master-detail pattern with faceted search; once that's named, the component choices follow (table + drawer + filter chips + persistent stats), and component-by-component invention stops.

### 3.4 GOV.UK Design System (S4)

**What it teaches.** GOV.UK's most distinctive feature is the *negative space* in its guidance. Every component page lists:

- *When to use this component*
- *When not to use this component*
- *How it works*
- *Research on this component* (with links to studies)

The component set is small on purpose: buttons, checkboxes/radios, date input, details (disclosure), error message, error summary, fieldset, file upload, header/footer, inset text, notification banner, pagination, panel, phase banner, radios, select, summary list, tabs, tag, text input, warning text. Pattern set is small and task-shaped: helping users to start, helping users find content, helping users complete tasks, helping users recover from errors.

**Key claims that carry weight.**

- *Content first, components second.* A clear paragraph of plain English often beats a component. If you can solve the problem without the component, do.
- *Progressive enhancement.* Components must work without JavaScript. If the JS layer fails, the user still completes the task.
- *Plain language and reading age.* The system explicitly targets a low reading age and short sentences so the interface is usable by the widest possible audience.
- *Research-driven omission.* Components that are common elsewhere (carousels, accordions for primary content, modals) are deliberately absent or restricted because research showed they reduced task success.

**What it omits or under-emphasises.** GOV.UK is for transactional public services — applying for a passport, paying tax, claiming a benefit. It is not for dense reviewer-facing data tools. Its data-table guidance is thin. Its drawer guidance is non-existent (GOV.UK doesn't use drawers).

**Strongest takeaway for this topic.** "When *not* to use this component" is the single most under-used piece of design discipline in industry. Every component choice on the Destination Master Browser should be defensible against a "when not to use" criterion. This is the gate that prevents decorative additions.

### 3.5 Don Norman — affordances, signifiers, feedback (S5)

**What it teaches.** Norman draws the now-canonical distinction:

- *Affordance* — what the object can do. A button affords pressing.
- *Signifier* — how the user *knows* it can be done. The button looks pressable: raised, coloured, hovered, focused.
- *Feedback* — confirmation that the action happened. The button visually responds; the system state updates; the user sees cause and effect.

Norman's deeper claim is that *signifiers do most of the design work*, because affordances exist in the system whether the user perceives them or not. A clickable card without hover treatment has the affordance of being clicked but no signifier — so for most users the affordance does not exist.

The chapter also distinguishes *real affordance* (physical: the door has a handle) from *perceived affordance* (the on-screen control looks like it can be pressed). For digital interfaces, almost all affordance is perceived affordance — meaning all affordance is in the signifier.

**Key claims that carry weight.**

- Without a signifier, an affordance is invisible. "It works if you know" is a failure.
- Without feedback, an action is indistinguishable from a system that did not respond. The user retries, or worse, double-acts.
- Constraints (what the user *cannot* do) are as important as affordances (what they can). Disabled states, validation that prevents bad input, and unavailable actions reduce error.

**What it omits or under-emphasises.** Norman's book pre-dates much of the modern web vocabulary (chips, drawers, virtualization). His examples are doors, kettles, light switches. The translation to interfaces is generally faithful but takes work.

**Strongest takeaway for this topic.** Every interactive in the Destination Master Browser must answer three questions, not one. *Affordance*: what can this do? *Signifier*: how does the reviewer know? *Feedback*: what does the reviewer see when it happens? A control that scores well on the first and fails the second or third is a control that "works if you know" — i.e., does not work.

## 4. Source comparison

### 4.1 Where the five required sources agree

- A component is a system (anatomy + states + behaviour + content rules + accessibility), not just a shape.
- States are first-class. `default`, `hover`, `focus`, `active`, `disabled` are universally listed; loading / empty / error / success are universally important even when listed less prominently.
- Consistency reduces cognitive load. The same action should look and behave the same wherever it appears.
- Accessibility is part of the component, not an audit done after.

### 4.2 Where they differ — by emphasis

| Question | Material | Apple HIG | Carbon | GOV.UK | Norman |
|---|---|---|---|---|---|
| What is the unit of design? | Component (with strong visual system rules) | Component constrained by platform | Pattern (master-detail, table-with-batch) | Component bounded by "when *not* to use" | The signified action itself, not the component |
| How prescriptive is visual treatment? | High (motion, density, elevation rules) | High but platform-specific | Medium (visual language is corporate but flexible) | Low (content first, plain styling) | Out of scope (visual treatment is downstream of signifier) |
| How strict is "consistency"? | Strict, within the Material system | Strict, with the platform's existing conventions | Strict, within the enterprise system | Strict, but minimised by having fewer components | Conceptually strict — same action should produce same affordance/signifier/feedback everywhere |
| How does it handle modality? | Permissive (dialogs are common) | Restrictive (modal must be earned) | Restrictive (drawer/side panel preferred for detail) | Very restrictive (avoid where possible) | Out of scope but implied: modality is a constraint, use sparingly |
| How does it handle data tables? | Light coverage | Light coverage | Heavy, first-class | Light (transactional tables only) | Out of scope |
| How does it handle data trust? | Through the *Status indicator* and *Tag* components | Through alerts and labels | Through *Status indicator* and *Notification* patterns | Through *Notification banner*, *Warning text*, and content tone | Out of scope (Norman's domain is the control, not the data) |
| Reading age / content discipline | Moderate | High (clarity is a foundation principle) | Moderate | Very high — explicit | Out of scope |

### 4.3 Where they diverge in ways that matter for the browser

- **Modal vs drawer.** Material is permissive about dialogs. Apple HIG, Carbon, and GOV.UK are all sceptical of modality and prefer non-modal containers (drawers, side panels, dedicated pages). The Destination Master Browser is a reviewer tool where peripheral context (the list) matters; the HIG/Carbon/GOV.UK majority position is right for this tool.
- **Component count.** Material publishes ~80 components; GOV.UK publishes ~24. The Material assumption is "we have a component for that". The GOV.UK assumption is "if it isn't published, you probably don't need it". For an internal tool with a small build budget, GOV.UK's posture is the right default.
- **Whose research?** GOV.UK publishes user-research links *per component* — a level of transparency the other systems mostly do not match. For a tool that has to defend its design choices in a viva, citable evidence is preferable to "Material says so".
- **Data tables.** Only Carbon treats the data table as a first-class enterprise primitive. For a master browser whose central task is comparing many records, Carbon's table patterns are the single most important design system input.

### 4.4 What each source omits explicitly

- **Material**: under-specifies *when not to use* a component; data tables under-specified.
- **Apple HIG**: web translation; dense data; non-Apple-platform context.
- **Carbon**: consumer surfaces; marketing-facing screens; small-team adoption cost.
- **GOV.UK**: enterprise data tools; drawers; complex master-detail; charts.
- **Norman**: modern web vocabulary; specific component patterns; visual treatment.

No single source is sufficient. The five together cover the topic; one or two would not.

## 5. CodeMike interpretation

For the CodeMike workspace, UI design is the discipline of converting reviewer-task understanding into component decisions that can be defended in two ways:

1. **By task** — each component must name the reviewer task it serves.
2. **By alternative** — each component must name a less-costly alternative it beat, with the reason it beat it.

This is stricter than "use the right component". It forces the designer to refuse decoration: a component that cannot name a task it serves, or cannot name an alternative it beat, should not be added.

The five sources collectively produce a CodeMike-shaped working definition:

> UI design = (choose container) + (choose elements inside the container) + (specify all states) + (verify affordance / signifier / feedback for each interactive) + (defend against a "when not to use" gate)

Anything not on this list — colour palette experiments, typographic flourish, animation polish — is either downstream of these (visual treatment of a chosen component) or out of scope (decorative).

## 6. Application to the Destination Master Browser

The Destination Master Browser is a **master-detail data-review tool with faceted filtering**. That phrase, sourced from Carbon's pattern vocabulary, fixes most component choices.

### 6.1 Pattern decisions that follow from the topic

| Decision | Choice | Why | Sources |
|---|---|---|---|
| Main pattern | Master-detail with faceted search | Carbon's named pattern for this exact use case; the reviewer scans many records and inspects one at a time | S3 |
| Main list container | **Table by default, cards as secondary view** | Table wins for *scan many records by one or two attributes* and *sort by a column* — both core reviewer tasks; cards are kept as an alternative for record-as-rich-object browsing | S3, E2 |
| Record inspection | **Drawer**, not modal, not full-page | Drawer preserves list context (HIG, Carbon, GOV.UK majority position); modal is over-blocking; full-page is over-scoped for the current task | S2, S3, S4 |
| Filter UI | **Filter chips** for low-cardinality facets (verified, planner-ready); **dropdowns** for high-cardinality (region, type); **search input** for free-text | Carbon's filter-panel pattern + GOV.UK's content-first posture | S3, S4 |
| Empty state | First-class, with active-filter summary and a "Clear all" recovery action | Carbon's *Empty State* component is canonical here | S3 |
| Loading state | Skeleton loaders for the table, not a full-page spinner | Spinner removes context; skeletons preserve layout while data loads | S1, S3 |
| Error state | Inline error banner inside the result region, with what happened and what to do next | GOV.UK *Notification banner* + Carbon *Inline notification* | S3, S4 |
| Trust signalling | A *Status indicator* on every record at every depth (list row + drawer header), plus a top-level *Notification banner* explaining the dataset's overall trust state | Carbon *Status indicator* + GOV.UK *Warning text* + Norman's *signifier* requirement | S3, S4, S5 |
| Primary action position | Top-right of each context (table header for batch actions, drawer header for record actions) | HIG/Material convention | S1, S2 |
| Modality | Used only for *destructive* or *must-finish* actions (e.g. "promote 3 records to Planner — confirm?") | HIG/Carbon/GOV.UK consensus | S2, S3, S4 |

### 6.2 Trust signal — full specification

Topic 1's central finding was that data-trust must be signalled at every depth of the journey, not just once on the list. Topic 2 turns that into a component-level specification:

- **List row**: a *Status indicator* (icon + colour + text label) in the leftmost column. Colour is reinforced by text and icon (WCAG colour-alone failure prevented). States: `verified`, `unverified`, `planner-ready`, `blocked`, `missing-fields`, `conflict`. *No badge* means "no state assigned yet" and is itself rendered (small grey "unassigned" pill) — silence is not allowed (Norman).
- **Drawer header**: a *Notification banner* repeating the record's status with one sentence of explanation. Persistent — does not scroll out.
- **Top-level**: a *Notification banner* on the page describing the dataset's overall state (e.g. "Reference layer — not Planner-ready"). Persistent — sticky on the header.
- **Confirmation modal** (for any action that changes status): re-states the current status before showing the new status.

This is four separate trust signals at four depths. Each is a component decision, not a design flourish.

### 6.3 State coverage commitments

Every interactive control and container in v1.1 must implement the nine standard states where they apply:

```text
default / hover / focus / active / disabled / loading / empty / error / success
```

Loading, empty, and error are the three most commonly missing in data-review tools. They are also the three states a reviewer most needs when the data layer is being honest. Lab 02 will produce the state-coverage matrix that turns this commitment into a per-component checklist.

## 7. Anti-patterns to refuse

The topic identifies seven anti-patterns specific to data-review tools. The Destination Master Browser v1.1 redesign must refuse each:

1. **Modal-as-default container.** Inspecting a record should not block the list. Use a drawer.
2. **Cards as the only main list view.** Cards fail the *scan by attribute* and *sort by column* tasks. Provide a table.
3. **Decorative badges.** A badge with no operational meaning trains the reviewer to ignore badges in general — including the badges that matter (verified, blocked). Every badge must have a defined state.
4. **Colour-only signalling.** A status conveyed only by colour fails reviewers with low-contrast displays, colour-vision difference, or screen readers. Colour is reinforced by icon and label.
5. **Empty-state silence.** A zero-result filter combination must produce a content-rich empty state (what was filtered, how to clear, what to try) — not a blank pane.
6. **Loading silence.** A request in flight must render a skeleton or progress indicator. Blank waiting time is a Norman feedback failure.
7. **Inconsistent affordance.** The same action (e.g. "open record detail") must use the same control across every context. If the list-row click opens a drawer, the table-row click must also open a drawer.

Each of these is sourced from at least two of the five required sources; none is one source's idiosyncrasy.

## 8. Implementation implications for Browser v1.1

The Lab 02 *consolidated rule sheet* at `design/foundations/ui-design-component-rules.md` will be the canonical input. This section names the implementation work that v1.1 commits to:

1. **Add a table mode** alongside the existing cards view. Card/table toggle in the list-header right slot. Sortable columns, sticky header, optional row expansion.
2. **Add a record-detail drawer** that opens on row click. Persistent trust banner in drawer header. Drawer is non-modal; the list remains scrollable behind it.
3. **Add an active-filter summary** above the result list — chips that show which filters are applied and let the reviewer remove them individually.
4. **Add a "Clear all filters" recovery action** in the empty state when filters return zero records.
5. **Add skeleton loading states** for the result region. Spinners only for global page loads.
6. **Add an inline error notification** for failed CSV loads — what failed, why, what to do.
7. **Add a top-level dataset-trust notification banner** that persists with the header.
8. **Standardise the trust badge** — one component, six states, used at row + drawer + modal.
9. **Add focus rings** to every interactive (cards, chips, drawer close, table sort headers). Keyboard navigation must work for every list action.
10. **Defer** all decorative additions until 1–9 are complete. No new colour palette, type scale, illustration, or animation in v1.1.

These ten items are the v1.1 backlog; Lab 02 will refine them with per-component rules.

## 9. Further reading and exercise tasks

The reading-pack already specifies five extension sources (E1–E5). The applied exercises that Lab 02 will execute against this topic are:

- **Component catalogue** — every UI pattern in v1, with reviewer task and current variants.
- **State coverage matrix** — every pattern × nine states, marking present / missing / N/A.
- **Affordance / signifier / feedback audit** — every interactive scored on Norman's three questions.
- **Container-selection rule sheet** — when to use card / table / list / drawer / modal.
- **Filter-UI rule sheet** — when to use chips / dropdowns / search / faceted panel.
- **Consolidated rule sheet** — the merge that becomes Browser v1.1's input.

Lab 02's "decision gate" is reproducibility: a second reviewer applying the rule sheet to two new records must produce the same container and filter choices. If they don't, the rules are under-specified and the lab is not done.

## 10. Checklist updates

Topic 2 adds the following items to `design/checklists/master-browser-design-checklist.md` (to be appended in Lab 02):

- **Container-selection gate**: before adding any new top-level container, name the reviewer task it serves and the existing container it could replace.
- **State-coverage gate**: every interactive must implement (or explicitly N/A) all nine standard states; missing-state findings block release.
- **Affordance/signifier/feedback gate**: every interactive must answer Norman's three questions; an empty signifier or feedback column is a finding.
- **Modality gate**: a modal must be either *confirm-destructive* or *must-finish-or-cancel*; any other use is rejected.
- **Colour-plus-text rule**: status conveyed by colour must also be conveyed by icon and text.
- **Empty-state content rule**: zero-result states must include the active filters, a clear-all action, and a what-to-try-next message; blank empty states are findings.
- **Loading-state shape rule**: skeleton over spinner, except for global page loads.
- **When-not-to-use clause** (GOV.UK-style): every component in the system must have a documented "when not to use".

## 11. Reusable CodeMike capability extracted from this topic

This topic produces three reusable design capabilities for the CodeMike workspace:

1. **Master-detail-with-faceted-search pattern card** — applicable to any future data-review tool (datasets browser, validator review, Planner review). Lives in `capabilities/` once Lab 02 finalises it.
2. **Nine-state interactive checklist** — applicable to any UI work CodeMike does anywhere. Default / hover / focus / active / disabled / loading / empty / error / success.
3. **Affordance-signifier-feedback triple-check** — a per-control review item suitable for any code review of UI work.

These transfer beyond DES-001 — they are general-purpose design capabilities the workspace gains by completing this topic, in line with the CodeMike Operating Loop's *Package → Transfer* steps.

## 12. Reflection on the source set

The reading was honest in one specific way: no source said the same thing twice. Material brought density, motion, and elevation as meaningful. Apple HIG brought platform-consistency and modality discipline. Carbon brought the enterprise-grade table and the pattern-as-unit-of-decision. GOV.UK brought "when not to use" and progressive enhancement. Norman brought the underlying affordance / signifier / feedback model that the others silently inherit.

The cost of stopping at a single source — particularly Material, which is the most widely cited — would have been a design vocabulary biased toward consumer surfaces, permissive about modality, weak on tables, and weak on "when not to use". The browser would have inherited those biases. The multi-source standard, in this case, is not academic discipline — it is a defence against a specific known failure mode in the design literature.

## 13. Open work

- Run **Lab 02** against this topic (`labs/lab-02-ui-design-component-inventory.md`).
- Produce the **consolidated rule sheet** at `design/foundations/ui-design-component-rules.md`.
- After Lab 02 closes, run **Topic 3 — UX design** (reviewer journey + UX acceptance criteria).
- After Topic 3 closes, implement **Browser v1.1** against the consolidated rule sheet and the UX gates.
