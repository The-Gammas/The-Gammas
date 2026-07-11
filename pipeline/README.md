# Pipeline — group-reviewed notebooks

This folder contains the **shared story of the analysis**, not every experiment the team tries.
Right now it contains only a notebook template because the project is still in its exploratory
stage.

The working direction is:

1. Data ingestion and EV segmentation
2. Functional connectivity
3. Matrices to graphs
4. Graph metrics
5. Prediction and testing

These are planned stages, not completed notebooks. Work begins in `sandbox/<name>/`; a notebook is
added here only after the group can run it, understand it and agree that it represents the current
method.

Start with [`00_NOTEBOOK_TEMPLATE.ipynb`](00_NOTEBOOK_TEMPLATE.ipynb). A promoted notebook should:

- explain its question and inputs;
- run from top to bottom;
- show key checks and visualisations;
- avoid subject identifiers and large outputs;
- end with findings, limitations and a clear hand-off to the next stage.

