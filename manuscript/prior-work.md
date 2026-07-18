# Prior internal work

Explorations by the team that the project builds on. Kept as technical notes: what was done,
what it shows, and how it feeds the current plan.

> **Historical precursor.** The prediction, permutation and validation steps proposed below were
> subsequently implemented in notebooks `04` and `05`. Use the
> [living project plan](../docs/project-plan.md) for current status and interpretation.

## POC — "Neural Thermodynamics of the Triple Network" (Goutham)

[Colab notebook](https://colab.research.google.com/drive/1Wu9Ke8bqr_UQp8_ZmtLTus-l0Xja3oIq)

**What it does.** A first proof-of-concept on the consolidated HCP contrast CSVs
(`con_hcp.csv`, `df_subject_profiles.csv`). It frames the **Triple Network Model** — Frontoparietal
(FPN), Default (DMN), and Cingulo-Opercular / Salience — and asks whether Salience activation maps
onto the FPN/DMN shift under working-memory load. Method: a linear regression from the
Cingulo-Opercular `2bk − 0bk` contrast onto the FPN and DMN contrasts.

**Result.**

```
X = Cingulo-Opercular (salience) contrast   ->   Y = [FPN, DMN] contrast
R² = 0.627      coefficients: FPN = 0.83, DMN = 0.71
```

≈63% of the variance in the FPN/DMN load-related shift is captured by Salience activation
(on activation contrasts, within the same task).

**How it fed the plan.** This was a useful signal that Salience/Cingulo-Opercular was worth keeping
as a network of interest. The next step at the time, per the Project TA, was to **operationalize it as prediction on
held-out subjects with cross-validation**, using standard terms (low/high WM load), and move from
activation contrasts to the per-condition functional-connectivity features of the main pipeline.
Considerations for that step: a high R² between contrasts of the same task can reflect a shared
third factor (general engagement), so add inference (permutation test, CV) and controls (motion,
age). Prediction, the permutation null and a DVARS-proxy check are now implemented; age is unavailable
in the curated data. The framing ("network control theory", "thermodynamic actuator") is narrative; the measured
quantity is a regression on functional data — keep the wording technical in the write-up.
