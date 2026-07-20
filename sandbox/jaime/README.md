# Jaime's sandbox — data layer, modelling audit and validation

**Status (20 Jul):** seven notebooks. The data onboarding is represented in shared `pipeline/01`; the
modelling/audit notebooks `04`–`06` remain exploratory until the team reviews the method and
final-week scope on Monday. Notebook `06` (tangent-space method candidate) is the newest and is the
only one whose outputs are currently cleared.

This folder began as Jaime's data-ingestion contribution and now records the full evidence path:
choose and understand the HCP cohorts, prepare 0-back/2-back inputs, port and audit Goutham's model on
B, and validate it externally on A. The notebooks are evidence for team review, not unilateral method
decisions.

The six notebooks are a **narrated path, one per role**, and are written in the **four-step modelling frame** taught
in W2D1 ([Blohm et al., 2019](https://doi.org/10.1523/ENEURO.0352-19.2019); the tutorial is pulled to
`coursework/W2D1/`), so the reasoning is replicable and shares the vocabulary the whole group uses. Read them in order.
Each is an EXPLORE log: clean code, tables and focused plots, every decision tied to its evidence, and the official
NMA loaders referenced as the code-style base.

## Contents — read in order

| File | Role | Purpose | Current state |
|---|---|---|---|
| [`00_framing_and_dataset_choice.ipynb`](00_framing_and_dataset_choice.ipynb) | **why these data** | Blohm 4 steps (phenomenon→question→ingredients→hypothesis) → derive requirements and compare the original dataset candidates. Historical decision path leading to B as the primary analysis cohort. | Executed against real data |
| [`01_ingestion_and_ev.ipynb`](01_ingestion_and_ev.ipynb) | **the deliverable (tasks 1–2)** | Ingestion + EV segmentation: BOLD time series, 0/2-back frame selection, `Stats.txt` target, region table and anti-leakage subject split. | Executed with real outputs |
| [`02_eda_and_data_dictionary.ipynb`](02_eda_and_data_dictionary.ipynb) | **understand the data** | Download/access + step-by-step EDA of both cohorts (A 100-subj and B 339-subj): load → columns → networks → conditions → target → basic viz. Plus a data dictionary. | Executed with real outputs |
| [`03_dataset_comparison.ipynb`](03_dataset_comparison.ipynb) | **the A/B decision** | Both cohorts on one shared code layer: side-by-side QC, target distribution, an example FC reconfiguration map, and the evidence for their current roles. | Executed with real outputs |
| [`04_goutham_pipeline_on_B.ipynb`](04_goutham_pipeline_on_B.ipynb) | **the experiment (dataset B)** | Goutham's FC pipeline on B (336 subj): per-condition FC → 2bk−0bk reconfiguration → 78-dim fingerprint → RidgeCV + permutation null. Prediction, specificity (trait vs reconfiguration, general ability, motion), direction, `d′` correction, multiple comparisons. | Executed with real outputs |
| [`05_dataset_A_external_validation.ipynb`](05_dataset_A_external_validation.ipynb) | **using dataset A** | Same experiment, A as an independent cohort: A/B subject-overlap constraint, four train/test designs, and the recommended one — train on B-only (301), test on A (100), leakage-free external validation (r≈0.40, p<0.001). | Executed with real outputs |
| [`06_tangent_fc_benchmark.ipynb`](06_tangent_fc_benchmark.ipynb) | **method candidate** | Does a log-Euclidean tangent representation beat the 78-network fingerprint? One estimator, three feature sets, 4 s HRF-delayed windows; audited reproduction gate → d′ robustness → development-only CV → identity-disjoint B→A transfer. | Code reorganised 20 Jul; **outputs cleared, needs a re-run** (cache makes it cheap) |
| [`datasets.py`](datasets.py) | **loaders / I-O** | Config + raw loaders (A **and** B): `DatasetSpec`, `spec_a`/`spec_b`, constants, `load_subjects`, `load_timeseries` (`bold7`=RL/`bold8`=LR for B), `list_rest_runs`/`load_rest_timeseries` (B) | Regression-verified vs. the old A helpers |
| [`preprocessing.py`](preprocessing.py) | **preprocessing** | Raw → analysis-ready: `condition_frames`/`condition_timeseries` (both take `delay=` for the HRF shift), `behaviour_table`, `signal_detection_table`, `region_table` | A+B; B yields 339→336 analytic subjects |
| [`connectivity.py`](connectivity.py) | **FC representations** | BOLD → features: `subject_covariances` (Ledoit-Wolf), `matrix_logarithms`, `log_triangles`, `TangentCentering` (train-only reference), `network_fingerprint` (78-dim baseline) | Used by `06`; synthetic tests green |
| [`evaluation.py`](evaluation.py) | **split + QC + statistics** | `make_split` (leakage-safe, N-agnostic), `validate_dataset` (aggregate A/B QC), plus the shared `ridge_pipeline`, `correlation`, `permutation_p`, `bootstrap_ci`, `partial_correlation` | A/B verified |
| [`test_connectivity.py`](test_connectivity.py) | **checks** | Synthetic tests for the leakage-critical tangent reference, paired reconfiguration, chunked log extraction, fingerprint layout and the delayed EV conversion | `python -m unittest discover -s .` — 7 green |
| [`artifacts_staging/`](artifacts_staging/) | staged outputs | Local generated tables and exploratory split | Ignored by Git; not part of the initial public scaffold |
| [`docs/`](docs/README.md) | **writing** | Prose deliverables, kept apart from the notebooks and code layer. [`05_abstract_proposal.md`](docs/05_abstract_proposal.md) is the pre-workshop Valeria + results merge, restructured to NMA's **ABC…G** | v2, 2026-07-17; status checked 2026-07-18; evidence-based review Monday |

The reusable code layer is organised **by data-science category, not by dataset** — `datasets` (I/O)
→ `preprocessing` (transforms) → `connectivity` (FC representations) → `evaluation` (split + QC +
statistics) — so A and B live behind one interface. The modelling notebooks `04`–`06` consume that
layer but are not themselves a shared API.

Tangent geometry in `connectivity` is **log-Euclidean** (reference = arithmetic mean of training
matrix logs). `nilearn`'s `ConnectivityMeasure(kind="tangent")` is *not* a drop-in — it uses the
affine-invariant geometric mean, so swapping it in would silently move every benchmark number.

Figures live **embedded** in the notebooks (no loose `fig*.png` in the folder; they are gitignored).

## Datasets on disk

Both HCP cohorts live under `data/` (gitignored). **B** (`load_hcp`, 339 subjects; 336 analytic) is
the primary MVP analysis cohort. **A** (`load_hcp_task_with_behaviour`, 100 subjects) is the
independent external-validation cohort and is not merged with B. Full layout, provenance and load
contract → [`data/README.md`](../../data/README.md) ·
[`docs/data-dictionary.md`](../../docs/data-dictionary.md).

## How to run

The notebooks open from the repository root or from this directory. Their setup cells locate the repository and use
the `data/` root by default — files are grouped by loader (`A_load_hcp_task_with_behaviour/`, `B_load_hcp/`), with a
flat-layout fallback; set `GAMMAS_DATA_DIR` to use another local directory. The data are not stored in Git and require
accepting the HCP Data Use Terms — download, placement and a minimal load example are in [`data/README.md`](../../data/README.md).

**This folder is the shared A/B data layer.** `datasets.py` → `preprocessing.py` → `evaluation.py` are meant to be
**imported read-only** by everyone (teammates work in their own `sandbox/<name>/` but reach these here). The
[notebook template](../../pipeline/00_NOTEBOOK_TEMPLATE.ipynb) wires the import automatically; the minimal call
sequence lives in [`data/README.md` → Load it](../../data/README.md#load-it-shared-ab-interface). Signatures may still
evolve before the layer is promoted to a package — if you need stability, pin to a commit.

To re-run and re-embed a notebook's outputs, after `pip install -r requirements.txt` from the repo root:

```bash
python -m nbconvert --to notebook --execute --inplace 01_ingestion_and_ev.ipynb
```

(The maintainer runs the same command through the repo's private `pixi` env; plain `python` after the venv install works too.)

## Findings verified during exploration

- WM time series have shape `(360, 405)` per run.
- Pooling four stimulus categories gives 156 frames per load and run, or 312 after LR+RL are combined.
- The 0-back and 2-back frame sets do not overlap.
- `acc_2bk` is present for all 100 subjects in cohort A and ranged ≈ 0.54–0.99 in this subset.
- Network labels stored in `regions.npy` are truncated and are expanded by `NETWORK_FULL`.
- The official helper functions do not parse the behavioural `Stats.txt`; this sandbox implements that parser.
- Cohort A contains **no resting-state**; cohort B does (4 rest runs × 1200 frames) — see `02` for the sample rest FC.
- Cohort B's `wm.csv` carries per-condition ACC/RT comparable to A's `Stats.txt` (mean `acc_2bk` ≈ 0.85) — **not** coarser.

These facts describe the inspected data. The split/model and corrected d′ are implemented; FC
estimation, the 78-feature summary and the final reporting hierarchy remain team-level decisions.

## Before promotion

1. Rerun the candidate promoted notebook from top to bottom using the documented data path.
2. Review the FC method, 78-feature summary and hand-off format with the group.
3. Reconcile the sandbox function signatures with whatever shared API the team actually needs.
4. Remove subject identifiers and keep only safe, useful outputs in the promoted notebook.
5. Promote only the modelling story selected for the final-week sprint; do not overwrite this
   exploratory record.
