# Abstract (draft)

> **Historical snapshot — not a current team decision.** Captured from the shared
> [Google Doc](https://docs.google.com/document/d/1mRC-UZhOGJ_ovPqXBudEBEPUyIp_AzjkJqvoIsAyouk/edit)
> on **2026-07-10**, before Valeria Moraga's
> [research proposal](research-proposal.md). Preserve this text for provenance; edit the live Doc and
> create a new dated snapshot at the next agreed milestone. **Due Fri Jul 17 (W2D5).**

## Research question

> Does functional connectivity reconfigure between low and high working-memory load
> (0-back vs 2-back), and does this reconfiguration predict working-memory performance?

## Current draft

The human brain is one of the most complex biological systems, and its functional organization
can be characterized as a connectivity network using fMRI. Brain regions of interest (ROIs) are
nodes; functional interactions are edges. Graph theory provides a framework for quantifying the
topological properties of brain networks and how information is organized across distributed
neural systems.

A fundamental principle of brain network organization is the balance between functional
**segregation** (specialized local processing) and functional **integration** (communication
across distributed systems). Efficient cognition requires a dynamic balance between the two.
Alterations in this balance have been associated with differences in cognitive function.

Beyond intrinsic organization, cognitive demands can drive dynamic reconfiguration of functional
networks: during a task, connectivity is modulated to support task-specific requirements.

This study investigates (1) how functional segregation and integration differ across cognitive
load (0-back vs 2-back); (2) how intrinsic organization balances segregation and integration; and
(3) whether these network properties **predict individual working-memory performance**.

## Open flags recorded with this snapshot

See the [living project plan](../docs/project-plan.md#open-now) for current decisions.

- **Objective 2 (resting-state / intrinsic organization):** the task dataset has no clean resting
  state. Decide whether to drop objective 2, reframe it as a caveat, or use a different loader.
  Recommended narrowing: objectives **1 + 3** (task reconfiguration + prediction).
- **Concretize:** a single falsifiable hypothesis, the named prediction target (from `Stats.txt`),
  the graph metrics, and the prediction model — the abstract should read as a study, not a review.
- **Terminology:** use *low / high working-memory load* (standard), avoid vague wording.
