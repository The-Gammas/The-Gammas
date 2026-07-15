# Data map & dictionary — The Gammas

Where the data come from, how they sit on disk, and **what is inside every file**. Raw data are
gitignored in both repos — only this document travels. Read top to bottom: it funnels from
*provenance* → *loaders* → *layout* → *file-by-file variables* → *what the code hands you*.

> **One idea to hold:** **4 folders + 1 atlas = 2 datasets, not 4.** Finalist A is one folder;
> Finalist B is one loader (`load_hcp`) that unpacks into 3 folders + an atlas. Everything is an
> official NMA/OSF download; the only local convention is renaming B's task folder to
> `hcp_task_339` so it can coexist with A's `hcp_task/`.

---

## 1 · Provenance — where every number comes from

| Layer | What | Source |
|---|---|---|
| Study | **Human Connectome Project (HCP) Young Adult** — healthy adults, 3T MRI | [humanconnectome.org](https://www.humanconnectome.org/study/hcp-young-adult) |
| Curation | NMA repackages a subset and hosts tarballs on **OSF**; official loader notebooks download + document them | [NMA fMRI guide](https://compneuro.neuromatch.io/projects/fMRI/README.html) |
| Parcellation | **Glasser et al. 2016** — 360 **cortical** ROIs (HCP-MMP1.0), 180/hemisphere. *Cortex only — no subcortex, no cerebellum.* | [Nature 536:171](https://doi.org/10.1038/nature18933) |
| Network labels | **Cole–Anticevic** 12-network partition (Ji et al. 2019) — each ROI → one of 12 functional networks | [NeuroImage 185:35](https://doi.org/10.1016/j.neuroimage.2018.10.006) |
| License | **HCP Data Use Terms** — accept before any download | [HCP DUT](https://www.humanconnectome.org/study/hcp-young-adult/document/wu-minn-hcp-consortium-open-access-data-use-terms) |

---

## 2 · The two finalists — one loader each, what each delivers

Both are NMA-curated HCP subsets with the **same** task, parcellation and network logic. They are
**different cohorts** (see §7), packaged differently, and reached by **different official loaders**.

| | **Finalist A** | **Finalist B** |
|---|---|---|
| Official loader | [`load_hcp_task_with_behaviour`](https://github.com/NeuromatchAcademy/course-content/blob/v3.0.2/projects/fMRI/load_hcp_task_with_behaviour.ipynb) | [`load_hcp`](https://github.com/NeuromatchAcademy/course-content/blob/v3.0.2/projects/fMRI/load_hcp.ipynb) |
| Subjects | 100 | 339 (**336 analytic**, see §6) |
| Subject IDs | real HCP (6-digit) | pseudo (`0…338`), mapped by `orig_ids.txt` |
| Task fMRI (7 tasks) | ✅ time series **+ EVs** together | ✅ time series **and** EVs, in separate branches |
| WM behaviour | per-subject `Stats.txt` | consolidated `hcp/behavior/wm.csv` |
| Resting-state | ❌ | ✅ 4 runs |
| Atlas geometry | ❌ | ✅ `hcp_atlas_339.npz` |
| Delivers → folder(s) | `hcp_task/` | `hcp_task_339/` · `hcp_rest/` · `hcp/` · `hcp_atlas_339.npz` |

> **Name trap (stated once).** Two official loaders read the **same 339-subject task archive**:
> `load_hcp_task` exposes *only* the task time series (no behaviour); **`load_hcp` is Finalist B** and
> adds rest + behaviour + atlas. The official B task folder is called `hcp_task/`; we rename it
> **`hcp_task_339`** locally so it does not collide with A's different 100-subject `hcp_task/`.
> `load_hcp_retino` (retinotopy) is unrelated and never downloaded.

---

## 3 · Local layout — where the files sit

```text
data/                                        ≈9.1 GB · all gitignored (except data/README.md + this doc)
├── A_load_hcp_task_with_behaviour/          Finalist A
│   └── hcp_task/            1.1 GB            task time series + EVs + per-subject Stats.txt
├── B_load_hcp/                              Finalist B  (8.1 GB)
│   ├── hcp_task_339/        3.7 GB            task time series (timeseries/) + EVs (EVs/), split apart
│   ├── hcp_rest/            4.4 GB            resting-state, 4 runs
│   ├── hcp/                  17 MB            behaviour CSVs + demographics + pseudo→real ID map
│   └── hcp_atlas_339.npz     92 KB           atlas — ROI coordinates + surface vertex→ROI maps
├── HCP_S1200_Release_Reference_Manual.pdf    shared HCP reference manual
└── README.md
```

Folders are grouped by loader (`A_…/`, `B_…/`); [`datasets.py`](../sandbox/jaime/datasets.py) resolves
this grouped layout **or** a legacy flat one automatically. Leaf-folder names (`hcp_task/`,
`hcp_task_339/`, …) are never changed.

---

## 4 · File & variable dictionary

The core of this document. For each file: **what it is**, its **shape/format**, and — where it has
fields — a **variable table**. Read §4.1 (shared building blocks) first; it is reused by both datasets.

### 4.1 · Shared building blocks (identical in A and B)

#### `regions.npy` — the ROI table

The parcellation, one row per ROI. Shape **(360, 3)**, dtype `<U12` (**all three columns are
strings**). Rows **0–179 = Right** hemisphere, **180–359 = Left**. Identical file in A and B.

| Col | Field | Example | Meaning |
|---|---|---|---|
| 0 | ROI name | `R_V1`, `L_FEF` | Glasser label; `R_`/`L_` prefix = hemisphere |
| 1 | network (raw) | `Visual1`, `Cingulo-Oper` | Cole–Anticevic label, **truncated to 12 chars** — de-truncated by `region_table` |
| 2 | myelin | `2.209` | T1w/T2w myelin estimate (≈1.5–2.35); structural, **not a target**; not surfaced by `region_table` |

The 12 networks and their ROI counts: Posterior-Multimodal 77, Cingulo-Opercular 56, Visual2 54,
Frontoparietal 50, Somatomotor 39, Language 23, Default 23, Auditory 15, Dorsal-attention 7,
Visual1 6, Orbito-Affective 6, Ventral-Multimodal 4.

#### `data.npy` / `bold##_…npy` — the BOLD time series

The signal itself. Shape **(360, frames)**, `float64` = mean BOLD per ROI per frame (parcellated
BOLD). A WM run = **405 frames** (× 0.72 s ≈ 292 s); a rest run = **1200 frames**. A stores it as
`data.npy`; B as `bold##_Atlas_MSMAll_Glasser360Cortical.npy` (see §4.3 for which `##` is WM).

#### `EVs/<condition>.txt` — the timing (Explanatory Variable) files

Say **when** each condition happens. Whitespace, **3 columns = onset(s) · duration(s) · amplitude**
(FSL 3-column format). WM ships two kinds — only the first drives our load split:

| Kind | Files | Rows / form | Use |
|---|---|---|---|
| **Block / condition** | `0bk_{body,faces,places,tools}`, `2bk_…` | 1 row/run · a **27.5 s block** | **the 0/2-back frame split** — pool the 4 categories → `COND_0BACK` / `COND_2BACK` |
| **Trial outcome** | `0bk_{cor,err,nlr}`, `2bk_…`, `all_bk_{cor,err}` | per-trial · **2.5 s** each | correct / error / no-response; trial-level modelling only, **not** our split |

`condition_frames` converts onset/duration → frame indices via `floor(onset/TR)` / `ceil(dur/TR)`.

#### `Sync.txt` — scanner sync offset

One number (e.g. `26.108`): the seconds between scanner start and the EV clock origin. Alignment
metadata; not used directly by the pipeline.

---

### 4.2 · Finalist A — `hcp_task/`

Task time series, EVs and behaviour live **together** under each run folder.

```text
hcp_task/
├── regions.npy                          # §4.1 · (360,3) ROI table
├── subjects_list.txt                    # 100 real HCP IDs (one per line)
└── subjects/<ID>/                       # <ID> = 6-digit HCP id
    └── <TASK>/                          # EMOTION GAMBLING LANGUAGE MOTOR RELATIONAL SOCIAL WM
        └── tfMRI_<TASK>_<LR|RL>/         # two phase-encoding runs
            ├── data.npy                 # §4.1 · (360, 405) BOLD — sits WITH the EVs
            └── EVs/                      # 18 files for WM:
                ├── <block/trial>.txt    #   §4.1 · timing files
                ├── Stats.txt            #   behaviour summary  ← ONLY in A
                └── Sync.txt             #   §4.1 · sync offset
```

| File | What it is |
|---|---|
| `subjects_list.txt` | 100 real HCP IDs; the cohort for A. Loaded by `load_subjects`. |
| `data.npy` | §4.1 — one WM run, (360, 405). |
| `EVs/` (WM) | 18 files: 8 block EVs (`0bk_/2bk_ × 4 cat`), 8 trial-outcome EVs, `Stats.txt`, `Sync.txt`. |

#### `Stats.txt` (A only) — the per-subject behaviour summary

**48 lines** of `key: value`, one file per subject per run. Every key follows one grammar:

```
{load} {category} {measure}
  load     ∈ { 0-Back , 2-Back }
  category ∈ { BP , Faces , Places , Tools }        # BP = Body Parts
  measure  ∈ { Median ACC , Median ACC Target , Median ACC Non-Target ,
               Median RT  , Median RT  Target , Median RT  Non-Target }
```

2 loads × 4 categories × 6 measures = **48 values**. What the measures mean:

| Measure | Units | Meaning |
|---|---|---|
| `Median ACC` | 0–1 | accuracy over all trials of that load×category → **the target** (`acc_2bk`) |
| `Median ACC Target` | 0–1 | accuracy on *match* trials (would be the **hit rate**) |
| `Median ACC Non-Target` | 0–1 | accuracy on *non-match* trials (would give **false-alarm = 1 − this**) |
| `Median RT …` | ms | reaction-time counterparts of the three above |

> ⚠️ **Why A cannot give d′.** A's `… Target` / `… Non-Target` accuracy fields are **internally
> inconsistent** (a known HCP WM issue), so hit/false-alarm — and therefore d′ — are unreliable on A.
> Use `Median ACC` (→ `acc_2bk`). For d′, use **B's `wm.csv`** (§4.3), whose target fields are clean.

Parsed by [`_parse_stats`](../sandbox/jaime/preprocessing.py) → `behaviour_table` averages the 4
categories × 2 runs into `acc_0bk`, `acc_2bk`, `rt_0bk`, `rt_2bk`.

---

### 4.3 · Finalist B — `B_load_hcp/`

Same task, but **time series and EVs are split into separate branches**, and behaviour is moved to
central CSVs. Pseudo-IDs `0…338` throughout.

```text
B_load_hcp/
├── hcp_task_339/
│   ├── regions.npy                      # §4.1 (identical to A)
│   └── subjects/<n>/                    # pseudo-ID 0…338
│       ├── EVs/tfMRI_<TASK>_<LR|RL>/    # timing files (NO Stats.txt; Sync.txt present)
│       └── timeseries/                  # ← BOLD in a SEPARATE branch
│           └── bold##_Atlas_MSMAll_Glasser360Cortical.npy
├── hcp_rest/
│   └── subjects/<n>/timeseries/
│       └── bold{1,2,3,4}_…npy           # 4 rest runs, each (360, 1200); no EVs (rest has no conditions)
├── hcp/
│   ├── behavior/*.csv                   # wm.csv (+ 5 other tasks)
│   ├── pseudo_demographics.npy
│   ├── orig_ids.txt
│   └── subjects/<n>/EVs/…               # EV copies only — 0 timeseries here
└── hcp_atlas_339.npz
```

#### `timeseries/bold##_…npy` — which `##` is WM?

Each subject has **14 bold files, numbered `bold5`–`bold18`** = 7 tasks × 2 runs. **WM = `bold7`
(RL, run 0) and `bold8` (LR, run 1)**, each (360, 405). Note B's run 0 is **RL** (A's run 0 is
**LR**) — `load_timeseries` maps this via `RUN_LABELS`, so callers never worry about it. Whole B task
set = 339 × 7 × 2 = **4 746** run-level `.npy`.

#### `hcp/behavior/wm.csv` — B's WM behaviour (the prediction source)

One row per **subject × run × condition**; shape **(5382, 9)**.

| Column | Type | Range | Meaning |
|---|---|---|---|
| `Subject` | int | 0–338 | pseudo-ID |
| `Run` | int | 0 / 1 | acquisition run |
| `ConditionName` | str | 8 values | `0BK_/2BK_ × {BODY,FACE,PLACE,TOOL}` |
| `ACC` | float | 0.1–1.0 | overall accuracy → `acc_2bk` when aggregated |
| `ACC_TARGET` | float | 0–1 | accuracy on match trials = **hit rate** |
| `ACC_NONTARGET` | float | 0–1 | accuracy on non-match trials → **false alarm = 1 − ACC_NONTARGET** |
| `MEDIAN_RT` | float | 291–1839 ms | median reaction time |
| `MEDIAN_RT_TARGET` | float | ms (**488 NaN**) | RT on match trials — NaN where no timed response |
| `MEDIAN_RT_NONTARGET` | float | ms (9 NaN) | RT on non-match trials |

> **d′ inputs (B only):** `hit = ACC_TARGET`, `fa = 1 − ACC_NONTARGET`. `signal_detection_table`
> returns these per subject; the extreme-rate correction and d′ itself are a team choice (§6).

#### `hcp/behavior/{emotion,gambling,language,relational,social}.csv` — the other 5 tasks

Bundled by `load_hcp`; **noise for this WM project** but documented for completeness. All keyed by
`Subject, Run, ConditionName`; the metric columns differ per task:

| CSV | Shape | Task-specific columns |
|---|---|---|
| `emotion.csv` | (1356, 5) | `ACC`, `MEDIAN_RT` |
| `relational.csv` | (1356, 5) | `ACC`, `MEDIAN_RT` |
| `language.csv` | (1356, 6) | `ACC`, `AVG_DIFFICULTY_LEVEL`, `MEDIAN_RT` |
| `gambling.csv` | (1356, 8) | `MEDIAN_RT_{LARGER,SMALLER}`, `PROP_{LARGER,SMALLER,NLR}` |
| `social.csv` | (1356, 10) | `MEDIAN_RT_{RANDOM,TOM,UNSURE}`, `PROP_{RANDOM,TOM,UNSURE,NLR}` |

#### `hcp/pseudo_demographics.npy` — synthetic covariates

Shape **(339, 25)**, `float64`, z-scored (≈ −4.1 … 3.7, mean ≈ 0). **Model-generated from
resting-state FC — NOT real age/sex/motion.** Do **not** use as confounds for an FC-based predictor
(circular). Not used by any loader.

#### `hcp/orig_ids.txt` — pseudo → real ID map

339 lines mapping each pseudo-ID to its real 6-digit HCP ID. The bridge used to verify the A∩B
overlap (§7). Real IDs are subject-level — keep them out of committed outputs.

#### `hcp_atlas_339.npz` — atlas geometry (B only)

A zip of 3 named arrays; the *spatial* description the rest of the data lacks. **Not yet used** by any
loader.

| Array | Shape | Type | Meaning |
|---|---|---|---|
| `coords` | (360, 3) | float64 | ROI centroid x,y,z in mm (≈ −89 … 70) — node layout for graphs |
| `labels_R` | (10242,) | int32 | right-hemi fsaverage5 vertex → ROI 0–179 (**−1 = medial wall / unassigned**) |
| `labels_L` | (10242,) | int32 | left-hemi vertex → ROI 180–359 (−1 = unassigned) |

Enables painting any per-ROI value onto a brain surface (e.g. where 0→2-back reconfiguration peaks).

---

## 5 · What the code hands you (derived layer)

A newcomer usually consumes these **DataFrames / arrays**, not the raw files above. All sit behind the
shared A/B interface in [`sandbox/jaime/`](../sandbox/jaime/) — `datasets.py` (I/O) ←
`preprocessing.py` (transforms) ← `evaluation.py` (split + QC). Switch dataset with `spec_a` / `spec_b`;
nothing downstream branches.

| Function | Returns | Notes |
|---|---|---|
| `load_subjects(spec)` | list of IDs | analytic cohort — A: 100 · B: 336 (drops 3 without complete 2-back) |
| `region_table(spec)` | 360 × `roi_index, name, network_raw, hemi, network` | `network` de-truncated to full Cole–Anticevic name |
| `condition_timeseries(spec, subj, level)` | ndarray `(360, 312)` | BOLD for one load, both runs; `runs=(0,)` → `(360, 156)` |
| `behaviour_table(spec)` | `subject, acc_0bk, acc_2bk, acc_cost, rt_0bk, rt_2bk, rt_cost` | ACC 0–1, RT ms; `acc_2bk` is the target (§6) |
| `signal_detection_table(spec)` | `subject, hit_0bk, fa_0bk, hit_2bk, fa_2bk` | **B only** (A raises); d′ inputs, d′ not computed |
| `make_split(spec)` | dict: train/test/CV by subject | leakage-safe; held-out subjects |
| `validate_dataset(spec)` | QC dict | shapes, frame counts, missingness |

**Condition mapping** (how the 8 EV names collapse to two loads): `COND_0BACK` = `0bk_{body,faces,
places,tools}`; `COND_2BACK` = `2bk_{…}`. B's `wm.csv` uses the singular `FACE/PLACE/TOOL`; A's
`Stats.txt` uses `BP/Faces/Places/Tools` — the loaders reconcile both.

---

## 6 · Prediction target — `acc_2bk` (and the d′ option)

**The N-back task.** A stream of images (body / faces / places / tools) under two loads:
- **0-back (low load)** — "does this match a *fixed* target?" — attention/perception control; near-ceiling.
- **2-back (high load)** — "does this match the image *2 back*?" — genuine working memory; where people **differ**.

`acc_2bk` = mean 2-back accuracy per subject (A: from `Stats.txt`; B: from `wm.csv`). Candidate
targets exposed by `behaviour_table`:

| Target | Definition | Note |
|---|---|---|
| `acc_0bk` | mean 0-back accuracy | near-ceiling (≈0.93) → little variance |
| **`acc_2bk`** | mean 2-back accuracy | **primary**: A ≈ 0.54–0.99; B ≈ 0.41–1.00 (336 analytic) |
| `acc_cost` | `acc_2bk − acc_0bk` | load cost (mostly < 0) |
| `rt_2bk`, `rt_cost` | median RT (ms) | speed alternatives |

**d′ (B only).** A cleaner sensitivity measure than raw accuracy (separates it from response bias),
built from `wm.csv`: `hit = ACC_TARGET`, `fa = 1 − ACC_NONTARGET`, `d′ = z(hit) − z(fa)`. Needs an
extreme-rate correction (hit=1 / fa=0 blow up z) — a prespecified team choice. A cannot supply it
(§4.2). Caveat for either target: bounded proportion with a ceiling — consider a logit transform.

---

## 7 · A vs B decision + cohort overlap

| | **A** | **B** |
|---|---|---|
| Subjects | 100 | **339** (336 analytic, 3.4×) |
| Resting-state | ❌ | ✅ |
| WM behaviour | `Stats.txt` | `wm.csv` (comparable, not coarser; **+ clean d′ inputs**) |
| IDs | real HCP | pseudo (`0…338`) |
| Ingestion | done | done + verified |

> **Cohorts are mostly independent, not nested:** only **35 subjects are shared** (404 unique people
> across A∪B), verified by mapping A's real IDs against B's `orig_ids.txt`. Pooling A∪B would add only
> ~65 subjects over B while forcing two heterogeneous pipelines and deduplicating the overlap to avoid
> leakage — so **B alone is the clean path**. Reproduced in
> [`sandbox/jaime/03` §6](../sandbox/jaime/03_dataset_comparison.ipynb). Full A/B/C costing:
> [`sandbox/jaime/00`](../sandbox/jaime/00_framing_and_dataset_choice.ipynb).

---

## 8 · Glossary

| Term | Meaning |
|---|---|
| **ROI** | *Region Of Interest* — one of the 360 Glasser cortical parcels; a graph **node**. |
| **frame** | one fMRI time point (one whole-brain volume), sampled every **TR**. WM run = 405 frames ≈ 292 s. |
| **TR** | *Repetition Time* = 0.72 s (time between frames). |
| **BOLD** | *Blood-Oxygen-Level-Dependent* signal — what fMRI measures; each `(360, frames)` array is mean BOLD per ROI per frame. |
| **EV** | *Explanatory Variable* — FSL timing file: onset(s) · duration(s) · amplitude. Says *when* a condition happens. |
| **LR / RL** | the two **phase-encoding directions**. HCP scans every task twice with opposite directions to cancel distortion; we concatenate both for more frames / more stable FC. |
| **tfMRI** | *task* fMRI (vs. resting-state). |
| **MSMAll** | *Multimodal Surface Matching* — HCP's cross-subject surface registration (in the timeseries filenames). |
| **Glasser360Cortical** | the parcellation used for the time series. |
| **ACC / RT** | *Accuracy* (fraction correct) / *Reaction Time* (ms). |
| **hit / false alarm** | on a match/non-match task: hit = correct "yes" on a match; false alarm = wrong "yes" on a non-match. Inputs to **d′**. |
| **myelin** | per-ROI T1w/T2w ratio (3rd column of `regions.npy`); structural, not a target. |
| **`.npy` / `.npz`** | NumPy binary array / zip of named arrays. Load with `np.load`. |

**Sources:** [project plan](project-plan.md) · [official fMRI guide](https://compneuro.neuromatch.io/projects/fMRI/README.html) · [10 Jul meeting](meetings/2026-07-10.md) · verified against the on-disk data 15 Jul 2026.
