# Living project plan

**Last reviewed:** 15 July 2026  
**Stage:** Week 2 — direction provisionally set; **dataset (B) and hypothesis are the group's lean, pending Goutham's read + Friday's lock.**

A working plan, not a claim that every stage is implemented. NMA projects are iterative: question,
methods and division of work may change as the group learns from the data.

## Working question

> Does functional connectivity reconfigure between low and high working-memory load
> (0-back → 2-back), and can that reconfiguration predict individual working-memory performance?

The Project TA's north star is **prediction on unseen subjects**. FC and graph metrics are candidate
features, not the final goal. The hypothesis stays falsifiable.

## Hypothesis (lean — pending Goutham's read)

> Increasing WM load from 0-back to 2-back reconfigures whole-brain FC from a more **segregated**
> toward a more **integrated** state; and individual differences in this reconfiguration **predict**
> 2-back performance (`acc_2bk`, or **d′**) in held-out subjects — those who reconfigure more toward
> integration tend to perform better.

- **The primary test is non-directional** — does reconfiguration predict performance at all
  (association / held-out prediction vs a permutation null). *"Toward integration → better"* is the
  expectation we test, **not an assumption** (prior work shows integration is *selective*, not
  uniformly adaptive — a negative-direction result is still valid).
- Project TA's read: group-level part *"clean, testable"*; individual-differences part
  *"plausible… I'd trust it to start with."*

Source: Arefeh's proposal, refined 15 July → [research-proposal](../manuscript/research-proposal.md).

## Dataset → Finalist B (lean — pending Goutham's read + Friday lock)

**B** = [`load_hcp`](https://github.com/NeuromatchAcademy/course-content/blob/v3.0.2/projects/fMRI/load_hcp.ipynb):
339 subjects (336 analytic), 360 Glasser cortical regions, two WM runs (LR/RL), eight WM conditions
(0-back / 2-back × four stimulus categories).

Two reasons for B over **A** ([`load_hcp_task_with_behaviour`](https://github.com/NeuromatchAcademy/course-content/blob/v3.0.2/projects/fMRI/load_hcp_task_with_behaviour.ipynb), 100 subjects):

- **Power** — 339 ≫ 100 → less overfitting, more confidence (Project TA).
- **d′ is computable only on B** — d′ needs hit / false-alarm rates; B's `wm.csv` has
  `ACC_TARGET` / `ACC_NONTARGET`, A's `Stats.txt` fields are internally inconsistent (HCP WM bug).

A is set aside — **not** merged (only ~35 subjects overlap, and A can't yield d′). Detail:
[data dictionary](data-dictionary.md) · [`sandbox/jaime/00`](../sandbox/jaime/00_framing_and_dataset_choice.ipynb).

## Confirmed direction

- Behaviour is the prediction target; compare low vs high WM load (0-back vs 2-back).
- **Target: `acc_2bk` primary; d′ preferred where available (B).**
- Functional (not directed/effective) connectivity; graphs weighted and undirected.
- **Prediction on held-out subjects is the main evaluation principle.**
- **Success = beating a permutation null, not a high R²** (Project TA) — build the null from our own
  data (permute the target, re-run the whole CV); an accuracy above it counts even if small.
- One dataset; no chasing extra data in the course window.
- **Objective 2 (resting-state / intrinsic organisation) is out of the MVP** — a possible extension
  on B, not a Week-2 goal.

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

This is a **real negative on A**, not a bug to explain away — a valuable early feasibility flag.
Three non-exclusive reasons it could be flat, each with a lever we can test:

| Possible cause | Lever |
|---|---|
| Underpowered (N = 100) | **Dataset B** (339 subjects) |
| Noisy / ceiling-compressed target (raw `acc_2bk`) | **d′** — a cleaner, better-distributed target |
| No true effect | **Permutation null** — the arbiter of whether any signal survives |

If B + d′ still show nothing above the permutation null, a clean negative is itself a valid result
(per the Project TA). Note: graph-theoretic metrics proper (modularity, efficiency, clustering) are
a **different, still-untried** feature family — the negative so far is on FC reconfiguration and
triple-network features only.

## Pilot follow-up on dataset B (audited 15 Jul)

B + d′ were run through the **same pipeline** (port validated — A reproduces exactly: fingerprint
r = −0.0150, triple r = 0.0760). The result is a **genuine positive, but weaker and more specific**
than the raw number suggests.

| Method → target | Out-of-sample r | R² | Note |
|---|---|---|---|
| Reconfiguration fingerprint → `acc_2bk` | **0.31** held-out (n = 67) | 0.09 | repeated-CV central 0.37 ± 0.02; seed-42 0.41 is optimistic |
| Reconfiguration fingerprint → **d′** | 0.40 (seed 42) | 0.16 | retains signal under the ability control |
| Triple-network → `acc_2bk` | 0.37 (seed 42) | 0.14 | adds little over the fingerprint |

- **Beats the permutation null** decisively (p < 0.001; null centred below 0 → no leakage) and is
  **not driven by motion** (FC barely encodes DVARS, r = 0.04; survives residualising it out, r = 0.35).
- **For `acc_2bk`, much of the signal is general cognitive ability.** Controlling `acc_0bk`, partial
  r falls to **0.22** and the fingerprint adds ~no R² over ability alone. **d′ retains signal** under
  the same control — an argument for **d′ as the primary target**.
- **Mostly trait FC, not reconfiguration.** Single-state FC already predicts (0bk-only r = 0.29);
  reconfiguration adds over that, it is not the whole effect.
- **Report as** *"FC predicts WM performance in unseen subjects, r ≈ 0.35 out-of-sample, p < 0.001,
  not explained by motion"* — **not** as *"reconfiguration predicts at r = 0.40"*.

Detail, code and the full check: [`sandbox/jaime/04_goutham_pipeline_on_B.ipynb`](../sandbox/jaime/04_goutham_pipeline_on_B.ipynb).

## Working stages

| Stage | Purpose | Lead(s) | Status |
|---|---|---|---|
| 1. Ingestion + EV segmentation | Separate low/high load frames; shared A/B loader | Jaime | **Done** — shared layer + `pipeline/01_explore_dataset_b` |
| 2. Functional connectivity | FC per load condition | Valeria + Arefeh | Prototype exists (Goutham's pilot); to generalise & review |
| 3. Graph construction | FC as weighted, undirected graphs | Goutham | Planned — graph metrics not yet built |
| 4. Graph metrics | Segregation / integration | Kerem + Arefeh | Planned |
| 5. Prediction / testing | Predict WM performance in unseen subjects + permutation null | Valeria + Arefeh | Pilot on A → null; port to B, add permutation null |

## Open now

- ❗ **Goutham's read on dataset B + the method** — the input we're waiting on before locking anything.
- d′ extreme-rate correction (e.g. loglinear) — prespecify.
- FC preprocessing / estimation details.
- Graph thresholding and treatment of negative edges.
- Graph metrics and level of aggregation.
- Prediction model + available confounds (motion, age).

## Milestones

| Date | Milestone |
|---|---|
| **17 July** | Project TA progress check *(prior docs say abstract submission — confirm the authoritative date with Azman / the portal)* |
| **20 July** (W3D1) | Abstract written |
| **24 July** | Final project story / presentation |

## Sources

- Meeting notes: [10 July](meetings/2026-07-10.md) · [14 July](meetings/2026-07-14.md) · [15 July](meetings/2026-07-15.md).
- Literature reviews → [`reviews/`](reviews/): e.g. the [2026-07-17 automated review](reviews/2026-07-17_literature-review.md) (WM-prediction benchmarks, same-task calibration, change-score reliability).
- The shared **"Ideas" Google Doc** (owner: Valeria) — its *Main Tasks* tab maps to the working stages;
  see [`../manuscript/README.md`](../manuscript/README.md) for how its tabs map into the repo.

New decisions update this plan; detailed discussion stays in dated meeting notes.
