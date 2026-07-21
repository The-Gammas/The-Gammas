# Pipeline — group-reviewed notebooks

This folder contains the **shared story of the analysis**, not every experiment the team tries.
It currently contains the reusable template plus the reviewed dataset-B onboarding/EDA notebook.
FC, prediction and external-validation results exist in `sandbox/jaime/`, but have not yet been
promoted as the group's final modelling pipeline.

| File | Shared status |
|---|---|
| [`00_NOTEBOOK_TEMPLATE.ipynb`](00_NOTEBOOK_TEMPLATE.ipynb) | Reusable starting point for personal sandboxes |
| [`01_explore_dataset_b.ipynb`](01_explore_dataset_b.ipynb) | Dataset-B onboarding and EDA on the shared data layer |

The working direction is:

1. Data ingestion and EV segmentation
2. Functional connectivity
3. Matrices to graphs
4. Graph metrics
5. Prediction and testing

These are conceptual stages, not a claim that five shared notebooks already exist. Work begins in
`sandbox/<name>/`; a notebook is added here only after the group can run it, understand it and agree
that it represents the current method. The team decided the final-week promotion scope and sprint
at the 20 July sync (see [`../docs/meetings/2026-07-20.md`](../docs/meetings/2026-07-20.md)); current
status lives in [`../docs/project-plan.md`](../docs/project-plan.md).

A promoted notebook should:

- explain its question and inputs;
- run from top to bottom;
- show key checks and visualisations;
- avoid subject identifiers and large outputs;
- end with findings, limitations and a clear hand-off to the next stage.
