# Research Question Development

> Markdown transcription of Valeria's contribution, received via Discord.
> Source: [`Research Question Development.pdf`](Research%20Question%20Development.pdf)
>
> **Source record, preserved unchanged.** This captures Valeria's proposal at the time it was shared;
> it is not the current task tracker. Accepted results and open decisions live in the
> [project plan](../../docs/project-plan.md).

## Step 1. Identify the phenomenon and formulate the research question

### Phenomenon

Working memory depends on the coordinated activity of distributed brain systems rather than on isolated brain regions. As working-memory demands increase, the brain may reorganize its functional interactions to facilitate communication between task-relevant regions while maintaining sufficient specialization among large-scale networks.

The Human Connectome Project working-memory task includes a low-load 0-back condition and a higher-load 2-back condition. The contrast between these conditions provides an opportunity to investigate whether increasing working-memory load is accompanied by a reconfiguration of functional brain networks.

### Main research question

**Does whole-brain functional connectivity reconfigure between low and high working-memory load, and are individual differences in this reconfiguration associated with working-memory performance?**

### Operational subquestions

1. Do functional connectivity patterns differ between the 0-back and 2-back conditions?
2. Do graph-theoretical measures of network integration and segregation differ between these conditions?
3. Are individual differences in load-related network reconfiguration associated with behavioral performance during the 2-back condition?

The proposed conceptual pathway is:

> Working-memory load -> functional connectivity -> network integration and segregation -> behavioral performance.

## Step 2. Understand the state of the art

Previous studies indicate that large-scale functional brain networks dynamically reorganize in response to cognitive demands. Rather than producing a uniform increase in connectivity, cognitive tasks appear to modify the balance between functional integration, which supports communication across systems, and segregation, which preserves specialized processing within networks.

Cohen and D'Esposito reported that working-memory performance was associated with greater integration across functional networks, whereas motor performance was associated with greater network segregation. Their findings suggest that network reconfiguration is task-dependent and that increased integration can support working-memory performance.

Studies manipulating working-memory load have also shown that graph properties such as modularity and hub organization change as task demands increase. Stanley and colleagues found that global and regional properties were not affected identically by working-memory load, indicating that a single whole-brain metric may not fully describe the relevant reconfiguration. More recent work similarly describes decreases in network modularity as working-memory load increases, consistent with reduced segregation or increased cross-network interaction under more demanding conditions.

Evidence from the HCP working-memory task further supports load-dependent reconfiguration. Using data from 737 participants, Cai and colleagues found that directed interactions among salience, frontoparietal, and default-mode regions differed between the 0-back and 2-back conditions. They also identified load-dependent changes in network controllability and in the causal influence of specific regions. These findings demonstrate that high and low working-memory loads involve distinguishable network configurations.

Network dynamics have also been related to individual behavior. Fransson and colleagues used time-varying functional connectivity and temporal network analysis to examine the balance between integration and segregation during working memory, supporting the idea that behaviorally relevant changes may occur over the course of a task rather than being fully represented by one static connectivity matrix. Taghia and colleagues similarly found that properties of latent brain states during the 2-back condition predicted working-memory accuracy. In addition, previous research has shown that functional network modularity can account for both interindividual and intraindividual variation in working-memory capacity.

Nevertheless, the association between integration and performance is unlikely to follow a simple “more integration is always better” rule. In an HCP-based study, Murphy and colleagues showed that working memory was supported by coordinated multimodal network dynamics, while some interactions involving frontoparietal and default-mode systems were associated with poorer performance. This suggests that successful cognition may depend on selective integration among task-relevant systems, rather than on a nonspecific increase in global connectivity.

There is also an important methodological issue. Recent comparisons of task-modulated functional-connectivity methods demonstrate that different approaches can produce substantially different estimates of connectivity differences between 2-back and 0-back. In particular, correlations calculated from condition-specific timepoints can reflect both genuine changes in interregional coupling and shared task-evoked responses.

### Scientific gap

The existing literature therefore supports three conclusions:

1. Functional brain networks reconfigure during working-memory tasks.
2. Higher working-memory load often involves changes in integration, segregation, modularity, and hub organization.
3. Some of these network properties are associated with individual differences in performance.

Consequently, it would not be accurate to claim that load-dependent functional reconfiguration has not been studied. A more defensible gap is:

> Although previous research demonstrates load-dependent network reconfiguration, it remains unclear whether individual differences in whole-brain integration and segregation between the HCP 0-back and 2-back conditions reliably explain behavioral performance, and whether global graph measures capture behaviorally relevant changes beyond specific interactions among task-relevant networks.

The proposed study would therefore provide a focused replication and extension. It would test whether established observations of load-dependent network reconfiguration can be recovered in the available HCP dataset and determine whether subject-level changes in interpretable graph measures are associated with working-memory performance.

## Step 3. Determine the basic ingredients

### Participants

Let $i = 1, \ldots, N$ represent the participants included after applying predefined data-quality and behavioral-data criteria.

### Experimental condition

For each participant, working-memory load is represented by:

$$c \in \{0B, 2B\},$$

where $0B$ denotes the low-load 0-back condition and $2B$ denotes the high-load 2-back condition.

### Regional BOLD signals

For participant $i$, region $r$, and condition $c$, the regional BOLD time series is:

$$x_{irc}(t).$$

The HCP explanatory-variable files will be used to identify the blocks corresponding to each task condition. Condition assignment must account for the delayed hemodynamic response and the temporal structure of the task.

### Functional-connectivity matrices

For every participant and condition, functional connectivity between regions $r$ and $s$ will initially be estimated as:

$$C_{i,c}(r,s) = \operatorname{corr}\left(x_{irc}(t), x_{isc}(t)\right).$$

This produces two connectivity matrices per participant:

$$C_{i,0B} \quad \text{and} \quad C_{i,2B}.$$

A general measure of connectivity-pattern reconfiguration may be defined as the distance between these matrices:

$$R_i = d\left(C_{i,2B}, C_{i,0B}\right),$$

where $d(\cdot)$ could be a correlation distance or another prespecified matrix-distance measure.

### Graph representation

Each connectivity matrix will be represented as a graph:

$$G_{i,c} = (V, E_{i,c}),$$

where brain regions constitute the nodes $V$, and functional connections constitute the weighted edges $E_{i,c}$.

The analysis must prespecify:

- whether graphs are weighted or binary;
- whether negative connections are retained;
- how self-connections are treated;
- whether proportional thresholding is used;
- how results are tested for robustness across graph densities.

Weighted graphs may be preferable for the primary analysis because they preserve information and avoid dependence on one arbitrary threshold.

### Network segregation

A possible whole-brain segregation measure is:

$$S_{i,c} = \frac{W_{i,c} - B_{i,c}}{W_{i,c}},$$

where $W_{i,c}$ is the mean within-network connectivity and $B_{i,c}$ is the mean between-network connectivity.

Higher values indicate stronger separation between predefined functional networks.

Modularity may be considered as an alternative or complementary segregation measure:

$$Q_{i,c},$$

although the community definition and resolution parameter would need to be specified in advance.

### Network integration

Integration could be represented by global efficiency:

$$E_{i,c} = \frac{1}{K(K-1)} \sum_{r \ne s} \frac{1}{d_{rs}},$$

where $K$ is the number of brain regions and $d_{rs}$ is the shortest weighted path between regions $r$ and $s$.

Participation coefficient could provide a complementary measure of how strongly individual regions connect across network boundaries. However, the primary analysis should use a limited number of theoretically justified metrics rather than testing many correlated graph measures.

### Load-related reconfiguration

For each graph measure, the within-participant change will be calculated as:

$$\Delta S_i = S_{i,2B} - S_{i,0B},$$

$$\Delta E_i = E_{i,2B} - E_{i,0B}.$$

Therefore:

- $\Delta S_i < 0$ represents reduced segregation under high load;
- $\Delta E_i > 0$ represents increased integration under high load.

### Behavioral performance

A primary behavioral outcome must be defined before analysis. Possible measures include:

$$P_i = \text{2-back accuracy},$$

or, when target and nontarget responses are available:

$$P_i = d'_i = Z(\text{hit rate}_i) - Z(\text{false-alarm rate}_i).$$

A sensitivity measure such as $d'$ may distinguish task performance more effectively than raw accuracy because it accounts for both correct target detection and false alarms.

Reaction time may be retained as a secondary outcome, but it should not be combined with accuracy without a clearly justified procedure.

### Potential confounding variables

At minimum, the analysis should consider:

- head motion;
- age;
- sex, when scientifically justified;
- number of usable timepoints;
- run or phase-encoding direction;
- overall mean connectivity;
- task accuracy or compliance thresholds.

Head motion is particularly important because it can produce systematic changes in estimated functional connectivity and graph topology.

## Step 4. Formulate specific and mathematical hypotheses

### Hypothesis 1: working-memory load and integration

**Verbal hypothesis:** High working-memory load will be associated with greater whole-brain functional integration than low working-memory load.

$$H_1: \mathbb{E}[E_{2B} - E_{0B}] > 0.$$

The corresponding null hypothesis is:

$$H_{0,1}: \mathbb{E}[E_{2B} - E_{0B}] = 0.$$

### Hypothesis 2: working-memory load and segregation

**Verbal hypothesis:** High working-memory load will be associated with reduced whole-brain network segregation relative to low working-memory load.

$$H_2: \mathbb{E}[S_{2B} - S_{0B}] < 0.$$

The corresponding null hypothesis is:

$$H_{0,2}: \mathbb{E}[S_{2B} - S_{0B}] = 0.$$

Because the same participants complete both conditions, these hypotheses require paired within-participant comparisons.

### Hypothesis 3: reconfiguration and performance

**Verbal hypothesis:** Participants who show greater adaptive reconfiguration between the 0-back and 2-back conditions will demonstrate better 2-back performance.

A directional version based on integration is:

$$H_{3a}: \operatorname{corr}(\Delta E_i, P_i) > 0.$$

A directional version based on segregation is:

$$H_{3b}: \operatorname{corr}(\Delta S_i, P_i) < 0.$$

These relationships could be evaluated using regression:

$$P_i = \beta_0 + \beta_1 \Delta E_i + \boldsymbol{\gamma}^{\top} \mathbf{Z}_i + \varepsilon_i,$$

where $\mathbf{Z}_i$ contains prespecified confounding variables. The directional prediction is:

$$\beta_1 > 0.$$

A corresponding model can be constructed for segregation.

Because previous findings suggest that integration may be beneficial only for particular network combinations, the most conservative primary hypothesis is:

$$H_3: \operatorname{corr}(R_i, P_i) \ne 0,$$

where $R_i$ is a prespecified measure of reconfiguration. Directional hypotheses for global integration and segregation can then be treated as theoretically motivated secondary hypotheses.

## Suggestions for Improving the Project

### 1. Define the contribution as a replication and focused extension

The broad question of whether functional networks reconfigure during working memory has already been addressed. Therefore, the project should not claim to discover the phenomenon for the first time. A credible scientific contribution would be:

> To reproduce load-dependent changes in functional network organization in the available HCP sample and test whether individual differences in those changes explain behavioral performance.

The extension could involve comparing:

- global integration and segregation;
- specific between-network connections;
- absolute high-load organization versus within-subject change from low to high load.

This would make the contribution clear, feasible, and scientifically honest.

### 2. Select one primary graph measure for each concept

“Integration” and “segregation” are broad constructs that can be operationalized in several ways. Testing many metrics without a hierarchy would increase the number of statistical comparisons and make interpretation difficult.

The project should prespecify, for example:

- global efficiency as the primary integration measure;
- system segregation as the primary segregation measure;
- modularity and participation coefficient as secondary or robustness analyses.

The measures should be selected because they represent the hypotheses, not simply because they are available in a graph-analysis library.

### 3. Include a network-specific secondary analysis

The literature indicates that successful working memory may depend on selective communication among the frontoparietal, dorsal-attention, salience, visual, and default-mode systems. Therefore, global integration alone may hide important effects.

A manageable secondary analysis could estimate:

$$\Delta FC_i^{A,B} = FC_{i,2B}^{A,B} - FC_{i,0B}^{A,B}$$

for a small number of theoretically selected network pairs, such as:

- frontoparietal-dorsal attention;
- frontoparietal-visual;
- frontoparietal-default mode;
- salience-frontoparietal.

These comparisons should be selected from the literature before examining the behavioral results.

### 4. Define “reconfiguration” mathematically

The term should not remain conceptual. At least two definitions are possible:

**Change in a graph property**

$$\Delta M_i = M_{i,2B} - M_{i,0B}.$$

**Whole-pattern reconfiguration**

$$R_i = 1 - \operatorname{corr}\left[\operatorname{vec}(C_{i,0B}), \operatorname{vec}(C_{i,2B})\right].$$

The first is easier to interpret, while the second captures changes that may not be visible in a single global metric. One should be identified as the primary definition.

### 5. Avoid equating task coactivation with functional connectivity

Directly concatenating timepoints from 0-back and 2-back blocks and correlating regional signals is an understandable starting point, but shared task-evoked responses can inflate correlations.

The project should therefore consider at least one of the following:

- removing condition-evoked mean responses before calculating connectivity;
- using residual time series from a task GLM;
- beta-series correlation;
- generalized psychophysiological interaction analysis;
- presenting simple blockwise correlations as an exploratory measure and explicitly acknowledging the limitation.

The most appropriate option depends on the exact preprocessing and available data, and should be confirmed with the Project TA.

### 6. Account for the hemodynamic response

EV files identify when experimental events occurred, but BOLD responses are delayed and temporally blurred. Simply selecting scans whose acquisition times fall inside an EV interval may misassign part of the response.

The analysis should clearly specify whether it will:

- shift block timings by an approximate hemodynamic delay;
- convolve condition regressors with a hemodynamic response function;
- use a GLM-based method that models the response directly;
- remove transition timepoints between conditions.

### 7. Confirm the reliability of condition-specific connectivity

Each condition contains a limited number of timepoints. Connectivity estimates may therefore be noisy. Before conducting the main analysis, the project should report:

- the number of usable timepoints per participant and condition;
- whether both runs are combined;
- split-half or between-run reliability;
- sensitivity to motion censoring;
- whether the amount of data differs across participants.

A graph measure cannot reliably predict behavior if its underlying connectivity estimate is unstable.

### 8. Choose the behavioral variable before examining associations

The primary outcome should be specified in advance. A suitable order would be:

1. 2-back $d'$, when calculable;
2. 2-back accuracy;
3. median correct-response time as a secondary outcome.

Using several behavioral outcomes without correction would create an unclear hypothesis and increase false-positive risk.

### 9. Use appropriate statistical controls

The load effect should be evaluated using within-participant comparisons. Brain-behavior associations should include prespecified covariates, especially head motion.

For prediction rather than association, performance evaluation must be conducted out of sample:

$$\text{training participants} \cap \text{test participants} = \varnothing.$$

Feature selection, scaling, and confound regression must be performed inside the cross-validation procedure to prevent information leakage.

For a short project, an association analysis may be more realistic and interpretable than claiming behavioral prediction.

### 10. Distinguish association from prediction

A significant correlation between reconfiguration and performance establishes an association, not necessarily prediction.

The project should use:

- **associated with** when testing an in-sample correlation or regression;
- **predicts** only when performance is estimated for held-out participants using cross-validation.

Accordingly, the safest research question is:

> Does functional connectivity reconfigure between low and high working-memory load, and is the magnitude of this reconfiguration associated with working-memory performance?

The word “predict” should be retained only if a genuine out-of-sample predictive analysis is implemented.

### 11. Establish a minimal viable project

A feasible primary project would consist of:

1. one predefined parcellation;
2. one connectivity-estimation method;
3. one integration measure;
4. one segregation measure;
5. one primary behavioral outcome;
6. paired comparisons between conditions;
7. two brain-behavior association tests;
8. motion and robustness controls.

Network-specific and dynamic-connectivity analyses should be treated as extensions rather than requirements.

### 12. State the expected scientific contribution carefully

A suitable final contribution statement is:

> This study will test whether established load-dependent changes in functional network organization can be reproduced in the available HCP working-memory data and whether individual variability in these changes is behaviorally meaningful. By comparing global graph measures with selected network-specific interactions, the study will also evaluate whether whole-brain integration and segregation provide sufficient descriptions of adaptive working-memory reconfiguration.

This formulation is specific, testable, and appropriately situated within previous research.
