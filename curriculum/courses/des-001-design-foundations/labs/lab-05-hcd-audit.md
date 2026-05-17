# Lab 05 — HCD Audit (v1.1 + Lab 04 Loop 1)

## Lab objective

Run a full **human-centred design audit** of the Destination Master Browser v1.1 (post-PR #12) and Lab 04 Loop 1 against ISO 9241-210's four activities, six principles, and the W3C accessibility / usability / inclusion triad. Produce a per-activity evidence table, a gap analysis with prioritised findings, and a list of HCD findings to address in v1.2.

The audit is *evidence-based* — every claim ties to a specific artifact in the workspace.

## Materials

- `curriculum/courses/des-001-design-foundations/lectures/lecture-05-human-centered-design.md`
- `curriculum/courses/des-001-design-foundations/readings/topic-05-human-centered-design-reading-pack.md`
- `design/foundations/topic-05-hcd.md` (deep-reading doc, PR A)
- All prior DES-001 evidence: Topic 1–4 deep-reading docs; Lab 01–04 outputs; v1.1 build + walkthrough; rule sheet + acceptance-criteria sheet
- ISO 9241-210 + W3C Accessibility/Usability/Inclusion (the standards being audited against)

## Lab steps

### Step 1 — Activity 1 audit: Context of use

For each named user persona, document:

- **User**: the persona (with characteristics drawn from prior Topic 3/4 work)
- **Tasks**: what the user does with the system (drawn from the seven-step journey)
- **Environment**: physical, technical, organisational context
- **Equipment**: device, network, assistive technology if any
- **Constraints**: workflow, regulatory, organisational, time

For the Destination Master Browser, work through:
- First-time reviewer
- Power reviewer
- Accessibility-need reviewer

Plus the **systems context** (per Norman's critique): what's downstream of the browser? What's upstream? Who else depends on its outputs?

### Step 2 — Activity 2 audit: User requirements

For each requirement currently encoded in the workspace, capture:

- The requirement (in GOV.UK user-need form or acceptance-criterion form)
- Which artifact encodes it (rule sheet section / criteria sheet ID / etc)
- Which W3C triad lens it serves (usability / accessibility / inclusion)
- Gap analysis: what requirements are *implicit* in v1.1 but not explicitly captured?

### Step 3 — Activity 3 audit: Design solutions

For each major design solution shipped or specified in v1.1, capture:

- The solution (component, behaviour, or pattern)
- Which user requirement it satisfies
- Which Topic 4 loop produced it (if any)
- Whether the solution shape was *chosen* (alternatives considered) or *defaulted* (first plausible adopted)

### Step 4 — Activity 4 audit: Evaluation

For evaluation evidence in the workspace:

- The 19-gate Playwright walkthrough (machine-grade evaluation)
- The smoke test (post-PR #10)
- The polish behavioural tests (PR #12)
- Lab 04's falsification criteria (test specifications, not run)
- Gap analysis: what *human-grade* evaluation exists? (Honest answer: very little; named as a gap.)

### Step 5 — Six-principle audit

For each of ISO 9241-210's six principles, mark Pass / Partial / Fail with evidence:

1. The design is based on an explicit understanding of users, tasks, and environments
2. Users are involved throughout design and development
3. The design is driven and refined by user-centred evaluation
4. The process is iterative
5. The design addresses the whole user experience
6. The design team includes multidisciplinary skills and perspectives

For each Partial or Fail, propose the honest mitigation (which may be "name the limitation explicitly" rather than "fix it").

### Step 6 — W3C triad audit

Apply each lens to v1.1:

- **Usability**: typical-case task completion (covered by the 19-gate walkthrough)
- **Accessibility**: assistive-tech compatibility (covered partially by ARIA + focus + keyboard work; explicit gaps named)
- **Inclusion**: full diversity of users — language, culture, age, device, context, ability — what's *missing* from v1.1?

### Step 7 — Findings and prioritised list

Consolidate the audit into:

- **Strengths**: where v1.1 + the design discipline cleanly satisfy HCD
- **Gaps**: where HCD activities or principles are under-served
- **Prioritised findings**: ranked list of HCD-driven recommendations for v1.2, with each item tagged by which ISO activity it serves

### Step 8 — Master-browser checklist Topic 5 section

Append Topic 5 gates and anti-patterns to `design/checklists/master-browser-design-checklist.md`:

- Four HCD gates (per-activity, applied to every v1.2 backlog item)
- Four anti-patterns specific to HCD in solo workspaces
- A canonical pointer to the HCD audit doc

## Expected outputs

```text
design/foundations/topic-05-hcd-audit.md
  ├─ Step 1: Context-of-use for three personas + systems context
  ├─ Step 2: User-requirements audit + gap analysis
  ├─ Step 3: Design-solutions audit
  ├─ Step 4: Evaluation audit + honest naming of human-grade gap
  ├─ Step 5: Six-principle audit (Pass/Partial/Fail per principle)
  ├─ Step 6: W3C triad audit
  └─ Step 7: Findings + prioritised v1.2 HCD list

curriculum/courses/des-001-design-foundations/submissions/
  lab-05-hcd-audit-results.md
    Formal lab submission with exec summary, key findings, decision-gate
    satisfaction, and reusable capabilities extracted.

design/checklists/master-browser-design-checklist.md
  Topic 5 section appended (§26 + §27 + §28).
```

## Submission checklist

- [ ] All four ISO activities audited with evidence per activity (Steps 1–4)
- [ ] All six ISO principles graded Pass/Partial/Fail with evidence (Step 5)
- [ ] All three W3C triad lenses applied to v1.1 (Step 6)
- [ ] Prioritised v1.2 HCD findings list (Step 7)
- [ ] Master-browser checklist Topic 5 section appended (Step 8)

## Rubric alignment

- *Multi-source coverage* — every audit cell cites the source(s) (ISO / Norman / IDEO / W3C) that constrain it
- *Application to CodeMike/browser* — the audit runs against v1.1, not a hypothetical
- *Checklist/actionability* — outputs feed into v1.2 backlog with HCD activity tags
- *Academic discipline* — audit is versioned (Audit 1) so future audits can be tracked

## Decision gate before closing the lab

Lab 05 is complete when:

1. All four ISO activities have at least one piece of evidence
2. All six ISO principles are graded with evidence
3. All three W3C triad lenses have explicit findings
4. The v1.2 HCD findings list is prioritised, not just enumerated
5. Each finding is tagged with the ISO activity it serves

Failure on any of these means re-run the relevant step. This is the *audit discipline* HCD demands.
