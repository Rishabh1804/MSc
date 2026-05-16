# PRODUCTISATION.md — Notebook to Product Workflow

CodeMike should not let useful data science remain trapped in notebooks.

## Productisation Path

```text
notebook → script → reusable module → API/function → UI integration → documented transfer
```

## Stages

## 1. Exploration

Use notebooks to understand data, test assumptions, and create first evidence.

## 2. Stabilisation

Move repeated logic into scripts or reusable functions.

## 3. Packaging

Create a clear input/output contract and place stable logic under `src/` or the relevant project folder.

## 4. Evaluation

Check correctness, reproducibility, edge cases, and limitations.

## 5. Transfer

Apply the method to a real project and record the transfer in `TRANSFER_LOG.md`.

## Productisation Checklist

- Is the decision or user problem clear?
- Are inputs and outputs documented?
- Is exploratory code separated from reusable code?
- Are assumptions documented?
- Is the method evaluated against a baseline where relevant?
- Are privacy and responsible AI risks checked?
- Is there an evidence artifact?
- Is the transfer logged?
