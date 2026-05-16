# Pattern — EDA Notebook Template

## Purpose

Use this pattern to structure exploratory data analysis notebooks so they are readable, restartable, and useful as evidence.

## Notebook Header

```md
# Exploratory Data Analysis — <dataset/project>

Date:
Author: CodeMike
Linked module/project:
Dataset:
Privacy level:
Objective:
Decision supported:
```

## 1. Objective

State what the notebook is trying to learn.

Good objective examples:

- Understand sales variation by product and region.
- Identify missingness and quality issues before modelling.
- Explore trip option tradeoffs before recommendation scoring.
- Identify production bottlenecks from synthetic batch data.

## 2. Dataset Summary

Include:

- source
- row count
- column count
- time period
- grain of data
- privacy level
- known limitations

## 3. Imports and Setup

Keep setup minimal and reproducible.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

## 4. Load Data

Show:

- file path or source
- load command
- first rows
- data shape

## 5. Schema and Types

Check:

- column names
- data types
- missing values
- duplicates
- date parsing
- categorical fields
- numeric fields

## 6. Data Quality Review

Use the data cleaning checklist.

Summarise:

- missingness
- duplicate issues
- invalid values
- outliers
- inconsistencies
- privacy concerns

## 7. Univariate Exploration

For important columns:

- distributions
- counts
- min/max
- mean/median where useful
- category frequencies

## 8. Bivariate / Relationship Exploration

Explore relationships relevant to the decision:

- category vs value
- time vs value
- group comparisons
- correlations where appropriate
- segment differences

## 9. Visual Analysis

Each visual should answer a question.

For every chart, include:

- question
- chart
- interpretation
- limitation

## 10. Key Findings

Use this structure:

```md
## Key Findings

1. Finding:
   Evidence:
   Limitation:

2. Finding:
   Evidence:
   Limitation:
```

## 11. Risks and Limitations

Record:

- data quality risks
- missing data risks
- bias risks
- small sample issues
- privacy concerns
- assumptions

## 12. Next Actions

Possible next actions:

- clean dataset
- build baseline model
- create dashboard
- define scoring criteria
- collect more data
- create capability card
- transfer to project

## Completion Criteria

- [ ] Objective is stated
- [ ] Dataset is registered
- [ ] Privacy level is classified
- [ ] Data quality is reviewed
- [ ] Findings are evidence-backed
- [ ] Limitations are stated
- [ ] Next action is clear
- [ ] Evidence entry is created if useful

## Related Files

- `DATASETS.md`
- `EVIDENCE.md`
- `QA_CHECKLIST.md`
- `patterns/data-cleaning-checklist.md`
