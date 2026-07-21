# Pipeline — group-reviewed notebooks

This folder contains the **shared story of the analysis**, not every experiment the team tries.
It contains the reusable template, the dataset-B onboarding/EDA notebook and a canonical evidence
notebook that consolidates the analyses proposed for the W3D5 presentation. The underlying source
notebooks remain in `sandbox/jaime/` so the full audit trail is preserved.

| File | Shared status |
|---|---|
| [`00_NOTEBOOK_TEMPLATE.ipynb`](00_NOTEBOOK_TEMPLATE.ipynb) | Reusable starting point for personal sandboxes |
| [`01_explore_dataset_b.ipynb`](01_explore_dataset_b.ipynb) | Dataset-B onboarding and EDA on the shared data layer |
| [`02_canonical_analysis_and_slides.ipynb`](02_canonical_analysis_and_slides.ipynb) | Executed canonical evidence path: FC prediction, identity-disjoint B→A transfer, activation robustness benchmark, segregation direction and presentation figures. Evidence complete; narrative proposal pending team approval. |

The working direction is:

1. Data ingestion and EV segmentation
2. Functional connectivity
3. Matrices to graphs
4. Graph metrics
5. Prediction and testing

These are conceptual stages, not a claim that five separate shared notebooks exist. `02` consolidates
the evidence into one reproducible path while linking every block to its source notebook. Its
recommended narrative keeps FC reconfiguration as the primary analysis and presents regional
activation as an unexpected benchmark; that placement remains a proposal until the team approves it.
Current status lives in [`../docs/project-plan.md`](../docs/project-plan.md).

A promoted notebook should:

- explain its question and inputs;
- run from top to bottom;
- show key checks and visualisations;
- avoid subject identifiers and large outputs;
- end with findings, limitations and a clear hand-off to the next stage.
