# Jaime's sandbox — data preparation

**Status:** active exploratory work; not yet promoted to the shared pipeline.

This folder contains Jaime's assigned contribution: choose and understand the HCP working-memory dataset, prepare the
0-back / 2-back inputs (**tasks 1–2**), inspect the behavioural target and document the hand-off to the rest of the
group. The work stays here until it is finished and reviewed with the team.

The three notebooks are a **narrated path, one per role**, and are written in the **four-step modelling frame** taught
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
| [`ingestion.py`](ingestion.py) | shared logic | Reusable loading, EV, behaviour, region-table and exploratory split helpers | Executed against the real dataset; API still local to this sandbox |
| [`artifacts_staging/`](artifacts_staging/) | staged outputs | Local generated tables and exploratory split | Ignored by Git; not part of the initial public scaffold |

Figures live **embedded** in the notebooks (no loose `fig*.png` in the folder; they are gitignored).

## Datasets on disk

Both HCP candidates are downloaded locally under `data/` (all gitignored — see notebook `00`/`02` for why each exists):

- `data/hcp_task/` — **Finalist A**, `load_hcp_task_with_behaviour`, 100 subjects, task only, per-subject `Stats.txt`. Current base for tasks 1–2.
- `data/hcp_rest/`, `data/hcp_task_339/`, `data/hcp/` — **Finalist B**, `load_hcp`, 339 subjects, adds real resting-state (4 runs) and consolidated behaviour (`hcp/behavior/wm.csv`).

## How to run

The notebooks can be opened from the repository root or from this directory. Their setup cells locate the repository
and use `data/hcp_task/` (and `data/hcp*/` for B) as the default data location. Set `GAMMAS_DATA_DIR` to use another
local directory. The data are not stored in Git and require acceptance of the HCP Data Use Terms.

To re-run and re-embed outputs (executed with the repo's `pixi` env):

```bash
pixi run --manifest-path <NeuroAcademy>/pyproject.toml python -m nbconvert \
  --to notebook --execute --inplace 01_ingestion_and_ev.ipynb
```

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
