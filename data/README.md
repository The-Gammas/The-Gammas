# Data — local only

This directory documents where local data live; its contents are ignored by Git.

> 🗺️ **Full data map, folder structures, object shapes and glossary → [`docs/data-dictionary.md`](../docs/data-dictionary.md).**
> Read it first: the two group folders here are the **2 datasets** (Finalist A + B), with **different internal structures**.

Files are grouped by the NMA loader they come from. The loaders in `sandbox/jaime/datasets.py`
resolve this grouped layout **and** fall back to the legacy flat layout (`data/hcp_task/…`), so
grouped data, flat data, or a fresh flat download all read unchanged.

```text
data/
├── A_load_hcp_task_with_behaviour/          # Finalist A · load_hcp_task_with_behaviour
│   └── hcp_task/                             #   regions.npy · subjects_list.txt · subjects/ (+ Stats.txt)
├── B_load_hcp/                              # Finalist B · load_hcp
│   ├── hcp_task_339/                         #   task time series + EVs (pseudo-IDs)
│   ├── hcp_rest/                             #   resting-state (4 runs)
│   ├── hcp/                                  #   behavior/wm.csv + covariates + ID map
│   └── hcp_atlas_339.npz                     #   atlas geometry (coords + vertex→ROI)
├── HCP_S1200_Release_Reference_Manual.pdf    # shared reference (both datasets)
└── README.md
```

## Obtain the data (replicate this exact layout)

The tree above is the **contract** — `datasets.py` looks for those exact folder names. To reproduce it
on your machine:

**1. Accept the [HCP Data Use Terms](https://www.humanconnectome.org/study/hcp-young-adult/document/wu-minn-hcp-consortium-open-access-data-use-terms)** — required before any download.

**2. Download each finalist** with its official NMA loader notebook (each one pulls its OSF tarballs):

| Finalist | Loader notebook | It downloads | Place it at |
|---|---|---|---|
| **A** | [`load_hcp_task_with_behaviour`](https://compneuro.neuromatch.io/projects/fMRI/load_hcp_task_with_behaviour.html) | `hcp_task/` | `data/A_load_hcp_task_with_behaviour/hcp_task/` |
| **B** | [`load_hcp`](https://compneuro.neuromatch.io/projects/fMRI/load_hcp.html) | a task folder, `hcp_rest/`, `hcp/`, `hcp_atlas_339.npz` | `data/B_load_hcp/` — **rename B's task folder to `hcp_task_339/`** (our convention, so it never clashes with A's `hcp_task/`) |

**3. Simpler alternative** — skip the group dirs and drop the folders **flat** in `data/`
(`data/hcp_task/`, `data/hcp_task_339/`, `data/hcp_rest/`, `data/hcp/`, `data/hcp_atlas_339.npz`); the
loaders resolve grouped **or** flat. Point `GAMMAS_DATA_DIR` at any root if your data live elsewhere.

**4. Verify** you matched the layout — run
[`sandbox/jaime/00_framing_and_dataset_choice.ipynb`](../sandbox/jaime/00_framing_and_dataset_choice.ipynb),
or from the repo root:

```bash
python -c "import sys; sys.path.insert(0, 'sandbox/jaime'); import datasets as ds; \
  print('A ok:', ds.spec_a('data').task_dir.exists(), '| B ok:', ds.spec_b('data').task_dir.exists())"
```

Two `True` and you match our setup.

Full object map, shapes and glossary → [`docs/data-dictionary.md`](../docs/data-dictionary.md). Raw data,
per-subject behaviour, splits and other derived files must never be committed (all of `data/` except this
README is gitignored).

