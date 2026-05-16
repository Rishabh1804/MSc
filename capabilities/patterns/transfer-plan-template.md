# Pattern — Transfer Plan Template

## Purpose

Use this pattern when moving a method, notebook, model, scoring system, template, or capability from the MSc workspace into another project.

## Core Principle

A capability is not fully useful until it can transfer cleanly.

## 1. Transfer Summary

```md
Transfer title:
Date:
Source module/capability:
Target project:
Transfer owner:
Status: proposed / in progress / transferred / rejected / monitoring
```

## 2. Target Project Need

```md
Problem:
Decision supported:
User/audience:
Why this transfer matters:
```

## 3. Source Artifact

```md
Source artifact:
Path:
Evidence:
Maturity level:
Known limitations:
```

## 4. Transfer Scope

What exactly is moving?

- concept
- checklist
- notebook
- script
- function
- model
- scoring rule
- dashboard pattern
- documentation
- prompt
- test

```md
In scope:
Out of scope:
```

## 5. Adaptation Needed

Record changes required for the target project:

- data schema changes
- UI changes
- performance needs
- privacy changes
- constraints
- domain assumptions
- user language
- testing requirements

## 6. Risks

```md
Risk:
Impact:
Mitigation:
```

Common risks:

- method does not fit target data
- assumptions hidden
- privacy level changes
- model overtrusted
- UI cannot explain output
- performance too slow
- target repo duplicates logic

## 7. Acceptance Criteria

```md
- [ ] Target project need is clear
- [ ] Source evidence exists
- [ ] Assumptions documented
- [ ] Input/output contract clear
- [ ] Privacy checked
- [ ] Responsible AI checked if relevant
- [ ] Target integration tested
- [ ] Transfer logged
```

## 8. Post-Transfer Review

```md
Outcome:
What improved:
What broke or weakened:
What should return to MSc as a lesson:
Next version:
```

## Required Logs

After transfer, update:

- `TRANSFER_LOG.md`
- `CAPABILITIES.md`
- `PROJECT_LOG.md`
- target project documentation

## Related Files

- `TRANSFER_LOG.md`
- `CAPABILITIES.md`
- `PRODUCTISATION.md`
- `QA_CHECKLIST.md`
