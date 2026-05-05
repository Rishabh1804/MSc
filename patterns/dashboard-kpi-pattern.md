# Pattern — Dashboard KPI Design

## Purpose

Use this pattern when designing dashboards, KPI views, or visual decision-support interfaces.

## Core Principle

No dashboard before the decision it supports is clear.

## 1. Decision Context

```md
Dashboard name:
Decision supported:
Primary user:
Decision frequency:
Action expected:
```

## 2. Audience

```md
Audience:
Technical level:
Device/context:
Time available:
Main question they need answered:
```

## 3. KPI Definition

Each KPI should be defined before visualisation.

```md
KPI name:
Definition:
Formula:
Unit:
Grain:
Time window:
Owner:
Target/threshold:
Known limitation:
```

## 4. KPI Quality Check

Ask:

- Does this KPI support a decision?
- Is the formula unambiguous?
- Is the data reliable?
- Can users interpret it correctly?
- Could it create perverse incentives?
- Is a target or benchmark needed?

## 5. Visual Selection

Use chart types intentionally.

Examples:

- trend over time → line chart
- part-to-whole → stacked bar or table, not always pie chart
- ranking → sorted bar
- distribution → histogram or box plot
- relationship → scatter plot
- operational status → scorecard + exception list

## 6. Layout

A useful dashboard usually needs:

1. Summary status
2. Key drivers
3. Exceptions or risks
4. Details / drilldown
5. Recommended action or next step

## 7. Interpretation Layer

For each major visual, include:

- what changed
- why it matters
- what action may be needed
- what limitation exists

## 8. Data and Refresh

```md
Data source:
Refresh frequency:
Data owner:
Lag:
Known data quality issue:
```

## 9. Mobile / PWA Considerations

If used in a PWA or mobile environment:

- avoid horizontal scrolling
- use readable touch targets
- prioritise summary cards
- collapse details progressively
- keep charts legible
- make empty/loading/error states clear

## 10. QA Checklist

- [ ] Decision is clear
- [ ] Audience is clear
- [ ] KPIs are defined
- [ ] Formulas are documented
- [ ] Data source is known
- [ ] Charts match questions
- [ ] Limitations are visible
- [ ] Mobile/readability considered
- [ ] Next action is clear

## Common Failures

- Vanity metrics
- Too many KPIs
- Undefined formulas
- No decision link
- Misleading chart scales
- No target or benchmark
- Data source hidden
- Dashboard as decoration instead of decision support

## Related Files

- `decision-science/`
- `QA_CHECKLIST.md`
- `PRODUCTISATION.md`
- `TRANSFER_LOG.md`
