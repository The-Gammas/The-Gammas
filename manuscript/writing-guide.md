# Writing guide

Shared criteria for the team's written output, so revisions are argued against a standard instead of
personal taste. Written for the NMA abstract; what survives here is the part that transfers to any
paper we write next.

Canonical sources: [Ten simple rules for structuring papers](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005619)
(Mensh & Kording 2017, **especially Figure 1**) · [NMA project guidance](https://github.com/NeuromatchAcademy/course-content/blob/v3.0.2/projects/docs/project_guidance.md)
for the ABC…G structure and its worked data-project example · the
[UW–Madison Writer's Handbook](https://writing.wisc.edu/handbook/assignments/) where NMA is silent
(word discipline, paraphrase, tense).

## The abstract — ABC…G

Answer each question, then paraphrase the answers into a single paragraph. **Do not leave the letters
in.**

| | Question | Note |
|---|---|---|
| **A** | What is the phenomenon? | Only the part our work addresses |
| **B** | What is the key scientific question? | Clearly articulated |
| **C** | What was our hypothesis? | The key relationships we relied on |
| **D** | How did the analysis work? | Overview, main components. "Here we…" |
| **E** | What did we find? | Key outcomes of the evaluation |
| **F** | What can we conclude? | Against the hypothesis, **within the limits of the approach** |
| **G** | Limitations and future directions? | What is left to learn; what was left out |

**The structure is fractal.** That is the point of *Ten simple rules* Figure 1: context → gap → what
we did → results → conclusion applies to the abstract, to each paragraph, and to the whole paper. If a
paragraph doesn't have that shape, it isn't finished. Using the paper's vocabulary when critiquing each
other turns "I don't like this" into a diagnosis with a prescribed fix.

**Flow.** Each sentence continues from where the previous one left off, and no jargon appears before it
is defined.

**Where NMA sets no rule:** 150–250 words (~6–7 sentences), counted not estimated · no author-year
citations inside an abstract — those live in [`references.md`](references.md) · self-contained, no
undefined shorthand · past tense for previous work and for what we did and found, present for
rationale, "Here we…" and significance.

**One process lesson worth keeping.** Everyone drafting their own version *in parallel* and then
merging the best sentences beats one person drafting and everyone else reviewing: it surfaces
genuinely different framings instead of anchoring the group on the first draft.

## Using sources

**Source:** [Quoting and Paraphrasing](https://writing.wisc.edu/handbook/quotingsources/) (UW). This
is the gap that matters most given how we draft.

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

## On AI-drafted text

NMA prescribed LLM feedback as the *starting point* for workshopping a draft you wrote, using
[their system prompt](https://osf.io/bhs4q/download). Note what that endorses precisely: feedback on a
human draft, not the model writing the text.

The output reliably over-parenthesises, over-hedges, over-emphasises, closes on meta-commentary
instead of significance, and — most seriously — patchwork-paraphrases its sources. Say plainly when a
draft was machine-written, and have a human rewrite it in their own voice before it ships. The
checklist below catches most of it; the paraphrase check has to be done against the source itself.

## Checklist

- [ ] Every one of **A–G** is answered, and the letters are gone
- [ ] Abstract, each paragraph and the whole story each have the *Ten simple rules* shape
- [ ] Each sentence continues from the previous one; no jargon used before it is defined
- [ ] 150–250 words, counted — not estimated
- [ ] No author-year citations inside the abstract body; tenses follow the convention above
- [ ] **Every number changes a conclusion.** Secondary r values and robustness checks belong in
      Results. A wall of parentheses reads as a data dump and is the clearest tell of unedited
      machine drafting
- [ ] **No typographic emphasis** for stress — no italics, bold or CAPS
- [ ] **No meta-commentary about the authors.** "We report an honest dissociation" describes us; an
      abstract describes the work
- [ ] **F is stated within the limits of the approach**, and **G is present** — limitations are
      required by the structure, not optional
- [ ] Claims calibrated to n and to a single dataset — "may", not a verdict. No causal language
- [ ] Every AI-assisted description of a source checked against the original for patchwork paraphrase
- [ ] Sample size and dataset match [`../docs/final-report.md`](../docs/final-report.md) §3

## Compressing prose onto a slide

The same content, two registers — UW's example, and the habit worth copying:

> *In a paper:* "This project sought to establish the ideal specifications for clinically useful
> wheelchair pressure mapping systems, and to use these specifications to influence the design of an
> innovative wheelchair pressure mapping system."
>
> *On a slide:* **Aims** — Define the ideal system · Design a new system to meet it

## If we write the ISP proposal

The [ISP application](https://neuromatch.io/impact-scholars-program/) — 2-page proposal, 6-slide deck,
5-minute video, deadline 3 Sep — is a grant proposal, not an abstract. UW's
[Planning and Writing a Grant Proposal](https://writing.wisc.edu/handbook/grants/) is the right guide
for it; everything above still applies to the prose inside.
