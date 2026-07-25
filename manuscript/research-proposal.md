# Research proposal — synthesis for team review

> **Status:** proposal for team discussion, **not an accepted project decision**. It stays the
> attributable source of the original hypothesis; the cohorts, the tested method, the settled
> framing and the open threads are in the [final report](../docs/final-report.md), which
> supersedes Step 4's predictive extension without touching the proposal's attribution.
>
> **Source contribution:** Valeria Moraga, *Research Question Development*, received via Discord
> ([source PDF](../sandbox/valeria/research-question-development.pdf) ·
> [repository transcription](../sandbox/valeria/research-question-development.md)).
>
> **Editorial scope:** This document condenses Valeria's analysis into the
> [four-step NMA W2D1 framework](https://compneuro.neuromatch.io/tutorials/W2D1_ModelingPractice/student/W2D1_Tutorial1.html)
> and adds claim-level qualifications already documented in the project bibliography.
> The source files remain unchanged and are the authoritative record of her contribution.

This synthesis gives the team a compact object to review. Statements below describe **proposed**
questions, hypotheses and methods unless the [final report](../docs/final-report.md) records
them as accepted decisions.

## Step 1 — Phenomenon and research question

### Phenomenon

Working memory depends on coordinated activity across distributed brain systems. Increasing demand
from the active low-load **0-back** condition to the high-load **2-back** condition may reorganize
functional relationships among large-scale cortical networks, altering the balance between
within-network specialization and cross-network communication.

### Proposed primary question

> Does whole-brain functional connectivity reconfigure between low and high working-memory load,
> and are individual differences in this reconfiguration associated with 2-back performance?

This wording supports paired condition comparisons and in-sample brain–behaviour association. The
stronger verb **predicts** should be used only if performance is estimated for held-out participants.
Under that extension, the question becomes:

> Can prespecified features of 0-back-to-2-back functional reconfiguration predict 2-back
> performance in participants not used to fit the model?

### Operational subquestions

1. Do functional-connectivity patterns differ between 0-back and 2-back?
2. Do prespecified measures of functional integration and segregation differ between conditions?
3. Is subject-level reconfiguration associated with 2-back performance?
4. If a leak-free held-out analysis is implemented, does reconfiguration improve prediction over a
   simple behavioural baseline?

The proposed conceptual sequence is **load → estimated functional connectivity → network
organization → behavioural performance**. It organizes the analysis; it is not itself a causal
model.

## Step 2 — State of the art and scientific gap

Large-scale functional networks reconfigure with cognitive demand, but the direction and behavioural
meaning of that reconfiguration depend on task and network. Cohen and D'Esposito reported greater
integration during working memory and a positive association between integration and 3-back
accuracy; in their motor task, greater segregation was associated with *worse*, more variable
performance. Stanley and colleagues found regional changes in modularity but no significant mean
whole-brain modularity effect in a small sample. These results motivate multiscale analysis rather
than a universal “more integration is better” account.

Evidence from HCP working-memory data is convergent but methodologically heterogeneous. Cai and
colleagues identified load-dependent **directed** interactions among selected salience,
frontoparietal and default-mode nodes; this supports the load contrast but does not directly validate
whole-brain Pearson connectivity or undirected graph measures. Taghia and colleagues related latent
brain-state occupancy to 2-back accuracy, although the behavioural held-out scheme is not described
well enough to serve as a complete leak-free template. Murphy and colleagues further showed that
working-memory performance depends on selective, not uniformly greater, integration. See the
[annotated bibliography](references.md) for study-specific scope and limitations.

There is also an estimand problem. Condition-specific correlations may combine genuine changes in
coupling with shared task-evoked responses; available task-modulated FC methods can yield materially
different answers. Therefore, blockwise Pearson correlations are defensible as an exploratory
starting point only when this limitation is explicit and the team prespecifies how task-evoked
activity will be handled.

### Defensible gap and contribution

Load-dependent network reconfiguration is already established. The proposed contribution is a
focused replication and extension:

> Reproduce load-dependent changes in functional network organization in the available HCP sample,
> then test whether individual variability in prespecified whole-brain and network-specific changes
> is behaviourally meaningful.

This framing asks whether global integration and segregation summarize the relevant variation, or
whether selected network-to-network interactions provide a more informative description. It does
not claim discovery of task-related reconfiguration.

## Step 3 — Basic ingredients

| Component | Proposed operationalization | Status requiring team review |
|---|---|---|
| Participants | Subjects meeting prespecified signal, event and behavioural completeness criteria | Final dataset and analytic cohort |
| Conditions | Active low-load 0-back and high-load 2-back; LR and RL runs retained for QC | Run combination and reliability rule |
| Regional signals | Glasser 360 regional BOLD time series indexed by HCP event files | HRF/transition handling |
| Connectivity | One matrix per participant and condition | Primary FC estimator and task-evoked-response strategy |
| Reconfiguration | Prespecified matrix distance and/or change in one graph property | Primary definition |
| Graphs | Weighted, undirected candidates | Signed weights, self-edges, thresholding and density robustness |
| Behaviour | Validated 2-back performance measure | `acc_2bk` versus validated d′ |
| Evaluation | Paired condition tests, brain–behaviour association and optional held-out prediction | Inferential model, covariates and CV scheme |

For participant $i$, region pair $(r,s)$ and condition $c \in \{0B,2B\}$, an exploratory
condition-specific estimate is

$$
C_{i,c}(r,s)=\operatorname{corr}\left[x_{irc}(t),x_{isc}(t)\right].
$$

Two complementary definitions of reconfiguration are proposed:

$$
R_i=d\left(C_{i,2B},C_{i,0B}\right),
\qquad
\Delta M_i=M_{i,2B}-M_{i,0B},
$$

where $d$ is a prespecified matrix distance and $M$ is one prespecified network measure. The
first captures whole-pattern change; the second is easier to interpret.

### Candidate network measures

**System segregation** is proposed as an interpretable candidate:

$$
S_{i,c}=\frac{W_{i,c}-B_{i,c}}{W_{i,c}},
$$

where $W$ and $B$ are mean within- and between-system connectivity. Before use, the team must
define Fisher transformation, system membership, treatment of negative edges and behaviour when
$W$ approaches zero.

**Global efficiency** is a candidate integration measure, not yet an operational definition. It
cannot be applied directly to signed correlations: the analysis must first define a reproducible
weight-to-length transformation and rules for negative, zero and disconnected edges. Modularity and
participation coefficient are possible secondary measures, not additional defaults.

### Behaviour and covariates

The primary outcome should be selected before inspecting brain–behaviour results. D-prime is a
candidate only if hit and false-alarm rates come from validated fields or trials and an extreme-rate
correction is prespecified. Otherwise, **2-back accuracy** is the defensible primary outcome;
reaction time remains secondary.

Motion, usable timepoints, run or phase-encoding direction and other covariates should be included
only when available and scientifically justified. Age and sex must not be implied if the selected NMA
package does not provide validated values. In predictive analyses, scaling, feature selection and
confound regression must occur inside cross-validation.

### Methodological guardrails

- **Task coactivation:** simple blockwise correlations may mix coupling with shared evoked activity;
  treat them as exploratory unless an explicit task-modulated FC strategy is selected.
- **Hemodynamic timing:** define whether event windows are shifted, convolved with an HRF, modelled
  through a GLM or trimmed at transitions.
- **Reliability:** report usable frames and LR/RL agreement before relating FC or graph metrics to
  behaviour.
- **Graph construction:** prespecify signed-weight, self-edge and threshold policies before
  calculating topology.
- **Network labels:** use the atlas label **Cingulo-Opercular**. A relationship to the salience
  network requires an explicit ROI/network crosswalk; the labels are not interchangeable by default.
- **Data leakage:** split by participant; keep every data-driven transformation inside the training
  procedure and reserve the held-out set for final evaluation.

## Step 4 — Proposed hypotheses

### Primary inferential hypothesis

The most conservative primary hypothesis is non-directional:

$$
H_3:\operatorname{corr}(R_i,P_i)\neq 0,
$$

where $R_i$ is the prespecified reconfiguration measure and $P_i$ is the validated 2-back
outcome. A covariate-adjusted regression is an alternative implementation of the same associational
question.

### Secondary directional hypotheses

Valeria proposes two literature-motivated paired hypotheses:

$$
H_1:\mathbb{E}[E_{2B}-E_{0B}]>0,
\qquad
H_2:\mathbb{E}[S_{2B}-S_{0B}]<0.
$$

These should remain secondary until the integration and segregation metrics are operationally fixed.
Prior work does not support treating uniformly greater integration as universally adaptive.

### Predictive extension

If the team retains prediction as the project endpoint, the operational claim is not a significant
correlation but improved generalization:

$$
\operatorname{MAE}_{\mathrm{held\text{-}out}}(f_{\Delta FC})
<
\operatorname{MAE}_{\mathrm{held\text{-}out}}(f_{\mathrm{baseline}}).
$$

Participants used for evaluation must be absent from fitting, feature selection, scaling and
confound estimation. Out-of-sample $R^2$, permutation testing and uncertainty across folds may be
reported alongside MAE.

## Provenance and attribution

The underlying research framing, literature synthesis, candidate ingredients, mathematical
hypotheses and project-improvement recommendations were contributed by **Valeria Moraga** in
*Research Question Development*. This document is an editorial condensation for team review; it
does not replace or modify her [original PDF](../sandbox/valeria/research-question-development.pdf)
or [repository transcription](../sandbox/valeria/research-question-development.md). Scientific
qualifications are traceable through the [annotated bibliography](references.md). Subsequent team
decisions should be attributed through meeting notes and the living project plan.
