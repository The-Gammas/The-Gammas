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

**Verified:** shared A/B ingestion layer, dataset-B onboarding, Goutham's FC/prediction pipeline
reproduced on A and ported to B, permutation testing, corrected d′, leakage-free B→A external
validation, and the complete presentation evidence path in
[`pipeline/02`](../pipeline/02_canonical_analysis_and_slides.ipynb).

**Not yet locked by the group:** whether the activation benchmark belongs in the five main slides or
in backup/Q&A, the presenter/figure allocation, the FC preprocessing/estimation caveat, and the final
interpretation of integration/segregation. The evidence is consolidated; the narrative choice remains
a proposal. (The abstract was submitted 20 July; see the milestones below.)

## Working question

> Does functional connectivity reconfigure between low and high working-memory load
> (0-back → 2-back), and can that reconfiguration predict individual working-memory performance?

The post-submission robustness question is:

> Does reconfiguration add predictive information beyond single-condition 0-back FC, and how does
> it compare with the simpler regional activation signal?

This second question refines the interpretation of the original hypothesis; it does not replace it.

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
  feedback, not a methodological veto. The pattern-vs-scalar dissociation still holds, but nb08 (21
  July) showed it is no longer sufficient as the whole conclusion: reconfiguration does not clearly
  add over single-condition 0-back FC, and a task-activation contrast predicts more strongly under
  the current unmatched representations. The evidence therefore does not establish that the
  predictive signal is specific to connectivity reconfiguration.

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

**A is the held-out transfer cohort** (same HCP source, disjoint identities), not merged into B. Only
~35 subjects overlap; the leakage-free design trains on 301 B-only participants and tests on all 100 A
participants. A cannot yield clean d′, so the transfer test uses accuracy. These operational roles were
carried into the 20 Jul team sync and remain in force. Detail: [data dictionary](data-dictionary.md)
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
- The full graph-metric layer is post-MVP unless the team explicitly restores it to the final-week sprint.

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
Project TA). The full graph layer is still not a shared `pipeline/` stage: notebook `04` covers
within/between FC and Newman modularity, and [nb09](../sandbox/jaime/09_goutham_pipeline_replication.ipynb)
now also runs Chan-style system segregation and K-Means/FCM clustering in Jaime's sandbox (both weak);
efficiency, thresholding and signed-edge handling remain untried.

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
  permutation null, robust to a DVARS proxy); the one-number directional summaries do not. Under the
  current unmatched representations, a task-activation contrast (2bk − 0bk mean BOLD; 360 regional
  features) predicts more strongly than the 78-feature network FC summary (r ≈ 0.60 pooled, ≈ 0.48
  held out over both people and runs), and adding FC shows no clear gain (nested delta-R² ≈ −0.003).
  This comparison does not establish FC-specific predictive value, but it is not a feature-matched
  biological contest. Per-run centering also makes 0bk/2bk/contrast collinear (contrast vs 0bk ≈
  −0.86), so the contrast is not a load-independent trait. Do not use the seed-42-optimistic
  *"reconfiguration predicts at r = 0.40"*.

Detail, code and the reproduction gate: [`sandbox/jaime/04_goutham_pipeline_on_B.ipynb`](../sandbox/jaime/04_goutham_pipeline_on_B.ipynb)
(still valid; it is nb08's reproduction gate). **Canonical evidence notebook:**
[`pipeline/02_canonical_analysis_and_slides.ipynb`](../pipeline/02_canonical_analysis_and_slides.ipynb).
**Focused robustness notebook:**
[`sandbox/jaime/08_activation_vs_reconfiguration.ipynb`](../sandbox/jaime/08_activation_vs_reconfiguration.ipynb).
The tangent-space benchmark [`sandbox/jaime/06_tangent_fc_benchmark.ipynb`](../sandbox/jaime/06_tangent_fc_benchmark.ipynb)
remains **POSTPONE ADOPTION**.

## Working stages

| Stage | Purpose | Lead(s) | Status |
|---|---|---|---|
| 1. Ingestion + EV segmentation | Separate low/high load frames; shared A/B loader | Jaime | **Done** — shared layer + `pipeline/01_explore_dataset_b` |
| 2. Functional connectivity | FC per load condition | Valeria + Arefeh | **Canonical evidence consolidated in `pipeline/02`**; estimator caveat retained |
| 3. Graph construction | FC as weighted, undirected graphs | Goutham | Descriptive network view included in `pipeline/02`; extended graph work remains exploratory in nb09 |
| 4. Graph metrics | Segregation / integration | Kerem + Arefeh | Segregation direction included in `pipeline/02`; clustering and full graph layer remain post-MVP |
| 5. Prediction / testing | Predict WM performance in unseen subjects + permutation null | Valeria + Arefeh | **Internal and B→A evidence consolidated in `pipeline/02`**; final presentation framing pending team approval |

Owners above are the prior working allocation, not the final-week sprint. Reassign as the W3D5
presentation split is agreed and then update this table and the root README together.

## Open now

- ❗ **Team presentation decision:** review the canonical notebook and approve or revise its proposed
  story: keep FC reconfiguration primary, show activation as the unexpected benchmark, remove the
  unsupported *beyond static FC* claim, and avoid opening new clustering/FCM experiments. A narrower
  fallback puts activation in backup/Q&A while retaining the corrected conclusion.
- **Presentation allocation:** choose the final FC figure and one-minute interpretation, then assign
  one slide / one minute per presenter.
- ❗ **Goutham's read on the 78-feature method** — why average 360 ROIs into 12 networks and retain
  the 12 within-network diagonal summaries alongside 66 between-network edges.
- ✅ **Goutham's numbers reconciled (21 Jul, [nb09](../sandbox/jaime/09_goutham_pipeline_replication.ipynb)).**
  His analysis functions run verbatim on our data layer. The fingerprint reconfiguration comes out
  r ≈ 0.366 (repeated CV) / 0.405 (single seed), so his committed 0.2376 was a data-loading artifact,
  not a method problem: the canonical **r ≈ 0.366** is what to present. The ΔSegregation direction
  reproduces (segregation drops 0-back → 2-back, p = 3.45e-05) but its magnitude is about −0.024, not the
  abstract's −0.048, and individual-difference prediction is weak (corr ≈ −0.10, p = 0.05); present
  segregation qualitatively, not as the number −0.048. nb09 also regenerates his brain maps in-notebook
  (static maps + an interactive 3D map with a semi-transparent cortex), so those no longer wait on his
  loose Colab HTML exports.
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
| **21 July** | ✅ nb08 re-check: reconfiguration does not clearly add over 0-back FC; regional activation predicts more strongly under the current unmatched representations; FC specificity is not established |
| **21 July** | ✅ nb09: Goutham's pipeline replicated on our data; numbers reconciled (fingerprint 0.366; his 0.2376 a data-loading artifact); segregation direction reproduced (magnitude −0.024, not −0.048); brain maps regenerated |
| **21 July** | ✅ `pipeline/02`: canonical evidence and presentation figures consolidated; recommended narrative documented as a proposal pending team approval |
| **24 July** (W3D5) | Final presentation: 1 slide / 1 minute per person |

## Sources

- Meeting notes: [10 July](meetings/2026-07-10.md) · [14 July](meetings/2026-07-14.md) · [15 July](meetings/2026-07-15.md) · [17 July](meetings/2026-07-17.md) · [20 July](meetings/2026-07-20.md).
- Literature reviews → [`reviews/`](reviews/): e.g. the [2026-07-17 automated review](reviews/2026-07-17_literature-review.md) (WM-prediction benchmarks, same-task calibration, change-score reliability).
- The shared **"Ideas" Google Doc** (owner: Valeria) — its *Main Tasks* tab maps to the working stages;
  see [`../manuscript/README.md`](../manuscript/README.md) for how its tabs map into the repo.

New decisions update this plan; detailed discussion stays in dated meeting notes.
