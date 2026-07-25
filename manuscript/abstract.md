# Abstract

The **submitted** text below is canonical and is never rewritten. Corrections to its numbers live in
[`../docs/final-report.md`](../docs/final-report.md); the flags after it say which ones the repo
reproduces.

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

**Provenance flags** ([`pipeline/04`](../pipeline/04_goutham_pipeline_reconciliation.ipynb), 21 Jul,
runs Goutham's functions verbatim on our data layer; three submitted numbers came from his Colab):

- **r ≈ 0.35 → canonical repeated-CV r ≈ 0.366** (his committed 0.2376 was a data-loading artifact);
  **r ≈ 0.28** is an ambiguous token — undifferenced whole-task FC = 0.278, 0-back alone = 0.274, so
  name the protocol.
- **ΔSegregation = −0.048** reconciles in direction only (drop 0-back → 2-back, paired t
  p = 3.45e-05); the magnitude is ≈ **−0.024** and the individual ΔSeg → accuracy link is weak
  (r ≈ −0.10, p = 0.05). Report segregation qualitatively, never as −0.048.
- **"complementary information beyond static FC"** is not supported by the current comparison
  ([nb08](../sandbox/jaime/08_activation_vs_reconfiguration.ipynb)): nested ΔR² = +0.034 (SD 0.022,
  under 2 SD), and a 360-region activation contrast predicts more strongly than the 78-feature FC
  summary (r ≈ 0.60 pooled). The representations are unmatched, so this establishes neither
  equivalence nor FC-specific predictive value.

</details>

## Citation keys in the submitted text

The `(1)`–`(5)` markers above are the reference list of the submitted PDF, which is **not** the
bibliography in [`references.md`](references.md). Only (2) has an entry there.

1. Shine JM et al., *The Dynamics of Functional Brain Networks: Integrated Network States during
   Cognitive Task Performance*, **Neuron** 92(2):544–554, 2016. doi:10.1016/j.neuron.2016.09.018
2. Finc K et al., *Dynamic reconfiguration of functional brain networks during working memory
   training*, **Nature Communications** 11(1):2435, 2020. doi:10.1038/s41467-020-15631-z —
   `references.md`, *Core anchors*.
3. Zhang H et al., *Static and dynamic functional connectome reveals reconfiguration profiles of
   whole-brain network across cognitive states*, **Network Neuroscience** 7(3):1034–1050, 2023.
   doi:10.1162/netn_a_00314
4. Shen X et al., *Using connectome-based predictive modeling to predict individual behavior from
   brain connectivity*, **Nature Protocols** 12(3):506–518, 2017. doi:10.1038/nprot.2016.178
5. Ray KL et al., *Dynamic reorganization of the frontal parietal network during cognitive control
   and episodic memory*, **Cognitive, Affective, & Behavioral Neuroscience** 20(1):76–90, 2020.
   doi:10.3758/s13415-019-00753-9

## History

Superseded versions are not kept here: the 21 Jul corrected draft (never resubmitted, and it retained
the non-reproducible −0.048), the two 20 Jul pre-submission working drafts, the 17 Jul merge version
and the 10 Jul snapshot are in git history. The merge that produced the submitted text is documented
in [`../docs/archive/2026-07-17_abstract-merge-rationale.md`](../docs/archive/2026-07-17_abstract-merge-rationale.md).
