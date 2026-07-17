# Abstract (draft)

> Two dated snapshots are kept side by side **for comparison**. The **current proposal (2026-07-17)**
> reflects an automated literature review + a reliability analysis on dataset B; the **previous
> snapshot (2026-07-10)** is preserved **unchanged** below. Neither replaces the live editing surface —
> the shared [Google Doc](https://docs.google.com/document/d/1mRC-UZhOGJ_ovPqXBudEBEPUyIp_AzjkJqvoIsAyouk/edit)
> Abstract tab (drafted by Arefeh). The current proposal is offered for team discussion, not a decision.

## Current proposal — 2026-07-17 (dissociation framing)

> Does load-driven functional-connectivity reconfiguration (0-back → 2-back) predict working-memory
> performance in held-out subjects, over and above baseline connectivity?

Working-memory (WM) load reconfigures functional connectivity (FC), but it is unclear whether that
reconfiguration carries individual predictive signal beyond baseline FC. Using the HCP N-back dataset
(336 subjects, Glasser 360 ROIs, 12 Cole-Anticevic networks), we test whether the 0-back→2-back FC
change predicts WM performance in held-out subjects. We compute per-condition FC, a subject-level
reconfiguration matrix (2-back−0-back), a 78-dimensional 12-network fingerprint, and 5-fold
cross-validated RidgeCV prediction, evaluated against a permutation null (N=1000). Working-memory task
FC predicts 2-back accuracy out-of-sample: the undifferenced network fingerprint reaches repeated-CV
r≈0.28 (p<0.001; robust to a DVARS motion proxy), consistent with connectome-based WM prediction
(Avery et al. 2020, r=0.36, 10-fold CV — same task and target, different model; a conceptual
replication). The *multivariate* load reconfiguration pattern (2-back−0-back, 78-dimensional) also
predicts (repeated-CV r≈0.37; leakage-free cross-run r≈0.28). What does NOT predict are the *scalar
directional summaries* of reconfiguration — net between-network integration change (r≈0.04) and mean
modularity change — a pattern-vs-scalar dissociation consistent with difference-score psychometrics
(Hedge et al. 2018): subtracting two correlated conditions destroys the shared true-score variance a
single scalar contrast needs, while a multivariate model can still aggregate weak-but-consistent signal
across edges. The predictive signal is largely trait/general ability (single-condition 0-back FC alone
predicts, repeated-CV r≈0.27; controlling 0-back accuracy attenuates to a comparable partial r≈0.22–0.24
for accuracy and d′) and requires large n (at n≈100 the 78-feature fingerprint is unstable, r≈0.08). d′
is the primary target on measurement grounds (separating sensitivity from response bias), not because it
is more robust. For direction, individual integration change does not predict; only baseline 0-back
modularity does, weakly (r≈0.18). We report an honest dissociation: the multivariate reconfiguration
pattern predicts WM in unseen subjects, but its scalar directional summaries do not.

**What changed vs the 2026-07-10 snapshot (and why):**
- **One falsifiable, non-directional question** (does reconfiguration predict?), not three objectives.
  Objective 2 (resting-state) dropped from the MVP scope (kept as a possible extension; dataset B does
  include resting-state runs).
- **Named target and numbers**: 2-back accuracy (d′ on measurement grounds), 336 subjects, held-out
  CV, permutation null — reads as a study, not a review.
- **Honest framing**: the prediction is consistent with Avery 2020 (conceptual replication); the
  contribution is the *pattern-vs-scalar dissociation* (the multivariate reconfiguration pattern
  predicts; its scalar directional summaries do not) with a difference-score-reliability explanation.
- Terminology fixed to *low/high working-memory load*; "salience" → Cingulo-Opercular.

---

## Previous snapshot — 2026-07-10 (preserved unchanged)

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

See the [living project plan](../docs/project-plan.md#open-now) for current decisions.

- **Objective 2 (resting-state / intrinsic organization):** the task dataset has no clean resting
  state. Decide whether to drop objective 2, reframe it as a caveat, or use a different loader.
  Recommended narrowing: objectives **1 + 3** (task reconfiguration + prediction).
- **Concretize:** a single falsifiable hypothesis, the named prediction target (from `Stats.txt`),
  the graph metrics, and the prediction model — the abstract should read as a study, not a review.
- **Terminology:** use *low / high working-memory load* (standard), avoid vague wording.
