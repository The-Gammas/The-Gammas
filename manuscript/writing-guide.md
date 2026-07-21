# Writing guide

Shared criteria for the team's written output, so revisions are argued against a standard instead of
personal taste.

## Which standard wins

1. **NMA course guidance is canonical.** It defines the abstract structure (ABC…G), the required
   reading, and the presentation format. It overrides everything below.
2. **[UW–Madison Writer's Handbook](https://writing.wisc.edu/handbook/assignments/)** is
   supplementary — used only where NMA is silent (word discipline, paraphrase/plagiarism, tense).

Canonical NMA sources, all in the course clone:

- [`projects/docs/project_guidance.md`](../../../../official/course-content/nma_course_content/projects/docs/project_guidance.md)
  — Abstract Writing Day (W3D1) and Final Presentations (W3D5)
- [`projects/modelingsteps/TrainIllusionDataProject.ipynb`](../../../../official/course-content/nma_course_content/projects/modelingsteps/TrainIllusionDataProject.ipynb)
  — Step 10 "Summary": the worked ABC…G example for a **data** project (ours is a data project)
- [Ten simple rules for structuring papers](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005619)
  (Mensh & Kording 2017) — required skim, **especially Figure 1**
- [NMA LLM system prompt](https://osf.io/bhs4q/download) — the prescribed starting point for
  workshopping (see below)

**Deliverables:** abstract → **Abstract Writing Day (W3D1, Mon 20 Jul)**, submitted via
[Airtable](https://airtable.com/app1MtChyjyKEDzAt/shr0ozNAhXq6K1p8o); final slides → **W3D5 (Fri
24 Jul)**, via [Airtable](https://airtable.com/shrvoz2N9UulAVqqU).

> Note on dates: NMA's own record of the abstract is explicitly **"not used for matching or
> evaluation"** and its day is W3D1. **Fri 17 Jul** was Azman's progress-check date; W3D1 is the full
> workshop for revising the abstract. The abstract was submitted 20 Jul (22:12) via Airtable; NMA
> does not grade it, so the 17 July snapshot is superseded.

---

## The abstract — ABC…G (canonical)

NMA's structure. Answer each question, then paraphrase the answers into a single paragraph.
**Do not leave the letters in.**

| | Question | Note |
|---|---|---|
| **A** | What is the phenomenon? | Only the part our work addresses |
| **B** | What is the key scientific question? | Clearly articulated |
| **C** | What was our hypothesis? | The key relationships we relied on |
| **D** | How did the analysis work? | Overview, main components. "Here we…" |
| **E** | What did we find? | Key outcomes of the evaluation |
| **F** | What can we conclude? | Against the hypothesis, **within the limits of the approach** |
| **G** | Limitations and future directions? | What is left to learn; plausibility; what was left out |

Read the worked example in `TrainIllusionDataProject.ipynb` (Step 10) before drafting — it shows the
whole A→G chain and then the assembled paragraph.

### Ten simple rules (required skim)

Figure 1 is the point: **the same structure applies to the abstract, to each paragraph, and to the
whole paper.** Context → gap → what we did → results → conclusion. If a paragraph doesn't have that
shape, it isn't finished. Use the paper's vocabulary when critiquing each other's drafts — it turns
"I don't like this" into a diagnosis with a prescribed fix.

### Flow (NMA's own emphasis)

- Each sentence continues from where the previous one left off.
- Never use jargon without defining it first.
- Optional but recommended by NMA: Williams, *Style: Toward Clarity and Grace*,
  [ch. 3 on cohesion](https://sites.duke.edu/niou/files/2014/07/WilliamsJosephM1990StyleTowardClarityandGrace.pdf).

### Supplementary constraints (UW, where NMA is silent)

NMA does not set a word count or a citation policy. These fill the gap:

| Rule | Detail |
|---|---|
| **Length** | 150–250 words, ~6–7 sentences |
| **No citations** | An abstract describes what *we* studied, found and argue. Author-year citations go in [`references.md`](references.md) |
| **Self-contained** | Intelligible without the paper. No undefined shorthand |
| **Tense** | Past for previous work / what we did / what we found. Present for rationale, "Here we…", and significance |

---

## The NMA workflow for Abstract Writing Day

This is prescribed, and it is worth following literally on 20 Jul:

1. **(30 min)** Each person answers ABC…G themselves → first version.
2. **(30 min)** Individually skim *Ten simple rules*, Figure 1.
3. **(1 h)** Workshop as a group, referring back to the paper's principles.
4. **(45 min)** Edit **individually**, each in your own doc — so we end with as many abstracts as
   people.
5. **(30 min)** Put them all in one doc, compare, pick and choose the best sentences from each.
6. **(45 min)** Take it to the Project TA (Azman) for explicit feedback.
7. **Pod exchange:** present to the other group, read each other's abstracts, say what you do and
   don't understand.

Step 5 is the one we have not been doing. Everyone writing their own version *in parallel* and then
merging beats one person drafting and everyone else reviewing — it surfaces genuinely different
framings instead of anchoring the group on the first draft.

---

## Slides (W3D5, 24 Jul)

Hard format constraints from NMA — these are not suggestions:

- **1 slide per person, 1 minute per person.** ~5 min per group total.
- **Always an intro slide and a conclusion slide.** With ≥5 people, someone owns each.
- No introductions during the presentation — go straight into the material.
- Leave the conclusion slide up for questions.
- Template: [Google Slides](https://docs.google.com/presentation/d/1A1uaYarVot9YyCdbAAB4VDvsQfK6emqq-TwIZ9xVNwo/edit)
  or [PowerPoint](https://osf.io/ky6fj/download), or our own.

NMA's framing: this is an **elevator pitch told as a story**, not a report readout. Everyone takes a
turn. Tell how the hypotheses changed and how they were refined. Rehearse it many times — that is
the whole method.

**Explicitly fine per NMA:** most groups won't have a result, and a negative result is a real result
— report it and say what it does to the hypothesis. The goal is to communicate the *logic* of the
project. For us, the honest result is that FC reconfiguration predicts performance, but does not show
a clear incremental gain over 0-back FC; regional activation predicts more strongly under the current
unmatched representations. This refines the conclusion without erasing the original result.

Content compression, from UW's poster guide (its layout advice is for physical posters — ignore it):

> *In a paper:* "This project sought to establish the ideal specifications for clinically useful
> wheelchair pressure mapping systems, and to use these specifications to influence the design of an
> innovative wheelchair pressure mapping system."
>
> *On a slide:* **Aims** — Define the ideal system · Design a new system to meet it

---

## Using sources

**Source:** [Quoting and Paraphrasing](https://writing.wisc.edu/handbook/quotingsources/) (UW). NMA
says nothing about this; it is the gap that matters most given how we draft.

- **Summarise, don't quote.** In the natural sciences the convention is to summarise. Quote only to
  invoke an authority, critique a position, or when the exact wording carries the meaning.
- **The patchwork paraphrase is plagiarism.** Rearranging a source's phrases into a new pattern —
  even *with* the citation — is plagiarism if the borrowed language isn't quoted. **This is precisely
  what LLM summarisation produces by default.** Any AI-assisted paragraph describing Avery, Hedge or
  Cole must be checked against the original, not just against our draft.
- **Method that works:** read until you understand it, look away, then write. If you can't, you don't
  understand it yet — which is itself useful information.
- **Shared language needs no quotation marks.** *Functional connectivity*, *cross-validation*,
  *working-memory load*, *held-out subjects* are the field's conventional vocabulary. Paraphrasing
  them into circumlocutions makes writing worse, not more original. Non-native speakers: this is
  permission, use it.

---

## Pre-submission checklist

- [ ] Every one of **A–G** is answered, and the letters are gone
- [ ] Abstract, each paragraph, and the whole story each have the *Ten simple rules* shape
- [ ] Each sentence continues from the previous one; no jargon used before it is defined
- [ ] 150–250 words, counted — not estimated
- [ ] No author-year citations inside the abstract body
- [ ] Tenses follow the convention above
- [ ] **Every number changes a conclusion.** Secondary r values, sensitivity and robustness checks
      belong in Results. A wall of parentheses reads as a data dump and is the clearest tell of
      unedited machine drafting
- [ ] **No typographic emphasis** — no italics, bold or CAPS for stress
- [ ] **No meta-commentary about the authors.** "We report an honest dissociation" describes us; an
      abstract describes the work
- [ ] **F is stated within the limits of the approach**; **G is present** — limitations are required
      by the structure, not optional
- [ ] Claims calibrated to n and to a single dataset — "may", not a verdict. No causal language
- [ ] Every AI-assisted description of a source checked against the original for patchwork paraphrase
- [ ] Sample size and dataset match the canonical decision in
      [`../docs/project-plan.md`](../docs/project-plan.md)

---

## On AI-drafted text

**NMA prescribes LLM feedback**: *"The starting point for workshopping your abstract should be
getting feedback from an LLM using the [NMA system prompt](https://osf.io/bhs4q/download)."* Using a
model here is course-endorsed, not a workaround — and we should be using *their* system prompt rather
than an ad-hoc one.

Note what it endorses precisely: an LLM for **feedback on a draft you wrote**, as the *starting
point* of a group workshop. It does not endorse the model writing the abstract. Both things can be
true at once: machine drafting is a legitimate way to pull scattered evidence into a structure fast,
*and* the prescribed workflow is ABC…G by hand → LLM feedback → group workshop.

The output reliably over-parenthesises, over-hedges, over-emphasises, closes on meta-commentary
instead of significance, and — most seriously — patchwork-paraphrases its sources. Say plainly when a
draft was machine-written, and have a human rewrite it in their own voice before it ships. The
checklist catches most of it; the paraphrase check has to be done against the source itself.

---

## Appendix — UW resources reviewed but rejected

Recorded so the selection is not re-litigated. All CC BY-NC-SA.

| Resource | Why not |
|---|---|
| [Planning and Writing Research Papers](https://writing.wisc.edu/handbook/planresearchpaper/) | For library-based papers: choosing a topic, bibliography cards. Our question is fixed and our data collected |
| [Writing a Review of Literature](https://writing.wisc.edu/handbook/reviewofliterature/) | For standalone reviews. Our A–B does this in two sentences. Kept one idea: *space denotes significance* — how much room a study gets is itself a claim about how much it matters |
| [Writing Annotated Bibliographies](https://writing.wisc.edu/handbook/annotatedbibliography/) | [`references.md`](references.md) already is one. Kept one idea: *combination* style as house standard — 1–2 sentences of what the source found, then 1–2 of what it means **for us** |
| [Formatting Science Reports (IMRaD)](https://writing.wisc.edu/handbook/sciencereport/) | Superseded by ABC…G for the abstract and by the 1-slide format for the presentation. We produce no IMRaD paper. Its Discussion warnings are folded into the checklist above |

**Bookmarked:** [Planning and Writing a Grant Proposal](https://writing.wisc.edu/handbook/grants/) —
irrelevant to 24 Jul, but the ISP application (2-page proposal + 6-slide deck + 5-min video, deadline
3 Sep) is exactly a grant proposal. Revisit in August if we continue.
