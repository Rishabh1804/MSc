# CodeMike UI Learning Map

Purpose: define the design-learning path CodeMike must follow before improving HTML artifacts.

Status: active learning map  
Scope: UI/UX, data-review artifacts, dashboards, browsers, and future PWA interfaces.

## 1. Why this exists

CodeMike should not invent design principles. Design decisions must come from recognised foundations, then be translated into project-specific criteria.

This learning map prevents the pattern:

```text
functional HTML → arbitrary styling → fragile interface
```

and replaces it with:

```text
reading → principles → checklist → audit → implementation → review
```

## 2. Core Design Learning Sequence

| Order | Topic | Why it matters for CodeMike | Output artifact |
|---:|---|---|---|
| 1 | UI design principles | Gives the basic rules for hierarchy, disclosure, consistency, contrast, accessibility, proximity, and alignment | Principle digest |
| 2 | Design basics | Frames design as product purpose, interaction, layout, typography, colour, accessibility, and systems | Foundation digest |
| 3 | UI vs UX | Prevents visual-only redesigns | UX objective statement |
| 4 | What is UI design | Clarifies interface elements and patterns | Component vocabulary |
| 5 | UX design | Clarifies user goals, friction, review flow, and outcomes | User-task map |
| 6 | Design thinking | Creates a disciplined process: empathize, define, ideate, prototype/test, implement | Design process checklist |
| 7 | Human-centred design | Keeps user needs ahead of technical cleverness | User-needs brief |
| 8 | Gestalt principles | Improves grouping, scanability, and visual perception | Layout audit checklist |
| 9 | Fitts' law | Improves tappability and control placement | Touch-target checklist |
| 10 | Button states | Improves interaction feedback | Control-state checklist |
| 11 | Typography | Improves reading and scanning | Type scale/token guide |
| 12 | Colour theory | Makes status and warning signals meaningful | Colour semantics guide |
| 13 | Web grid/layout | Improves alignment and responsiveness | Grid/layout rules |
| 14 | Design systems | Makes patterns reusable and consistent | Component system guide |
| 15 | Prototyping/wireframing | Tests structure before polishing | Wireframe notes |

## 3. CodeMike Design Competency Ladder

### Level 0 — Undisciplined Styling

Signs:

- makes a page prettier without defining the user task
- adds colours without semantic rules
- dumps data into cards or tables without hierarchy

Status: avoid.

### Level 1 — Functional Artifact

Signs:

- page loads data
- basic search/filter exists
- user can inspect records in some form

Destination master browser v1 is currently here.

### Level 2 — Principle-Aware Artifact

Signs:

- design decisions map to principles
- warning/status hierarchy is clear
- related fields are grouped
- UI has basic accessibility discipline

Destination master browser v1.1 should aim here.

### Level 3 — Review-Optimised Artifact

Signs:

- supports card and table modes
- has detail drawer/modal
- supports sort and quick filters
- handles mobile and desktop well
- reduces cognitive load for QA

Destination master browser v1.2/v2 should aim here.

### Level 4 — Product-Ready Interface

Signs:

- tested with actual use cases
- scalable to larger datasets
- has robust empty/error/loading states
- has reusable design tokens/components
- can become a PWA module

Future target.

## 4. Design Domains for CodeMike Artifacts

### 4.1 Information Architecture

Core questions:

- What is the page for?
- What is the first decision the user needs to make?
- What information must be visible immediately?
- What can be hidden until requested?

For destination master browser:

- page purpose: inspect master destination records
- first decision: search/filter or understand dataset status
- immediately visible: validation status, row count, not-Planner-ready warning, search
- hidden until requested: full source notes, normalisation notes, master notes

### 4.2 Interaction Design

Core questions:

- What actions does the user perform repeatedly?
- Are those actions easy to reach?
- Does the interface respond predictably?

For destination master browser:

- repeated actions: search, filter, sort, inspect, switch view
- controls must be large, clear, and consistent
- filter results must update predictably

### 4.3 Visual Design

Core questions:

- Is the hierarchy clear?
- Are related things grouped?
- Are contrast and typography supporting comprehension?

For destination master browser:

- destination name and status should dominate card hierarchy
- tags should be grouped by meaning
- warnings should not look like normal metadata

### 4.4 Accessibility

Core questions:

- Can the interface be read easily?
- Can controls be tapped on mobile?
- Are statuses text-labelled and not colour-only?
- Does the layout avoid horizontal overflow?

For destination master browser:

- minimum control height: 44px
- labels must remain visible
- mobile layout must collapse cleanly

### 4.5 Data Trust and Safety

Core questions:

- What should the user not over-trust?
- What does the dataset not prove?
- Where must uncertainty be explicit?

For destination master browser:

- structurally valid does not mean source verified
- not Planner-ready must remain visible
- source confidence and verification status must be clear

## 5. Standard Design Workflow for HTML Artifacts

Every important HTML artifact should follow:

```text
1. Define artifact purpose
2. Define user tasks
3. Define safety/trust constraints
4. Map relevant design principles
5. Create checklist
6. Audit current artifact
7. Specify changes
8. Implement changes
9. Verify behaviour
10. Update artifact index and project log
```

## 6. Destination Master Browser v1.1 Target

The next browser upgrade should not be a visual overhaul. It should be a principle-aware usability upgrade.

Target additions:

- compact filter panel
- quick-filter chips
- sort controls
- card/table toggle
- click-to-inspect detail drawer
- clearer status grouping
- better mobile layout
- stronger warning hierarchy
- better empty/loading/error states

## 7. Design Decision Rule

Every design change must answer:

```text
Which user task does this improve?
Which design principle supports it?
What risk does it reduce?
```

If a change cannot answer those questions, defer it.

## 8. Current Recommendation

Before editing the browser, create and use:

```text
design/checklists/master-browser-design-checklist.md
```

Then audit:

```text
docs/destination-master-browser-v1.html
```

Only then implement v1.1.
