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
reading → principles → notes → further reading → checklist → audit → implementation → review
```

## 2. Deep Reading Rule

Every deep-reading topic must use multiple sources.

Minimum standard:

```text
at least 3 sources per topic
at least 1 primary/high-authority source where possible
at least 1 practical/applied source
at least 1 cross-checking or alternative framing source
```

Why:

```text
one source can expose bias
one source can overfit to its own product philosophy
one source can omit accessibility, research, engineering, or edge-case concerns
```

Every deep reading must produce:

- topic summary
- key principles
- source comparison
- disagreements or emphasis differences between sources
- CodeMike interpretation
- application to current artifact
- anti-patterns to avoid
- further reading suggestions
- implementation implications
- checklist updates if needed

A topic is not considered fully digested until these outputs exist.

## 3. Core Design Learning Sequence

| Order | Topic | Why it matters for CodeMike | Output artifact |
|---:|---|---|---|
| 1 | UI design principles | Gives the basic rules for hierarchy, disclosure, consistency, contrast, accessibility, proximity, and alignment | Principle digest + source comparison |
| 2 | Design basics | Frames design as product purpose, interaction, layout, typography, colour, accessibility, and systems | Foundation digest + further reading |
| 3 | UI vs UX | Prevents visual-only redesigns | UX objective statement + source comparison |
| 4 | What is UI design | Clarifies interface elements and patterns | Component vocabulary + source comparison |
| 5 | UX design | Clarifies user goals, friction, review flow, and outcomes | User-task map + source comparison |
| 6 | Design thinking | Creates a disciplined process: empathize, define, ideate, prototype/test, implement | Design process checklist + source comparison |
| 7 | Human-centred design | Keeps user needs ahead of technical cleverness | User-needs brief + source comparison |
| 8 | Gestalt principles | Improves grouping, scanability, and visual perception | Layout audit checklist + source comparison |
| 9 | Fitts' law | Improves tappability and control placement | Touch-target checklist + source comparison |
| 10 | Button states | Improves interaction feedback | Control-state checklist + source comparison |
| 11 | Typography | Improves reading and scanning | Type scale/token guide + source comparison |
| 12 | Colour theory | Makes status and warning signals meaningful | Colour semantics guide + source comparison |
| 13 | Web grid/layout | Improves alignment and responsiveness | Grid/layout rules + source comparison |
| 14 | Design systems | Makes patterns reusable and consistent | Component system guide + source comparison |
| 15 | Prototyping/wireframing | Tests structure before polishing | Wireframe notes + source comparison |

## 4. Deep Reading Output Format

Use this format inside the HTML study dashboard or a consolidated companion digest.

```md
## Topic Name

### Sources Consulted

| Source | Type | Why included |
|---|---|---|
| Source A | primary/high-authority | ... |
| Source B | applied/practical | ... |
| Source C | cross-checking/alternative | ... |

### Core Notes

### Source Comparison

### CodeMike Interpretation

### Application to Current Browser

### Anti-Patterns to Avoid

### Further Reading Suggestions

### Checklist Updates
```

## 5. CodeMike Design Competency Ladder

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
- deep-reading notes support the design choices

Destination master browser v1.1 should aim here.

### Level 3 — Review-Optimised Artifact

Signs:

- supports card and table modes
- has detail drawer/modal
- supports sort and quick filters
- handles mobile and desktop well
- reduces cognitive load for QA
- uses multiple-source design notes to justify choices

Destination master browser v1.2/v2 should aim here.

### Level 4 — Product-Ready Interface

Signs:

- tested with actual use cases
- scalable to larger datasets
- has robust empty/error/loading states
- has reusable design tokens/components
- can become a PWA module
- has an explicit design rationale and audit trail

Future target.

## 6. Design Domains for CodeMike Artifacts

### 6.1 Information Architecture

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

### 6.2 Interaction Design

Core questions:

- What actions does the user perform repeatedly?
- Are those actions easy to reach?
- Does the interface respond predictably?

For destination master browser:

- repeated actions: search, filter, sort, inspect, switch view
- controls must be large, clear, and consistent
- filter results must update predictably

### 6.3 Visual Design

Core questions:

- Is the hierarchy clear?
- Are related things grouped?
- Are contrast and typography supporting comprehension?

For destination master browser:

- destination name and status should dominate card hierarchy
- tags should be grouped by meaning
- warnings should not look like normal metadata

### 6.4 Accessibility

Core questions:

- Can the interface be read easily?
- Can controls be tapped on mobile?
- Are statuses text-labelled and not colour-only?
- Does the layout avoid horizontal overflow?

For destination master browser:

- minimum control height: 44px
- labels must remain visible
- mobile layout must collapse cleanly

### 6.5 Data Trust and Safety

Core questions:

- What should the user not over-trust?
- What does the dataset not prove?
- Where must uncertainty be explicit?

For destination master browser:

- structurally valid does not mean source verified
- not Planner-ready must remain visible
- source confidence and verification status must be clear

## 7. Standard Design Workflow for HTML Artifacts

Every important HTML artifact should follow:

```text
1. Define artifact purpose
2. Define user tasks
3. Define safety/trust constraints
4. Read multiple sources for relevant design topics
5. Generate notes and further reading suggestions
6. Map relevant design principles
7. Create or update checklist
8. Audit current artifact
9. Specify changes
10. Implement changes
11. Verify behaviour
12. Update artifact index and project log
```

## 8. Destination Master Browser v1.1 Target

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

## 9. Design Decision Rule

Every design change must answer:

```text
Which user task does this improve?
Which design principle supports it?
Which sources support or challenge it?
What risk does it reduce?
```

If a change cannot answer those questions, defer it.

## 10. Current Recommendation

Before editing the browser, use:

```text
docs/design-foundations.html
design/checklists/master-browser-design-checklist.md
```

Then audit:

```text
docs/destination-master-browser-v1.0.html
```

Only then implement v1.1.
