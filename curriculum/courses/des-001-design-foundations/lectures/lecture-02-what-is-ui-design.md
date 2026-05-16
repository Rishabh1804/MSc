# Lecture 02 — What is UI design

## Learning objectives

By the end of this lecture, CodeMike should be able to:

- define UI design as a discipline rather than a visual style choice
- name the standard categories of UI element and what task each supports
- enumerate the standard component states and explain why each matters
- distinguish affordance, signifier, and feedback
- justify why consistency is a load-reducer, not an aesthetic preference
- choose between card, table, list, drawer, and modal for a given reviewer task

## Core distinction

UI design is the deliberate selection, arrangement, behaviour, and visual treatment of interface elements so that a user can complete a task with low cognitive cost and unambiguous feedback.

Visual design (colour, typography, illustration, mood) is a sub-skill inside UI design. Producing a pleasant surface is not the same as producing a usable one.

```text
UI design  =  choose elements + arrange them + define behaviour + style them
                                       ↑
                                 (visual design lives here)
```

## Element vocabulary

Most production UIs reduce to a small number of categories:

| Category | Examples | What task it supports |
|---|---|---|
| Controls | button, input, toggle, select, slider | Initiate or constrain an action |
| Containers | card, panel, drawer, modal, accordion | Group related content; control how much is visible |
| Navigation | menu, tabs, breadcrumbs, pagination | Move between scopes; show where you are |
| Data display | table, list, grid, tree, badge, chip | Show records, statuses, and structure |
| Feedback | toast, banner, progress, validation message | Signal what just happened, or what must happen |
| Editorial | heading, body, caption, link | Tell the user what they are looking at |

A capable UI picks one element per task slot. A weak UI uses several elements for the same slot or one element across multiple slots.

## States

Every interactive element exists in a state machine. UI design specifies all of them:

- `default` — the resting appearance
- `hover` — pointer over the element
- `focus` — keyboard or assistive-tech focus
- `active` / `pressed` — the moment of interaction
- `disabled` — the element exists but cannot be used now
- `loading` — the element is doing work
- `empty` — there is no data to display
- `error` — something failed; the user must see what
- `success` — confirmation that something worked

Missing states are the most common UI failure in a data-review tool. Empty, error, and loading are the states reviewers see when something is wrong with the data — exactly the moment the interface needs to be most honest.

## Affordance, signifier, feedback

From Don Norman:

- **Affordance**: what the element can actually do. A button can be clicked.
- **Signifier**: how the user knows it can be done. The button looks pressable.
- **Feedback**: confirmation that it happened. The button visibly responds.

A polished UI without signifiers is a guessing game. A polished UI without feedback feels broken even when it works.

## CodeMike interpretation

For the Destination Master Browser, UI design asks:

```text
For each reviewer task, what is the right element, in the right state, in the right container, with the right feedback?
```

This is the question the lab will execute against the actual product.

## Common misconception

UI design is not "make the screen look better". It is "decide what each pixel is doing on behalf of a task". A redesign that swaps colours and fonts but keeps the same wrong containers and missing states is a visual refresh, not a UI redesign.

## Application to browser redesign

For each component pattern in `docs/destination-master-browser-v1.0.html` answer:

1. Which reviewer task does this component serve?
2. Which element category does this pattern belong to?
3. Which states are implemented? Which are missing?
4. Does the affordance match the action (e.g. is a clickable card visually clickable)?
5. Is the feedback honest (loading visible, empty addressed, error explained)?
6. Is the chosen container the right one — card, table, list, drawer, or modal — for the task?

## Discussion questions

1. The browser currently shows records as a grid of cards. For which reviewer tasks is a table the better container?
2. When should a record open in a drawer versus a full-page detail view versus a modal?
3. Where in the browser is feedback missing today?
4. Which signifiers in v1 are decorative rather than functional, and which are functional rather than decorative?
5. How should "unverified record" be encoded in the UI — colour, badge, position, copy, or all four?
6. What is the cost of inconsistency between the cards view and a future table view?

## Key takeaway

UI design is the discipline of choosing the right element with the right behaviour for the right task, and proving that choice across every state the element can be in.
