# Data — local only

This directory documents where local data live; its contents are ignored by Git.

> 🗺️ **Full data map, folder structures, object shapes and glossary → [`docs/data-dictionary.md`](../docs/data-dictionary.md).**
> Read it first: the two group folders here are **2 cohorts** (A + B), with different internal
> structures. **B is the current primary analysis cohort; A is external validation.**

Files are grouped by the NMA loader they come from (`A_…/`, `B_…/`); `sandbox/jaime/datasets.py`
resolves this layout for you. Cohort A reads unchanged; cohort B always needs its two renames
(see the table below). A flat layout works too — see step 3.

```text
data/
├── A_load_hcp_task_with_behaviour/          # Cohort A · external validation
│   └── hcp_task/                             #   regions.npy · subjects_list.txt · subjects/ (+ Stats.txt)
├── B_load_hcp/                              # Cohort B · primary MVP analysis
│   ├── hcp_task_339/                         #   task time series + EVs (pseudo-IDs)
│   ├── hcp_rest/                             #   resting-state (4 runs)
│   ├── hcp/                                  #   behavior/wm.csv + covariates + ID map
│   └── hcp_atlas_339.npz                     #   atlas geometry (coords + vertex→ROI)
├── HCP_S1200_Release_Reference_Manual.pdf    # shared reference (both datasets)
└── README.md
```

## Obtain the data (replicate this exact layout)

The tree above is the **contract** — `datasets.py` looks for those exact folder names. Check your disk
space first: cohort A is ~1 GB, cohort B ~8 GB. To reproduce the layout on your machine:

**1. Accept the [HCP Data Use Terms](https://www.humanconnectome.org/study/hcp-young-adult/document/wu-minn-hcp-consortium-open-access-data-use-terms)** — required before any download. This is a legal acknowledgement; the NMA loaders fetch a *repackaged* subset from **OSF**, so you do **not** need ConnectomeDB credentials or the HCP downloader.

**2. Run the official NMA loader notebook** for the cohort you need (open it in Colab — it runs and
pulls its OSF tarballs), then **move** what it writes into `data/`, applying cohort B's two renames. A
and B write to *different* places (the "working dir" is Colab's `/content/…`, or the folder you launch
the notebook from locally):

| Cohort | Current role | Loader (opens in Colab · pinned v3.0.2) | Where it writes | Move into `data/…` as |
|---|---|---|---|---|
| **A** | External validation | [`load_hcp_task_with_behaviour`](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/v3.0.2/projects/fMRI/load_hcp_task_with_behaviour.ipynb) | `hcp_task/` (in the working dir) | `A_load_hcp_task_with_behaviour/hcp_task/` |
| **B** | Primary MVP analysis | [`load_hcp`](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/v3.0.2/projects/fMRI/load_hcp.ipynb) | `DATA/hcp_task/`, `DATA/hcp_rest/`, `DATA/hcp/` (extracted into a **`DATA/` subfolder**) **plus** `atlas.npz` (in the working-dir root) | `B_load_hcp/` as `DATA/hcp_task/`→**`hcp_task_339/`**, `DATA/hcp_rest/`→`hcp_rest/`, `DATA/hcp/`→`hcp/`, `atlas.npz`→**`hcp_atlas_339.npz`** |

Only the **bold** names change (so B's task data and atlas don't collide with A's `hcp_task/`); `hcp_rest/`
and `hcp/` keep their names. **Name trap:** `load_hcp_task` is a separate task-only entry point for the same
339-subject task archive B uses — **not** an additional dataset here; use `load_hcp` for cohort B.

**3. Flat layout (optional, simpler)** — you may skip the group dirs and drop the leaf folders directly under
`data/` (`data/hcp_task/`, `data/hcp_task_339/`, `data/hcp_rest/`, `data/hcp/`, `data/hcp_atlas_339.npz`);
the loaders resolve grouped **or** flat. B's two renames are still required even flat. Point
`GAMMAS_DATA_DIR` at any root if your data live elsewhere (see [Load it](#load-it-shared-ab-interface)).

**4. Verify** (needs the environment installed first — `pip install -r requirements.txt`). From the repo
root, first confirm every artifact is in place:

```bash
python -c "import sys; sys.path.insert(0,'sandbox/jaime'); import datasets as ds; \
a, b = ds.spec_a('data'), ds.spec_b('data'); \
print('A  task:', a.task_dir.exists()); \
print('B  task:', b.task_dir.exists(), 'rest:', b.rest_dir.exists(), 'behaviour:', b.behaviour.exists(), 'atlas:', b.atlas.exists())"
```

All `True` for the cohort you downloaded means the paths are in place — but path existence is **not** proof
of a complete download. Then run the aggregate QC (subject counts, shapes, condition frames, missingness),
which raises a clear error if the download is incomplete:

```bash
python -c "import sys; sys.path.insert(0,'sandbox/jaime'); import datasets as ds, evaluation as ev; \
print(ev.validate_dataset(ds.spec_b('data')))"   # or ds.spec_a('data')
```

For the narrated, side-by-side QC of both cohorts see
[`sandbox/jaime/02_eda_and_data_dictionary.ipynb`](../sandbox/jaime/02_eda_and_data_dictionary.ipynb) and
[`03_dataset_comparison.ipynb`](../sandbox/jaime/03_dataset_comparison.ipynb).

## Load it (shared A/B interface)

Both cohorts sit behind **one** interface in [`sandbox/jaime/`](../sandbox/jaime/) — `datasets.py` (I/O)
→ `preprocessing.py` (transforms) → `evaluation.py` (split + QC). Import them read-only; switch dataset by
calling `spec_a` vs `spec_b` — nothing downstream branches on A vs B.

```python
import os, sys
from pathlib import Path

sys.path.insert(0, "sandbox/jaime")           # the shared A/B layer (run from the repo root)
import datasets as ds, preprocessing as pp, evaluation as ev

DATA = Path(os.environ.get("GAMMAS_DATA_DIR", "data"))

spec = ds.spec_b(DATA)                         # primary MVP; use spec_a for external validation
subjects = ds.load_subjects(spec)              # analytic cohort (A: 100 · B: 336)
ts    = pp.condition_timeseries(spec, subjects[0], "2back")   # (360, 312) BOLD, both runs
beh   = pp.behaviour_table(spec)               # per-subject target: acc_2bk, …
split = ev.make_split(spec)                    # leakage-safe train/test + CV, by subject
qc    = ev.validate_dataset(spec)              # aggregate QC (shapes, frames, counts)
```

`condition_timeseries(..., runs=(0,))` returns a single 156-frame run (for split-half reliability); the
default concatenates LR+RL to 312 frames. Working from your own `sandbox/<name>/` folder? The notebook
template ([`pipeline/00_NOTEBOOK_TEMPLATE.ipynb`](../pipeline/00_NOTEBOOK_TEMPLATE.ipynb)) ships a setup cell
that locates the repo root and this layer automatically, so its imports work from anywhere. Function-by-function
reference: the module docstrings and [`sandbox/jaime/README.md`](../sandbox/jaime/README.md).

---

Full object map, shapes and glossary → [`docs/data-dictionary.md`](../docs/data-dictionary.md). Raw data,
per-subject behaviour, splits and other derived files must never be committed (all of `data/` except this
README is gitignored).
