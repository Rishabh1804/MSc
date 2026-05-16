# Quiz 02 — Answers

Answer date: 2026-05-16. Written from the lecture, the five required sources, and the deep-reading doc at `design/foundations/topic-02-what-is-ui-design.md`, then self-marked against `quiz-02-what-is-ui-design-answer-key.md`. Examples come from the Destination Master Browser v1.

## 1. Definition (verbs included)

UI design is the discipline of **choosing** which interface elements appear, **arranging** them in space and hierarchy, **specifying their behaviour across all states**, and **visually treating** them — so the user can complete a task with low cognitive cost and unambiguous feedback. The verbs carry the load: UI design is decision work, not decoration work. Visual design (colour, typography, mood) is a sub-skill *inside* UI design, not a synonym for it.

## 2. Six element categories with browser examples

| Category | Destination Master Browser example |
|---|---|
| Controls | search input; "verified only" toggle; filter chips for region / status |
| Containers | record card (v1); future record-detail drawer; the stats banner |
| Navigation | source-layer / verification-status filter row (functions as scope nav); future card/table toggle |
| Data display | the card grid; future table mode; trust-status badge on each record |
| Feedback | top-of-page warning that the dataset is not Planner-ready; (currently missing) toast on filter change |
| Editorial | "X of Y records" headline; the QA-only-use subtitle; future help copy in the empty state |

## 3. The nine states; the three commonly missing

`default`, `hover`, `focus`, `active`, `disabled`, `loading`, `empty`, `error`, `success`.

The three most commonly missing in data-review tools are **loading**, **empty**, and **error**. They only appear when the data layer is being honest with the reviewer (waiting, returning nothing, or failing) — exactly the moment the reviewer needs to know what is happening. A polished happy-path interface tends to skip them, which leaves reviewers without a signal in the moments where signal matters most.

## 4. Affordance vs signifier vs feedback (filter chip)

- **Affordance**: the filter chip can be toggled on or off — it constrains the result set to records matching one property.
- **Signifier**: the chip *looks* pressable — distinct background, hover treatment, a checkmark or filled state when active.
- **Feedback**: clicking the chip visibly changes its appearance and the record count updates with a transition so the reviewer sees cause and effect.

Removing the hover treatment breaks the signifier even though the affordance still exists; for most reviewers the affordance therefore does not exist. Removing the count animation breaks the feedback — the reviewer cannot tell whether the click registered.

## 5. Two tasks where a table beats cards; the switching criterion

Tasks where a table is the better container for the Destination Master Browser:

- **Compare an ordered or numeric attribute across many records** — table rows make column alignment possible (e.g. comparing source-confidence values, scale, or verification dates).
- **Sort by a column** — sorting is a primary table affordance; in cards it is hidden behind another control or absent entirely.

**Criterion for choosing**: when the reviewer task is *"scan many records along one or two precise attributes"* or *"order records by a value"*, table wins. When the task is *"browse and inspect rich, mixed-format records one at a time"*, cards win. The browser should offer both, with a toggle, because both tasks exist in the reviewer journey.

## 6. A signifier–affordance mismatch in v1; the fix

The record cards are entirely clickable (affordance: open detail) but show no hover treatment, no focus ring, and no "open" icon (no signifier). Reviewers therefore cannot tell the card is clickable until they accidentally click it. **Fix**: add a subtle hover background change, a keyboard focus ring, and a small "open" chevron in the card's top-right corner. The affordance does not change; the signifier becomes visible.

## 7. Empty state when filters return zero records

- **Content**: "No records match the active filters." Followed by a list of which filters are currently applied (e.g. *Verified only*, *Scale = country*, *Region = West Asia*) as removable chips.
- **Controls**: a **"Clear all filters"** primary button; each active-filter chip is individually removable.
- **Tone**: factual, not apologetic. Zero results is sometimes the correct answer to a reviewer's query (e.g. "show me unverified records in this region — and there happen to be none"). The user did not fail; the filters narrowed correctly.

The state is a **constrained-success state**, not a failure state.

## 8. Consistency, and one v1 inconsistency

Consistency means the same pattern is used for the same action wherever it appears, so the reviewer learns the product once instead of per screen. It reduces cognitive load because the reviewer does not re-derive how each control works from scratch on each view.

**v1 inconsistency**: the search input and the filter chips are both narrowing controls but use different visual languages (rectangular input vs rounded chip), different states (input has clear-button + focus ring; chips currently have neither), and produce different feedback (input live-updates; chip toggle is harder to perceive). A reviewer must learn each separately. v1.1 should make both controls part of one unified "narrow the result set" pattern.

## 9. Drawer vs modal vs full-page detail

- **Drawer** — for inspecting a record while the reviewer wants to keep the list in peripheral context. *Best fit for the v1.1 "open record"* action.
- **Modal** — for blocking tasks the reviewer must finish or cancel before continuing. *Best fit*: confirming a destructive batch action (e.g. *"promote 3 records to Planner — confirm?"*).
- **Full-page detail** — for records with so much information that the list context is not useful while inspecting, or for editing flows that have their own substructure. *Best fit*: preparing a verified, Planner-ready record for export.

The drawer/modal/full-page boundary is set by *how much peripheral context the task needs* (drawer: full context; modal: none, blocking; full-page: own context).

## 10. A design-decision gate for new components

> "Which reviewer task does this new component improve, and what evidence shows the existing components cannot serve that task?"

A wrong answer ("it looks better"; "competitors have it"; "the data team requested it") fails this question on its face. A right answer cites a specific reviewer task and a specific failure of the current pattern — ideally drawing on Lab 01's heuristic findings, Lab 02's component catalogue, or a reviewer interview. The gate is GOV.UK-shaped: a component must justify itself, and a "when not to use" clause must accompany it.

## Self-mark

Cross-checked against the answer key. The two answers that diverge meaningfully are:

- **Q5 (table vs cards)**: my answer adds "order records by a value" as a second-criterion task, slightly broadening the key's wording. Equivalent.
- **Q6 (signifier–affordance mismatch)**: my answer specifies the cards rather than leaving it as "plausible candidates". The answer key already names the cards as one such candidate, so this is a concretisation, not a divergence.

All ten answers are grounded in either the deep-reading doc or Lab 01's findings. None of the answers depends on a single source.
