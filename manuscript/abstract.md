# Abstract (draft)

> **Status checked 18 Jul:** the 17 July merge remains the current repository proposal and is queued
> for Monday's team workshop. It is not a final decision; the shared Google Doc remains the live
> editing surface.
>
> Two dated snapshots are kept side by side **for comparison**. The **current proposal (2026-07-17)**
> merges Valeria Moraga's abstract draft with the dataset-B results and reliability analysis, structured
> to NMA's ABC…G; the **previous snapshot (2026-07-10)** is preserved **unchanged** below. Neither
> replaces the live editing surface — the shared
> [Google Doc](https://docs.google.com/document/d/1mRC-UZhOGJ_ovPqXBudEBEPUyIp_AzjkJqvoIsAyouk/edit)
> Abstract tab (drafted by Arefeh). The current proposal is offered for team discussion, not a decision.

## Current proposal — 2026-07-17 (merge: Valeria's draft + dataset-B results)

**Merge of Valeria Moraga's abstract draft** ([`sandbox/valeria/Abstract_v1.pdf`](../sandbox/valeria/Abstract_v1.pdf))
**and the 17 Jul dataset-B results**, structured to NMA's ABC…G (246 words). <u>Underlined</u> = added in
the merge; everything else is Valeria's prose, kept deliberately. Full rationale, authorship tiers and
the ABC…G check: [`sandbox/jaime/docs/05_abstract_proposal.md`](../sandbox/jaime/docs/05_abstract_proposal.md).

> Cognitive demands reconfigure the brain's functional connectivity, and working-memory load is a
> strong driver of this reorganisation. Whether that reconfiguration carries information about an
> individual's ability, beyond what connectivity already shows at low load, remains unclear.
> <u>We hypothesised that the change from low to high load would predict performance in unseen
> individuals, and that it would be captured by directional summaries of network integration and
> segregation.</u> Using Human Connectome Project N-back data from 336 participants, we estimated
> connectivity for each condition across 360 cortical regions grouped into 12 networks, defined
> reconfiguration as the difference between conditions, and summarised both as a 78-feature
> fingerprint. We predicted 2-back performance using cross-validated ridge regression against a
> permutation null. Task connectivity predicted performance out of sample (r ≈ 0.28), and so did the
> multivariate reconfiguration pattern (r ≈ 0.37; r ≈ 0.28 across independent runs). <u>The
> directional scalar summaries we expected to carry the effect did not (r ≈ 0.04). This
> pattern-versus-scalar dissociation is what difference-score reliability predicts: subtracting two
> highly correlated conditions removes the shared variance a single contrast depends on, while a
> multivariate model can still pool weak but consistent signal across edges.</u> Load-driven
> reconfiguration therefore carries individual predictive signal, but only when it is read as a
> distributed pattern. Much of that signal is trait-general, since low-load connectivity alone
> predicts nearly as well. <u>These task data cannot establish causality, and whether scalar
> reorganisation indices are simply too unreliable for individual prediction is directly testable
> with repeated sessions.</u>

**Status — proposal for team discussion, not a decision.** On 17 Jul Azman (Project TA) commented that
pattern-versus-scalar could read as a feature-count comparison rather than the *meaning* of
integration/segregation, and that the reliability argument may be over-weighted. That is one framing
comment, not a veto of the finding. At Monday's workshop the team will evaluate this wording against
the method, robustness checks and competing B→A-validation story, then retain, refine or replace it
based on the evidence. Goutham's read on the method is still pending — see the
[17 Jul minutes](../docs/meetings/2026-07-17.md).

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
