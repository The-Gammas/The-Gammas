# Jaime's sandbox — data preparation

**Status:** active exploratory work; not yet promoted to the shared pipeline.

This folder contains Jaime's assigned contribution: choose and understand the HCP working-memory dataset, prepare the
0-back / 2-back inputs (**tasks 1–2**), inspect the behavioural target and document the hand-off to the rest of the
group. The work stays here until it is finished and reviewed with the team.

The four notebooks are a **narrated path, one per role**, and are written in the **four-step modelling frame** taught
in W2D1 ([Blohm et al., 2019](https://doi.org/10.1523/ENEURO.0352-19.2019); the tutorial is pulled to
`coursework/W2D1/`), so the reasoning is replicable and shares the vocabulary the whole group uses. Read them in order.
Each is an EXPLORE log: clean code, tables and focused plots, every decision tied to its evidence, and the official
NMA loaders referenced as the code-style base.

## Contents — read in order

| File | Role | Purpose | Current state |
|---|---|---|---|
| [`00_framing_and_dataset_choice.ipynb`](00_framing_and_dataset_choice.ipynb) | **why these data** | Blohm 4 steps (phenomenon→question→ingredients→hypothesis) → derive the data requirements → pick the dataset (prose + links to the official guide, not defensive loaders). The costed A/B/C decision for Monday. | Executed against real data |
| [`01_ingestion_and_ev.ipynb`](01_ingestion_and_ev.ipynb) | **the deliverable (tasks 1–2)** | Ingestion + EV segmentation: BOLD time series, 0/2-back frame selection, `Stats.txt` target, region table and anti-leakage subject split. | Executed with real outputs |
| [`02_eda_and_data_dictionary.ipynb`](02_eda_and_data_dictionary.ipynb) | **understand the data** | Download/access (with guide links) + a **step-by-step EDA of both finalists** (A 100-subj and B 339-subj): load → columns → networks → conditions → target → basic viz. Plus a data dictionary of the objects. | Executed with real outputs |
| [`03_dataset_comparison.ipynb`](03_dataset_comparison.ipynb) | **the A/B decision** | Both finalists on one shared code layer: side-by-side QC, target distribution, an example FC reconfiguration map, and a reasoned A-vs-B recommendation. Decision support for the team, not a unilateral choice. | Executed with real outputs |
| [`datasets.py`](datasets.py) | **loaders / I-O** | Config + raw loaders (A **and** B): `DatasetSpec`, `spec_a`/`spec_b`, constants, `load_subjects`, `load_timeseries` (`bold7`=RL/`bold8`=LR for B), `list_rest_runs`/`load_rest_timeseries` (B) | Regression-verified vs. the old A helpers |
| [`preprocessing.py`](preprocessing.py) | **preprocessing** | Raw → analysis-ready: `condition_frames`/`condition_timeseries`, `behaviour_table`, `signal_detection_table`, `region_table` | A+B; B yields 339→336 analytic subjects |
| [`evaluation.py`](evaluation.py) | **split + QC** | `make_split` (leakage-safe, N-agnostic) + `validate_dataset` (aggregate A/B QC) | A/B verified |
| [`artifacts_staging/`](artifacts_staging/) | staged outputs | Local generated tables and exploratory split | Ignored by Git; not part of the initial public scaffold |

The code layer is organised **by data-science category, not by dataset** — `datasets` (I/O) ← `preprocessing` (transforms) ← `evaluation` (split + QC) — so A and B live behind one interface. Modelling (FC, graphs, prediction) is intentionally downstream (the team's), not here.

Figures live **embedded** in the notebooks (no loose `fig*.png` in the folder; they are gitignored).

## Datasets on disk

Both HCP candidates live under `data/` (gitignored). **Finalist A** (`hcp_task/`, 100 subj) is the current
base for tasks 1–2; **Finalist B** (`load_hcp`, 339 subj) adds resting-state and consolidated behaviour. Full
layout, provenance and the load contract → [`data/README.md`](../../data/README.md) · [`docs/data-dictionary.md`](../../docs/data-dictionary.md).

## How to run

The notebooks open from the repository root or from this directory. Their setup cells locate the repository and use
the `data/` root by default — files are grouped by loader (`A_load_hcp_task_with_behaviour/`, `B_load_hcp/`), with a
flat-layout fallback; set `GAMMAS_DATA_DIR` to use another local directory. The data are not stored in Git and require
accepting the HCP Data Use Terms — download, placement and a minimal load example are in [`data/README.md`](../../data/README.md).

**This folder is the shared A/B data layer.** `datasets.py` ← `preprocessing.py` ← `evaluation.py` are meant to be
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
- `acc_2bk` is present for all 100 subjects (Finalist A) and ranged ≈ 0.54–0.99 in this subset.
- Network labels stored in `regions.npy` are truncated and are expanded by `NETWORK_FULL`.
- The official helper functions do not parse the behavioural `Stats.txt`; this sandbox implements that parser.
- Finalist A contains **no resting-state**; Finalist B does (4 rest runs × 1200 frames) — see `02` for the sample rest FC.
- Finalist B's `wm.csv` carries per-condition ACC/RT comparable to A's `Stats.txt` (mean `acc_2bk` ≈ 0.85) — **not** coarser.

These facts describe the inspected data. Whether 312 frames are sufficient for stable FC, which target is primary and
which split/model to use remain team-level methodological decisions.

## Before promotion

1. Rerun the notebooks from top to bottom using the documented data path.
2. Review the candidate target and hand-off format with the group.
3. Reconcile the sandbox function signatures with whatever shared API the team actually needs.
4. Remove subject identifiers and keep only safe, useful outputs in the promoted notebook.
5. Create the first real shared notebook in `pipeline/`; do not overwrite this exploratory record.
