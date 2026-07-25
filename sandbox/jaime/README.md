# Jaime's sandbox — exploration record

**Frozen after the course (24 Jul 2026).** Seven executed exploratory notebooks, kept as the audit
trail of how the analysis was reached. Nothing here is a source of truth: results live in
[`docs/final-report.md`](../../docs/final-report.md), evidence in
[`pipeline/02`](../../pipeline/02_canonical_analysis_and_slides.ipynb).

**What left this folder.** The shared A/B code layer became the [`gammas`](../../gammas/) package with
its tests in [`tests/`](../../tests/); `06_tangent_fc_benchmark` became
[`pipeline/03`](../../pipeline/03_method_benchmark_tangent_fc.ipynb) with its
[report](../../pipeline/03_tangent_benchmark_report.md); `09_goutham_pipeline_replication` became
[`pipeline/04`](../../pipeline/04_goutham_pipeline_reconciliation.ipynb); the abstract merge proposal
became [`manuscript/archive/2026-07-17_abstract-merge-rationale.md`](../../manuscript/archive/2026-07-17_abstract-merge-rationale.md).
All by `git mv`, so `git log --follow` keeps the history.

This folder began as the data-ingestion contribution and grew into the full evidence path: choose and
understand the HCP cohorts, prepare 0-back/2-back inputs, port and audit Goutham's model on B, and
validate it on A. The notebooks were evidence for team review, not unilateral method decisions.

They are a **narrated path, one per role**, written in the **four-step modelling frame** taught in W2D1
([Blohm et al., 2019](https://doi.org/10.1523/ENEURO.0352-19.2019)), so the reasoning is replicable and
shares the vocabulary the whole group used. Read them in order. Each is an EXPLORE log: clean code,
tables and focused plots, every decision tied to its evidence, and the official NMA loaders referenced
as the code-style base.

## Contents — read in order

| File | Role | Purpose | Current state |
|---|---|---|---|
| [`00_framing_and_dataset_choice.ipynb`](00_framing_and_dataset_choice.ipynb) | **why these data** | Blohm 4 steps (phenomenon→question→ingredients→hypothesis) → derive requirements and compare the original dataset candidates. Historical decision path leading to B as the primary analysis cohort. | Executed against real data |
| [`01_ingestion_and_ev.ipynb`](01_ingestion_and_ev.ipynb) | **the deliverable (tasks 1–2)** | Ingestion + EV segmentation: BOLD time series, 0/2-back frame selection, `Stats.txt` target, region table and anti-leakage subject split. | Executed with real outputs |
| [`02_eda_and_data_dictionary.ipynb`](02_eda_and_data_dictionary.ipynb) | **understand the data** | Download/access + step-by-step EDA of both cohorts (A 100-subj and B 339-subj): load → columns → networks → conditions → target → basic viz. Plus a data dictionary. | Executed with real outputs |
| [`03_dataset_comparison.ipynb`](03_dataset_comparison.ipynb) | **the A/B decision** | Both cohorts on one shared code layer: side-by-side QC, target distribution, an example FC reconfiguration map, and the evidence for their current roles. | Executed with real outputs |
| [`04_goutham_pipeline_on_B.ipynb`](04_goutham_pipeline_on_B.ipynb) | **the experiment (dataset B)** | Goutham's FC pipeline on B (336 subj): per-condition FC → 2bk−0bk reconfiguration → 78-dim fingerprint → RidgeCV + permutation null. Prediction, specificity (reconfiguration vs single-condition FC, general ability, motion), direction, `d′` correction, multiple comparisons. | Executed with real outputs |
| [`05_dataset_A_external_validation.ipynb`](05_dataset_A_external_validation.ipynb) | **using dataset A** | Same experiment, A as a held-out transfer cohort (same HCP source, disjoint identities): A/B subject-overlap constraint, four train/test designs, and the recommended one — train on B-only (301), test on A (100), leakage-free identity-disjoint transfer (r≈0.40, p<0.001). | Executed with real outputs |
| [`08_activation_vs_reconfiguration.ipynb`](08_activation_vs_reconfiguration.ipynb) | **robustness question** | Re-check of the reconfiguration story (21 Jul): reconfiguration does not clearly add over single-condition 0-back FC (nested delta-R2 +0.034, sd 0.023, under 2 sd); a task-activation contrast (2bk−0bk mean BOLD) predicts more strongly (r ≈ 0.60 pooled, ≈ 0.48 held-out people and runs), while adding FC shows no clear gain (delta-R2 -0.003). The comparison is unmatched (360 regional activation vs 78 network FC features), and per-run centering makes 0bk/2bk/contrast collinear, so current evidence does not establish FC-specific predictive value or a load-independent activation trait. Includes paired OOF scatterplots beside the method-comparison bars. | Executed 21 Jul; framing carried into `pipeline/02` as a proposal |

The numbering is the original sandbox sequence, kept as it was: `00`–`06` and `08`–`09` were the
notebooks, with a gap at `07`, which was deleted. Renumbering would break the cross-references in
`pipeline/02` and `docs/`, so the gap stays and this is its explanation.

`artifacts_staging/` (not versioned) holds locally generated outputs of these notebooks: `regions.csv`
(ROI, network and hemisphere table), `behaviour.csv` (per-subject behavioural summaries) and
`splits.json` (exploratory subject-level train/test and development folds). All three are regenerable
from the ingestion notebook, none is an input to any published result, and every subject-level file
stays outside the public repository.

Figures live **embedded** in the notebooks (no loose `fig*.png` in the folder; they are gitignored).

## Datasets on disk

Both HCP cohorts live under `data/` (gitignored). **B** (`load_hcp`, 339 subjects; 336 analytic) is
the primary MVP analysis cohort. **A** (`load_hcp_task_with_behaviour`, 100 subjects) is the held-out
transfer cohort (same HCP source, disjoint identities), not merged with B. Full layout, provenance and
load contract → [`data/README.md`](../../data/README.md) ·
[`docs/data-dictionary.md`](../../docs/data-dictionary.md).

## How to run

The notebooks open from the repository root or from this directory: their setup cell locates the
repository root and imports the shared layer from [`gammas`](../../gammas/). They use the `data/` root
by default — files are grouped by loader (`A_load_hcp_task_with_behaviour/`, `B_load_hcp/`), with a
flat-layout fallback; set `GAMMAS_DATA_DIR` to use another local directory. The data are not stored in
Git and require accepting the HCP Data Use Terms — download, placement and a minimal load example are
in [`data/README.md`](../../data/README.md).

To re-run and re-embed a notebook's outputs, after `pip install -r requirements.txt` from the repo root:

```bash
python -m nbconvert --to notebook --execute --inplace 01_ingestion_and_ev.ipynb
```

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

(Written during exploration and left as it stood. The reviewed statements of the same facts, and the
decisions that were taken afterwards, are in [`docs/data-dictionary.md`](../../docs/data-dictionary.md)
and [`docs/final-report.md`](../../docs/final-report.md).)
