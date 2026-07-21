# Living project plan

**Last reviewed:** 21 July 2026
**Stage:** Week 3 (W3D1 was Mon 20 July). The FC/prediction pilot and external validation are verified
on `main`; the Monday 20 July team sync happened (see [meetings/2026-07-20.md](meetings/2026-07-20.md))
and the abstract was submitted 20 July 22:12. Focus is now the **W3D5 presentation (Fri 24 July)**.

This is the canonical detailed status. [`../README.md`](../README.md) is its short snapshot; dated
meeting notes preserve the discussion behind changes. A working plan is not a claim that every stage
is group-approved: NMA projects are iterative, and methods and ownership may change as the team learns
from the data.

## Current snapshot

**Verified on `main`:** shared A/B ingestion layer, dataset-B onboarding, Goutham's FC/prediction
pipeline reproduced on A and ported to B, permutation testing, corrected d′, and leakage-free B→A
external validation.

**Not yet locked by the group:** the 78-feature network summary, FC preprocessing/estimation choices,
and the interpretation of integration/segregation. (The abstract was submitted 20 July; see the
milestones below.)

## Working question

> Does functional connectivity reconfigure between low and high working-memory load
> (0-back → 2-back), and can that reconfiguration predict individual working-memory performance?

The Project TA's north star is **prediction on unseen subjects**. FC and graph metrics are candidate
features, not the final goal. The hypothesis stays falsifiable.

## Original working hypothesis and current result

> Increasing WM load from 0-back to 2-back reconfigures whole-brain FC from a more **segregated**
> toward a more **integrated** state; and individual differences in this reconfiguration **predict**
> 2-back performance (`acc_2bk`, or **d′**) in held-out subjects — those who reconfigure more toward
> integration tend to perform better.

- **The primary, non-directional test passed:** the multivariate reconfiguration pattern predicts
  held-out performance above a permutation null.
- **The directional expectation did not:** neither the net integration index nor mean modularity
  change predicts performance. The result therefore does not support *"more integration → better"*
  as a one-number individual-differences account.
- The numbers are verified; the story is not locked. Azman's 17 July comment was that the current
  wording could read as a feature-count comparison rather than the scientific meaning of integration
  and segregation, and that external validation might be a stronger headline. This is framing
  feedback, not a methodological veto. The pattern-vs-scalar framing was superseded on 21 July by
  notebook 08 (see the follow-up section): reconfiguration does not clearly add over single-condition
  0-back FC, a task-activation contrast predicts better, and the predictive signal is not specific to
  connectivity reconfiguration.

Source: Arefeh's proposal, refined 15 July → [research-proposal](../manuscript/research-proposal.md).

## Dataset roles for the current MVP

**B** = [`load_hcp`](https://github.com/NeuromatchAcademy/course-content/blob/v3.0.2/projects/fMRI/load_hcp.ipynb):
339 subjects (336 analytic), 360 Glasser cortical regions, two WM runs (LR/RL), eight WM conditions
(0-back / 2-back × four stimulus categories).

**B is the primary analysis cohort for the current MVP.** Two reasons for B over **A**
([`load_hcp_task_with_behaviour`](https://github.com/NeuromatchAcademy/course-content/blob/v3.0.2/projects/fMRI/load_hcp_task_with_behaviour.ipynb), 100 subjects):

- **Power** — 339 ≫ 100 → less overfitting, more confidence (Project TA).
- **d′ is computable only on B** — d′ needs hit / false-alarm rates; B's `wm.csv` has
  `ACC_TARGET` / `ACC_NONTARGET`, A's `Stats.txt` fields are internally inconsistent (HCP WM bug).

**A is the independent external-validation cohort**, not merged into B. Only ~35 subjects overlap;
the leakage-free design trains on 301 B-only participants and tests on all 100 A participants. A
cannot yield clean d′, so external validation uses accuracy. These are the operational roles already
implemented; the team will formally reconfirm the MVP on Monday. Detail: [data dictionary](data-dictionary.md)
· [`sandbox/jaime/00`](../sandbox/jaime/00_framing_and_dataset_choice.ipynb) ·
[`sandbox/jaime/05`](../sandbox/jaime/05_dataset_A_external_validation.ipynb).

## Confirmed direction

- Behaviour is the prediction target; compare low vs high WM load (0-back vs 2-back).
- **Reporting anchor:** `acc_2bk`, for comparison with Avery 2020 and for B→A validation.
- **Measurement-focused companion:** corrected d′ on B, which separates sensitivity from response
  bias. Both are implemented; the abstract must label their roles consistently.
- Functional (not directed/effective) connectivity; graphs weighted and undirected.
- **Prediction on held-out subjects is the main evaluation principle.**
- **Success = beating a permutation null, not a high R²** (Project TA) — build the null from our own
  data (permute the target, re-run the whole CV); an accuracy above it counts even if small.
- No additional data search: B is the primary cohort and the already-downloaded A cohort is used only
  for independent external validation, not pooled training.
- **Objective 2 (resting-state / intrinsic organisation) is out of the MVP** — a possible extension
  on B, not a final-week goal.
- The full graph-metric layer is post-MVP unless the team explicitly restores it to Monday's sprint.

## Pilot signal check (dataset A)

Goutham's pilot on **dataset A (100 subjects)** ran the full pipeline — FC reconfiguration
(`2bk − 0bk`) collapsed to a network fingerprint, plus a separate triple-network feature set —
into cross-validated prediction of 2-back accuracy. **Neither predicted performance:**

| Features → target | Held-out result (N = 100) |
|---|---|
| Reconfiguration fingerprint → `acc_2bk` | r = −0.02, R² = −0.04 |
| Triple-network → `acc_2bk` | r = 0.08, R² = −0.01 |

(The strong correlations in that notebook — salience↔FPN, salience↔DMN — are brain–brain couplings
driven by task engagement, not prediction of individual performance.)

This is a **real negative for the A-only n=100 training design**, not a bug to explain away — a
valuable early feasibility flag, but not evidence that cohort A contains no transferable signal.
Three non-exclusive reasons it could be flat, each with a lever we can test:

| Possible cause | Lever |
|---|---|
| Underpowered (N = 100) | **Dataset B** (339 subjects) |
| Noisy / ceiling-compressed target (raw `acc_2bk`) | **d′** — a cleaner, better-distributed target |
| No true effect | **Permutation null** — the arbiter of whether any signal survives |

B + d′ were then run (next section): the reconfiguration **pattern did beat the null**, and an n = 100
subsampling of B reproduces A's flat r (≈ 0.08 ± 0.15), so **A's null was underpowered, not a true
absence** — the power lever was the right one. A clean negative would still have counted (per the
Project TA). The full graph layer remains unbuilt: notebook `04` contains exploratory within/between
FC and Newman modularity, while system segregation, efficiency, clustering, thresholding and signed
edge handling remain untried.

## Pilot follow-up on dataset B (audited 15 Jul; reframed 17 Jul post-audit)

B + d′ were run through the **same pipeline** (port validated — A reproduces exactly: fingerprint
r = −0.0150, triple r = 0.0760). The result is a **genuine positive, but weaker and more specific**
than the raw number suggests.

| Method → target | Out-of-sample r | R² | Note |
|---|---|---|---|
| Reconfiguration fingerprint → `acc_2bk` | **0.31** held-out (n = 67) | 0.09 | repeated-CV central 0.37 ± 0.02; seed-42 0.41 is optimistic |
| Reconfiguration fingerprint → **d′** | 0.40 (seed 42) | 0.16 | retains signal under the ability control |
| Triple-network → `acc_2bk` | 0.37 (seed 42) | 0.14 | adds little over the fingerprint |

- **Beats the permutation null** decisively (p < 0.001; null centred below 0 → no leakage) and is
  **robust to a DVARS motion proxy** (FC barely encodes DVARS, r = 0.04; survives residualising it out,
  r = 0.35; FD unavailable in the curated set).
- **For `acc_2bk`, much of the signal is general cognitive ability.** Controlling `acc_0bk`, partial
  r falls to **0.22** and the fingerprint adds ~no R² over ability alone. **d′ retains signal** under
  the same control — support for keeping d′ as the measurement-focused companion, not evidence that
  it is more robust than accuracy.
- **Reconfiguration pattern vs single-condition FC (revised 21 Jul, nb08).** The multivariate
  reconfiguration pattern predicts held-out performance (repeated-CV r ≈ 0.366), and single-condition
  0-back FC alone predicts at r ≈ 0.274. The 17 Jul reading that reconfiguration *adds* over
  single-condition FC did not survive re-check: nb08's nested delta-R² is only +0.034 (sd 0.023, under
  2 sd), so reconfiguration does not clearly add over 0-back FC. Only the scalar directional summaries
  (net integration index r ≈ 0.04, mean modularity change) remain flat, as before.
- **Verified numerical statement (revised 21 Jul, nb08).** The multivariate load-reconfiguration
  pattern predicts WM in unseen subjects (repeated-CV r ≈ 0.366, p ≈ 0.001 against a corrected
  permutation null, robust to a DVARS proxy); the one-number directional summaries do not. nb08's
  current headline is that this predictive signal is **not specific to connectivity reconfiguration**:
  a task-activation contrast (2bk − 0bk mean BOLD) predicts better (r ≈ 0.60 pooled, ≈ 0.48 held out
  over both people and runs), FC adds nothing over that activation contrast (nested delta-R² ≈ −0.003),
  and per-run centering makes 0bk/2bk/contrast collinear (contrast vs 0bk ≈ −0.86), so the contrast is
  not a load-independent trait. Do not use the seed-42-optimistic *"reconfiguration predicts at r =
  0.40"*; the current headline notebook is 08.

Detail, code and the reproduction gate: [`sandbox/jaime/04_goutham_pipeline_on_B.ipynb`](../sandbox/jaime/04_goutham_pipeline_on_B.ipynb)
(still valid; it is nb08's reproduction gate). **Current headline notebook (21 Jul, peer-reviewed):**
[`sandbox/jaime/08_activation_vs_reconfiguration.ipynb`](../sandbox/jaime/08_activation_vs_reconfiguration.ipynb).
The tangent-space benchmark [`sandbox/jaime/06_tangent_fc_benchmark.ipynb`](../sandbox/jaime/06_tangent_fc_benchmark.ipynb)
remains **POSTPONE ADOPTION**.

## Working stages

| Stage | Purpose | Lead(s) | Status |
|---|---|---|---|
| 1. Ingestion + EV segmentation | Separate low/high load frames; shared A/B loader | Jaime | **Done** — shared layer + `pipeline/01_explore_dataset_b` |
| 2. Functional connectivity | FC per load condition | Valeria + Arefeh | **Prototype exists** on A and B; compare, review and generalise |
| 3. Graph construction | FC as weighted, undirected graphs | Goutham | Not yet built as a shared stage; scope Monday |
| 4. Graph metrics | Segregation / integration | Kerem + Arefeh | Exploratory integration/modularity only; full layer post-MVP unless restored Monday |
| 5. Prediction / testing | Predict WM performance in unseen subjects + permutation null | Valeria + Arefeh | **Pilot verified on B + B→A external validation**; team review done 20 Jul (see [meetings/2026-07-20.md](meetings/2026-07-20.md)) |

Owners above are the prior working allocation, not the final-week sprint. Reassign after the Monday
method/story discussion and then update this table and the root README together.

## Open now

- ❗ **Goutham's read on the 78-feature method** — why average 360 ROIs into 12 networks and retain
  the 12 within-network diagonal summaries alongside 66 between-network edges.
- ❗ **Reconcile Goutham's numbers before any W3D5 slide.** His fingerprint r is inconsistent across the
  repo: the 20 Jul minutes cite r ≈ 0.35 (single 5-fold CV, Colab only), his committed
  [`sandbox/goutham/FCM_entropy.ipynb`](../sandbox/goutham/FCM_entropy.ipynb) reports r = 0.2376 (single
  split), and the canonical repeated-CV is r ≈ 0.366. His ΔSegregation = −0.048 (Chan-style) is not
  reproducible from the repo (nb04 has only Newman modularity). Present the reproducible r ≈ 0.366 and
  ask Goutham to reconcile the 0.35 and the ΔSegregation before they reach a slide. Teammate files:
  flag only, do not edit.
- **FC estimator/preprocessing:** decide how to handle task-evoked coactivation and document the
  Pearson-FC limitation.
- **Graph scope:** if graph metrics return to the MVP, prespecify thresholding, negative edges,
  metrics and aggregation. Otherwise keep the full layer explicitly post-MVP.

**Settled/implemented:** corrected d′ extreme rates; B permutation null; DVARS-proxy sensitivity
analysis; B→A external validation. Age, sex, family IDs and framewise displacement are unavailable in
the curated data and should be limitations, not open implementation promises.

## Milestones

| Date | Milestone |
|---|---|
| **17 July** | ✅ Project TA progress check; verified results + framing comments for team review |
| **20 July** (W3D1) | ✅ Team method/story sync held ([meetings/2026-07-20.md](meetings/2026-07-20.md)); abstract submitted 22:12 |
| **21 July** | ✅ nb08 re-check: reconfiguration does not clearly add over 0-back FC; task-activation contrast predicts better; signal not connectivity-specific |
| **24 July** (W3D5) | Final presentation: 1 slide / 1 minute per person |

## Sources

- Meeting notes: [10 July](meetings/2026-07-10.md) · [14 July](meetings/2026-07-14.md) · [15 July](meetings/2026-07-15.md) · [17 July](meetings/2026-07-17.md).
- Literature reviews → [`reviews/`](reviews/): e.g. the [2026-07-17 automated review](reviews/2026-07-17_literature-review.md) (WM-prediction benchmarks, same-task calibration, change-score reliability).
- The shared **"Ideas" Google Doc** (owner: Valeria) — its *Main Tasks* tab maps to the working stages;
  see [`../manuscript/README.md`](../manuscript/README.md) for how its tabs map into the repo.

New decisions update this plan; detailed discussion stays in dated meeting notes.
