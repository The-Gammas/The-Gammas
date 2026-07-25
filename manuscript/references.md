# References

Running bibliography, collected by the team. Annotations note why each is relevant.

> **Status:** evidence record, not a task tracker. The project closed at W3D5 (24 Jul 2026); the
> settled framing, the canonical numbers and the open threads are in
> [`docs/final-report.md`](../docs/final-report.md). The dated decision trail is
> [`docs/meetings/`](../docs/meetings/) and [`docs/archive/`](../docs/archive/).

## Core anchors

- **Flexible adaptation of task-positive brain networks predicts efficiency of evidence
  accumulation** — *Communications Biology*, 2024.
  Uses **HCP n-back** data; individual performance relates to flexible adaptation of task-positive
  networks across low/high WM load. **Closest to our design — anchor here.**
  https://www.nature.com/articles/s42003-024-06506-w
- **Finc et al., Dynamic reconfiguration of functional brain networks during working memory
  training** — *Nature Communications* 11, 2435 (2020).
  Functional networks reorganize during a WM task and change with training. Supports the broader
  idea of task-related network reconfiguration.
  https://www.nature.com/articles/s41467-020-15631-z

## Segregation / integration framework

- **Chan M.Y., Park D.C., Savalia N.K., Petersen S.E., Wig G.S., Decreased segregation of brain
  systems across the healthy adult lifespan** — *PNAS* 111(46):E4997–E5006, 2014.
  Origin of the graph-theoretic **system segregation** metric — a within/between-network edge-fraction
  balance, SS = (Bw − Bb)/Bw, **not** Newman modularity. Resting-state; segregation declines across the
  adult lifespan. Cite as the origin (paired with Calder 2026) for the single claim that resting system
  segregation is linked to cognition — the analogy our notebook draws for the 0-back baseline modularity,
  qualified because 0-back is task, not rest.
- **Calder C.N., Helmick C., Hashmi J.A., High brain network system segregation is differentially
  linked with cognitive performance across the life span** — *Network Neuroscience* 10(2):352–373, 2026.
  Life-span extension of Chan 2014: resting-state system segregation (Chan within/between edge-fraction
  SS on a Schaefer 200-ROI / 7-network parcellation, **not** Newman modularity), n=296 across 18–89 y.
  Higher SS links to better cognition, but the link is **age-dependent** — semantic in both age groups,
  executive only in older adults; effects small (rs ≈ 0.2–0.3), the band our baseline-modularity result
  (r ~0.18) sits inside. *(Caveat: resting-state, **not** an HCP 0→2-back template; our 0-back Newman
  modularity is only a task analogue, and Calder's age-dependence is itself why a young-adult-only effect
  need not match. Also reports adding SS gave no incremental predictive value over cognition — a direct
  parallel to our own no-incremental-value caveat (nb08, 21 Jul: reconfiguration does not clearly add
  over single-condition 0-back FC).)*
  https://doi.org/10.1162/NETN.a.542
- **Cohen & D'Esposito, The Segregation and Integration of Distinct Brain Networks and Their
  Relationship to Cognition** — *J. Neurosci.* 36(48):12083–12094, 2016.
  35 healthy adults (**not HCP**; the n-back had 0-/2-/3-back blocks, behavioural correlations on 3-back
  lures — **no 0→2-back contrast**). Task reconfiguration moved in opposite directions on the
  segregation↔integration axis: WM increased between-network **integration**, the motor task increased
  within-network **segregation**. Performance links differ by task: in WM greater integration predicted
  better accuracy; in motor greater segregation predicted *worse* (more variable) responding. Cite for
  the segregation-vs-integration idea, not as an HCP 0→2-back predicts-performance template.
  https://doi.org/10.1523/JNEUROSCI.2965-15.2016

## Load-dependent reconfiguration & WM performance

*Surfaced in **Valeria Moraga's proposal contribution**
([source transcription](../sandbox/valeria/research-question-development.md)) and integrated into the
NMA-structured [`research-proposal.md`](research-proposal.md). Citations are annotated below at the
claim level. **Pending team discussion — not a team decision.***

- **Cai W., Ryali S., Pasumarthy R., Talasila V., Menon V., Dynamic causal brain circuits during
  working memory and their functional controllability** — *Nature Communications* 12(1):3314, 2021.
  HCP n-back (**737 subjects**): directed interactions among salience, frontoparietal and default-mode
  networks differ between 0-back and 2-back; load-dependent network controllability. **Closest to our
  load contrast on the same dataset family.**
  https://doi.org/10.1038/s41467-021-23509-x
- **Stanley M.L., Dagenbach D., Lyday R.G., Burdette J.H., Laurienti P.J., Changes in global and
  regional modularity associated with increasing working memory load** — *Frontiers in Human
  Neuroscience* 8:954, 2014.
  Regional modularity changed significantly (DMN ↓ p=0.020, WMN ↑ p<0.001) while whole-brain modularity
  showed **no significant mean effect (p>0.37)** — a null result the authors attribute to limited power
  (**n=14**), not established invariance; global modularity did track individual performance change.
  Motivates reporting metrics at more than one scale. *(Caveats: n=14; contrast is 1→2-back, not 0→2-back.)*
  https://doi.org/10.3389/fnhum.2014.00954
- **Fransson P., Schiffler B.C., Thompson W.H., Brain network segregation and integration during an
  epoch-related working memory fMRI experiment** — *NeuroImage* 178:147–161, 2018.
  Time-varying FC + temporal-network analysis of the integration/segregation balance during a
  2-back / 0-back task. Supports a dynamic (not single-matrix) reading — useful as a stated limitation.
  https://doi.org/10.1016/j.neuroimage.2018.05.040
- **Taghia J., Cai W., Ryali S., Kochalka J., Nicholas J., Chen T., Menon V., Uncovering hidden brain
  state dynamics that regulate performance and decision-making during cognition** — *Nature
  Communications* 9:2505, 2018.
  HCP n-back: occupancy rates of latent brain states in the 2-back condition are used to **predict**
  2-back accuracy — the authors "applied the model on unseen data" (out-of-sample, between-subject
  framing; predicted-vs-actual p<0.001, replicated across two sessions). *(Caveat: the held-out scheme
  for this behavioural regression is under-specified in Methods, so strict leak-free between-subject
  prediction can't be verified from the text.)*
  https://doi.org/10.1038/s41467-018-04723-6
- **Murphy A.C., Bertolero M.A., Papadopoulos L., Lydon-Staley D.M., Bassett D.S., Multimodal network
  dynamics underpinning working memory** — *Nature Communications* 11:3035, 2020.
  HCP (644 subjects): working memory relies on **selective** integration — frontoparietal–default-mode
  cooperation correlates with *poorer* performance. Warns against a "more integration is always better" read.
  https://doi.org/10.1038/s41467-020-15541-0
- **Avery E.W., Yoo K., Rosenberg M.D. et al., Distributed patterns of functional connectivity predict
  working memory performance in novel healthy and memory-impaired individuals** — *Journal of Cognitive
  Neuroscience* 32(2):241–255, 2020.
  HCP N-back: predicts **2-back accuracy** out-of-sample from task FC at **r=0.36** (rest r=0.20) —
  **the closest same-task/target WM benchmark and our calibration anchor; our r≈0.37 is consistent
  with it** — a conceptual replication (their 10-fold-CV CPM vs our 5-fold RidgeCV over network
  summaries), not an exact replication. *[verified]*
  https://pmc.ncbi.nlm.nih.gov/articles/PMC8004893/

## Background / methods

- **Masharipov R., Knyazeva I., Korotkov A., Cherednichenko D., Kireev M., Comparison of whole-brain
  task-modulated functional connectivity methods for fMRI task connectomics** — *Communications Biology*
  7:1402, 2024.
  Ground-truth benchmark: **no gold standard** for whole-brain task-modulated FC, and methods (CorrDiff,
  sPPI/gPPI/cPPI, beta-series) disagree substantially; condition correlations are **inflated by
  co-activation** ("simultaneous activations without communication"). Backs guardrail #5 (coactivation ≠ FC).
  https://doi.org/10.1038/s42003-024-07088-3
- **Hedge C., Powell G., Sumner P., The reliability paradox: why robust cognitive tasks do not produce
  reliable individual differences** — *Behavior Research Methods* 50:1166–1186, 2018.
  Difference/contrast scores subtract away the true-score variance shared between conditions, leaving
  mostly error, so a robust within-subject contrast can have near-zero between-subject reliability,
  which severely attenuates (rather than logically precludes) prediction. In our earlier reading it bit the
  **scalar** reconfiguration summary — the 2bk−0bk integration index barely predicts (r≈0.04), and the
  raw difference features are low-reliability (feature-wise ~0.02 vs ~0.33 per condition) — but **not**
  the multivariate pattern, which still predicts out-of-sample (leakage-free cross-run r≈0.28) by
  aggregating weak-but-consistent signal across edges. *[verified]* *Refined by nb08 (21 Jul):
  the multivariate pattern does not clearly add over single-condition 0-back FC, while regional
  activation predicts more strongly under the current unmatched representations. The evidence does
  not establish FC-specific predictive value, so the pattern-vs-scalar dissociation is weaker than
  this gloss implies.*
  https://doi.org/10.3758/s13428-017-0935-1
- **Logothetis N.K., What we can do and what we cannot do with fMRI** — *Nature* 453:869–878, 2008.
  BOLD is a hemodynamic (blood-flow) proxy, not a direct measure of neural firing, and is confounded
  by vascular variables. Backs the vascular-reactivity (CVR) caveat on the regional-activation
  benchmark (nb08 / `pipeline/02` §7): raised by Goutham Arcod (22 Jul, Discord); DVARS and acc_0bk
  control motion and ability only, not CVR, and the current dataset has no CVR proxy.
- **CVR reliability reference — pending full citation.** Shared by Goutham Arcod (22 Jul, Discord) as
  "Reliable quantification of BOLD fMRI cerebrovascular reactivity (CVR) and resting-state amplitude,"
  no author/year/journal given yet. Get the full citation from Goutham before replacing this entry.
