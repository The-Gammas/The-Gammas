# Abstract (draft)

> Two dated snapshots are kept side by side **for comparison**. The **current proposal (2026-07-17)**
> reflects an automated literature review + a reliability analysis on dataset B; the **previous
> snapshot (2026-07-10)** is preserved below unchanged. Neither replaces the live editing surface —
> the shared [Google Doc](https://docs.google.com/document/d/1mRC-UZhOGJ_ovPqXBudEBEPUyIp_AzjkJqvoIsAyouk/edit)
> Abstract tab (drafted by Arefeh). The current proposal is offered for team discussion, not as a
> decision.

## Current proposal — 2026-07-17 (dissociation framing)

> Does load-driven functional-connectivity reconfiguration (0-back → 2-back) predict working-memory
> performance in held-out subjects, over and above baseline connectivity?

Working-memory (WM) load reconfigures functional connectivity (FC), but it is unclear whether that
reconfiguration carries individual predictive signal beyond baseline FC. Using the HCP N-back dataset
(336 subjects, Glasser 360 ROIs, 12 Cole-Anticevic networks), we test whether the 0-back→2-back FC
change predicts WM performance in held-out subjects. We compute per-condition FC, a subject-level
reconfiguration matrix (2-back−0-back), a 78-dimensional 12-network fingerprint, and 5-fold
cross-validated RidgeCV prediction, evaluated against a permutation null (N=1000). Task/baseline FC
predicts 2-back accuracy out-of-sample (r≈0.35, p<0.001; not explained by head motion), replicating
connectome-based WM prediction (Avery et al. 2020, r=0.36). The load-driven reconfiguration change
score, however, does not predict (r≈0.04). We trace this to measurement reliability: the 2-back−0-back
fingerprint has near-zero between-run test-retest reliability (r≈0.02) versus ~0.33 for each
single-condition fingerprint, so the contrast cannot support individual-difference prediction by
construction — consistent with difference-score psychometrics. The predictive signal instead reflects
trait FC (0-back FC alone predicts, r≈0.29) and largely general cognitive ability (controlling 0-back
accuracy, partial r≈0.22); d′ retains signal under this control and is reported as a robustness target.
For direction, individual integration change does not predict; only baseline 0-back modularity does,
weakly (r≈0.18). We report an honest dissociation: FC predicts WM in unseen subjects, but load
reconfiguration per se does not — a cautionary, reliability-grounded result for change-based network
accounts.

**What changed vs the 2026-07-10 snapshot (and why):**
- **One falsifiable, non-directional question** (does reconfiguration predict?), not three objectives.
  Objective 2 (resting-state) dropped — the task dataset has no clean rest.
- **Named target and numbers**: 2-back accuracy (d′ as robustness), 336 subjects, held-out CV,
  permutation null — reads as a study, not a review.
- **Honest framing**: the prediction replicates Avery 2020; the contribution is the *dissociation*
  (reconfiguration does not predict) with a measurement-reliability explanation.
- Terminology fixed to *low/high working-memory load*; "salience" → Cingulo-Opercular.

---

## Previous snapshot — 2026-07-10 (preserved for comparison)

> **Historical snapshot — not a current team decision.** Captured from the shared Google Doc on
> **2026-07-10**, before Valeria Moraga's [research proposal](research-proposal.md).

### Research question

> Does functional connectivity reconfigure between low and high working-memory load
> (0-back vs 2-back), and does this reconfiguration predict working-memory performance?

### Draft

The human brain is one of the most complex biological systems, and its functional organization can be
characterized as a connectivity network using fMRI. Brain regions of interest (ROIs) are nodes;
functional interactions are edges. Graph theory provides a framework for quantifying the topological
properties of brain networks and how information is organized across distributed neural systems.

A fundamental principle of brain network organization is the balance between functional
**segregation** (specialized local processing) and functional **integration** (communication across
distributed systems). Efficient cognition requires a dynamic balance between the two. Alterations in
this balance have been associated with differences in cognitive function.

Beyond intrinsic organization, cognitive demands can drive dynamic reconfiguration of functional
networks: during a task, connectivity is modulated to support task-specific requirements.

This study investigates (1) how functional segregation and integration differ across cognitive load
(0-back vs 2-back); (2) how intrinsic organization balances segregation and integration; and (3)
whether these network properties **predict individual working-memory performance**.

### Open flags recorded with this snapshot

- **Objective 2 (resting-state / intrinsic organization):** the task dataset has no clean resting
  state. Recommended narrowing: objectives **1 + 3** (task reconfiguration + prediction). *(Resolved in
  the current proposal: dropped.)*
- **Concretize:** a single falsifiable hypothesis, a named prediction target, the graph metrics, and
  the prediction model. *(Resolved in the current proposal.)*
- **Terminology:** use *low / high working-memory load* (standard), avoid vague wording.
