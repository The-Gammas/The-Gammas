# Abstract: merge proposal

> **SUPERSEDED by nb08 (21 Jul).** The predictive signal is NOT specific to reconfiguration; a
> task-activation contrast (2bk-0bk mean BOLD) predicts better (r ~ 0.60); per-run centering shows it
> is not a load-independent trait. The "pattern-versus-scalar dissociation" and "trait-general"
> framing in the body below is refined or reversed by that re-check. The body is kept unchanged as the
> historical pre-workshop record (its value is the merge rationale and the three-tier authorship
> table). Headline notebook: [`08_activation_vs_reconfiguration.ipynb`](../08_activation_vs_reconfiguration.ipynb).

**Author:** Jaime Pineda · **Version:** v2 · **Date:** 2026-07-17 · **Status:** proposal for group
review, not a team decision, and not a replacement for the shared Google Doc.

> **Status update, 18 Jul:** preserved as the pre-workshop merge. The cohort discrepancy noted below
> is resolved (B = primary analysis, A = external validation). The scientific framing is still open:
> Azman questioned whether "pattern vs scalar" communicates scientific meaning and suggested
> considering external validation as the headline. This is feedback, not a veto; the team will retain,
> refine or replace the framing according to the method and evidence. See the
> [living plan](../../../docs/project-plan.md).

**Question it answers:** can Valeria's corrected draft and the 17 Jul results draft be merged into one
abstract that meets NMA's required structure inside the word limit?

**Short answer:** yes, because they are different genres rather than rival drafts. Her paragraphs 1 to
3 are an Introduction; the results draft is an abstract missing two required components. Merged below
at 246 words.

**Changelog**

- **v2 (17 Jul):** removed em dashes throughout (house style, see note at the end). Marked with
  <u>underline</u> what is new in this merge versus Valeria's draft, so the additions can be shown
  and defended.
- **v1 (17 Jul):** first merge.

---

## What this is based on

| Source | What it contributed |
|---|---|
| [`sandbox/valeria/Abstract_v1.pdf`](../../valeria/Abstract_v1.pdf) (Valeria Moraga, 17 Jul, via Discord) | The corrected prose, the neutral register, the methods sentences, the trait caveat, and the bibliography. Her §3 opener is the seed of **A**, and her closing question of §3 is **B** almost verbatim |
| [`manuscript/abstract.md`](../../../manuscript/abstract.md), current proposal, 17 Jul | The results, the numbers, and the difference-score mechanism |
| [`04_goutham_pipeline_on_B.ipynb`](../04_goutham_pipeline_on_B.ipynb) | Every number below. Goutham's FC pipeline on dataset B, with one p-value detail noted in the notebook |
| NMA [`projects/docs/project_guidance.md`](../../../../../../official/course-content/nma_course_content/projects/docs/project_guidance.md) and [`TrainIllusionDataProject.ipynb`](../../../../../../official/course-content/nma_course_content/projects/modelingsteps/TrainIllusionDataProject.ipynb) Step 10 | The **ABC…G** structure, which is canonical, and the reason C and G are now present |
| [`manuscript/writing-guide.md`](../../../manuscript/writing-guide.md) | The 150 to 250 word limit, no citations in the body, tense and flow rules |
| The 10 Jul snapshot in [`manuscript/abstract.md`](../../../manuscript/abstract.md) | The team's **original** segregation and integration framing, which is what makes C honest |

Bibliography is **not duplicated here**, see [`manuscript/references.md`](../../../manuscript/references.md).
Valeria's refs 6 (Calder 2026) and 7 (Finc 2020) were folded into the team bibliography on 17 July.
Finc is close enough to our topic that it still deserves a full team read before the abstract lock.

---

## The proposed abstract

<u>Underlined</u> = new in this merge. Everything else is Valeria's, kept deliberately.

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

**Verified against the checklist:** 246 words (limit 250, close to the ceiling, so any addition needs
a deletion), 11 sentences, longest sentence 37 words, no citations in the body, no typographic
emphasis, no em dashes. Marked and clean versions verified identical by script.

**Clean version for pasting** (no markup) is at the end of this file.

---

## Three tiers of authorship, so nothing is overclaimed

This matters if the marked-up version gets shown to the group. Not everything that is new to
Valeria's draft is *ours*; some of it is the team's from before she wrote.

| Tier | Content | Whose |
|---|---|---|
| **Kept from Valeria** | The phenomenon opener, the question, the methods sentences, the findings, the trait caveat, the bibliography | Valeria's, and it is most of the text |
| **New in this merge** | **C** (the hypothesis), the scalar null tied back to C, the difference-score mechanism, **G** (limitations and future) | Partly recovered, partly written here. See below |
| **Recovered, not invented** | The hypothesis in C comes from the team's own 10 Jul segregation and integration framing. The difference-score mechanism was in the 17 Jul results draft and Valeria cut it for space, understandably | The team's. **Do not present this as new thinking** |

Honest summary to give the group: *the merge adds two structurally required components that neither
draft had (C and G), and restores one explanation that was cut for space. The prose is Valeria's.*

---

## What actually differentiates us from Avery

This is a different axis from the one above, and worth keeping separate. Avery et al. 2020 ran CPM on
HCP predicting 2-back performance in held-out subjects. Same dataset, same task, same target.

| Element | In Avery? | Ours? |
|---|---|---|
| Predicting 2-back from FC in held-out subjects | Yes | Conceptual replication, r ≈ 0.28 vs their 0.36 |
| **0-back to 2-back reconfiguration as the predictor** | Not framed explicitly | **Yes.** The team's framing since 10 Jul, not new today |
| **Pattern versus scalar dissociation** | No | **Yes.** This is the finding |
| **Difference-score reliability as the explanation** | No | **Yes.** This is the contribution |
| Stating the trait-general caveat openly | Partly | Yes, via Valeria |

So the differentiator is the last three rows, and two of them are exactly what the underlined text
restores or adds. That is the argument for keeping them in despite the word budget: **without C, G and
the mechanism, we are a weaker replication of a six-year-old paper.** With them, we are answering a
question Avery did not ask.

---

## ABC…G check

| | Component | Where | Was it in the inputs? |
|---|---|---|---|
| **A** | Phenomenon | Sentence 1 | Valeria had it buried in §3; the results draft was missing it |
| **B** | Question | Sentence 2 | Both had it. Valeria's wording |
| **C** | Hypothesis | Sentence 3 | **Neither had it.** Recovered from the 10 Jul framing |
| **D** | How | Sentences 4 and 5 | Both had it. Valeria's wording |
| **E** | Findings | Sentences 6 and 7 | Both had the positives; the scalar null is sharpened here |
| **F** | Conclusion within limits | Sentences 9 and 10 | Both had it, now stated against C |
| **G** | Limitations and future | Sentences 11 and 12 | **Neither had it** |

**Why C matters more than it looks.** Stating the hypothesis we actually started with, that
reorganisation would show up in directional integration and segregation summaries, turns the abstract
from "we found an odd dissociation" into "we predicted X, X failed, and we know why". That is a
falsifiable arc, it is honest about our own history, and it is what the Project TA asked for. The
scalar result stops being a disappointing null and becomes the finding.

---

## What was cut from each input, and why

**From Valeria's draft, cut 279 words of general context.** Paragraphs 1 to 3 (brain complexity, graph
theory, segregation and integration, biomarkers) are 67% of her text and all of it precedes our
contribution. Under *space denotes significance* that proportion claims the background is the point.
**This material is not wasted, it is the Introduction** for the report and the intro slide, and it is
better written than anything I would produce. It should move there, not be deleted.

**From Valeria's draft, removed the inline citations (1) to (8).** Conference abstracts do not cite,
and NMA's own worked example has none. The refs live in `references.md`.

**From the results draft, deleted** the meta-commentary ("we report an honest dissociation"), all
typographic emphasis, and the secondary statistics (n ≈ 100 instability, r ≈ 0.18 modularity, partial
r ≈ 0.22 to 0.24). Those belong in Results. Every number that survived changes a conclusion.

---

## Open, needs the group rather than me

> **Closed (21 Jul).** These were open questions "for Monday" (20 Jul). That workshop day has passed
> and the abstract was submitted 20 Jul 22:12, so they are closed as pre-submission items; "Goutham
> should sign it off" and "before Monday" below are past. nb08 (21 Jul) also supersedes the
> pattern-vs-scalar framing these items assume (see the top banner). Left intact as the pre-workshop
> record.

1. **N discrepancy, resolved after this draft.** The current MVP uses B (336 analytic participants)
   for the primary analysis and A (100 participants) for external validation; the cohorts are not
   merged. Formal team confirmation remains part of Monday's method lock. See
   [`docs/project-plan.md`](../../../docs/project-plan.md).
2. **The last sentence is the most attackable.** Claiming scalar reorganisation indices may be too
   unreliable for individual prediction is a real claim about metrics the field uses. The hedge is
   kept and the test that would settle it is named. **Goutham should sign it off**, this is his side
   of the work.
3. **C is a reconstruction.** The hypothesis is inferred from the 10 Jul framing. If the group
   remembers it differently, C changes and F changes with it.
4. **Finc 2020** (Valeria's ref 7) is about reconfiguration during WM training, closer to us than it
   first appeared. Someone should read it properly before Monday. It may be a stronger comparator
   than Avery, or a problem.

---

## Note on process

NMA's Abstract Writing Day (W3D1, Mon 20 Jul) prescribes that **each person drafts their own version
independently, then the group merges the best sentences**, rather than one draft reviewed by
everyone. Two independent drafts already exist, which is why this merge was possible at all. Worth
doing properly on Monday rather than converging early. Also worth remembering: NMA's own abstract
record is explicitly *not used for evaluation*, and Monday is a full workshop day, so today's
submission is not final.

> **Update (21 Jul):** Monday 20 Jul has passed and the abstract was submitted 20 Jul 22:12. This
> section is kept as the pre-workshop process rationale.

**House style note.** Em dashes are removed throughout, deliberately. They are legitimate punctuation,
but they read as machine-written to some readers, and Arefeh has already raised that concern about our
drafts. Commas, colons and parentheses do the same work without the association. Proposed as a rule
for `manuscript/writing-guide.md`.

---

## Clean version for pasting

Cognitive demands reconfigure the brain's functional connectivity, and working-memory load is a
strong driver of this reorganisation. Whether that reconfiguration carries information about an
individual's ability, beyond what connectivity already shows at low load, remains unclear. We
hypothesised that the change from low to high load would predict performance in unseen individuals,
and that it would be captured by directional summaries of network integration and segregation. Using
Human Connectome Project N-back data from 336 participants, we estimated connectivity for each
condition across 360 cortical regions grouped into 12 networks, defined reconfiguration as the
difference between conditions, and summarised both as a 78-feature fingerprint. We predicted 2-back
performance using cross-validated ridge regression against a permutation null. Task connectivity
predicted performance out of sample (r ≈ 0.28), and so did the multivariate reconfiguration pattern
(r ≈ 0.37; r ≈ 0.28 across independent runs). The directional scalar summaries we expected to carry
the effect did not (r ≈ 0.04). This pattern-versus-scalar dissociation is what difference-score
reliability predicts: subtracting two highly correlated conditions removes the shared variance a
single contrast depends on, while a multivariate model can still pool weak but consistent signal
across edges. Load-driven reconfiguration therefore carries individual predictive signal, but only
when it is read as a distributed pattern. Much of that signal is trait-general, since low-load
connectivity alone predicts nearly as well. These task data cannot establish causality, and whether
scalar reorganisation indices are simply too unreliable for individual prediction is directly
testable with repeated sessions.
