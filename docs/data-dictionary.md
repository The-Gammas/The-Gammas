# Data map & dictionary — The Gammas

Where the data come from, how they sit on disk, and **what is inside every file**. Raw data are
gitignored in both repos — only this document travels. Read top to bottom: it funnels from
*provenance* → *loaders* → *layout* → *file-by-file variables* → *what the code hands you*.

> **One idea to hold:** **4 folders + 1 atlas = 2 cohorts, not 4.** A is one folder; B is one loader
> (`load_hcp`) unpacking into 3 folders + an atlas. **B is the primary analysis cohort, A the
> identity-disjoint transfer cohort inside the same HCP study** — these roles are fixed here, not
> inferred. Everything is an official NMA/OSF download; the only local convention is renaming B's task
> folder to `hcp_task_339` so it can coexist with A's `hcp_task/`.

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

## 2 · The two cohorts — one loader each, what each delivers

Both are NMA-curated HCP subsets with the **same** task, parcellation and network logic. They are
**different cohorts** (see §7), packaged differently, and reached by **different official loaders**.

| | **Cohort A · identity-disjoint transfer** | **Cohort B · primary MVP** |
|---|---|---|
| Official loader | [`load_hcp_task_with_behaviour`](https://github.com/NeuromatchAcademy/course-content/blob/v3.0.2/projects/fMRI/load_hcp_task_with_behaviour.ipynb) | [`load_hcp`](https://github.com/NeuromatchAcademy/course-content/blob/v3.0.2/projects/fMRI/load_hcp.ipynb) |
| Subjects | 100 | 339 (**336 analytic**, see §6) |
| Subject IDs | real HCP (6-digit) | pseudo (`0…338`), mapped by `orig_ids.txt` |
| Task fMRI (7 tasks) | ✅ time series **+ EVs** together | ✅ time series **and** EVs, in separate branches |
| WM behaviour | per-subject `Stats.txt` | consolidated `hcp/behavior/wm.csv` |
| Resting-state | ❌ | ✅ 4 runs |
| Atlas geometry | ❌ | ✅ `hcp_atlas_339.npz` |
| Delivers → folder(s) | `hcp_task/` | `hcp_task_339/` · `hcp_rest/` · `hcp/` · `hcp_atlas_339.npz` |

---

## 3 · Local layout

≈9.1 GB, all gitignored. The on-disk tree, the two mandatory renames for B and the `load_hcp` vs
`load_hcp_task` name trap are the acquisition contract and live in
[`data/README.md`](../data/README.md); [`datasets.py`](../gammas/datasets.py) resolves that grouped
layout **or** a legacy flat one. Leaf-folder names (`hcp_task/`, `hcp_task_339/`, …) never change,
which is what makes the per-cohort dictionaries in §4.2 and §4.3 readable as paths.

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

`condition_frames` converts onset/duration → frame indices via `floor((onset + delay)/TR)` / `ceil(dur/TR)`.

**`delay` — the haemodynamic shift (seconds).** `condition_frames` and `condition_timeseries` take a
`delay` that moves every block forward before it is mapped to frames: BOLD peaks ~4–6 s after the
stimulus, so the raw onsets index frames the haemodynamic response has not reached yet. **`delay=4.0`
is mandatory to reproduce the canonical result; with `0.0` the same pipeline gives r = 0.152** (against
r = 0.366). Nothing raises — the number just changes, which is why it is documented here. It is now the
package default (`gammas.preprocessing.HRF_DELAY = 4.0`), so callers that pass nothing get the canonical
recipe. The shift moves the start index only, not the block length: frame counts are unchanged (156 per
run, 312 concatenated). Full provenance → [`final-report.md`](final-report.md) §7.

Alongside the EVs, `Sync.txt` holds one number (e.g. `26.108`) — seconds between scanner start and the
EV clock origin. Alignment metadata, not used by the pipeline.

---

### 4.2 · Cohort A — `hcp_task/`

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

**48 lines** of `key: value` per subject per run, keyed `{load} {category} {measure}` = 2 loads
(`0-Back`, `2-Back`) × 4 categories (`BP` = Body Parts, `Faces`, `Places`, `Tools`) × 6 measures.
The measures: `Median ACC` (0–1, accuracy over all trials of that load × category → **the target**,
`acc_2bk`), `Median ACC Target` (*match* trials, i.e. the **hit rate**), `Median ACC Non-Target`
(*non-match* trials, so **false alarm = 1 − this**), and the three `Median RT` counterparts in ms.

> ⚠️ **Why A cannot give d′.** A's `… Target` / `… Non-Target` accuracy fields are **internally
> inconsistent** (a known HCP WM issue), so hit/false-alarm — and therefore d′ — are unreliable on A.
> Use `Median ACC` (→ `acc_2bk`). For d′, use **B's `wm.csv`** (§4.3), whose target fields are clean.

Parsed by [`_parse_stats`](../gammas/preprocessing.py) → `behaviour_table` averages the 4
categories × 2 runs into `acc_0bk`, `acc_2bk`, `rt_0bk`, `rt_2bk`.

---

### 4.3 · Cohort B — `B_load_hcp/`

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

`load_hcp` also bundles `behavior/{emotion,gambling,language,relational,social}.csv` — same
`Subject, Run, ConditionName` keys, task-specific metric columns, no bearing on this WM project and read
by no function in `gammas/`. Inspect them with `pd.read_csv(...).columns` if you ever need one.

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
shared A/B interface in [`gammas/`](../gammas/); switch cohort with `spec_a` / `spec_b` and nothing
downstream branches.

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
| **`acc_2bk`** | mean 2-back accuracy | **reporting/validation anchor**: A ≈ 0.54–0.99; B ≈ 0.41–1.00 (336 analytic) |
| `acc_cost` | `acc_2bk − acc_0bk` | load cost (mostly < 0) |
| `rt_2bk`, `rt_cost` | median RT (ms) | speed alternatives |

**d′ (B only).** A measurement-focused companion to raw accuracy (it separates sensitivity from
response bias), built from `wm.csv`: `hit = ACC_TARGET`, `fa = 1 − ACC_NONTARGET`,
`d′ = z(hit) − z(fa)`. The extreme-rate correction is implemented and checked in notebook `04` §5:
loglinear and 1/2N clipping give near-identical results. A cannot supply clean d′ (§4.2). Caveat for
either target: bounded proportion with a ceiling; a logit transform remains a possible sensitivity
analysis.

---

## 7 · A/B roles + cohort overlap

Per-cohort contents are in §2; what fixes their **roles** is the overlap.

> **Cohorts are mostly independent, not nested:** only **35 subjects are shared** (404 unique people
> across A∪B), verified by mapping A's real IDs against B's `orig_ids.txt`. Pooling A∪B would add only
> ~65 subjects over B while forcing two heterogeneous pipelines and deduplicating the overlap to avoid
> leakage — so **B alone is the clean primary training cohort**. A remains useful as a separate
> identity-disjoint transfer cohort within the same HCP study: train on the 301 B-only participants and test on all 100 A participants,
> as implemented in [`sandbox/jaime/05`](../sandbox/jaime/05_dataset_A_external_validation.ipynb).
> Overlap analysis: [`sandbox/jaime/03` §6](../sandbox/jaime/03_dataset_comparison.ipynb). Original
> A/B/C costing: [`sandbox/jaime/00`](../sandbox/jaime/00_framing_and_dataset_choice.ipynb).

---

## 8 · Glossary

Only the terms that decode a name on disk or a convention of this project. Standard fMRI vocabulary
(ROI, BOLD, tfMRI, ACC/RT, hit/false alarm) is not restated here.

| Term | Meaning |
|---|---|
| **frame / TR** | one fMRI time point, sampled every *Repetition Time* = **0.72 s**. WM run = 405 frames ≈ 292 s. |
| **EV** | *Explanatory Variable* — FSL timing file: onset(s) · duration(s) · amplitude. Says *when* a condition happens. |
| **LR / RL** | the two **phase-encoding directions**. HCP scans every task twice with opposite directions to cancel distortion; we concatenate both for more frames / more stable FC. Note A's run 0 is LR, B's is RL. |
| **MSMAll** | *Multimodal Surface Matching* — HCP's cross-subject surface registration (in the timeseries filenames). |
| **Glasser360Cortical** | the parcellation used for the time series (in the timeseries filenames). |

**Sources:** [project plan](archive/2026-07-22_project-plan.md) · [official fMRI guide](https://compneuro.neuromatch.io/projects/fMRI/README.html) · [10 Jul meeting](meetings/2026-07-10.md) · verified against the on-disk data 15 Jul 2026.
