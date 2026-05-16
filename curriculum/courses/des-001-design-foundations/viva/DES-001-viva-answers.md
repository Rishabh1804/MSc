# DES-001 Viva Answers

Answer date: 2026-05-16. Written to be defendable under questioning rather than to recite the lecture. Each answer is followed by the line a viva examiner would push on, and the follow-up response.

## Topic 1 — UI vs UX

### 1. Why is UI not equivalent to UX?

UI is one ingredient of UX. UI is the surface — controls, layout, states, feedback — and you can produce a flawless UI surface for a system that fails its user (wrong information architecture, wrong content, broken data trust, inaccessible to the user's assistive technology, unworkable in the user's context). UX is the property of the *whole journey*: did the user understand the situation, complete the task, recover from errors, and leave with the right confidence? A polished UI passes a UI review; only the end-to-end task passing passes a UX review.

*Examiner push: "Couldn't a perfect UI guarantee perfect UX in a simple enough system?"*

Only by collapsing UX onto UI by removing every other variable — no data, no context, no users with different needs. Once you reintroduce any of those (which is the whole point of building a system), UX has axes that UI cannot reach: data quality, accessibility, content correctness, support, recovery from external errors. A user can correctly press the right perfect button and still get a wrong outcome.

### 2. Which source gave the broadest definition of UX?

NN/g / Don Norman. The NN/g definition treats UX as "all aspects of the end-user's interaction with the company, its services, and its products." That phrasing explicitly leaves the screen — it includes service touch-points, support quality, content, marketing — and is broader than Figma's product-focused framing, IxDF's design-discipline framing, or UXDT's interaction framing. The breadth matters because it forces the designer to look outside the rendered HTML for failure modes.

*Examiner push: "Is broader always better? Could the broad definition become unfalsifiable?"*

It can. If everything is UX, nothing diagnoses what to fix. The discipline is to use the NN/g definition to *find* failure modes that narrow definitions miss (e.g. data-trust collapse in a dashboard) and then narrow the analysis when prescribing fixes — heuristic per heuristic, journey step per journey step, as Lab 01 did.

### 3. Why is data credibility a UX concern in the Destination Master Browser?

The reviewer's purpose is to make downstream decisions — promote to Planner, mark for enrichment, reject. Those decisions are only as good as the reviewer's confidence about which records are verified. If the UI cannot distinguish verified from unverified, the reviewer either over-trusts (promoting bad records) or under-trusts (re-verifying records that don't need it). Both are UX failures: the reviewer leaves with the wrong mental model. So data credibility is not a backend concern that the UI passively reflects — it is an output of the UX that the UI must actively signal.

*Examiner push: "Why is that a UX concern rather than a data-engineering concern?"*

The data engineering decides *whether* a record is verified. The UX decides *whether the reviewer knows*. A correctly verified record whose verification is invisible to the reviewer is functionally identical to an unverified one for the purposes of the next decision. The boundary between back-end correctness and front-end honesty is exactly where UX lives.

### 4. What is one example of attractive UI causing poor UX?

The card style in v1: rich typography, colour-coded badges, generous spacing — visually appealing — but the most decision-relevant signal (verified vs unverified) is encoded in a small chip among other chips, which trains the reviewer to discount chips as decoration. The pleasant card style raises the *perceived* trustworthiness of the data while reducing the *signal-to-noise* of the trust indicator itself. The UI looks more credible while becoming less informative.

*Examiner push: "How do you know it's the polish causing the problem rather than the data?"*

Because the same data displayed in a stripped-down table — same records, same verification flags, no colour — produces faster correct identification of unverified records in a manual walk-through. The polish is not neutral; it is shifting attention away from the signal.

### 5. Which browser feature is most justified by Topic 1?

A persistent, repeated trust signal at every level of detail: list view (badge on card), detail view (banner at top of drawer), and any export confirmation step. Topic 1 specifically calls out that data-trust is a UX concern that has to be carried through the entire reviewer journey, not just shown once on the list. v1 shows the verification flag on cards but loses it in deeper contexts. Carrying the signal through is the feature Topic 1 most directly justifies.

*Examiner push: "Wouldn't repeating the signal be redundant noise?"*

Only if the reviewer's confidence is constant through the journey. It isn't — by the time the reviewer is inside the detail drawer comparing fields, the list-level signal is out of sight and out of working memory. Repetition is not noise when the alternative is forgetting.

### 6. How should uncertainty be represented in a data-review interface?

By visible, named states rather than absence. A record should be in one of a small set of named states — verified, unverified, planner-ready, blocked, missing-fields, conflict — each with a defined visual treatment. *No badge* should mean "no state assigned yet", which is itself a state. Uncertainty should never be encoded by silence; silence is indistinguishable from "we forgot to check". Colour alone is not enough — accessibility requires the state to be conveyed by text or icon as well.

*Examiner push: "Doesn't naming every state create cognitive overhead?"*

It does, but it's the right kind of overhead. The reviewer has to learn the state vocabulary once. The alternative is that they re-derive trust judgements per record from incomplete cues, which is far more cognitively expensive and produces worse decisions.

### 7. Why should accessibility be treated as part of UX?

Because UX is the property of the journey for the actual users — and some reviewers use keyboard navigation, screen readers, low-contrast displays, or magnification. A journey that succeeds for sighted mouse users and fails for keyboard or screen-reader users has not succeeded — it has succeeded for a subset of users and silently excluded the rest. Treating accessibility as a separate post-hoc audit means the design has already encoded exclusion that needs retrofitting. The W3C framing makes the point explicit: accessibility, usability, and inclusion are facets of the same property.

*Examiner push: "Is accessibility not a legal or compliance concern rather than a UX one?"*

It is also those, but framing it as compliance lets designers pass the bar without engaging with the experience. A WCAG-compliant interface can still be a miserable experience for a screen-reader user if the heading hierarchy is wrong or the ARIA labels are uninformative. The UX framing treats accessibility as a design quality measure, not an audit hurdle.

### 8. What would you revise in the browser after completing the heuristic audit?

In order, the highest-leverage changes from Lab 01:

1. **Add reset and active-filter summary** — addresses "user control and freedom" and recovery. v1 cannot easily undo a filter combination.
2. **Add a table mode for the main list** — addresses "match between system and real world" for the *compare-many* task that cards serve poorly.
3. **Add a detail drawer with persistent trust badging** — addresses "visibility of system status" inside record inspection.
4. **Add explicit empty, loading, and error states** — addresses "help users recognize, diagnose, and recover" and is the data-honesty work Topic 1 most demands.
5. **Add a sort affordance** — addresses Fitts'-style efficiency and aligns to the "scan-by-attribute" reviewer task.

Each of these changes is tied to a heuristic and a reviewer task, not to aesthetics. The order reflects expected impact on workflow completion and trust preservation, the two UX gaps Lab 01 identified.

*Examiner push: "Why not start with visual hierarchy?"*

Because v1's visual hierarchy is competent. Starting there would polish a working surface while leaving the workflow gaps untouched — which is exactly the anti-pattern Topic 1 trains the designer to refuse.

## How these answers were defended

These answers were written to survive viva-style questioning: each one names a specific Lab 01 finding, a specific source, or a specific reviewer task rather than relying on generic design language. The examiner-push lines are real likely follow-ups, not rhetorical fill — they correspond to the points where Topic 1's argument is least obvious.

## Topic 2 — What is UI design

### 1. Define UI design as a discipline and explain why visual design is a sub-skill rather than a synonym.

UI design is the discipline of *choosing* which elements appear, *arranging* them, *specifying their behaviour across all states*, and *visually treating* them — so a user can complete a task with low cognitive cost and unambiguous feedback. The verbs do the load-bearing work: it is decision work. Visual design (colour, typography, illustration, mood) sits *inside* that discipline as the "visually treating" step. A perfectly visually-treated interface that picked the wrong container, missed the loading state, and gave no feedback is a UI failure that happens to look good — which is exactly what makes the conflation dangerous.

*Examiner push: "If visual design is downstream, why do design teams hire visual designers?"*

Because visual treatment is a real specialism — type hierarchy, colour systems, illustration craft are deep skills. The point isn't that visual design is unimportant; it's that visual design serves a UI decision that has already been made. The team that hires a visual designer to fix a usability problem is treating the symptom; the team that hires a UI designer to make the component choices and a visual designer to treat those choices is doing it correctly.

### 2. Name the nine standard component states. Which three are most commonly missing in data-review tools, and why?

`default`, `hover`, `focus`, `active`, `disabled`, `loading`, `empty`, `error`, `success`.

The three most commonly missing are **loading**, **empty**, and **error**. They appear only when the data layer is being honest — waiting, returning nothing, failing. A happy-path UI doesn't render them because the developer never saw them during build. In data-review tools the reviewer specifically needs these states: *loading* tells them the system is fetching (not broken); *empty* tells them the filters narrowed correctly (not that the system failed); *error* tells them what failed and what to do. Their absence reads as silence at exactly the moments the reviewer needs signal.

*Examiner push: "Loading you can argue. But isn't 'empty' just bad data? Why design it?"*

Because in a reviewer tool, *empty is sometimes the correct answer*. The reviewer might be specifically looking for unverified records in a region that happens to have none — that is a successful query with zero rows, and treating it as a failure state confuses the reviewer. A content-rich empty state ("No records match these filters" + which filters are active + a clear-all action) tells the reviewer the query worked and the data answered.

### 3. Distinguish affordance, signifier, and feedback. Why does Norman argue that the signifier does most of the design work in digital interfaces?

- **Affordance** — what the object can do. A button affords being pressed.
- **Signifier** — how the user *knows* it can be done. The button looks pressable: raised, coloured, hovered, focused.
- **Feedback** — confirmation that the action happened. The button visibly responds; the system state updates.

Norman's argument: in the physical world, affordances are often perceivable directly — a door handle suggests pulling. In a digital interface, almost nothing has a physical handle. A clickable card has the affordance of being clicked, but unless the signifier (hover treatment, focus ring, cursor change) makes that affordance visible, the user has no way to know. For digital interfaces, *all affordance is perceived affordance* — which means all affordance lives in the signifier.

*Examiner push: "Doesn't the cursor change handle the signifier?"*

It handles some of it for mouse users — and even then, only after the user hovers. It does nothing for keyboard users, nothing for touch users, and nothing for users who simply don't move their cursor over the element. The cursor change is a *secondary* signifier; the *primary* signifier has to be visible without interaction.

### 4. The five required Topic 2 sources differ less on definition than on emphasis. Name two specific emphasis differences that change a v1.1 design decision.

First: **modality**. Material Design 3 is permissive about dialogs and treats them as a standard container. Apple HIG, Carbon, and GOV.UK are all sceptical and prefer non-modal containers (drawer, side panel, inline disclosure). This is the difference between v1.1 opening records in a modal (Material-shaped) and opening them in a drawer that preserves the list context (HIG/Carbon/GOV.UK-shaped). For a reviewer tool whose central task involves peripheral context, the majority position wins.

Second: **data tables**. Only Carbon treats the data table as a first-class enterprise primitive with sortable / sticky-header / batch-select / row-expansion patterns. Material is light on tables; HIG and GOV.UK are light on tables. The Destination Master Browser's main task is "compare many records along one or two attributes" — a table task. Without Carbon in the source set, the design would default to cards (Material's most prominent list pattern) and miss the central reviewer task.

*Examiner push: "Why not pick the source whose values you share and follow it consistently?"*

Because each source has known blind spots. Material is consumer-shaped; HIG is platform-shaped; Carbon is corporate-shaped; GOV.UK is transactional-shaped. The Destination Master Browser is none of those — it is an internal data-review tool. Picking one source means inheriting its blind spot. Reading all five and using each where it is strongest gives the design a more accurate operating range.

### 5. For the Destination Master Browser, when should a record open in a drawer rather than a modal? When does the choice flip?

Inspecting a record is a *non-blocking* task — the reviewer wants to read the record's full fields, possibly compare it to other records in the list, and either close the inspection or take an action. Peripheral context (the list, the active filters, the trust banner) matters during the inspection. That makes it a **drawer** task.

The choice flips when the task is *blocking and must finish or cancel*. Examples for this product:

- **Confirm destructive action**: "promote 3 records to Planner — confirm?" The reviewer cannot continue browsing while the action is in flight; cancellation is a real option; the wrong outcome is irreversible. **Modal.**
- **Edit with validation that must complete**: rare in this product, but if a single-record edit needed to validate against the master schema before saving, that's a modal task.

The criterion: *does the task need to block the rest of the UI?* If yes, modal. If no, drawer.

*Examiner push: "What about full-page for the inspect task?"*

Full-page is too much for "look at one record and decide". It strips the peripheral context the reviewer is using and adds navigation cost (back-button, scroll-restore). Full-page belongs to flows that have their own substructure — preparing a verified record for export, or editing a record across several fields. Inspect-then-decide is drawer-shaped.

### 6. Why does the topic argue that the unit of design is the *pattern* (master-detail, faceted search) rather than the *component*?

Because component-by-component decisions don't produce coherent interfaces. If a designer decides "add a card", then "add a filter", then "add a button", then "add a modal", each decision can be defensible on its own and the result still fails — because the pattern (the relationship between list, detail, filter, and action) was never named. Naming the pattern first ("this is a master-detail tool with faceted search") fixes most of the component choices: master-detail implies *table + drawer*; faceted search implies *filter chips + persistent active-filter summary*; the persistent stats banner becomes the natural top-of-pattern element. Component invention stops once the pattern is named.

*Examiner push: "Doesn't that just push the decision up a level? You still have to pick the pattern."*

Yes — and that's the point. Picking the pattern is a *task* decision (what is the reviewer doing?), not an *aesthetic* decision. There are maybe a dozen patterns for this whole category of tool; the designer has to pick the one that matches the task. Once that's done, the per-component decisions are mostly determined. Pushing the decision up a level is exactly the improvement.

### 7. Give one example of a Topic 2 anti-pattern that v1 commits, and the v1.1 fix.

v1 commits **inconsistent affordance** in its narrowing controls. The search input and the filter chips are both narrowing controls but use different visual languages (rectangular input vs rounded chip), different state treatments (the input has a clear-button and focus ring; the chips currently have neither visible focus ring nor obvious active state), and produce different feedback (input live-updates; chip toggles are slower to perceive). A reviewer has to learn each separately.

**v1.1 fix**: treat search-and-chips as one "narrow the result set" pattern. Standardise focus rings across both. Make chip-active and chip-inactive states visually as strong as the input's "has content / has been cleared" states. Make both produce the same feedback: a visible result-count animation when state changes.

*Examiner push: "Isn't visual consistency superficial?"*

It's not — it's the *signifier* that tells the reviewer two controls do similar work. Without that signifier the reviewer has to derive the relationship from documentation or trial-and-error. With it, the reviewer learns "things that look like this narrow the list" once and applies it everywhere.

### 8. The topic adds a "when not to use" gate to the master-browser checklist. Why is that gate more important than a "when to use" rule?

Because "when to use" rules are easy to satisfy — there is almost always a defensible reason to add a component. A team that wants to add a carousel can justify it ("it shows multiple items in less space", "competitors use it"). A team that wants to add a modal can justify it ("we needed somewhere to put the form"). "When to use" rules are permissive by construction.

"When not to use" rules are restrictive by construction. They prevent additions that would have passed a "when to use" test but fail the negative-space test ("modal is wrong here because the task is non-blocking; the carousel is wrong here because research shows users miss content past the first slide"). The GOV.UK Design System publishes "when not to use" guidance per component, with research links, precisely because they discovered that "when to use" guidance let through almost any addition.

For the Destination Master Browser, the gate is operationally useful: a request to add a new component must answer "what reviewer task does this serve?" AND "what is the case where this would be wrong?" If the second question has no answer, the component is decoration and is refused.

*Examiner push: "Couldn't a team just write a weak 'when not to use' clause to pass the gate?"*

They could. The mitigation is to make the "when not to use" clause come from user research, prior failure, or a competing pattern that already solves the task — not from imagination. That's the GOV.UK posture: every "when not to use" links to evidence, so it is testable. A "when not to use" clause without evidence is a smell.

## How the Topic 2 answers were defended

Each Topic 2 answer cites at least one specific source (Material, HIG, Carbon, GOV.UK, Norman) and at least one specific reviewer task or v1 finding. The examiner-push lines are the points where Topic 2's argument is least obvious — where a casual reader might agree and then drift back to component-shopping. The follow-ups close those drifts.
