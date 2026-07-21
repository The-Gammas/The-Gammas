# Manuscript

The scientific write-up: the abstract was **submitted on Mon 20 Jul** (22:12); focus is now the
**W3D5 presentation on Fri 24 Jul**. The 17 July deliverable was Azman's progress check, an intermediate
snapshot on the way to that submitted abstract (NMA does not grade the abstract).

## Source and status model

This folder separates source contributions, proposals, accepted decisions and manuscript snapshots
so that they do not silently become interchangeable:

- **Live abstract:** the shared multi-tab Google Doc titled **“Ideas”** remains the single editing
  surface for the team abstract (owner: Valeria Moraga; the *Abstract* tab was drafted by
  Arefeh) — [open Doc](https://docs.google.com/document/d/1mRC-UZhOGJ_ovPqXBudEBEPUyIp_AzjkJqvoIsAyouk/edit).
- **Proposal for team review:** [`research-proposal.md`](research-proposal.md) condenses Valeria
  Moraga's *Research Question Development* contribution into the
  [four-step NMA W2D1 framework](https://compneuro.neuromatch.io/tutorials/W2D1_ModelingPractice/student/W2D1_Tutorial1.html). It is
  explicitly a proposal, not a record of team agreement; the
  [PDF](../sandbox/valeria/Research%20Question%20Development.pdf) and
  [Markdown transcription](../sandbox/valeria/research-question-development.md) remain unchanged.
- **Dated abstract snapshots:** [`abstract.md`](abstract.md) leads with the **submitted version
  (20 Jul)** plus a 21 Jul corrected draft, and preserves the earlier 17 July merge proposal and
  10 July Google Doc text as history below. Neither snapshot replaces the live Google Doc.
- **Current direction:** [`../docs/project-plan.md`](../docs/project-plan.md) records the living plan,
  verified results and open decisions; dated meeting notes preserve why a proposal was accepted,
  rejected or deferred.
- **Canonical evidence:** [`../pipeline/02_canonical_analysis_and_slides.ipynb`](../pipeline/02_canonical_analysis_and_slides.ipynb)
  reproduces the calculations and figures proposed for the presentation while linking back to each
  source notebook.
- **Supporting record:** [`references.md`](references.md) is the annotated bibliography and
  [`prior-work.md`](prior-work.md) documents internal explorations.
- **Writing criteria:** [`writing-guide.md`](writing-guide.md) holds the shared standard for the
  abstract (NMA's **ABC…G** structure), Abstract Writing Day, source use and the W3D5 slides
  (1 slide / 1 min per person). NMA course guidance is canonical there; UW–Madison material is
  supplementary. Review drafts against it rather than against personal taste.

The Google Doc tabs map to the repository as follows:

- *Data Understanding* → data dictionary and exploratory analysis in `sandbox/jaime/`
- *Main Tasks* → [`../docs/project-plan.md`](../docs/project-plan.md)
- *Literature Related* → [`references.md`](references.md)
- *Abstract* → dated snapshots such as [`abstract.md`](abstract.md)

**Current next step:** the abstract is submitted, so the focus is the **W3D5 presentation (Fri 24 Jul)**.
The pattern-vs-scalar framing is refined by nb08 (21 Jul): reconfiguration does not clearly add over
single-condition 0-back FC (nested delta-R2 +0.034, sd 0.023, under 2 sd), while a task-activation
contrast (2bk-0bk mean BOLD) predicts more strongly (r ~ 0.60 pooled, ~0.48 held-out people and runs)
under the current unmatched representations. Adding FC shows no clear gain (delta-R2 ~ -0.003), so
the evidence does not establish FC-specific predictive value. The proposed resolution in
[`pipeline/02`](../pipeline/02_canonical_analysis_and_slides.ipynb) keeps FC as the primary analysis
and activation as an unexpected benchmark; its main-slide placement remains a team decision.

## Attribution and review workflow

1. Preserve each source contribution in its author's sandbox and link it explicitly.
2. Mark derived syntheses as proposals until the team records a decision in the living plan or
   meeting notes.
3. Keep scientific qualifications traceable to [`references.md`](references.md); do not duplicate a
   second bibliography in each proposal.
4. Update the live Google Doc first when revising the submitted abstract, then capture a dated
   repository snapshot at a meaningful milestone.

## Toward the full report

When the team moves past the abstract, accepted material can grow into Introduction · Methods ·
Results · Discussion · Limitations. Method details and decisions continue to come from
[`../docs/`](../docs/); proposals remain attributable to their source until accepted.
