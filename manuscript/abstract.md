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

**Provenance flags for the presentation (verified 20 Jul against `main`)**

Three claims in the submitted text are **not reproducible from the shared repo** and need Goutham's
code before they go on a slide unqualified:

| Claim in the abstract | Status vs repo |
|---|---|
| fingerprint **r ≈ 0.35, p < 0.0001** | Goutham's single 5-fold CV. Our canonical number is **repeated-CV r ≈ 0.366** (nb04 §4/§10). Consistent, but the slide should state which CV. |
| condition-specific **r ≈ 0.28** | Still the ambiguous token: undifferenced whole-task FC = 0.278 (nb04 c18), 0-back alone = 0.274 (c31). Name the protocol on the slide. |
| **ΔSegregation = −0.048, p < 0.005** | Goutham's **Chan-style system segregation**, computed in his Colab, **not in the repo**. nb04 (c30) has only **Newman modularity** (baseline 0-back r ≈ 0.18), flagged as a task *analogue*, not Chan SS. Cannot be reproduced from `main` yet. |
| *"complementary information beyond static FC"* | **Now tested ([nb08](../sandbox/jaime/08_activation_vs_reconfiguration.ipynb), 21 Jul): the claim is NOT supported.** Nested, same-fold: reconfig over 0-back FC gives ΔR² = +0.034 (sd 0.023, under 2 sd), and 0-back + reconfig (r 0.333) is *worse* than reconfig alone (0.366). A **regional activation** contrast (2bk−0bk) predicts far better (**r 0.60**, cross-run 0.53, partial\|acc_0bk 0.41, perm p 0.001) and **FC adds nothing over it** (ΔR² −0.003). The predictive signal is not connectivity-specific. Team decision for W3D5, see [W3D5 plan](../../W3D5_presentation_plan.md). |

</details>

---

<details>
<summary><b>📝 Our corrected draft — 21 Jul (reflects nb08; not resubmitted)</b></summary>

> **What this is.** The submitted abstract's closing overstates the evidence: *"complementary
> information beyond static FC"* was never tested before submission, and the 21 Jul re-check does not
> support it. Below is the submitted text with only the **closing revised** (in bold) to say what the
> data actually support. Offered for the presentation framing and team discussion, not resubmitted.

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
> regression against a permutation null, while graph-theoretical system segregation characterized
> global network reorganization. Results indicate that both condition-specific connectivity and
> load-dependent reconfiguration predict 2-back performance in unseen individuals. The multivariate
> reconfiguration fingerprint significantly predicted task accuracy (r ≈ 0.37, p < 0.001), while
> condition-specific connectivity also demonstrated predictive performance (r ≈ 0.28). Graph-theoretical
> analysis revealed a significant reduction in global system segregation from 0-back to 2-back
> (ΔSegregation = −0.048, p < 0.005), consistent with increased cross-network communication under
> higher cognitive load. **These findings show that individual working-memory performance can be
> predicted from distributed within- and between-network connectivity, and that global network
> organization shifts from segregation toward integration under higher load. On a nested, same-fold
> comparison, however, load reconfiguration did not clearly add predictive information beyond
> single-condition (0-back) connectivity (ΔR² = +0.03, under 2 sd), and a simpler task-activation
> contrast predicted performance at least as well (r ≈ 0.60). We therefore read load reconfiguration
> as a real but not connectivity-specific predictor of working-memory ability, and the observational
> design does not support causal claims.**

**What changed vs the submitted text**

| Change | Why |
|---|---|
| Closing "complementary information beyond static FC" → the bold revision | Overclaim. The incremental test was not run before submission; [nb08](../sandbox/jaime/08_activation_vs_reconfiguration.ipynb) shows ΔR² ≈ +0.03 (under 2 sd) and a simpler activation contrast (r ≈ 0.60) predicts at least as well. |
| fingerprint "r ≈ 0.35, p < 0.0001" → "r ≈ 0.37, p < 0.001" | Use our reproducible repeated-CV number (nb04) and the null we actually ran, rather than Goutham's single-split value. |
| "against a permutation null" added to methods | The nulls are complete (p < 0.001); naming the arbiter is honest and standard. |
| causal caveat added | The submitted closing had no limitation sentence; the design is observational. |

*Still not reproducible from `main`:* ΔSegregation = −0.048 (Goutham's Colab). Kept here as the team's
agreed graph result but flagged for the presentation until his code lands.

</details>

---

<details>
<summary><b>Working draft — 20 Jul (proposed edits on the accepted version)</b></summary>

> **Reading key.** **Bold** = a correction or addition applied now, because it is settled by evidence
> already in the repo and needs no group decision. *Italic* = left pending, because it depends on a
> team decision or on an analysis not yet run. Everything unmarked is Valeria's prose, untouched.
>
> Offered for the group, not applied to the shared Google Doc.

> The brain relies on a dynamic balance between functional segregation and integration,
> **reorganising connectivity** under varying cognitive demands. However, it remains unclear whether
> functional-connectivity reconfiguration between low and high working-memory loads predicts
> individual performance differences, and how this predictive value compares to connectivity patterns
> within single task conditions. **We hypothesised that individual differences in the multivariate
> change in connectivity from 0-back to 2-back would predict 2-back accuracy in held-out
> participants.**
>
> Using functional Magnetic Resonance Imaging (fMRI) data from 336 Human Connectome Project
> participants, **we evaluated** whether network reconfiguration from low (0-back) to high (2-back)
> working-memory load predicts **2-back accuracy** in unseen individuals. Connectivity across 360
> cortical regions—grouped into 12 networks—was summarized into 78 within- and between-network
> features. Reconfiguration was calculated as the feature-wise difference **between 2-back and
> 0-back**. Predictions were evaluated using cross-validated ridge regression **against a permutation
> null, with participants held out from every fitting step**.
>
> Preliminary evaluations show that undifferenced task connectivity predicts 2-back performance
> (**r ≈ 0.28, repeated cross-validation across participants**). Furthermore, multivariate
> reconfiguration patterns also successfully predict performance (**r ≈ 0.37; both exceeded the
> permutation null, p < 0.001**). *These distributed predictive patterns suggest that working-memory
> performance is driven by multiple network pairs rather than a uniform, global network
> reorganization.*
>
> Condition-specific connectivity contains **comparable** predictive information (**0-back alone,
> r ≈ 0.27**). Ongoing models will determine if reconfiguration contributes unique predictive variance
> beyond the connectivity already present during low-load states. *[pending — whether to report the
> directional-hypothesis result and the B→A external validation]* Due to the observational nature of
> the fMRI data, a causal relationship between network reconfiguration and cognitive performance
> cannot be established.

> ⚠️ **254 words — 4 over the team's 250 limit.** The overflow comes from the added hypothesis
> sentence, which now duplicates the methods sentence: both say *"predicts 2-back accuracy in
> held-out participants / unseen individuals"*. Cheapest fix, and it is my addition to pay for:
> drop *"2-back accuracy in unseen individuals"* from the methods sentence, since the hypothesis has
> already named the target and the holdout — that returns it to 248 without touching Valeria's other
> prose. Not applied here so the duplication stays visible for the group.

**What changed, and why**

| Edit | Reason | Source |
|---|---|---|
| "these networks" → **"reorganising connectivity"** | Segregation and integration are properties, not networks; the participle had no antecedent. | NMA Part 8.2 |
| **Hypothesis sentence added** | Letter C was missing entirely — NMA's minimum bar even without results. This is the *primary predictive* option, the one supported by data already in hand. | NMA Part 8.4; [research-proposal](research-proposal.md) Step 4 |
| "this study evaluates" → **"we evaluated"** | Matches the first person used elsewhere; past tense for what we did. | writing-guide |
| **"2-back accuracy"** named | Every r reported is `acc_2bk`; the target was never stated. | project-plan |
| "between conditions" → **"between 2-back and 0-back"** | Fixes the undefined sign, which is what carries the integration/segregation reading. | nb04 cell 4 |
| **"against a permutation null, with participants held out from every fitting step"** | Names the arbiter the project-plan sets as the success criterion, and states subject-level holdout. | nb04 cells 5, 10 |
| **Protocol attached to each r; the "0.28 to 0.37" range removed** | The range silently spanned two protocols. The cross-run 0.280 is dropped from this paragraph because it does not test unseen individuals (it trains and tests on the same 336 subjects, across runs) — keeping it under that framing was the misleading part. | nb04 cells 18, 21, 31 |
| **"p < 0.001" added** | The nulls are complete; reporting them replaces the claim that they are pending. | nb04 cell 10 |
| "substantial" → **"comparable … (0-back alone, r ≈ 0.27)"** | Replaces an unquantified qualifier with the number, which also sharpens the point: low-load connectivity alone is nearly as predictive. | nb04 cell 31 |
| *Removed:* "and will finalize statistical comparisons against permutation null models" | Factually superseded — the nulls are already run. | — |
| *Kept unchanged:* "Ongoing models will determine if reconfiguration contributes unique predictive variance..." | Correct as written. That comparison genuinely had not been run at the time; the existing `acc_0bk` control is behavioural, not a connectivity baseline. **Update: now run in [nb08](../sandbox/jaime/08_activation_vs_reconfiguration.ipynb) — the answer is "not clearly".** | nb04 cell 22 → nb08 |

</details>

---

<details>
<summary><b>Working analysis of the accepted draft — 20 Jul (pre-submission)</b></summary>

*214 words, 12 sentences, 4 paragraphs. Reference list kept in the Google Doc; per the
[writing guide](writing-guide.md) no author–year citations go in the abstract body.*

> The brain relies on a dynamic balance between functional segregation and integration, reconfiguring
> **these networks** under varying cognitive demands. However, it remains unclear whether
> functional-connectivity reconfiguration between low and high working-memory loads predicts
> individual performance differences, and how this predictive value compares to connectivity patterns
> within single task conditions.
>
> Using functional Magnetic Resonance Imaging (fMRI) data from 336 Human Connectome Project
> participants, **this study evaluates** whether network reconfiguration from low (0-back) to high
> (2-back) working-memory load predicts behavioral performance **in unseen individuals**. Connectivity
> across 360 cortical regions—grouped into 12 networks—was summarized into 78 within- and
> between-network features. Reconfiguration was calculated as the feature-wise difference **between
> conditions**. **Predictions were evaluated using cross-validated ridge regression.**
>
> Preliminary evaluations show that undifferenced task connectivity predicts 2-back performance
> (**r ≈ 0.28**). Furthermore, multivariate reconfiguration patterns also successfully predict
> performance (**r ≈ 0.28 to 0.37**). These distributed predictive patterns suggest that working-memory
> performance **is driven by multiple network pairs** rather than a uniform, global network
> reorganization.
>
> Condition-specific connectivity contains **substantial** predictive information. Ongoing models will
> determine if reconfiguration contributes unique predictive variance beyond the connectivity already
> present during low-load states, **and will finalize statistical comparisons against permutation null
> models**. Due to the observational nature of the fMRI data, a causal relationship between network
> reconfiguration and cognitive performance cannot be established.

**What each bold mark refers to**

| Passage | Issue | Source |
|---|---|---|
| "these networks" | Segregation and integration are organisational *properties*, not networks — the participle has no antecedent. | NMA Part 8.2 (flow/cohesion) |
| "this study evaluates" | Third person where the rest is first person; also the natural insertion point for the missing hypothesis (see A1). | — |
| "in unseen individuals" | Correct for the repeated-CV number, **not** for the cross-run number quoted two sentences later. See A3. | nb04 cell 21 |
| "between conditions" | Sign undefined. The pipeline is 2-back − 0-back, and the sign is what carries the integration/segregation reading. | nb04 cell 4 |
| "Predictions were evaluated using cross-validated ridge regression." | Names the estimator, omits the arbiter. Per [project-plan](../docs/project-plan.md) the success criterion is beating a permutation null, so the reader has no standard against which the next paragraph's r values mean anything. | project-plan |
| "r ≈ 0.28" (first) | Value correct — but unqualified, and 0.28 is indistinguishable from two other quantities in this abstract. See A2. | nb04 cell 18 |
| "r ≈ 0.28 to 0.37" | Reads as an uncertainty interval; it is actually two different evaluation protocols. See A2, A3. | nb04 cells 21, 31 |
| "is driven by multiple network pairs" | Causal phrasing on a correlational prediction, contradicting this abstract's own closing sentence; and no feature-importance or edge-level analysis was run, so "which pairs" was never measured. | writing-guide checklist; nb04 |
| "substantial" | An unquantified qualifier doing work a number should do. | NMA Part 8.4 (specificity) |
| "and will finalize statistical comparisons against permutation null models" | **Factually superseded** — the permutation nulls are already run. See A4. | nb04 cell 5, 10 |

> **Deliberately not marked:** *"Ongoing models will determine if reconfiguration contributes unique
> predictive variance beyond the connectivity already present during low-load states."* This clause is
> **correct as written** and should be kept. The comparison it describes — 0-back **connectivity**
> versus 0-back connectivity **plus** reconfiguration, on shared folds — had genuinely not been run.
> The existing `acc_0bk` control is a *behavioural* baseline (nb04 cell 22 labels it "general
> cognitive ability"), which answers a different question. See C1. **(Now run in nb08, 21 Jul.)**

</details>

---

<details>
<summary><b>Pending items (A–D) — retained as presentation guidance</b></summary>

### A. Factual corrections — evidence in hand, no group decision required

These are checkable against the notebooks; they are not matters of preference.

1. **The hypothesis (letter C) is absent.** The abstract goes A → B → D → E → F/G with no statement
   of what we expected. NMA Part 8.4 makes a clear, testable hypothesis "the minimum bar even without
   results", and Part 12.2 asks for directionality. We already have a directional hypothesis written
   in the *Hypothesis* tab of the Google Doc — it simply never reached the abstract.
2. **`0.28` is used for three different quantities.** Undifferenced whole-task FC = 0.278 ± 0.025
   (nb04 c18); cross-run reconfiguration = 0.280 (c21); 0-back alone = 0.274 ± 0.032 (c31). Each
   needs its protocol attached, and the "0.28 to 0.37" range should be split into its two protocols
   rather than hyphenated.
3. **The cross-run r does not test unseen individuals.** `_cross_run_r` (nb04 c21) trains on run 0
   fingerprints of all 336 subjects against `y_acc` and tests on run 1 of *the same* subjects against
   *the same* `y_acc`. It is leakage-free with respect to the **run** — which is what it was built
   for, as a reliability arbiter — but the model has seen every test subject's target. The numbers
   that do speak to unseen individuals are the subject-level repeated CV (0.366 ± 0.024, c31) and the
   B→A transfer (0.398, disjoint identities).
4. **The permutation nulls are already complete.** `perm_null()` refits on permuted targets, 1000
   permutations, (#exceed + 1)/(n + 1) estimator (Phipson & Smyth 2010); the main model gives
   p < 0.001 (nb04 c5, c10), and nb05 and nb06 carry their own. Describing them as pending
   understates finished work.
5. **The prediction target is never named.** Every r reported is `acc_2bk`. Two words.

### B. Group decisions — not for one person to settle

1. **Which hypothesis we declare.** Three options, with different consequences for F:
   (a) *predictive* — the multivariate reconfiguration pattern predicts `acc_2bk` in held-out
   participants (supported: 0.366 CV, 0.398 B→A);
   (b) *incremental* — reconfiguration improves on 0-back connectivity alone (this is exactly the
   open question in C1, **now answered by nb08: not clearly**);
   (c) *directional* — higher load shifts organisation toward integration and stronger shifters
   perform better (this is the recorded group hypothesis, and **its individual-differences half is
   not supported**: integration index r = +0.043, p = 0.43, c29).
   Adopting (c) means reporting honestly that it failed — which is a legitimate and interesting
   result, but it is the group's call, not an editorial fix.
2. **Whether the scalar null enters the abstract.** If (c) is declared, the r = 0.043 belongs in E.
   One caveat worth stating precisely: *not everything scalar fails.* Baseline modularity Q(0-back)
   does predict (r = +0.180, p = 9.3e-04), survives the behavioural control (partial | acc_0bk =
   +0.128) and its own null (p = 0.0005) — same cell 29. So any claim should name the specific index
   that was null, not the family.
3. **Whether the B→A external validation enters the abstract.** Train on 301 B-only subjects, predict
   100 held-out A subjects, disjoint identities: r = +0.398, permutation p < 0.001, bootstrap 95% CI
   [+0.250, +0.528] (nb05 c16). It is the strongest generalisation evidence we own and it appears in
   no draft. Abstract, or hold for the slides?
4. **"is driven by multiple network pairs".** The causal verb and the unmeasured specificity are
   both flagged above, but this is Valeria's sentence and the fix is hers or the group's to make.
5. **Whether integration/segregation stay in the opening.** They currently open the abstract, are
   never defined, and are never returned to. Either define them and report their test, or drop them
   and make the abstract purely about prediction. Azman's 17 Jul comment was precisely that these
   terms should carry their scientific meaning rather than serve as a label.

### C. Analysis that could close an open sentence — DONE (21 Jul)

1. **Incremental connectivity comparison — run.** Model A = 0-back FC; model B = 0-back FC +
   reconfiguration; same folds, same estimator, same scaler. Result in
   [nb08](../sandbox/jaime/08_activation_vs_reconfiguration.ipynb): reconfiguration does **not** clearly
   add over 0-back FC (ΔR² = +0.034, sd 0.023), and a task-activation contrast predicts far better
   (r ≈ 0.60) with FC adding nothing over it. Converts "ongoing models will determine" into a result.

### D. Explicitly out of scope for this abstract

- **Tangent-space representation.** nb06's own verdict is *postpone adoption*: it gains +0.198 r in
  internal CV but only +0.016 r in cross-cohort transfer, and with 100 external subjects the paired
  bootstrap cannot resolve differences below ~0.19 r. It is a methodological comparison, not a
  scientific claim, and it is not a group decision that has been taken.

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
