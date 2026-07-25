# The Gammas — final report

**Project:** does functional-connectivity reconfiguration under working-memory load predict individual
performance? · HCP N-back · Neuromatch Academy CompNeuro 2026 · Pod Ifrit Ras el Hanout (884), Group 1.
**Closed:** W3D5, 24 Jul 2026. **Canonical evidence:**
[`pipeline/02_canonical_analysis_and_slides.ipynb`](../pipeline/02_canonical_analysis_and_slides.ipynb).

> **Authority of this file.** Section 5 is the canonical results table of the repository. A number
> quoted anywhere else without a protocol, an `n` and a source cell is superseded by it. Everything
> dated before 24 Jul — the submitted abstract, the meeting minutes, the folder READMEs — is a record
> of what was known then, not a statement of current status.

---

## 1 · TL;DR

- **Question.** Does the 0-back → 2-back change in functional connectivity (FC) predict 2-back accuracy
  in participants the model never saw?
- **Cohort.** HCP N-back, cohort **B** = 336 analytic participants (339 released), 360 Glasser ROIs,
  12 Cole-Anticevic networks. Cohort **A** (100) is the identity-disjoint transfer target.
- **Primary result.** The 78-feature reconfiguration fingerprint predicts `acc_2bk` at repeated-CV
  **r = +0.366 ± 0.024** and transfers B→A at **r = +0.398**, bootstrap 95% CI [+0.25, +0.53].
- **What did not hold.** The directional prediction: segregation drops under load at group level
  (Δ = −0.0236, paired p = 3.45e-05), but a larger drop does not predict better performance
  (r = −0.105, p = 0.054). Reconfiguration shows no clear gain over 0-back FC, and FC none over a
  regional activation contrast.
- **Status.** Closed at W3D5. Evidence frozen in `pipeline/02`; re-run from `data/` on 25 Jul 2026.

---

## 2 · The question and the two pre-specified predictions

The project stated **two** predictions of different natures, written as one sentence in Arefeh Lali
Dehaghi's hypothesis ([15 Jul minutes](meetings/2026-07-15.md)) and condensed by Valeria Moraga in
[`manuscript/research-proposal.md`](../manuscript/research-proposal.md). They are reported here as the
two separate tests they always were.

| | **Pattern** | **Direction** |
|---|---|---|
| Object | 78-feature FC fingerprint of the 2-back − 0-back change | one signed scalar: Chan system segregation, 2-back − 0-back |
| Claim | the *set* of features predicts performance in held-out participants | load **lowers** segregation, and a larger shift accompanies **better** performance |
| Nature | multivariate, sign-free | univariate, directional |
| Verdict | **held** (§5, §6) | **refined**: group direction real, individual link absent (§5, §6) |

A distributed pattern and a one-number direction can dissociate: a multivariate model pools
weak-but-consistent signal across features that no single scalar carries. Hence two tests, not one.

**Success criterion**, set by the Project TA (Azman Akhter, [15 Jul](meetings/2026-07-15.md)): beat a
permutation null built by re-running the whole CV on permuted targets — *not* a high R². A clean
negative, shown properly, was declared a valid result.

---

## 3 · Data

One loader interface, two NMA-curated HCP N-back cohorts, nothing stored in Git. Files, variables and
cohort roles: [`docs/data-dictionary.md`](data-dictionary.md), the sole authority on the data. How to
obtain and place it: [`data/README.md`](../data/README.md).

**Cohort B — primary** (`load_hcp`): 339 released, **336 analytic** (3 lack complete 2-back
behaviour), pseudo-IDs, behaviour in `hcp/behavior/wm.csv`, which supports d′.
**Cohort A — transfer target** (`load_hcp_task_with_behaviour`): 100 participants, real HCP IDs,
behaviour in per-subject `Stats.txt` with no clean d′. The two share **35 identities**, verified by
mapping A's real IDs against B's `orig_ids.txt` — sibling samples of one HCP study, which is why the
B→A transfer in §5 removes them and asserts disjointness.

**Shared geometry.** 360 Glasser cortical ROIs (no subcortex, no cerebellum) → 12 Cole-Anticevic
networks. WM run shape (360, 405), TR 0.72 s, two phase-encoding runs (LR/RL) concatenated: 156 frames
per condition per run, **312 concatenated**, zero overlap between 0-back and 2-back frames (asserted in
`pipeline/02` cell 6).

**The `n` convention, fixed once.** `336` = B analytic · `301` = B minus the shared identities (the B→A
training pool) · `100` = A · `67` = fixed holdout test set · `269` = canonical development split.

---

## 4 · Method

Estimator and folds are held fixed across every comparison; only the feature representation changes.

| Stage | What happens | Implementation |
|---|---|---|
| 1 · Condition frames | EV onsets → frame indices with a **4 s HRF shift**: `floor((onset + delay)/TR)` | `gammas.preprocessing.condition_frames(..., delay=4.0)` |
| 2 · FC per condition | Pearson correlation over the concatenated LR+RL frames → one 360×360 matrix per condition | `np.corrcoef` |
| 3 · Fingerprint | 12 within-network + 66 between-network means = **78 features** per condition | `gammas.connectivity.network_fingerprint` |
| 4 · Reconfiguration | fingerprint(2-back) − fingerprint(0-back), 78 features | `pipeline/02` cell 8 |
| 5 · Model | `StandardScaler` + `RidgeCV`; scaling and penalty selection fit **inside** each training fold | `gammas.evaluation.ridge_pipeline` |
| 6 · Evaluation | repeated 5-fold CV (20 seeds) · fixed 80/20 holdout by subject · 1000-permutation full-refit null · identity-disjoint B→A transfer | `pipeline/02` cell 4 |

**Comparators** (same estimator, same folds): 0-back FC (78), 0-back + reconfiguration (156), regional
activation contrast 2bk−0bk (360), single-condition activation (360 each). Success is measured against
the permutation null, not against another model's score.

---

## 5 · Results — the canonical table

> **`±` is the standard deviation across CV partitions. It is never a confidence interval.** It says
> how much the estimate moves depending on which split of the 336 participants you draw, not how
> uncertain the population effect is. The **only** confidence interval in this project is the bootstrap
> CI on the B→A transfer, where the model is frozen and A's 100 participants are resampled.
>
> Cell numbers are 0-based positions in the notebook's cell list.

| Value | CV protocol | n | Notebook | Cell | Function |
|---|---|---|---|---|---|
| **r = +0.366 ± 0.024** | repeated 5-fold CV, 20 partitions, mean ± SD across partitions | 336 | `pipeline/02` | 10 (gate), 12 | `repeated_cv_r` → `ridge_pipeline` |
| r = +0.405 | single 5-fold CV realisation, seed 42 | 336 | `pipeline/02` | 12 | `cv_predict` |
| **p < 0.001** (1/1001), null max r = +0.188 | 1000 permutations with **full pipeline refit**; belongs only to the seed-42 r = 0.405 | 336 | `pipeline/02` | 12 | `permutation_null` |
| r = +0.312 | one fixed 80/20 split, leakage-safe by subject | 67 (test) | `pipeline/02` | 12 | `evaluation.make_split` |
| partial \| `acc_0bk` = +0.219 | partial correlation on the seed-42 out-of-fold prediction | 336 | `pipeline/02` | 12 | `evaluation.partial_correlation` |
| **r = +0.398**, 95% CI [+0.25, +0.53], p < 0.001 | train on 301 B-only, test on all 100 of A, 35 shared identities removed and asserted disjoint; 2000-sample bootstrap over A; permutation on A labels with B predictions fixed | 301 → 100 | `pipeline/02` | 16 | `ridge_pipeline` + bootstrap |
| r = +0.352 ± 0.026 (seed-42 0.399; partial \| `acc_0bk` 0.249) | same fingerprint, target **d′**, repeated CV ×20 | 336 | `pipeline/02` | 14 | `preprocessing.signal_detection_table` |
| 0-back FC **0.274 ± 0.032** · reconfiguration **0.366 ± 0.024** · 0bk+reconfig **0.333 ± 0.026** · activation contrast **0.600 ± 0.016** | repeated CV ×20, identical folds, only the representation changes | 336 | `pipeline/02` | 18 | `repeated_cv_r` |
| activation 0-back alone **0.571 ± 0.014** · 2-back alone **0.569 ± 0.015** | repeated CV ×20, 360 features, same folds as the row above | 336 | `pipeline/02` (first reported in `sandbox/jaime/08` cell 8) | 18 | `repeated_cv_r` |
| activation seed-42 0.598 · partial \| `acc_0bk` +0.412 · partial \| DVARS +0.580 · perm p < 0.001 · corr(contrast, 0-back) = −0.855 · corr(0-back, 2-back) = −0.482 | seed-42 CV, residualised controls, full-refit null, per-ROI mean correlations | 336 | `pipeline/02` | 20 | `permutation_null`, `partial_with_target` |
| cross-run: activation **0.475** vs reconfiguration **0.246**; between-run reliability: activation **0.169** vs reconfiguration **0.024** | train on one run, predict the other run of held-out participants; Fisher-averaged per-feature test-retest | 336 | `pipeline/02` | 20 | `cross_run_r`, `between_run_reliability` |
| **ΔSegregation = −0.0236**, paired p = **3.45e-05** (0.3271 → 0.3035); individual corr(ΔSeg, `acc_2bk`) r = −0.105, p = 0.054; corr(0-back seg, `acc_2bk`) r = +0.109, p = 0.046 | paired t-test over participants; direct correlations | 336 | `pipeline/02` | 22 | `measure_system_segregation` (Goutham's function, verbatim) |
| nested **ΔR² = +0.034 (SD 0.022)** reconfiguration over 0-back FC; **ΔR² = −0.003 (SD 0.007)** FC over activation | paired incremental out-of-fold R² on identical folds, 20 seeds; "no clear gain" when the mean is below 2 SD | 336 | `pipeline/02` | 18 | `incremental_r2` |

**The B→A transfer is a transfer between identity-disjoint cohorts inside the same HCP study.** Not an
external validation, not an independent validation, not an independent cohort: same scanner, same
protocol, sibling samples, 35 identities that had to be removed. The evidence gradient is
*reshuffling your own data < identity-disjoint same-HCP transfer (this) < independent-site replication*.
This wording is a reviewed rule of the final deck; it binds every future text reusing these numbers.

**The submitted abstract's ΔSegregation of −0.048 is not reproducible.** The canonical value is
**−0.0236** — same sign, about half the magnitude (`pipeline/02` cell 28 derives the reconciliation).
Report segregation qualitatively; do not reuse −0.048.

**Independent re-run, 25 Jul 2026.** Feature extraction plus 20-seed repeated CV, from `data/` through
the `gammas` package on the recorded environment (Python 3.12), in **23 s**, no cache and no stored
artifact: 0.3664 ± 0.0237, seed-42 0.4052, and the six-row representation panel (0.2745 · 0.3664 ·
0.3329 · 0.6000 · 0.5713 · 0.5688) all reproduced to four decimals.

---

## 6 · What held, what was refined, what stayed unresolved

| Survives | Refined | Unresolved |
|---|---|---|
| The **pattern** hypothesis: the 78-feature difference predicts unseen 2-back accuracy (0.366) and transfers across identity-disjoint cohorts (0.398, CI [0.25, 0.53]). | The **direction** hypothesis: segregation falls under load at group level (p = 3.45e-05), but a larger shift does not predict better individual performance (r = −0.105, p = 0.054). Reconfiguration shows no clear gain over single-condition 0-back FC; FC none over activation. | Is the predictive information connectivity-specific, or shared with task activation? Cerebrovascular reactivity remains uncontrolled in the activation comparator. |

**The most transferable lesson.** An overwhelming group effect does not grant individual predictive
value. Group change, individual prediction and network topology are three different levels of evidence.

**On the activation comparator.** It is a post-hoc specificity check, not a competition: 360 features
against 78, unmatched, decided after seeing the primary result. 0-back activation alone predicts 0.571
and 2-back alone 0.569, against 0.600 for the contrast — so the activation advantage is **not
load-specific**. Per-run centring makes the three collinear (contrast vs 0-back = −0.855): one
activation axis seen three ways.

---

## 7 · Limitations

Transcribed from the `limitation` column of `pipeline/02` cell 30, one per claim, unedited:

| Claim | Limitation as recorded |
|---|---|
| Reconfiguration FC predicts WM in unseen subjects | Same-task, associational; attenuates to partial r = 0.22 controlling `acc_0bk` |
| d′ retains signal under the ability control | B-only (A has no usable false-alarm rate) |
| Model transfers B→A | Sibling HCP cohorts (35 shared removed); `acc_2bk` only; kinship unmodelled |
| Reconfiguration adds no clear gain over 0-back FC | Heuristic (2 sd), not a formal test |
| Under current representations, activation predicts more strongly | Not count-matched (360 vs 78); one collinear activation axis |
| Activation robust to ability & motion | Controls do not prove "no artifact"; CVR/vascular reactivity untested (no proxy in dataset) |
| Segregation drops under load (group direction) | Individual link weak (r = −0.11); magnitude ≠ abstract's −0.048 |

Carried from the same evidence base:

- **Task-evoked coactivation.** Condition-correlation FC is inflated by simultaneous activation without
  communication; there is no gold standard for task-modulated FC (Masharipov 2024, in
  [`manuscript/references.md`](../manuscript/references.md)). Separating coactivation from coupling is
  open work, not a solved control.
- **Ceiling in the target.** `acc_2bk` is a bounded proportion, left-skewed with participants at 1.000;
  `acc_0bk`, the ability control, is itself near ceiling. Both cap the attainable correlation.
- **No demographic or motion covariates modelled.** Kinship, age, sex and framewise displacement are
  not in the models; DVARS is a motion proxy only.
- **Reproduction warning — the HRF delay.** More than half the effect lives in one preprocessing
  constant. With the canonical `delay=4.0` the pipeline gives **r = 0.366 ± 0.024**; with `delay=0.0`
  the *same* code on the *same* data gives **r = 0.152 ± 0.037** (verified 25 Jul 2026). Nothing fails
  and nothing warns you — you simply get a different number. `gammas.preprocessing.HRF_DELAY = 4.0` is
  now the default, so a caller who passes nothing reproduces the canonical result.

---

## 8 · Reproduce it

1. **Environment.** Python 3.12; `pip install -r requirements.txt` from the repo root. The frozen run
   used NumPy 2.5.1, SciPy 1.18.0, scikit-learn 1.9.0, pandas 3.0.3, matplotlib 3.11.0 (`pipeline/02`
   cell 32). Sanity check without any data: `python -m unittest discover -s tests` (seconds, no data).
2. **Data.** Not in Git. Accept the HCP Data Use Terms, run the two official NMA loader notebooks and
   place the output exactly as [`data/README.md`](../data/README.md) specifies (≈1 GB for A, ≈8 GB for
   B). `GAMMAS_DATA_DIR` points the loaders elsewhere.
3. **Order.** [`pipeline/01`](../pipeline/01_explore_dataset_b.ipynb) for the data tour, then
   [`pipeline/02`](../pipeline/02_canonical_analysis_and_slides.ipynb) for every number in §5. Cell 10
   is a hard reproduction gate: it asserts r = 0.366 ± 0.01 and stops the notebook before any
   interpretation if the pipeline no longer reproduces it. Re-executed top to bottom on 25 Jul 2026:
   **0 error cells, gate absolute error 0.000** against the 0.366 reference, every figure identical.
4. **Cost.** The frozen full run took **342.8 s**, dominated by the 1000-permutation null (131 s) that
   refits the pipeline on every permuted target. `GAMMAS_NPERM=100` gives a fast pass — the p floor is
   1/(N+1), so it moves with N. Without the nulls the primary number takes under half a minute.
5. **Nothing local is required.** No cache, staged artifact, exported figure or stored notebook output
   is an input to any result: every number in §5 is recomputed from `data/` through `gammas`.
6. **The delay default is now 4.0.** Callers of `condition_frames`/`condition_timeseries` that pass no
   `delay` now match the canonical recipe (see §7).

**Provenance rule that held throughout.** Where a submitted number could not be reproduced, it was
reconciled rather than quietly replaced: `pipeline/04` re-runs the original functions verbatim on the
shared data layer, and `pipeline/02` cell 28 derives the submitted-vs-canonical difference in code
instead of retyping it. The submitted abstract stays exactly as sent; the corrections live here.

---

## 9 · Where each fact is authoritative

The directory tree lives in the [root README](../README.md) and the rules for adding to it in
[`CONTRIBUTING.md`](../CONTRIBUTING.md). Listed here: only the ownerships a path name does not reveal.

| Path | Source of truth for |
|---|---|
| [`docs/data-dictionary.md`](data-dictionary.md) | anything about the data: files, variables, loader layer, cohort roles |
| [`pipeline/02`](../pipeline/02_canonical_analysis_and_slides.ipynb) | every number in §5 — the canonical evidence path |
| [`pipeline/03`](../pipeline/03_method_benchmark_tangent_fc.ipynb) + [report](../pipeline/03_tangent_benchmark_report.md) | the tangent-FC POSTPONE ADOPTION verdict |
| [`pipeline/04`](../pipeline/04_goutham_pipeline_reconciliation.ipynb) | why the submitted numbers differ from the canonical ones |
| [`manuscript/abstract.md`](../manuscript/abstract.md) | what was submitted, exactly as sent |

**Why [`docs/archive/`](archive/) is kept.** Its three files are the decision trail, so they are moved,
dated and banner-marked, never condensed or rewritten; their internal links point at pre-archive paths
and are not maintained. `2026-07-22_project-plan.md` is the plan that ran the project until the W3D5
scope freeze (cohort choice, cohort-A pilot, open items as they stood), `2026-07-10_goutham-poc.md` is
Goutham Arcod's Triple-Network proof-of-concept — the origin of the method the project ended up
testing, kept unaltered including its attribution — and `2026-07-17_abstract-merge-rationale.md`
records how the submitted abstract was merged.

---

## 10 · Open threads and how to continue

**The five tests from the final deck (backup slide 10).** Decision criterion: FC must add reliable
held-out value beyond activation and single-condition FC.

1. Match activation and FC dimensionality inside nested CV before comparing them.
2. Separate coactivation from coupling with a prespecified estimator, not a condition correlation.
3. Harder generalisation: another site or session, with HCP kinship modelled.
4. Run the activation model on **resting-state** — cohort B already ships 4 rest runs, so this one is
   runnable today. If rest predicts as well, the signal is task-independent.
5. Model the load transition as a dynamic graph (ST-GNN, Goutham's proposal), not one static difference.

**Tangent-space FC — POSTPONE ADOPTION** ([`pipeline/03`](../pipeline/03_method_benchmark_tangent_fc.ipynb),
[report](../pipeline/03_tangent_benchmark_report.md)). Internal CV 0.5642 ± 0.0228 against the baseline's
0.3664 (**+0.198 r**), but B→A transfer 0.4145 against 0.3981 — a paired difference of **+0.016** with a
bootstrap CI of **[−0.195, +0.190]** that crosses zero. With 100 external participants the paired
bootstrap cannot resolve differences below ≈0.19 r, so the absent gain is not evidence of equivalence.
The 78-feature fingerprint keeps the network-level interpretation the project is built on.

**Graph metrics — partially explored, outside the canonical path.**
[`sandbox/jaime/04`](../sandbox/jaime/04_goutham_pipeline_on_B.ipynb) cell 29: the group shift is tiny
but consistent (within-FC −0.0052, between-FC +0.0026, Newman Q −0.0052 → toward integration); the
scalar integration index does **not** predict (r = +0.043, p = 0.43); baseline modularity Q(0-back)
**does** (r = +0.180, p = 9.3e-04, partial | `acc_0bk` = +0.128, null p = 0.0005). A density-matched
graph layer over `gammas` is the natural next notebook. `networkx` is deliberately not declared in
`requirements.txt` — add it in the pull request that adds the graph notebook, not before.

**Closed or weak avenues.** FCM / K-Means clustering was weak in
[`pipeline/04`](../pipeline/04_goutham_pipeline_reconciliation.ipynb) and never entered the canonical
path. The 17 Jul cohort-A null (r = −0.015) is a power artifact, not a cohort difference: subsampling B
to n = 100 over 30 draws gives r = 0.078 ± 0.146, range [−0.21, +0.40], which brackets it
([`sandbox/jaime/04`](../sandbox/jaime/04_goutham_pipeline_on_B.ipynb) cell 36). Finc 2020 and Calder
2026, still listed as pending in the 17 and 20 Jul minutes, are already in
[`manuscript/references.md`](../manuscript/references.md); the CVR reliability reference is genuinely
open — it has no author, year or journal and cannot be cited until Goutham supplies the full citation.

**Reusable as-is:** the `gammas` package, the reproduction gate pattern (`pipeline/02` cell 10), the
identity-disjoint transfer design with its leakage assertion (cell 16), the model-refit permutation null,
and the paired incremental-R² comparison on identical folds.

---

## 11 · Timeline and decision provenance

One row per meeting record. This is the index of [`docs/meetings/`](meetings/).

| Date | Record | The decision it fixed | Still binding? |
|---|---|---|---|
| 10 Jul | [`2026-07-10.md`](meetings/2026-07-10.md) | The 6-step pipeline, the role split and weighted-undirected graphs; the Project TA sets **prediction on held-out subjects** as the core of the project, with FC and graph metrics as features. | Yes — it is the success criterion the whole analysis is evaluated against. |
| 14 Jul | [`2026-07-14.md`](meetings/2026-07-14.md) | Move the analysis to **cohort B** (336) and compare it against A, driven by overfitting risk at n = 100; d′ proposed as a B-only target. | Yes — B is the primary cohort; A became the transfer target. |
| 15 Jul | [`2026-07-15.md`](meetings/2026-07-15.md) | Arefeh's hypothesis adopted with a **non-directional primary test**, and the evaluation bar set to a permutation null re-running the full CV (Azman). | Yes — §2 and the null in §5 come from here. |
| 17 Jul | [`2026-07-17.md`](meetings/2026-07-17.md) | Numbers accepted, framing reopened: "pattern vs scalar" may read as a feature count rather than science; the B→A transfer (r ≈ 0.40) enters as a candidate headline. | Partly — the framing question was settled by the 21 Jul re-checks and the final deck. |
| 20 Jul | [`2026-07-20.md`](meetings/2026-07-20.md) | **Abstract submitted (22:12).** Predictive hypothesis primary, directional one at group level only; author list of five fixed with Pratik explicitly not an author; tangent FC closed as POSTPONE ADOPTION. | Yes — authorship and the submitted text are closed records. |
| 22 Jul | [`2026-07-22.md`](meetings/2026-07-22.md) | **W3D5 scope frozen at `pipeline/02`**; the presentation waits for no further analysis, and later proposals are follow-up work. | Yes — it is why `pipeline/02` is the canonical evidence path. |

Not a meeting, but part of the chronology: the 21 Jul post-submission re-checks (activation comparator
and the reconciliation of Goutham's pipeline) produced the refinements in §6, and the presentation was
delivered on 24 Jul with pod TA Andrea Buccellato and Project TA Azman Akhter.

---

## 12 · Authorship and contributions

Author list as fixed on [20 Jul](meetings/2026-07-20.md), in that order: **Valeria Moraga · Kerem
Akyurt · Goutham Arcod · Jaime Alonso Pineda Moreno · Arefeh Lali Dehaghi**. Pratik Bhandari was a pod
member and, by recorded decision, not an author.

**Per-person CRediT roles, each with the file, commit or minutes that evidence it, live in
[`AUTHORS.md`](../AUTHORS.md)** — the only place they are maintained, and the reason commit history is
not read as a contribution split here. Teammate sandboxes were never edited: where a technical caveat
about that material was needed it went outside their files, into §5, §6 and `pipeline/04`.
