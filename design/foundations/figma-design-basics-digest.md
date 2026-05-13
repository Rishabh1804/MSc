# Figma Design Basics Digest — CodeMike Design Foundation

Source family:

- Figma Resource Library — Design Basics
- Figma Resource Library — UI Design Principles
- Figma Resource Library — Gestalt Principles
- Figma Resource Library — Design Thinking

Status: foundational design-reading artifact  
Purpose: prevent CodeMike from treating design as decoration or making up design principles ad hoc.

## 1. Core Lesson

Design is not just how an interface looks.

For CodeMike, design means the deliberate shaping of:

- user goals
- information hierarchy
- interaction behaviour
- visual grouping
- accessibility
- layout
- typography
- colour use
- feedback states
- product purpose
- review workflow

The destination master browser should therefore be treated as a data-review product, not as a decorative HTML page.

## 2. Design Basics as a Curriculum Map

Figma's Design Basics resource library is a hub of design fundamentals. For CodeMike, it becomes a curriculum map with these practical learning areas:

| Area | CodeMike interpretation |
|---|---|
| UI/UX design principles | Understand the difference between interface elements and user experience outcomes |
| Prototyping and wireframing | Test layout and interaction ideas before overbuilding |
| Web design | Structure responsive review pages clearly |
| Typography | Make text scannable and readable |
| Colour theory | Use colour to signal status, priority, and risk without relying on colour alone |
| Brand and storytelling | Explain what the artifact is, why it exists, and what users should do next |
| Design systems | Reuse components, tokens, spacing, chips, cards, controls, and status styles consistently |
| Interaction design | Make filters, sorting, toggles, and detail drawers predictable |
| Accessibility | Ensure the artifact works for more users and devices |

## 3. UI Design Principles Digest

Figma's UI design principles article identifies seven essential principles:

```text
hierarchy
progressive disclosure
consistency
contrast
accessibility
proximity
alignment
```

### 3.1 Hierarchy

Meaning:

The most important information should be easiest to find first.

For CodeMike artifacts:

- put task-critical information above secondary metadata
- make dataset status visible before detailed records
- make warnings visible before users trust the data

For the destination master browser:

- show row count, validation status, and not-Planner-ready warning at the top
- keep search and primary filters before record cards
- make destination name, state, type, and status more prominent than raw source notes

Anti-patterns:

- all fields having the same visual weight
- warnings hidden below the fold
- cards where source IDs are louder than destination names

### 3.2 Progressive Disclosure

Meaning:

Show enough information to make the next decision, but do not expose everything at once.

For CodeMike artifacts:

- use summary cards, expandable detail panels, and drill-down views
- hide raw fields until inspection is needed
- keep complex validation notes out of the primary browsing path

For the destination master browser:

- card view should show summary
- table view should show QA fields
- full row should appear in a drawer/modal when clicked

Anti-patterns:

- dumping all CSV columns into every card
- making the user scroll through huge text blocks for every record
- hiding detail completely with no inspection path

### 3.3 Consistency

Meaning:

Repeated UI elements should look and behave the same way.

For CodeMike artifacts:

- use a consistent component vocabulary: cards, chips, badges, filters, tables, drawers
- keep the same status names and colours across artifacts
- preserve predictable control behaviour

For the destination master browser:

- all cards should use the same section order
- status chips should use consistent labels
- filters should work the same way across source layer, region, scale, and status

Anti-patterns:

- one status shown as a chip in one place and plain text in another
- inconsistent spacing between card sections
- different filter behaviours for similar controls

### 3.4 Contrast

Meaning:

Important elements need visual distinction.

For CodeMike artifacts:

- use contrast to separate warnings, primary actions, and metadata
- make risk/status information hard to miss
- do not use contrast purely for decoration

For the destination master browser:

- not-Planner-ready warning should be visually distinct
- Planner-ready count should not look positive if it is zero
- caution tags should differ from vibe tags

Anti-patterns:

- low contrast text
- warnings styled like neutral metadata
- overusing bright colours so nothing stands out

### 3.5 Accessibility

Meaning:

Interfaces should work for users across devices, abilities, and contexts.

For CodeMike artifacts:

- use readable type sizes
- ensure controls are large enough for touch
- avoid colour-only signals
- support keyboard-friendly controls where practical
- keep contrast high

For the destination master browser:

- controls should be at least 44px tall
- mobile layout should not require horizontal scrolling
- warning text should be textual, not only colour-coded
- table mode should remain readable on mobile or collapse gracefully

Anti-patterns:

- tiny filters
- pale grey text on dark backgrounds
- status relying only on red/yellow/green
- cards too dense to tap or scan

### 3.6 Proximity

Meaning:

Related items should be visually grouped together.

For CodeMike artifacts:

- group source lineage separately from destination facts
- group validation state separately from content tags
- group filters by user task

For the destination master browser:

- source layer/source ID/source file should live together
- vibes/trip tags/context tags/caution tags should have distinct sections
- verification/promotion/planner status should be grouped together

Anti-patterns:

- mixing status, geography, source lineage, and vibes in one undifferentiated block
- placing labels far away from values
- filters scattered across the page

### 3.7 Alignment

Meaning:

Alignment makes information easier to scan and compare.

For CodeMike artifacts:

- use grid layouts deliberately
- align labels and values consistently
- make card/table structure predictable

For the destination master browser:

- cards should follow a consistent grid
- metadata blocks should align across cards
- table columns should align with QA tasks

Anti-patterns:

- uneven card heights causing major scan difficulty
- inconsistent field placement
- controls placed without a layout system

## 4. Gestalt Principles Digest

Figma's Gestalt resource explains how people group visual information into meaningful patterns. The most useful principles for CodeMike browser artifacts are:

| Gestalt principle | CodeMike use |
|---|---|
| Proximity | Group related fields together |
| Similarity | Use consistent chip/card/status styling for similar items |
| Continuity | Guide the eye from dataset status → filters → records → details |
| Closure | Let compact cards imply a larger full record that can be opened |
| Figure-ground | Make the active content area distinct from background panels |
| Prägnanz | Prefer simpler forms over visual complexity |
| Symmetry | Use balanced cards and panels where possible |
| Connectedness | Use borders, drawers, and grouped panels to show related controls |
| Common region | Put related metadata inside the same card section |
| Focal point | Make warnings, row counts, and destination names focal points |
| Common fate | Use consistent transitions/expansion behaviour for similar interactions |

## 5. Design Thinking Digest

Figma's design-thinking resource frames design thinking as an iterative, human-centred way to solve complex problems.

### 5.1 Three lenses

CodeMike should evaluate design improvements through:

| Lens | Browser question |
|---|---|
| Desirability | Does this help the user review destination records better? |
| Feasibility | Can this be implemented in static HTML/JS without overengineering? |
| Viability | Will this still work as the dataset grows beyond 359 rows? |

### 5.2 Five stages

| Stage | CodeMike adaptation |
|---|---|
| Empathize | Understand the reviewer: they need to inspect, filter, and avoid trusting unverified data |
| Define | State the browser problem clearly before styling |
| Ideate | Generate interface options: cards, table, drawer, chips, sort controls |
| Prototype/test | Implement a small v1.1 and inspect behaviour in browser |
| Implement | Commit the improved interface only after it serves the review task |

## 6. Design-Basics Translation for Destination Master Browser

The current browser is functional. It should now be improved according to design principles, not taste.

### 6.1 Product definition

```text
The destination master browser is a QA/review tool for inspecting 359 structurally valid but unverified destination records.
```

### 6.2 User goals

- find a destination quickly
- filter by region/source/status/scale
- understand whether a row is seed or normalized candidate
- inspect full row details when needed
- identify records that need enrichment or verification
- avoid confusing structure with verified travel truth

### 6.3 Safety goal

The interface must repeatedly and clearly communicate:

```text
Structurally valid does not mean Planner-ready.
```

### 6.4 Browser design priorities

1. clarity before decoration
2. safe status communication before visual polish
3. compact scan before full detail
4. progressive disclosure before field dumping
5. consistent reusable components before one-off styling
6. mobile usability before dense desktop dashboarding
7. review workflow before presentation aesthetics

## 7. Design Anti-Patterns for CodeMike

Avoid:

- making the browser visually impressive but less useful
- using colours without semantic meaning
- hiding warnings
- showing every field everywhere
- building complex UI before the information architecture is stable
- designing only for desktop
- treating validated structure as verified truth
- using inconsistent status labels
- adding animations before solving scanability
- using small touch targets

## 8. Required Design Process Before HTML Upgrade

Before redesigning `destination-master-browser-v1.html`, CodeMike must:

1. read the relevant design principles
2. translate principles into project-specific criteria
3. audit the current browser
4. define v1.1 changes
5. implement only changes tied to criteria
6. re-check usability after implementation

## 9. Current Design Conclusion

The current browser is acceptable as a functional v1, but weak as a review product.

The next design pass should focus on:

- stronger hierarchy
- better grouping
- collapsible filters
- card/table view toggle
- full-record inspection drawer
- consistent status chips
- clear validation and not-Planner-ready messaging
- mobile-safe controls
- sort and quick-filter chips

The goal is not to make it pretty. The goal is to make it trustworthy, scannable, and useful.
