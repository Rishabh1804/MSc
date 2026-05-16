# Quiz 02 — Answer Key

These are guideline answers, not the only correct answers. A response that says the same thing differently — particularly grounded in the Destination Master Browser — scores equally.

## 1. Definition

UI design is the discipline of **choosing**, **arranging**, **specifying the behaviour of**, and **visually treating** the elements a user interacts with, so the user can complete a task with low cognitive cost and unambiguous feedback. The verbs are the load-bearing part: UI design is decision work, not decoration work.

## 2. Element categories with browser examples

| Category | Browser example |
|---|---|
| Controls | Search input, filter chip, "show verified only" toggle |
| Containers | Record card, future drawer for the detail view |
| Navigation | (Currently thin — could add tabs for "all / verified / planner-ready") |
| Data display | The card grid; future table mode; status badge on each card |
| Feedback | Stats banner at top; (missing) toast on filter changes |
| Editorial | The "X of Y records" headline; help copy under filters |

## 3. Nine states; the commonly missing three

`default`, `hover`, `focus`, `active`, `disabled`, `loading`, `empty`, `error`, `success`.

The three most commonly missing in data-review tools are **loading**, **empty**, and **error** — because they only appear when the data layer is being honest with the reviewer (waiting, returning nothing, or failing). A polished happy-path UI often skips them, which leaves reviewers without a signal at exactly the moment they need one.

## 4. Affordance / signifier / feedback on a filter chip

- **Affordance**: a filter chip can be toggled on or off.
- **Signifier**: the chip looks pressable — distinct background, hover treatment, a checkmark when active.
- **Feedback**: clicking the chip visibly changes its appearance and the record count updates, ideally with a transition so the reviewer sees cause and effect.

A chip with no hover treatment and no visible "active" style breaks both signifier and feedback even though the affordance still exists.

## 5. Card vs table for the browser

Tasks where a table beats cards:

- **Compare numeric / ordered fields across many records** — table rows make column alignment possible.
- **Sort by a column** — sorting is a primary table affordance; in cards it is hidden.

Criterion for switching: when the reviewer task is "scan many records along one or two precise attributes", a table wins. When the task is "browse and inspect rich, mixed-format records one at a time", cards win.

## 6. Signifier–affordance mismatch in v1

Plausible candidates: a record card may be entirely clickable (affordance) but show no hover/focus treatment (no signifier), so reviewers do not know they can click. Fix: add a hover background change, a focus ring, and a small "open" icon in the corner.

## 7. Empty state when filters return nothing

- **Content**: "No records match your filters." Followed by which filters are active.
- **Controls**: a "Clear all filters" button, and individual filter chips that can be removed one at a time.
- **Tone**: factual, not apologetic. Reviewers should not feel they did something wrong by getting zero results — getting zero results is sometimes the right answer.

The state is not a failure state; it is a constrained-success state.

## 8. Consistency

Consistency is the property that the same pattern is used for the same action wherever it appears, so the reviewer learns the product once instead of per-screen. It reduces cognitive load because each screen does not require relearning what a button looks like or where the filter live.

Possible v1 inconsistency: the search input and the filter chips may not share visual treatment, even though both narrow the result set. A reviewer has to learn each control's affordance separately.

## 9. Drawer vs modal vs full-page detail

- **Drawer** — for record inspection where the reviewer wants to keep the list in peripheral context. Best for the v1 "open record" action.
- **Modal** — for *blocking* tasks the reviewer must finish or cancel before continuing (e.g. confirm-delete or edit-with-validation). Bad fit for browsing.
- **Full-page detail** — for records with so much information that the list context is not useful while inspecting. Best fit for verified, Planner-ready records being prepared for export.

## 10. Design-decision gate

"Which reviewer task does this new component improve, and what evidence shows the existing components cannot serve that task?"

A wrong answer ("it looks better" / "competitors have it" / "the data team requested it") is immediately visible against this question. A right answer cites a specific reviewer task and a specific failure of the current pattern, ideally drawing on Lab 01 or Lab 02 evidence.
