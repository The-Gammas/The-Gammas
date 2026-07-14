# References

Running bibliography, collected by the team. Annotations note why each is relevant.

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

- **Wang R. et al., Segregation, integration, and balance of large-scale resting brain networks
  configure different cognitive abilities** — *PNAS* 118(23), 2021.
  Balance of segregation/integration relates to cognitive ability. *(Resting-state — see the
  resting-state caveat in the [living project plan](../docs/project-plan.md#open-now).)*
  https://doi.org/10.1073/pnas.2022288118
- **Cohen & D'Esposito, The Segregation and Integration of Distinct Brain Networks and Their
  Relationship to Cognition** — *J. Neurosci.* 36(48):12083–12094, 2016.
  35 healthy adults (**not HCP**; the n-back had 0-/2-/3-back blocks, behavioural correlations on 3-back
  lures — **no 0→2-back contrast**). Task reconfiguration moved in opposite directions on the
  segregation↔integration axis: WM increased between-network **integration**, the motor task increased
  within-network **segregation**. Performance links differ by task: in WM greater integration predicted
  better accuracy; in motor greater segregation predicted *worse* (more variable) responding. Cite for
  the segregation-vs-integration idea, not as an HCP 0→2-back predicts-performance template.
  https://doi.org/10.1523/JNEUROSCI.2965-15.2016
- **Bassett & Sporns, Network neuroscience** — *Nature Neuroscience* 20(3):353–364, 2017.
  Foundational framing of the brain as a complex network.
- **Segregated Systems of Human Brain Networks** — *Trends in Cognitive Sciences*, 2017.
  Supports a network-level (rather than region-level) read of WM-related activity.
- **Sporns O., Network attributes for segregation and integration in the human brain** —
  *Current Opinion in Neurobiology* 23(2):162–171, 2013.
  Defines the segregation/integration attributes our graph metrics (step 4) operationalize.
  *(From the team's shared "Ideas" Doc — Literature Related tab.)*
  https://doi.org/10.1016/j.conb.2012.11.015
- **Ren S., Li J., Taya F., deSouza J., Thakor N.V., Bezerianos A., Dynamic Functional Segregation and
  Integration in Human Brain Network During Complex Tasks** — *IEEE Trans. Neural Syst. Rehabil. Eng.*
  25(5):547–556, 2017.
  Dynamic graph metrics of segregation/integration under task load; cited by the group as a
  **theoretical base, not applied directly**. *(From the shared "Ideas" Doc — Literature Related tab.)*
  https://ieeexplore.ieee.org/document/7563788/

## Load-dependent reconfiguration & WM performance

*Surfaced in **Valeria's proposal contribution** ([`sandbox/valeria/research-question-development.md`](../sandbox/valeria/research-question-development.md)); citations checked against PubMed (real papers, correct metadata) with a per-paper interpretation note. **Pending team discussion — not a team decision.***

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
- **Stevens A.A., Tappon S.C., Garg A., Fair D.A., Functional brain network modularity captures inter-
  and intra-individual variation in working memory capacity** — *PLoS ONE* 7(1):e30468, 2012.
  Modularity of a cognitive-control network tracks **both** between- and within-subject variation in
  visual short-term memory capacity. *(Caveat: resting-state, n=22, change-detection task — supports the
  theoretical claim, not our task-based HCP design.)*
  https://doi.org/10.1371/journal.pone.0030468

## Background / methods

- E. W. Lang et al., *Brain connectivity analysis: a short survey*, Comput. Intell. Neurosci., 2012.
- J. Bijsterbosch et al., *Challenges and future directions for representations of functional brain
  organization*, Nature Neurosci., 23(12):1484–1495, 2020.
- Puxeddu M.G. et al., *Leveraging multivariate information for community detection in functional
  brain networks*, Commun. Biol. 8(1):840, 2025.
- **Masharipov R., Knyazeva I., Korotkov A., Cherednichenko D., Kireev M., Comparison of whole-brain
  task-modulated functional connectivity methods for fMRI task connectomics** — *Communications Biology*
  7:1402, 2024.
  Ground-truth benchmark: **no gold standard** for whole-brain task-modulated FC, and methods (CorrDiff,
  sPPI/gPPI/cPPI, beta-series) disagree substantially; condition correlations are **inflated by
  co-activation** ("simultaneous activations without communication"). Backs guardrail #5 (coactivation ≠ FC).
  https://doi.org/10.1038/s42003-024-07088-3
