# Jaime's sandbox — data preparation

**Status:** active exploratory work; not yet promoted to the shared pipeline.

This folder contains Jaime's assigned contribution: choose and understand the HCP working-memory
dataset, prepare the 0-back / 2-back inputs, inspect behavioural variables and document the hand-off
to the rest of the group. The work stays here until it is finished and reviewed with the team.

The three notebooks are a **narrated cognitive path** — read them in order. Each is an EXPLORE log:
clean code, tables and focused plots over long prints, with every decision tied to the evidence that
drove it. Nothing is a straitjacket; when we learn something new, we revise.

## Contents — read in order

| File | Purpose | Current state |
|---|---|---|
| [`00_project_and_dataset_selection.ipynb`](00_project_and_dataset_selection.ipynb) | **Start here.** From research intent → the whole dataset landscape → ruling out the unfit → hands-on comparison of the two HCP finalists (100-subj vs 339-subj) → the costed A/B/C decision for Monday | Executed against both real datasets + official loader source |
| [`01_ingestion_and_ev.ipynb`](01_ingestion_and_ev.ipynb) | Ingestion + EV segmentation (steps 1–2): BOLD time series, 0/2-back frame selection, `Stats.txt` target, region table and anti-leakage subject split, with plots | Executed with real outputs |
| [`02_data_dictionary.ipynb`](02_data_dictionary.ipynb) | Self-generating dictionary of the objects, shapes, networks and candidate targets, with plots | Executed with real outputs |
| [`ingestion.py`](ingestion.py) | Reusable loading, EV, behaviour, region-table and exploratory split helpers | Executed against the real dataset; API still local to this sandbox |
| [`artifacts_staging/`](artifacts_staging/) | Local generated tables and exploratory split | Ignored by Git; not part of the initial public scaffold |

The flat layout is intentional: the notebooks import the neighbouring `ingestion.py`, and adding
more directory levels would make the setup harder to explain.

## Datasets on disk

Both HCP candidates are downloaded locally under `data/` (all gitignored — see notebook 00 for why
each exists):

- `data/hcp_task/` — **Finalist A**, `load_hcp_task_with_behaviour`, 100 subjects, task only, per-subject `Stats.txt`. Current base for notebooks 01/02.
- `data/hcp_rest/`, `data/hcp_task_339/`, `data/hcp/` — **Finalist B**, `load_hcp`, 339 subjects, adds real resting-state (4 runs) and consolidated behaviour (`hcp/behavior/wm.csv`).

## How to run

The notebooks can be opened from the repository root or from this directory. Their setup cells
locate the repository and use:

```text
data/hcp_task/
```

as the default dataset location. Set `GAMMAS_DATA_DIR` to use another local directory. The data are
not stored in Git and require acceptance of the HCP Data Use Terms.

The embedded outputs document the successful run performed before this structural cleanup. After
changing setup paths, rerun the notebooks against the local dataset before promoting them.

## Findings verified during exploration

- WM time series have shape `(360, 405)` per run.
- Pooling four stimulus categories gives 156 frames per load and run, or 312 after LR+RL are combined.
- The 0-back and 2-back frame sets do not overlap.
- `acc_2bk` is present for all 100 subjects and ranged from approximately 0.54 to 0.99 in this subset.
- Network labels stored in `regions.npy` are truncated and are expanded by `NETWORK_FULL`.
- The official helper functions do not parse the behavioural `Stats.txt`; this sandbox implements that parser.
- Finalist A (`load_hcp_task_with_behaviour`) contains **no resting-state** acquisition (7 tasks only). Resting-state exists in Finalist B (`load_hcp`, 339 subjects, 4 rest runs × 1200 frames). This bears on abstract Objective 2 — see `00_project_and_dataset_selection.ipynb` for the full comparison and the three costed options.
- Finalist B's behaviour file `hcp/behavior/wm.csv` carries per-condition ACC/RT (mean `acc_2bk` ≈ 0.85, range 0.41–1.0 over 336 subjects) — **comparable** to our `Stats.txt` target, not coarser. This corrected an earlier assumption and makes switching to B more attractive than first thought.

These facts describe the inspected data. Whether 312 frames are sufficient for stable FC, which
target is primary and which split/model should be used remain team-level methodological decisions.

## Before promotion

1. Rerun both notebooks from top to bottom using the documented data path.
2. Review the candidate target and hand-off format with the group.
3. Reconcile the sandbox function signatures with whatever shared API the team actually needs.
4. Remove subject identifiers and keep only safe, useful outputs in the promoted notebook.
5. Create the first real shared notebook in `pipeline/`; do not overwrite this exploratory record.

