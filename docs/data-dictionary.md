# Data map & dictionary — The Gammas

**What this is.** Everything under `data/`: provenance, layout, glossary. Raw data **gitignored** in both repos — only this doc travels.

> **TL;DR** — **4 folders + 1 atlas = 2 datasets**, not 4. Finalist A = one folder; Finalist B = one loader
> (`load_hcp`) unpacking into 3 folders + atlas. All official NMA/OSF downloads. Only local convention: the folder
> name `hcp_task_339`, so B's task data coexists with A's `hcp_task/`.

---

## 1 · Provenance

| Layer | What | Source |
|---|---|---|
| Study | **Human Connectome Project (HCP) Young Adult** — healthy adults, 3T MRI | [humanconnectome.org](https://www.humanconnectome.org/study/hcp-young-adult) |
| Curation | NMA repackages a subset and hosts tarballs on **OSF**; official loader notebooks download + document them | [NMA fMRI project guide](https://compneuro.neuromatch.io/projects/fMRI/README.html) |
| Parcellation | **Glasser et al. 2016** — 360 **cortical** ROIs (HCP-MMP1.0), 180/hemisphere. *Cortex only: no subcortex, no cerebellum.* | [Nature 536:171](https://doi.org/10.1038/nature18933) |
| Network labels | **Cole-Anticevic** 12-network partition (Ji et al. 2019) — assigns each of the 360 ROIs to one of 12 functional networks | [NeuroImage 185:35](https://doi.org/10.1016/j.neuroimage.2018.10.006) |
| License | **HCP Data Use Terms** must be accepted before download | [HCP DUT](https://www.humanconnectome.org/study/hcp-young-adult/document/wu-minn-hcp-consortium-open-access-data-use-terms) |

---

## 2 · Original NMA loaders

Only three are HCP-WM-relevant; the rest are vision/retinotopy studies rejected in
[`sandbox/jaime/00`](../sandbox/jaime/00_framing_and_dataset_choice.ipynb).

| Official loader | Subjects | **Delivers → folder(s) on disk** | What you get | Our verdict |
|---|---|---|---|---|
| [`load_hcp_task_with_behaviour`](https://github.com/NeuromatchAcademy/course-content/blob/v3.0.2/projects/fMRI/load_hcp_task_with_behaviour.ipynb) | 100 (real IDs) | `hcp_task/` | 7 tasks' time series **+ per-subject `Stats.txt` behaviour** | **Finalist A** ✅ |
| [`load_hcp_task`](https://github.com/NeuromatchAcademy/course-content/blob/v3.0.2/projects/fMRI/load_hcp_task.ipynb) | 339 (pseudo IDs) | task-only component under its configured HCP directory | 7 tasks, **no behaviour**; same OSF task archive used by `load_hcp` | not a separate finalist; included within B |
| [`load_hcp`](https://github.com/NeuromatchAcademy/course-content/blob/v3.0.2/projects/fMRI/load_hcp.ipynb) | 339 (pseudo IDs) | official `hcp_task/` · `hcp_rest/` · `hcp/` · `atlas.npz`; locally renamed as described below | task **+ resting-state** + consolidated behaviour (`wm.csv`) + covariates + atlas | **Finalist B** ✅ |
| `load_hcp_retino` | — | — *(never downloaded)* | retinotopic mapping (not WM) | rejected |

> ⚠️ **Name trap (the one that bites).** Both `load_hcp_task` and `load_hcp` use the same
> **339-subject task archive**. `load_hcp_task` exposes only that component; Finalist B uses
> `load_hcp`, which adds resting-state, covariates/behaviour and the atlas. The official B task folder
> is `hcp_task/`; `_339` is a **local rename** so it can coexist with A's different 100-subject
> `hcp_task/`.

---

## 3 · Local layout

```
data/                                        9.1 GB total · all gitignored (except this doc's link + data/README.md)
├── A_load_hcp_task_with_behaviour/          Finalist A — load_hcp_task_with_behaviour (100 subj, real HCP IDs)
│   └── hcp_task/            1.1 GB            task time series + per-subject Stats.txt behaviour
├── B_load_hcp/                              Finalist B — load_hcp (339 subj, pseudo-IDs)
│   ├── hcp_task_339/        3.7 GB            task time series + EVs
│   ├── hcp_rest/            4.4 GB            resting-state (4 rest runs)
│   ├── hcp/                  17 MB            behaviour CSVs + demographics + ID map
│   └── hcp_atlas_339.npz     92 KB           atlas — ROI coordinates + vertex→ROI labels
├── HCP_S1200_Release_Reference_Manual.pdf    shared reference manual (both datasets)
└── README.md
```

Folders are grouped by loader (`A_load_hcp_task_with_behaviour/`, `B_load_hcp/`); `datasets.py`
resolves the grouped layout and falls back to the legacy flat layout automatically. The leaf folder
names below (`hcp_task/`, `hcp_task_339/`, …) are unchanged.

Folder → what's *uniquely* in it (loader and subject count are in §2):

| Folder | Dataset | IDs | What's unique to this folder |
|---|---|---|---|
| `hcp_task/` | **A** | real HCP (`100307`) | task time series **with `Stats.txt`** behaviour alongside |
| `hcp_task_339/` | **B** | pseudo (`0…338`) | task time series — EVs and timeseries **split into separate branches** |
| `hcp_rest/` | **B** | pseudo | **resting-state** (4 runs × 1200 frames) |
| `hcp/` | **B** | pseudo | `behavior/*.csv` (incl. `wm.csv`), `pseudo_demographics.npy`, `orig_ids.txt` |
| `hcp_atlas_339.npz` | **B** | — | ROI 3-D coords + surface vertex→ROI labels |

---

## 4 · Folder structures

**A vs B packaging:** both derive from HCP Young Adult and use the same task/parcellation logic, but
they are **different NMA-curated subsets**, not identical cohorts. A keeps each task's time series + EVs
together; B splits them (`EVs/`, `timeseries/`) and moves behaviour to a central CSV.

### Finalist A — `hcp_task/`
```
hcp_task/
├── regions.npy                     # (360,3) ROI table
├── subjects_list.txt               # 100 real HCP IDs
└── subjects/<ID>/                  # e.g. 100307
    └── <TASK>/                     # EMOTION GAMBLING LANGUAGE MOTOR RELATIONAL SOCIAL WM
        └── tfMRI_<TASK>_<LR|RL>/    # two phase-encoding runs (see §6)
            ├── data.npy            # (360, frames)  ← time series sits WITH the EVs
            └── EVs/
                ├── <condition>.txt # onset/dur/amp (see §6)
                ├── Stats.txt       # per-subject behaviour  ← ONLY in A
                └── Sync.txt
```

### Finalist B · task — `hcp_task_339/`
```
hcp_task_339/
├── regions.npy
└── subjects/<n>/                   # pseudo-IDs 0…338
    ├── EVs/                        # ← EVs grouped here, one folder per task/run
    │   └── tfMRI_<TASK>_<LR|RL>/
    │       └── <condition>.txt     # NO Stats.txt (behaviour lives in hcp/behavior/wm.csv)
    └── timeseries/                 # ← time series in a SEPARATE branch
        └── bold##_Atlas_MSMAll_Glasser360Cortical.npy   # (360, frames)
```
> `hcp_task_339/subjects/0/EVs` shows per-task EV folders (`tfMRI_EMOTION_*`, …); the signal is one level over in
> `timeseries/`. **Confirmed:** 4 746 timeseries `.npy` (339 subjects × 7 tasks × 2 runs),
> `tfMRI_WM_{LR,RL}` present — B is usable for the task project, not only rest.

### Finalist B · rest — `hcp_rest/`
```
hcp_rest/
└── subjects/<n>/timeseries/
    └── bold{1,2,3,4}_Atlas_MSMAll_Glasser360Cortical.npy   # 4 rest runs, each (360, 1200); no EVs (rest has no conditions)
```

### Finalist B · covariates — `hcp/`
```
hcp/
├── behavior/
│   ├── wm.csv                      # (5382, 9) consolidated WM behaviour  ← B's prediction target
│   └── {emotion,gambling,language,relational,social}.csv
├── pseudo_demographics.npy         # (339, 25) anonymised, z-scored covariates (candidate confounds)
├── orig_ids.txt                    # pseudo-ID → real HCP ID
└── subjects/<n>/EVs/…              # EV copies only — 0 timeseries here
```

---

## 5 · Object dictionary

| Object | Shape / form | What it is | Loaded by |
|---|---|---|---|
| `regions.npy` | **(360, 3)** `<U12` | `[ROI name, network(12-char), myelin]`; rows 0–179 = Right, 180–359 = Left | `region_table` |
| `data.npy` (A) / `bold##…npy` (B) | **(360, frames)** float64 | Parcellated BOLD time series (WM run ≈ 405 frames; rest = 1200) | `load_timeseries` |
| `EVs/<cond>.txt` | rows `(onset_s, dur_s, amp)` | Condition timing in **seconds** (FSL 3-column format) | `condition_frames` |
| `Stats.txt` (A only) | ~46 lines `key: value` | Per-condition ACC & RT summary → the target | `_parse_stats` |
| `wm.csv` (B) | **(5382, 9)** | `Subject, Run, ConditionName, ACC, ACC_NONTARGET, ACC_TARGET, MEDIAN_RT, …` | pandas |
| `pseudo_demographics.npy` (B) | **(339, 25)** float64 | Anonymised, z-scored demographic covariates | numpy |
| `hcp_atlas_339.npz` (B) | `coords (360,3)`, `labels_R (10242,)`, `labels_L (10242,)` | ROI centroid coordinates + surface-vertex→ROI maps | numpy (**not yet used** — see §8) |

---

## 6 · Nomenclature glossary

| Term | Meaning |
|---|---|
| **ROI** | *Region Of Interest* — one of the 360 Glasser cortical parcels. In graph language, a **node**. |
| **frame** | One fMRI time point (= one whole-brain volume), sampled every **TR**. WM run = 405 frames ≈ 291 s. |
| **TR** | *Repetition Time* = 0.72 s here (time between frames). |
| **`.npy`** | NumPy's binary array format (preserves shape + dtype). Load with `np.load`. |
| **`.npz`** | A zip of several named `.npy` arrays. `hcp_atlas_339.npz` holds 3 (`coords`, `labels_R`, `labels_L`). |
| **EV** | *Explanatory Variable* — FSL timing file, 3 columns: **onset(s) · duration(s) · amplitude**. Says *when* a condition happens. |
| **LR / RL** | The two **phase-encoding directions** (Left→Right, Right→Left). HCP scans every task **twice** with opposite directions to cancel geometric distortion. Same task content, different acquisition geometry — that is why every task has two `tfMRI_<TASK>_<LR|RL>` folders. We concatenate both for more frames / more stable FC. |
| **tfMRI** | *task fMRI* (vs. resting-state). |
| **MSMAll** | *Multimodal Surface Matching* — HCP's cross-subject surface registration (appears in the timeseries filenames). |
| **Glasser360Cortical** | The parcellation used for the timeseries. |
| **ACC** | *Accuracy* — fraction of correct responses. In the files it is a per-condition **Median ACC**. |
| **RT** | *Reaction Time* (ms). |

### EV condition names, by task
Only **WM** matters for us; the others come bundled in B and are noise for this project.

| Task | EV files | Meaning |
|---|---|---|
| **WM** ✅ | `0bk_/2bk_ × {body,faces,places,tools}` | 8 conditions = 2 loads × 4 stimulus categories |
| | `0bk_cor/err/nlr`, `2bk_…`, `all_bk_cor/err` | trial outcomes: correct / error / no-response |
| | `Stats.txt`, `Sync.txt` | behaviour summary (A only) / scanner sync timing |
| EMOTION | `fear`, `neut` | fearful vs neutral faces |
| GAMBLING | `win`, `loss`, `neut`, `*_event` | reward/punishment; block (`win`) vs event-related (`win_event`) |
| LANGUAGE | `story`, `math`, `cue`, `present_/question_/response_*` | listen to stories vs solve arithmetic |
| MOTOR | `lf`, `lh`, `rf`, `rh`, `t`, `cue` | left/right foot, left/right hand, tongue |
| RELATIONAL | `match`, `relation`, `error` | relational reasoning conditions |

---

## 7 · Prediction target — `acc_2bk`

**The N-back task.** Subjects see a stream of images (body / faces / places / tools) and respond under two loads:
- **0-back (low load):** "does this match a *fixed* target shown at block start?" — an attention/perception control; near-ceiling.
- **2-back (high load):** "does this match the image *2 positions back*?" — requires holding + updating a memory buffer; this is genuine working memory, and where people **differ**.

**`acc_2bk` = mean 2-back accuracy per subject.** In A it is parsed from `Stats.txt` (`_parse_stats` → `behaviour_table`),
averaging *Median ACC* over the 4 categories × 2 runs. In B the same number comes from `wm.csv`
(`groupby(Subject, load).ACC.mean()` on `2BK`). Candidate targets exposed by `behaviour_table`:

| Target | Definition | Note |
|---|---|---|
| `acc_0bk` | mean 0-back accuracy | near-ceiling (≈0.93) → little variance to predict |
| **`acc_2bk`** | mean 2-back accuracy | **primary candidate**: A ≈ 0.54–0.99; B ≈ 0.41–1.00 after excluding 3 subjects without complete 2-back |
| `acc_cost` | `acc_2bk − acc_0bk` | *load cost* (mostly < 0) |
| `rt_2bk`, `rt_cost` | median reaction time (ms) | speed alternatives |

Caveat for the modelling step: `acc_2bk` is a bounded proportion with a ceiling — not Gaussian; worth noting as a
limitation (or a logit transform) when we fit the predictor.

---

## 8 · Atlas file — `hcp_atlas_339.npz`

`hcp_atlas_339.npz` — **not yet used** by any notebook or the `datasets`/`preprocessing` loaders. The *spatial* description the rest of the data lacks:

- **`coords` (360, 3)** — 3-D centroid per ROI. Anatomical node layout for graphs (steps 3–4), instead of an arbitrary circle.
- **`labels_R` / `labels_L` (10242,)** — surface vertex → ROI map (fsaverage5). Paints any per-ROI value onto a brain surface (e.g. where 0→2-back reconfiguration is strongest).

> Proposed use: `atlas_geometry` demo plotting the 360 ROIs by network from `coords`, as an anatomical skeleton for the graph team. (Figure pending.)

---

## 9 · A vs B decision

| | **A — `hcp_task`** | **B — `hcp` (load_hcp)** |
|---|---|---|
| Subjects | 100 | **339** (3.4×) |
| Task time series | ✅ | ✅ (**confirmed present** — 4 746 run-level `.npy`) |
| Resting-state | ❌ | ✅ (unlocks abstract Objective 2) |
| WM behaviour | `Stats.txt` per subject | `wm.csv` consolidated (comparable, not coarser) |
| Subject IDs | real HCP | pseudo (`0…338`, mapped by `orig_ids.txt`) |
| Ingestion status | **done** (tasks 1–2 run) | **done and verified** (339 total; 336 analytic) |

**Bottom line:** both finalists are ingested and can be compared directly. B provides 3.4× total subjects
(336 analytically complete) **and** resting-state; the final A/B decision remains a team decision. Full costing:
[`sandbox/jaime/00`](../sandbox/jaime/00_framing_and_dataset_choice.ipynb).

---

## 10 · Derived layer

| Artifact | Where | What |
|---|---|---|
| `datasets.py` · `preprocessing.py` · `evaluation.py` | [`sandbox/jaime/`](../sandbox/jaime/) | config + I/O · EV segmentation, `Stats.txt` parser, region table · anti-leakage split + QC |
| `00_framing_and_dataset_choice` | sandbox | Blohm 4-step framing → dataset choice (A/B/C) |
| `01_ingestion_and_ev` | sandbox | the deliverable: (360×312) per-condition matrices + target + split |
| `02_eda_and_data_dictionary` | sandbox | side-by-side EDA of A and B |
| `regions.csv`, `behaviour.csv`, `splits.json` | `sandbox/jaime/artifacts_staging/` (gitignored) | staged hand-off files |

**Sources:** [project plan](project-plan.md) · [official fMRI guide](https://compneuro.neuromatch.io/projects/fMRI/README.html) · [10 Jul meeting](meetings/2026-07-10.md)
