# Abstract

> **How to read this file.** Every version of the abstract is kept here, newest first, each inside a
> collapsible block so the file stays short. The **submitted** version is canonical (open by default).
> The **21 Jul corrected draft** reflects the activation re-check
> ([nb08](../sandbox/jaime/08_activation_vs_reconfiguration.ipynb)); it is offered for the W3D5
> presentation and team discussion and was **not** resubmitted (NMA does not grade the abstract).
> Click a triangle to expand.

---

<details open>
<summary><b>✅ SUBMITTED — 20 Jul 2026, 22:12 (final, via Airtable/PDF)</b></summary>

> **The abstract deliverable is closed.** The team merged the graph-theory result and Goutham's FC
> number into a longer version late on W3D1 and submitted it. NMA states the abstract is *not
> evaluated*; the focus now moves to the **W3D5 presentation (Fri 24 Jul)**.
>
> **Title:** *Adaptive Functional Network Reconfiguration for Predicting Individual Working-Memory
> Performance* (Valeria softened "Predicts" → "for Predicting" to avoid a direct affirmation).
> **Authors (5):** Valeria Moraga · Kerem Akyurt · Goutham Arcod · Jaime Alonso Pineda Moreno · Arefeh
> Lali Dehaghi. *(Pratik is not on the author list.)*

**Submitted text (Valeria, 21:17 — about 308 words, over the team's 250 guide but NMA sets no limit)**

> Cognitive performance depends on the ability of large-scale brain networks to dynamically
> reorganize their functional architecture in response to changing task demands (5). Functional
> connectivity (FC) derived from fMRI provides a framework for characterizing whole-brain network
> organization. Graph-theoretical approaches describe this organization through the complementary
> principles of functional segregation, which supports specialized processing within distributed
> systems, and functional integration enables communication across large-scale networks (1).
> Although static patterns of FC have been associated with cognitive ability, it remains unclear
> whether adaptive network reconfiguration provides additional information about individual
> differences in working-memory performance beyond connectivity observed within a single task
> condition (3,4). Working-memory provides an ideal framework for investigating adaptive network
> reorganization because increasing cognitive load requires coordinated changes in interactions
> within and between functional systems (2,5). Here, we examined whether functional-connectivity
> reconfiguration between low (0-back) and high (2-back) working-memory load predicts individual
> performance in unseen participants. Using HCP data from 336 participants, FC was estimated across
> 360 cortical regions grouped into 12 functional networks. Whole-brain connectivity was summarized
> into a 78-feature connectivity fingerprint (12 within-network and 66 between-network
> interactions), and load-dependent reconfiguration was quantified as the difference between 2-back
> and 0-back connectivity. Predictive performance was evaluated using cross-validated ridge
> regression, while graph-theoretical system segregation was used to characterize global network
> reorganization. Results indicate that both condition-specific connectivity and load-dependent
> reconfiguration predict 2-back performance in unseen individuals. The multivariate reconfiguration
> fingerprint significantly predicted task accuracy (r ≈ 0.35, p < 0.0001), while condition-specific
> connectivity also demonstrated predictive performance (r ≈ 0.28). Graph-theoretical analysis
> revealed a significant reduction in global system segregation from 0-back to 2-back
> (ΔSegregation = −0.048, p < 0.005), consistent with increased cross-network communication under
> higher cognitive load. These findings suggest that successful working-memory performance is
> associated with distributed reconfiguration of within- and between-network connectivity and that
> adaptive transitions from more segregated toward more integrated network organization provide
> complementary information beyond static FC.

**Provenance flags for the presentation (updated 21 Jul; [nb09](../sandbox/jaime/09_goutham_pipeline_replication.ipynb) now reconciles Goutham's pipeline on `main`)**

At submission (20 Jul) three of the submitted numbers came from Goutham's Colab and were not
reproducible from the repo. nb09 (21 Jul) runs his functions verbatim on our data layer and reconciles
them:

| Claim in the abstract | Status vs repo |
|---|---|
| fingerprint **r ≈ 0.35, p < 0.0001** | **Reconciled.** His committed 0.2376 was a data-loading artifact; nb09 reproduces **repeated-CV r ≈ 0.366** / 0.405 single-seed on our data. Present the canonical **r ≈ 0.366** and state which CV. |
| condition-specific **r ≈ 0.28** | Still the ambiguous token: undifferenced whole-task FC = 0.278 (nb04 c18), 0-back alone = 0.274 (c31). Name the protocol on the slide. |
| **ΔSegregation = −0.048, p < 0.005** | **Reconciled in direction, not magnitude.** nb09 reproduces the drop 0-back → 2-back (paired t p = 3.45e-05) but the magnitude is ≈ **−0.024**, not −0.048, and the individual ΔSeg → accuracy link is weak (r ≈ −0.10, p = 0.05). Present segregation qualitatively, not as −0.048. |
| *"complementary information beyond static FC"* | **Now tested ([nb08](../sandbox/jaime/08_activation_vs_reconfiguration.ipynb), 21 Jul): the claim is not supported by the current comparison.** Nested, same-fold: reconfiguration over 0-back FC gives ΔR² = +0.034 (sd 0.023, under 2 sd), and 0-back + reconfiguration (r 0.333) is not better than reconfiguration alone (0.366). A 360-region **activation** contrast (2bk−0bk) predicts more strongly than the 78-feature network FC summary (**r 0.60** pooled, ≈0.48 across held-out people and runs, partial\|acc_0bk 0.41, perm p ≈ 0.001 corrected null), while adding FC shows no clear gain (ΔR² −0.003). Because the representations are unmatched and per-run centering couples baseline and contrast, this does not establish either biological equivalence or FC-specific predictive value. Team decision for W3D5. |

</details>

---

<details>
<summary><b>📝 Our corrected draft — 21 Jul (reflects nb08; not resubmitted)</b></summary>

> **What this is.** The submitted abstract's closing overstates the evidence: *"complementary
> information beyond static FC"* was never tested before submission, and the 21 Jul re-check does not
> support it. Below is the submitted text with **our changes marked in bold**. The bold is a change
> marker, not emphasis: a clean version drops it, since the [writing guide](writing-guide.md) bars
> typographic emphasis in the final abstract. Offered for the presentation framing and team
> discussion, not resubmitted.

> Cognitive performance depends on the ability of large-scale brain networks to dynamically
> reorganize their functional architecture in response to changing task demands (5). Functional
> connectivity (FC) derived from fMRI provides a framework for characterizing whole-brain network
> organization. Graph-theoretical approaches describe this organization through the complementary
> principles of functional segregation, which supports specialized processing within distributed
> systems, and functional integration enables communication across large-scale networks (1).
> Although static patterns of FC have been associated with cognitive ability, it remains unclear
> whether adaptive network reconfiguration provides additional information about individual
> differences in working-memory performance beyond connectivity observed within a single task
> condition (3,4). Working-memory provides an ideal framework for investigating adaptive network
> reorganization because increasing cognitive load requires coordinated changes in interactions
> within and between functional systems (2,5). Here, we examined whether functional-connectivity
> reconfiguration between low (0-back) and high (2-back) working-memory load predicts individual
> performance in unseen participants. Using HCP data from 336 participants, FC was estimated across
> 360 cortical regions grouped into 12 functional networks. Whole-brain connectivity was summarized
> into a 78-feature connectivity fingerprint (12 within-network and 66 between-network
> interactions), and load-dependent reconfiguration was quantified as the difference between 2-back
> and 0-back connectivity. Predictive performance was evaluated using cross-validated ridge
> regression **against a permutation null**, while graph-theoretical system segregation was used to
> characterize global network reorganization. Results indicate that both condition-specific
> connectivity and load-dependent reconfiguration predict 2-back performance in unseen individuals.
> The multivariate reconfiguration fingerprint significantly predicted task accuracy
> (**r ≈ 0.37, p < 0.001**), while condition-specific connectivity also demonstrated predictive
> performance (r ≈ 0.28). Graph-theoretical
> analysis revealed a significant reduction in global system segregation from 0-back to 2-back
> (ΔSegregation = −0.048, p < 0.005), consistent with increased cross-network communication under
> higher cognitive load. **These findings show that individual working-memory performance can be
> predicted from distributed within- and between-network connectivity, and that global network
> organization shifts from segregation toward integration under higher load. Load reconfiguration,
> however, did not clearly add predictive information beyond single-condition (0-back) connectivity,
> and a regional task-activation contrast predicted more strongly under the current unmatched
> comparison (r ≈ 0.60). Load reconfiguration therefore remains a real predictor, but the current
> evidence does not establish connectivity-specific predictive value; the observational,
> single-task design does not support causal claims.**

**What changed vs the submitted text** (each marked in bold above)

| Change | Why |
|---|---|
| Methods: added **"against a permutation null"** | Names the success criterion the project set; the nulls were run (p < 0.001). |
| Results: **r ≈ 0.35, p < 0.0001 → r ≈ 0.37, p < 0.001** | Our reproducible repeated-CV number (nb04), not Goutham's single-split value. |
| Closing rewritten, dropping **"complementary information beyond static FC"** | Overclaim: [nb08](../sandbox/jaime/08_activation_vs_reconfiguration.ipynb) shows reconfiguration does not clearly add over 0-back FC (nested ΔR² +0.034, under 2 sd) and a task-activation contrast predicts better (r ≈ 0.60). The ΔR² itself stays out of the abstract body (a robustness stat belongs in Results per the writing guide). |
| Closing: added the limitation sentence (letter **G**), calibrated to "may" with no causal verdict | The submitted closing had no limitation; the design is observational and single-task. |

*Segregation, reconciled ([nb09](../sandbox/jaime/09_goutham_pipeline_replication.ipynb), 21 Jul):* the
draft keeps the submitted **−0.048** so it mirrors the sent text, but nb09 reproduces only the
**direction** (segregation drops 0-back → 2-back, paired t p = 3.45e-05); the magnitude is ≈ −0.024 and
the individual link is weak. For the presentation, report segregation qualitatively, not as −0.048.

</details>

---

<details>
<summary><b>Pre-submission working drafts (20 Jul, historical)</b></summary>

> Two working drafts circulated on 20 Jul before submission and are superseded by the **SUBMITTED**
> block above: proposed edits on the accepted version, then a line-by-line analysis of it. Both
> reproduced the same paragraphs with near-identical change tables. The corrections they tracked all
> reached the submitted or 21 Jul corrected text (hypothesis sentence added, 2-back target and
> permutation null named, the "0.28 to 0.37" range split into its two protocols, causal caveat added).
> Retained only as a record of that review.

</details>

---

<details>
<summary><b>Pending items (A to D), 20 Jul review (resolved post-submission)</b></summary>

> The A to D checklist (factual corrections, the group hypothesis choice, an incremental-connectivity
> analysis, out-of-scope items) guided the pre-submission review and is now moot. The abstract was
> submitted 20 Jul; the incremental test was run 21 Jul
> ([nb08](../sandbox/jaime/08_activation_vs_reconfiguration.ipynb): reconfiguration does not clearly
> add over 0-back FC, ΔR² = +0.034, and a task-activation contrast predicts better, r ≈ 0.60); the
> remaining framing choices belong to the W3D5 presentation.

</details>

---

<details>
<summary><b>History — 17 Jul proposal · 10 Jul snapshot</b></summary>

### Previous proposal — 2026-07-17 (merge: Valeria's draft + dataset-B results)

> **Superseded by the 20 Jul accepted version above.** Kept for the record. <u>Underlined</u> = added
> in the merge; the rest was Valeria's prose. Rationale:
> [`sandbox/jaime/docs/05_abstract_proposal.md`](../sandbox/jaime/docs/05_abstract_proposal.md).
>
> ⚠️ One sentence in this version is now known to be wrong and should not be reused: *"The directional
> scalar summaries we expected to carry the effect did not (r ≈ 0.04)"* generalises to a family what
> holds for one index — baseline modularity Q(0-back) predicts at r = +0.180, p = 9.3e-04 in the same
> notebook cell.

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

Context for this version: on 17 Jul Azman (Project TA) commented that pattern-versus-scalar could
read as a feature-count comparison rather than the *meaning* of integration/segregation, and that the
reliability argument may be over-weighted — see the [17 Jul minutes](../docs/meetings/2026-07-17.md).

### Previous snapshot — 2026-07-10 (preserved unchanged)

> **Historical snapshot — not a current team decision.** Captured from the shared Google Doc on
> **2026-07-10**, before Valeria Moraga's [research proposal](research-proposal.md).

#### Research question

> Does functional connectivity reconfigure between low and high working-memory load
> (0-back vs 2-back), and does this reconfiguration predict working-memory performance?

#### Draft

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

#### Open flags recorded with this snapshot

See the [living project plan](../docs/project-plan.md#open-now) for current decisions.

- **Objective 2 (resting-state / intrinsic organization):** the task dataset has no clean resting
  state. Decide whether to drop objective 2, reframe it as a caveat, or use a different loader.
  Recommended narrowing: objectives **1 + 3** (task reconfiguration + prediction).
- **Concretize:** a single falsifiable hypothesis, the named prediction target (from `Stats.txt`),
  the graph metrics, and the prediction model — the abstract should read as a study, not a review.
- **Terminology:** use *low / high working-memory load* (standard), avoid vague wording.

</details>
