# The Gammas — final storyboard (cover + team + 5 spoken + 4 backup)

## Production-wide rules

- **Document status:** presentation-ready flow for Friday. **Slides 3–7 are the five spoken content
  slides**, one slide and roughly one minute per presenter. Slides 1–2 (cover, team) are structural
  and carry no speaking beat beyond a greeting. Slides 8–11 are **backup**, opened only in Q&A.
- **Visible language:** concise English. **Production language:** Spanish.
- **Visual system:** 16:9 (720 × 405 pt), Poppins, restrained taupe/brown/pale-mint Neuromatch
  palette, generous margins, large takeaway titles, a simple footer/page marker, and **one dominant
  evidence visual per spoken slide**.
- **Charts carry no text (hard rule).** A slide chart is a **pure plot**: axes, marks, tick labels,
  axis titles and direct data labels. No figure header, no footnote caveat, no side annotation block.
  Every number, caveat and legend belongs in **native pptx text**, which stays sharp at any
  projection size. Slide charts are drawn at 26–30 pt on the 1152 pt canvas; placed `W` pt wide they
  render at `26·W/1152` on screen. Never two charts on one slide, never an inset.
- **Chart width: aim for 460 pt, and record it when the layout will not allow it.** The earlier flat
  “never below 460 pt” rule was written against a full-width layout and the deck does not obey it,
  because most slides are two-column. Measured and accepted: slide 4 **340 pt**, slide 5 **360 pt**
  (its metric cards start at L 384, so the left column caps the figure at ~355 — widening it to 498
  ran the plot underneath them), slide 6 **351 pt**, slide 9 **451 pt**, slide 10 **372 pt**. At
  350 pt a 26 pt label lands at 7.9 pt on screen: legible in a rendered export, small from the back
  of a room. Reaching 460 pt on these slides means restructuring the slide, not enlarging the
  picture — so decide it deliberately, never by dragging a corner.
- **Do not shrink the chart canvas to enlarge type.** Every renderer positions text in figure
  fractions while font sizes are absolute points, so a smaller canvas overflows all nine layouts.
  This was tried on 23 Jul (`FIGSIZE=(10, 5.625)`) and produced clipped axis labels and overlapping
  captions on every chart **while the whole test suite still passed** — nothing measures rendered
  text position. Legibility comes from removing chart text and raising font sizes, never from
  rescaling. Regenerating always requires a visual pass over `visuals/qa/charts-contact-sheet.png`.
- **Template hygiene:** the template supplies visual grammar only. Remove every placeholder, old
  result image, fake biography, stock portrait, source comment, comment-author record and hidden
  review artifact; do not invent people, figures, or results. Keep the frozen snapshot unchanged.
- **Statistical guardrail:** repeated-CV `±` is SD across 20 overlapping split partitions, never a
  confidence interval. The seed-42 full-refit permutation and the B→A fixed-prediction label
  permutation are distinct tests. **Full definitions live on backup Slide 11**; each spoken slide
  carries only the one label its own figure needs.
- **Narrative framing — read this before writing any speaker text.** We did **not** change our
  hypothesis in response to the data. We pre-specified **two** hypotheses; the evidence **confirmed
  one and refined the other**. Say *"we predicted two things: one held, one turned out narrower than
  we expected."* Never say the hypothesis *evolved*, *shifted* or *was replaced* — that would
  misdescribe the actual inferential sequence.
- **Density fallback:** never shrink narrative type to force a layout. Move detail to backup before
  reducing type.
- **Empirical assets:** reuse only the evidence in `visuals/charts/`. The method schematic is the one
  sanctioned non-data figure: it is a conceptual pipeline drawn as native shapes, not a chart.
- **The live deliverable is the team Google deck**
  ([`1A-FC-Hs2…Dk9E`](https://docs.google.com/presentation/d/1A-FC-Hs29PhzQ4ZID4hKFMMbXgLh2YIlnMQiUirDk9E/edit)),
  owned by Valeria Moraga. This file is its **spec**, not a copy of it; the two drift and must be
  reconciled by hand — see *Google deck reconciliation* at the end. `source-snapshots/` holds frozen
  PDF/PPTX exports of that deck and is only refreshed when someone runs an export, so it lags the
  live file. Verify against a fresh export, never against the newest snapshot on disk.
- **One snapshot at a time (owner's rule).** `source-snapshots/` keeps **only the most recent**
  export; older folders are deleted rather than accumulated, because stale copies of a deck that
  moves several times an hour are noise, not history. Nothing is lost — every superseded snapshot
  stays in git. Do not re-create a deleted snapshot folder.

## Structure rationale (why this shape)

Benchmarked against five 2025 NMA project decks in
[`../../../references/nma_project_examples_2025/`](../../../references/nma_project_examples_2025/).
Their shared spine: a cover carrying the project name and authors → a framing beat with an explicit
labelled hypothesis → one methods beat → a primary result carried by one dominant figure → **a
dedicated honest negative/surprise slide as the narrative hinge** → a synthesis conclusion → a
non-spoken backup tail. Three of the five also give the team its own slide.

Kept from our own work, not traded away for familiarity: charts bound to canonical evidence with
provenance in [`visuals/manifest.json`](visuals/manifest.json), and the Survives / Refined /
Unresolved conclusion that answers the opening hypotheses instead of recapping bullets.

> Prior decks did **not** compress to five spoken slides (their spoken cores run about 6 / 5 / 9 / 7 /
> 9). Five is the NMA rule, and this deck meets it: cover, team and backup carry no speaking slot.

## TA review — Andrea Buccellato, 23 Jul Zoom

Andrea walked the deck from Slide 3 and gave direct instructions. Her framing first, because it
changes how much any of the rest matters:

> *“It's more about the progress, the experience you did, rather than the actual findings. So don't
> worry if you can't say anything.”* — and, on comparing methods, *“you won't get any prize if this
> study is better or not.”*

**Binding instructions**, each applied in the slide section it belongs to:

1. **Define every concept you name.** Raised by **Arefeh Lali Dehaghi** (“what is your opinion to
   define some basic information, like segregation and integration?”) and endorsed as one of
   Andrea's own questions. FC must be defined as a Pearson correlation between nodes, each node an
   ROI, and **system segregation must be defined and its computation stated** — currently it appears
   on Slide 6 with no definition anywhere in the spoken deck.
2. **Less text, more visual.** Specifically on the method slide: *“maybe in the correlation matrix,
   you can add like the actual figure of the correlation matrix, make it more visual than text,
   because people can get lost in this.”*
3. **Cut the acquisition detail.** *“Just say it's the HCP data set, it's 336 participants, this is
   the task. That's it. I wouldn't go into the details about the acquisition parameters.”*
4. **One literature anchor in the intro**, not a survey: *“stick to one main thing… the thing that's
   mostly connected to what you're going to do.”*
5. **Enlarge the question on Slide 3** and take it out of the title; let the predictions sit slightly
   smaller beneath it.
6. **Read the axes out loud** on every figure: *“always make sure that people know what they're
   looking at.”*
7. **The bottom-right block on Slide 6 is too small.** *“Choose one of these things, summarize it,
   make it bigger — or shorter and bigger.”*
8. **Keep the references slide** in the submitted deck; the last presenter shows it for five seconds
   and does not read it.
9. **Team name prominent on the cover** — the deck is archived and read by next year's cohort.
10. **Rehearse to the minute.** Andrea offered a rehearsal round and tutorial time on Friday.

### Presenter assignment

| Slide | Presenter | Source |
|---|---|---|
| 3 · Intro | **Valeria Moraga** | She asked to go first; Andrea confirmed |
| 4 · Method | **Goutham Arcod** | Discord 23 Jul: “should i do methodology??” → “methodology is yours” |
| 5 · Primary result | *open* — Goutham proposed Jaime Pineda | Zoom, then Andrea left the swap open |
| 6 · The turn | *open* | — |
| 7 · Conclusion | *open* | — |

**Unresolved conflict:** on Zoom, Goutham's (garbled) line suggested **Arefeh** wanted the method
section, which collides with the Discord hand-off of methodology to Goutham. Settle this before
rehearsing — it is the only assignment where two people may believe they hold the same slide.

## Structural conventions every slide follows

### Section labels (eyebrows)

Every slide carries a small taupe label above its title naming which act of a normal scientific talk
it belongs to. An audience that has watched four decks before ours should never have to work out
where they are. Internal words like *pipeline* do not qualify — the label names the **act**, not the
artefact.

| Slide | Label |
|---|---|
| 3 | Introduction |
| 4 | Methods |
| 5 | Results |
| 6 | Results · robustness checks |
| 7 | Conclusions |
| 9 | Backup · directional result |
| 10 | Backup · validation |
| 11 | Backup · future work |
| 12 | Backup · references |

Set at 10 pt semibold in `#B99470`, at L 24, T 3–5, above a title that stays at T 18–21. Slide 3
carries its label inside its own title block, which is why it looks slightly lower; leave it.
Slide 5's old free-floating **“Analysis”** heading was deleted — it sat at T 35, underneath the
title, and had been invisible in every export.

### Layout discipline

- **Reading order must match numbering.** A numbered step that sits to the left of, or below, a
  step with a higher number is a defect, not a style choice.
- **No dead quadrant.** If a block is removed, close the gap; do not leave a hole where the eye
  expects content.
- **Do not resize a card group vertically.** These template cards are groups whose header strip
  scales with the group, so two side-by-side cards of different heights get visibly misaligned
  headers. Change width freely, height only when the card stands alone.
- **One paragraph with soft line breaks, never one paragraph per line.** The card bodies space
  paragraphs generously; a paragraph per line overflows the card silently and lands on whatever is
  underneath. This produced overlapping text on the method slide that no geometric check caught.
- **Check every picture's aspect ratio against its crop.** The directional chart shipped at
  451.4 × 196.4 from an uncropped 16:9 source — squashed 22 % vertically. Compute
  `width / height` and compare with `16(1 − cropL − cropR) / 9(1 − cropT − cropB)`.

---

## Slide 1 — Cover

- **Status:** Structural; no speaking beat.
- **Audience-facing title:** *Functional Connectivity Reconfiguration in N-back Working Memory*
- **Visible copy:**

  `Arefeh Lali Dehaghi · Goutham Arcod · Jaime Pineda · Kerem Akyurt · Valeria Moraga`

  `Ifrit Ras el Hanout — The Gammas · NMA Computational Neuroscience 2026`

  `HCP N-back · participant-level prediction`

- **Layout:** Two-line large title, left-aligned, with the author line and pod line beneath. Reuses
  the teammate template's cover typography and hierarchy.
- **Chart:** No pre-rendered chart. Typographic cover; do **not** bleed an evidence chart in as
  decoration — a data figure used ornamentally reads as a result.
- **Template mapping:** Valeria source slide 1. **Drop** its gears-in-a-head clip art and strip the
  leftover comment artifact.
- **Speaker note / transition:** “Portada. No consume minuto; se muestra mientras se presenta el
  equipo.”
- **Evidence / provenance:** Project title as submitted; author list per `manuscript/abstract.md`.
- **Scientific caveat:** The title names the measure, not a mechanism. “Reconfiguration” is a
  difference between two condition-aggregated FC matrices.

## Slide 2 — Team

- **Status:** Structural; brief greeting only.
- **Audience-facing title:** *Meet our team*
- **Visible copy:**

  `Arefeh Lali Dehaghi · Goutham Arcod · Jaime Pineda · Kerem Akyurt · Valeria Moraga`

  `Pod 884 “Ifrit Ras el Hanout” · Megapod Lotus · TA Andrea Buccellato · Project TA Azman Akhter`

- **Layout:** Staggered 3-over-2 grid of five member tiles, name beneath each, following the
  template's rhythm.
- **Chart:** No pre-rendered chart. Initial-monogram circles in the deck palette stand in for photos.
- **Template mapping:** Valeria source slide 2. **Two hard blockers, both must be removed:** the five
  stock studio portraits (they depict strangers and imply they are us) and the filler role labels
  *Actor / Doctor / Accountant / Chef / Journalist*, which are template dummy text.
- **Speaker note / transition:** “Solo nombres. **Pendiente de decisión del equipo:** si añadimos rol
  real por persona o dejamos únicamente los nombres. No inventar roles.”
- **Evidence / provenance:** Roster per `course-ops/pod/group-1-info.md`; pod and TA names per
  `course-ops/pod/pod-info.md`.
- **Scientific caveat:** Not applicable.

## Slide 3 — Intro: the question and the two things we predicted

- **Status:** Spoken · **Valeria Moraga**, presenting **first** (her request, confirmed by Andrea).
- **Audience-facing title:** *Does load-related brain connectivity predict working-memory performance?*
- **Visible copy:**

  `Functional connectivity = how strongly two brain regions rise and fall together; reconfiguration = how that coupling changes as memory load goes up.`

  `Avery et al. 2020 predicted 2-back accuracy from task FC in the same dataset (r = 0.36). We asked whether the change between loads carries that signal.`

  **We predicted two things**

  **Pattern**  `A 78-feature FC fingerprint of the 2-back − 0-back change predicts performance.`

  **Direction**  `Higher load shifts networks toward integration; larger shifts accompany better performance.`

  `A distributed pattern and a one-number direction are different claims.`

- **Layout:** The **question is the dominant element on the slide** — Andrea asked for it larger and
  the predictions a step smaller, so set the two prediction blocks below it at reduced weight rather
  than as equals. The single literature line sits between them, small. The team roster is **not**
  here — it lives on Slide 2, which frees the vertical space the two hypotheses need.
- **One literature anchor only (TA instruction 4).** Andrea asked for exactly one reference in the
  intro, the one closest to what we did. **Avery et al. 2020** is that reference and no other:
  same HCP N-back data, same target (2-back accuracy), out-of-sample task-FC prediction at r = 0.36.
  It is our calibration anchor in `manuscript/references.md`, so quoting it here also sets the scale
  the audience should judge our 0.366 against. Do **not** add a second citation to this slide.
- **Chart:** No pre-rendered chart. Resolve the pattern/direction distinction with type and simple
  native shapes.
- **Template mapping:** Valeria source slides 3–4; remove the unfinished bullet.
- **Speaker note / transition:** “Decir las **dos** predicciones al principio: una se confirma y la
  otra se matiza, y el relato solo se entiende si la audiencia oyó ambas antes de ver resultados. No
  decir que la hipótesis cambió.”
- **Evidence / provenance:** Internal-review storyboard, Slides 1–2; `pipeline/02` cell 0 framing;
  `docs/project-plan.md`.
- **Scientific caveat:** The directional hypothesis is the more restrictive one: it demands a sign
  and compresses a multivariate structure into a scalar.

## Slide 4 — Method: one pipeline, from scans to a held-out prediction

- **Status:** Spoken · **Goutham Arcod** (Discord 23 Jul: “should i do methodology??” → “methodology
  is yours”). See the unresolved conflict noted in the TA review section before rehearsing.
- **Audience-facing title:** *We evaluated a 78-feature FC difference in held-out people*
- **Definitions band — one line, set directly under the title:**

  `System segregation = (mean within-network FC − mean between-network FC) ÷ mean within-network FC, per participant per condition (Chan et al. 2014).`

  **Why only one line now.** The band originally carried three definitions. **Arefeh Lali Dehaghi**
  proposed moving all three to the introduction, and she was right about the problem: “FC
  reconfiguration” is in the deck title, in every footer, and inside the hypotheses on Slide 3, yet
  the audience met its definition one slide later. It is split rather than moved, because Andrea drew
  the line herself — *“just one notion, one explanation what it is, and how you computed that. The
  computation, like, okay, the method can be in the methods part.”*

  So the **notion** (plain language, no formulas) is now on Slide 3, where the terms first appear;
  the **computation** stays here. Segregation stays here in full: it is not used until Slide 6, and a
  formula in the opening slide would have nothing to attach to. The Pearson detail moved into the
  figure caption, beside the matrices it describes. Net effect: the method slide lost two lines of
  text, which is exactly what Andrea asked of this slide.

- **Visible copy — four schematic boxes, with the evidence figure carrying the middle of the pipeline:**

  `1 · Cohort` — `336 participants · HCP N-back working-memory task · 360 Glasser ROIs`

  `2 · Condition frames` — `0-back and 2-back frames kept separate, with no temporal overlap`

  → **figure: the three network matrices** (0-back FC, 2-back FC, and their difference) — this
  *replaces* the former text boxes 3, 4 and 5. Header `From frames to a 78-value fingerprint`;
  caption `Pearson FC between ROI time courses, summarized over 12 Cole-Anticevic networks · 12 within + 66 between = 78 values per person`

  `3 · Model and held-out evaluation` — `StandardScaler + RidgeCV, fitted strictly inside each training fold` · `repeated 5-fold CV · fixed holdout · 1000-permutation null · B→A transfer (301 → 100, identity-disjoint)`

  `All splits hold out participants; “±” = split SD, not CI.`

- **Cut on TA instruction 3 (acquisition detail).** Removed from the visible copy: `TR = 0.72 s`,
  `4 s HRF shift`, `312 frames per load`, `2 WM runs per subject`, and the `360 × 360` intermediate.
  Andrea: *“just say it's the HCP data set, it's 336 participants, this is the task. That's it.”*
  These facts move to the speaker note and stay available for Q&A — **the two-runs-per-person design
  must still be said aloud if anyone asks about the held-out cross-run marks on Slide 6.**
- **Layout:** Boxes 1–2 on the left, the three-matrix figure dominant in the centre, boxes 3–4 as a
  terminal band. Seven text boxes became four plus one picture — Andrea's instruction 2 was
  explicitly *“make it more visual than text, because people can get lost in this.”*
- **Chart:** [`visuals/charts/condition-fc-contrast.png`](visuals/charts/condition-fc-contrast.png)
  — the figure Andrea asked for by name (*“add like the actual figure of the correlation matrix”*).
  The surrounding pipeline stays **native pptx shapes**: the chart library validates visible numbers
  against the live notebook namespace and a conceptual box-and-arrow flow has no array to validate.
  **Re-rendered 23 Jul and ready to place.** It previously carried a figure header, a footer caveat
  and small panel labels — all removed. It is now a pure three-panel plot: three **equal** squares
  (a gridspec shrank the third to make room for the colorbar, and three matrices of different size
  read as three different things), operators between them, panel titles and colorbar at `SLIDE_*`
  sizes. The previously assigned `feature-construction` chart stays **out**: it covered only the
  78-block step and rendered its labels at ~3.6 pt.
- **Say this about the figure (it is not self-evident).** Panels 1 and 2 share **one** colour scale;
  panel 3 has **its own**, roughly an order of magnitude tighter. Three similarly saturated matrices
  therefore do *not* mean three similar magnitudes — the difference is small and the scale is
  stretched to make it visible. Only the difference panel carries a colorbar. Andrea's instruction 6
  applies directly here: say what the colours mean before drawing any conclusion from them.
- **Template mapping:** The pipeline flow proposed on Valeria source slide 5, with every
  graph-construction and graph-metric stage replaced by what we actually ran.
- **Speaker note / transition:** “Un solo recorrido: de los escáneres a una predicción en personas no
  vistas. Decir en voz alta las tres definiciones — FC, reconfiguración y segregación — porque Andrea
  lo pidió explícitamente y Arefeh lo preguntó. Al llegar a la figura, **nombrar los ejes**: tres
  matrices de red, misma escala, la tercera es la resta. Scaler y RidgeCV se ajustan **dentro** de
  cada fold; nunca se separan runs o frames de la misma persona. B estima el modelo; A comprueba
  transferencia sin identidades compartidas. **Detalle retirado de la slide, disponible si preguntan:**
  TR 0.72 s, desplazamiento HRF de 4 s, 312 frames por condición, 2 runs de memoria de trabajo por
  persona, matrices intermedias de 360 × 360.”
- **Evidence / provenance:** `pipeline/02` §3–§4 and §5–§6. `TR = 0.72 s` from
  [`datasets.py:37`](../../sandbox/jaime/datasets.py); HRF delay, frame counts and the 78-block
  summary from `preprocessing.py` and `connectivity.py`. Counts must be copied from
  `visuals/manifest.json`, not retyped from memory — this schematic is the one place in the deck
  where a number has no automated test behind it.
- **Scientific caveat:** Pearson task FC can reflect task-evoked coactivation; it does not
  demonstrate interregional communication or causality.

## Slide 5 — Primary result: the FC pattern predicts, and it transfers

- **Status:** Spoken · presenter **open** — Goutham proposed Jaime Pineda on the 23 Jul Zoom and
  Andrea left the swap to the team.
- **Audience-facing title:** *The FC pattern predicted performance—and transferred to a separate cohort*
- **Visible copy:**

  **B→A transfer**  `r = 0.398; bootstrap 95% CI [0.25, 0.53]`

  `301 B-only → 100 A · 35 shared identities removed`

  **Primary repeated CV**  `r = 0.366 ± 0.024 · 336 participants · 78 FC features`

  `Identity-disjoint same-HCP transfer—not independent-site validation.`

- **Layout:** One dominant evidence field. The transfer scatter is placed at ≥ 460 pt wide; the two
  metric blocks sit beside or beneath it as slide text.
- **Chart:** [`visuals/charts/identity-disjoint-transfer.png`](visuals/charts/identity-disjoint-transfer.png)
  alone. **The `primary-repeated-cv` inset is removed** — at 108 pt its internal text rendered at
  1–2 pt and it duplicated a number already printed as slide text. The fixed holdout and the
  full-refit null are on backup Slide 9.
- **Template mapping:** Valeria source slide 7 (evidence chart + explanation), with the old graph and
  placeholders replaced by canonical evidence.
- **Speaker note / transition:** “**Empezar nombrando los ejes** — instrucción directa de Andrea:
  *eje X, precisión 2-back observada en la cohorte A; eje Y, precisión predicha por un modelo que
  nunca vio a esas personas.* Cada punto es un participante. Luego el efecto primario: la media de CV
  repetida, `.366 ± .024`. La transferencia usa modelos entrenados solo en B y aplicados a A sin
  identidades compartidas: no es validación en otro sitio. Si preguntan por el holdout fijo o por el
  null, están en backup. Transición: establecida la predicción, toca revisar lo que **no** salió como
  esperábamos.”
- **Evidence / provenance:** `pipeline/02` §5–§6 and panels 9B/9C; `manifest.json` →
  `identity-disjoint-transfer` (cell 14).
- **Scientific caveat:** The SD summarizes sensitivity across 20 overlapping partitions, not
  population uncertainty. Sibling HCP cohorts are not cross-site generalization; kinship is
  unmodelled.

## Slide 6 — The turn: the signal survives, but it is not specific to connectivity

- **Status:** Spoken core; required to support the refined final conclusion. Presenter **open** — this
  is the hinge of the talk and the one slide that should not go to whoever is least rehearsed.
- **Audience-facing title:** *Two checks that narrowed what we can claim*

  Retitled 23 Jul. The previous title — *“The prediction held—but a simpler regional signal predicted
  better”* — read as a scoreboard, which is precisely what both the TA and Goutham Arcod objected to.
  See *Agreed language* below.

- **Visible copy:**

  `Repeated-CV correlation (mean ± split SD across 20 partitions)`

  `0-back FC  0.274 ± 0.032    ·    FC reconfiguration  0.366 ± 0.024`

  `0-back + reconfiguration  0.333 ± 0.026    ·    Activation contrast  0.600 ± 0.016`

  **Direction, as predicted—but only at group level**
  `Segregation fell under load (0.3271 → 0.3035; Δ = −0.0236; p = 3.45 × 10⁻⁵), yet larger shifts did not predict better performance (r = −0.105; p = .054).`

  `Open squares = held-out cross-run generalization.`

  **Two caveat lines, both at readable size — not four small ones:**

  `A specificity check, not a competition: post hoc, 360 activation features vs 78 FC features, and 0-back activation alone predicts as well (0.571), so the benchmark is not load-specific. FC reconfiguration stays the load-specific measure.`

  `Activation is a raw BOLD amplitude difference, not a GLM beta. Individual vascular reactivity (CVR) is uncontrolled, and this dataset carries no CVR proxy.`

- **Caveat band rebuilt on TA instruction 7.** Andrea: *“bottom right, it's too small… choose one of
  these things, summarize it, make it bigger — or shorter and bigger.”* The four tiny lines collapse
  to the **two** above, each set large enough to read from the back. Two rather than one because the
  CVR line is a commitment made to Goutham Arcod in writing (Discord, 23 Jul: *“I will document it as
  a caveat on the slides”*) and dropping it would break that. Andrea's objection was legibility, not
  an arithmetic limit. Everything cut — the GLM-beta distinction, the per-run collinearity, the DVARS
  partial — moves to the speaker note and backup Slide 9.
- **Layout:** The activation comparison chart is the **only** figure. The directional result is a
  single highlighted text block, not a second figure. The two caveat lines occupy a lower band at
  body size. If it does not fit, cut caveat wording — never add a second chart, and never shrink the
  caveats back to footnote size.
- **Chart:** [`visuals/charts/activation-robustness.png`](visuals/charts/activation-robustness.png)
  only, placed at ≥ 460 pt. Do **not** add `incremental-fc-test.png` (duplicates the numbers) and do
  **not** add `segregation-refinement.png` here — that figure is backup Slide 8.
- **Template mapping:** Valeria source slide 8 (sparse unexpected finding), rebuilt for the benchmark
  and its guardrails.

- **Agreed language — Discord consensus with Goutham Arcod, 23 Jul.** This is the settled wording;
  do not renegotiate it on the slide.

  **Say:** *specificity check*, *post hoc*, *unmatched dimensionality (360 vs 78)*, *vascular
  reactivity uncontrolled*, *not load-specific*, *FC reconfiguration is our pre-specified,
  amplitude-independent measure*, *we report activation as a specificity check, not a replacement*.

  **Never say:** *“Model A beat Model B”* or any scoreboard phrasing — Goutham's explicit objection
  and independently Andrea's. Also **never** *“FC reconfiguration is our most robust measure”*
  (our own reliability numbers contradict it) or *“true network dynamics”* (we have
  condition-aggregated static FC, not dynamic FC — the first thing a TA would catch). Both were
  proposed, both were dropped by agreement.

  **The interpretive frame Goutham supplied, and we accepted.** He read Hedge 2018 the other way
  round from us, and he was right: activation's *higher* between-run reliability and cross-run
  prediction are not evidence that it is a better cognitive measure. A difference score
  mathematically subtracts the stable trait variance — vascular plumbing, anatomy, trait-level motion
  footprint — leaving only the noisier cognitive state shift. So reconfiguration being less stable is
  the **expected** consequence of its construction, not a defect that favours activation. Combined
  with 0-back alone predicting 0.571, his conclusion holds: the activation advantage is driven by a
  static trait rather than by the task. Say this if anyone asks why the weaker predictor is the one
  we pre-specified.

  **Traceability gap to close.** The reliability pair that carries this argument (between-run
  reliability: reconfiguration ≈ 0.024, activation contrast ≈ 0.169) lives in
  [`nb08`](../../sandbox/jaime/08_activation_vs_reconfiguration.ipynb), **not** in `pipeline/02`, and
  is therefore not covered by `canonical_evidence.EXPECTED`. Keep it verbal and in the speaker note.
  **Do not print those two numbers on a slide until they are promoted into `pipeline/02`** — every
  visible number in this deck has an automated check behind it, and these two do not yet.

- **Why this slide stays, given the TA suggested dropping it.** Andrea's advice was *“if you're in
  doubt, I would suggest you just drop it… you won't get any prize if this study is better or not.”*
  She was responding to Goutham's live summary, which described the analysis as wanting *“to prove
  that activation model is better than FC reconfiguration”* — a framing this slide has never used.
  Her two conditions are both addressed rather than ignored: there is no prize being chased, because
  the slide claims no winner; and the doubt she was reacting to was a team disagreement about
  inclusion, not uncertainty about the evidence — the number is replicated across 20 partitions,
  survives a 1000-permutation null, and generalises to held-out people and runs. Removing it would
  also gut Slide 7's *Refined* column, which is the honest-negative beat NMA decks are built around,
  and it would delete the contribution Goutham spent two days arguing for. **If the team still
  prefers to follow the letter of the advice**, the fallback is to demote the activation half to
  backup Slide 9 and keep only the directional beat here — but Slide 7 must then be rewritten in the
  same pass, not left behind.
- **Speaker note / transition:** “El giro en dos tiempos. **Uno:** la dirección que predijimos
  existe — la segregación baja con la carga — pero como predictor individual es débil, así que la
  hipótesis direccional queda **matizada**, no confirmada. **Dos:** comprobamos si la señal era
  específica de conectividad, y no lo es claramente: un contraste de activación regional predice más
  fuerte. **No es una competición** — es post hoc, 360 rasgos frente a 78, y la activación de 0-back
  sola predice igual (0.571), así que ni siquiera es específica de carga. La activación **no borra**
  el resultado FC; impide afirmar que el mecanismo sea específico de conectividad. Nuestros controles
  (DVARS, acc_0bk) no capturan reactividad cerebrovascular, así que ese hueco queda declarado. **Si
  preguntan por qué mantenemos la medida más débil:** porque una resta elimina la varianza estable de
  rasgo (Hedge 2018), que es justo lo que infla la fiabilidad de la activación — argumento de
  Goutham, aceptado. **Nombrar los ejes** antes de leer ningún número.”
- **Evidence / provenance:** `pipeline/02` §7, the activation-controls block, and §8;
  `manifest.json` → `activation-robustness` (cells 18 and 20). Segregation figures quoted here come
  from `segregation-refinement` (cell 22), shown on backup Slide 8. The single-condition breakdown
  (activation 0-back alone **0.571**, 2-back alone **0.569**, contrast **0.600**) is canonical: it is
  computed in the `pipeline/02` §7 panel and stored as `res["load_specificity"]`. It was first found
  in [`nb08`](../../sandbox/jaime/08_activation_vs_reconfiguration.ipynb) cell 8 and raised by
  Goutham Arcod (23 Jul).
- **Scientific caveat:** Activation and FC are not feature-count matched (360 vs 78). Per-run
  centering makes 0-back, 2-back and their contrast strongly collinear — one activation axis seen
  three ways. **The benchmark is not load-specific:** a single-condition 0-back map predicts as well
  as the contrast, so the activation advantage cannot be attributed to the load manipulation. Its
  origin (efficiency, anatomy, vasculature) is not resolvable in this design; DVARS is controlled
  (partial 0.58) but no CVR proxy exists in this dataset. Claim no biological superiority, no
  FC-specific mechanism and no adaptive benefit.

## Slide 7 — Conclusion: what we predicted, and what the evidence did to it

- **Status:** Spoken · presenter **open**. **Keep projected during Q&A.** Andrea reviewed this slide
  and had no changes: *“Nice. Okay, perfect.”*
- **Audience-facing title:** *Predictive signal survives; connectivity-specific mechanism remains unresolved*
- **Visible copy:**

  **Survives — the pattern hypothesis**

  `A 78-feature FC difference predicts unseen 2-back accuracy.`

  `The model transfers across identity-disjoint same-HCP cohorts.`

  **Refined — the directional hypothesis**

  `Segregation fell under load, but larger shifts did not predict better performance.`

  `Reconfiguration showed no clear gain beyond 0-back FC.`

  `FC added no clear gain over activation under the current unmatched comparison.`

  **Unresolved**

  `Is the predictive information connectivity-specific, or shared with task activation?`

  `Vascular reactivity (CVR) is not controlled in the activation benchmark.`

- **Layout:** Three typographic columns — Survives / Refined / Unresolved — the third slightly wider.
  The first two headers name the two opening hypotheses so the loop closes. No figure.
- **Chart:** No pre-rendered chart.
- **Template mapping:** Valeria source slide 9 (conclusion/limitations), replacing L1/L2 and every
  placeholder.
- **Speaker note / transition:** “Cerrar nombrando las dos predicciones de la Slide 3: la de patrón
  **se sostiene**, la direccional **se matiza**. Frase final: *predictive signal survives;
  connectivity-specific mechanism remains unresolved.*”
- **Evidence / provenance:** `pipeline/02` §11–§12 (claim → result → figure → limitation table).
- **Scientific caveat:** Single-task observational study: it identifies neither causality, nor
  dynamic connectivity, nor adaptive benefit, nor biological specificity.

---

# Backup slides (not spoken)

Opened only if a question requires them. Styled as a distinct block, as in the prior-team decks.

## Slide 8 — Backup: the directional result in full

- **Audience-facing title:** *Group direction was real; the individual link was weak*
- **Visible copy:**

  `Group mean: 0-back 0.3271 → 2-back 0.3035`

  `Paired change: Δ = −0.0236; p = 3.45 × 10⁻⁵`

  `Across participants: r = −0.105; p = .054`

  `A reliable mean shift does not establish individual predictive relevance.`

- **Chart:** [`visuals/charts/segregation-refinement.png`](visuals/charts/segregation-refinement.png)
  at ≥ 460 pt — the coexistence of a group shift and a weak individual link is the whole point.
- **Purpose:** Demoted from the spoken deck so Slide 6 keeps one dominant figure. Open this if anyone
  asks what "the directional hypothesis was refined" actually means.
- **Evidence / provenance:** `pipeline/02` §8; `manifest.json` → `segregation-refinement` (cell 22).
- **Scientific caveat:** System segregation is a Chan-style scalar summary, not Newman modularity,
  and does not substitute for the 78-feature multivariate pattern. Do not reuse the submitted −0.048
  magnitude.

## Slide 9 — Backup: validation detail

- **Audience-facing title:** *The checks behind the primary result*
- **Visible copy:**

  `Fixed holdout: r = 0.312 in 67 unseen participants`

  `Full-refit null (seed 42): r = 0.405; p = 1/1001 ≈ .001`

  `B→A A-label permutation, fixed B predictions: p = 1/1001 ≈ .001`

  `Reconfiguration over 0-back FC: ΔR² = +0.0344 ± 0.0225 → no clear gain`

  `FC over activation: ΔR² = −0.0030 ± 0.0065 → no clear gain`

  `The permutation p belongs only to seed-42 r = 0.405; the holdout is a separate split.`

- **Chart:** [`visuals/charts/null-and-holdout.png`](visuals/charts/null-and-holdout.png) at ≥ 460 pt.
  [`visuals/charts/incremental-fc-test.png`](visuals/charts/incremental-fc-test.png) stays in the
  library for a question specifically about incremental value.
- **Purpose:** Demoted from spoken Slide 5. Open for "how do you know it is not chance?" or "what
  about the holdout?"
- **Evidence / provenance:** `pipeline/02` §5–§7; `manifest.json` → `null-and-holdout` (cell 12),
  `incremental-fc-test` (cell 18).
- **Scientific caveat:** The 2-SD decision rule is a split-sensitivity heuristic, not a formal
  superiority or equivalence test.

## Slide 10 — Backup: future work

- **Audience-facing title:** *Five tests could resolve the remaining question*
- **Visible copy:**

  `1. Match activation and FC dimensionality in nested participant-level CV.`

  `2. Separate task coactivation from coupling with a prespecified estimator.`

  `3. Test independent-site, repeat-session, family-aware generalization.`

  `4. Run the activation model on resting-state amplitude: if rest predicts 2-back accuracy as well as task frames, the signal is task-independent.`

  `5. Model the load transition as a dynamic graph (ST-GNN) instead of one static difference, so the network reorganisation is learned rather than summarized.`

  `Decision criterion: FC must add reliable held-out value beyond activation and single-condition FC.`

- **Chart:** No pre-rendered chart. Native numbered list plus the decision criterion.
- **Speaker note:** “Cada experimento ataca respectivamente comparabilidad, coactivación,
  generalización, independencia de tarea y representación. El **quinto es propuesta de Goutham
  Arcod**, que ya está construyendo un pipeline ST-GNN en una rama propia (aún sin publicar en el
  remoto el 23 jul). Su argumento: una red de grafos espacio-temporal deja que las aristas se
  actualicen en el tiempo, de modo que el modelo *observa* la reorganización de los módulos en vez de
  resumirla en una resta. Queda como dirección futura por decisión de alcance del 22 jul, no por
  desacuerdo técnico — y Andrea mencionó que NMA abre un programa de continuación en
  septiembre/octubre, que es la ventana natural para ejecutarlo. El cuarto es también **propuesta de
  Goutham (23 jul)** y es
  **ejecutable con lo que ya tenemos**: cohorte B trae 4 runs de reposo (4,4 GB descargados) y
  `datasets.py` expone `load_rest_timeseries()`. Si alguien pregunta: un resultado positivo
  probaría que la señal es **independiente de la tarea**, no que sea vascular — un rasgo estable
  puede ser materia gris o arousal basal. Referencia para calibrar: Avery 2020 predice acc_2bk
  desde FC de reposo a r=0.20, así que que el reposo prediga algo es lo esperado; lo llamativo
  sería acercarse a 0.57.”
- **Evidence / provenance:** `pipeline/02` §12 claim–result–limitation table.
- **Scientific caveat:** These are proposed experiments, not completed analyses.

## Slide 11 — Backup: references and statistical guardrails

- **Audience-facing title:** *References and statistical guardrails*
- **Visible copy:**

  `Avery et al. (2020) · Distributed patterns of FC predict WM · J. Cognitive Neuroscience · PMC8004893`

  `Chan et al. (2014) · Decreased segregation of brain systems · PNAS`

  `Murphy et al. (2020) · Multimodal network dynamics underpinning WM · Nature Communications · 10.1038/s41467-020-15541-0`

  `Masharipov et al. (2024) · Task-modulated FC methods · Communications Biology · 10.1038/s42003-024-07088-3`

  `Hedge et al. (2018) · The reliability paradox · Behavior Research Methods · 10.3758/s13428-017-0935-1`

  `Logothetis (2008) · What we can do and what we cannot do with fMRI · Nature`

  `Full annotated bibliography: manuscript/references.md`

  `r = 0.366 ± 0.024 = mean ± split SD across 20 repeated-CV partitions.`

  `seed-42 r = 0.405; p ≈ .001 (1/1001) = full-refit permutation.`

  `B→A r = 0.398; 95% CI [0.25, 0.53] = identity-disjoint same-HCP transfer.`

- **Layout:** Two columns — references left, guardrail definitions right. This slide is where the
  statistical definitions live now that the spoken slides carry only one label each.
- **Chart:** No pre-rendered chart.
- **Open team decision — two parallel bibliographies (23 Jul).** The Google deck currently carries
  **two** reference slides: this one and Valeria's original (Shine 2016, Finc 2020, Zhang 2023,
  Shen 2017, Ray 2020). They are not competing versions — hers are *framing* citations (why the
  question matters), these are *claim-backing* citations (each one supports a sentence we say out
  loud). Only **Finc 2020** appears in both; Shine 2016, Zhang 2023, Shen 2017 and Ray 2020 are
  **not** in `manuscript/references.md` at all. Merge to a single slide, and if framing citations are
  kept, annotate them in `references.md` first. **Caution:** Shine 2016 and Zhang 2023 are
  *dynamic*-FC papers. Presenting them beside our condition-aggregated static difference invites the
  exact conflation the `dFC` label already caused — if they stay, say out loud that they are
  motivation, not our method.
- **How to present it (TA instruction 8).** Andrea: keep the references in the submitted deck, but
  *“it's useless to just read the references”* — the last presenter shows the slide, says these are
  the references we used, leaves it up for about five seconds, then takes questions. It costs no
  speaking minute. Note this also settles the bibliography question in principle: **one anchor
  citation on Slide 3** (instruction 4) and **the full list here**, nothing in between.
- **Evidence / provenance:** `manuscript/references.md`; `pipeline/02` §5, §6, §8 and §12.
- **Scientific caveat:** References frame or limit the work; they do not turn it into an exact
  replication or a causal validation. Logothetis frames the CVR gap on Slide 6 as a cited limitation,
  not a result of ours.

---

## Compression map: 15-slide internal-review version → this deck

| This deck | Internal slides | Reason |
|---|---|---|
| 1 (cover) | — | Structural; project name and authors, per prior-team convention. |
| 2 (team) | — | Structural; absorbs the roster formerly fused into the intro. |
| 3 (spoken) | 1–2 | Question and both hypotheses form one opening beat. |
| 4 (spoken) | 3–5 | Cohorts, feature construction and evaluation become one native pipeline schematic. |
| 5 (spoken) | 6, 8 | Primary CV and transfer; sub-checks demoted to backup 9. |
| 6 (spoken) | 9–12 | Directional refinement and the activation benchmark form one hinge; the segregation figure is demoted to backup 8. |
| 7 (spoken) | 13 | Conclusion, now naming both opening hypotheses. |
| 8 (backup) | 9–10 | Directional figure and full statistics. |
| 9 (backup) | 7, 11 | Null, fixed holdout and the incremental test. |
| 10 (backup) | 14 | Future work, now five tests. |
| 11 (backup) | 15 | References and the statistical guardrail definitions. |

Internal-review Slide 10 (anatomical context) stays out of both decks: it does not change any claim.
`condition-fc-contrast`, `anatomical-context`, `feature-construction`, `primary-repeated-cv` and
`incremental-fc-test` remain in the chart library as unassigned assets, still referenced by the
internal-review storyboard.

## Google deck reconciliation — review of 23 Jul

Reviewed against **fresh PDF exports** of the live team deck (Drive file `1A-FC-Hs2…Dk9E`), text
extracted and all pages rasterised. The current state — **19 slides** — is frozen in
[`source-snapshots/2026-07-23T17-42-40_CEST_valeria/`](source-snapshots/2026-07-23T17-42-40_CEST_valeria/),
whose metadata also carries the measured **format contract** (see below).

The deck is under **active multi-person editing**: `modifiedTime` advanced five times during the
afternoon (12:26:42Z → 13:20:29Z → 13:35:54Z → … → 15:05:07Z). Several corrections below were applied
while the review was still running, and one PDF export had to be discarded for being one edit stale.
Re-export and diff before trusting any row here.

### Live-deck numbering (19 slides) vs this storyboard (11)

A **Backup** divider was inserted, so the backup block shifted by one. Use the left column when
editing the Google deck and the right when reading this file.

| Live deck | This storyboard | |
|---|---|---|
| 1–2 | 1–2 | Cover, team |
| 3–7 | 3–7 | The five spoken slides |
| **8** | — | *New:* “Backup — Reference slides, opened only on demand during Q&A” |
| 9–12 | 8–11 | Backup: directional · validation · future work · references |
| 13–19 | — | Legacy tail: Valeria's four placeholder slides, two duplicate dividers, internal map |

**Numerical verdict: clean.** Every value on Google slides 3–11 matches `canonical_evidence.EXPECTED`
— cohort and pipeline counts, `0.398`/CI, `0.366 ± 0.024`, the four method means and SDs, `0.571`,
the segregation block, the holdout, the seed-42 null and both `ΔR²` values. The transcription from
this file into Slides introduced no numeric error. Everything below is text, layout or leftovers.

### Corrections (live deck numbering; status as of the 13:35:54Z revision)

| # | Slide | Fix | Severity | Status |
|---|---|---|---|---|
| 1 | 2 (Team) | Remove five stock portraits and the dummy roles *Actor / Doctor / Accountant / Chef / Journalist*; add the pod/TA line | Blocker | **Open** |
| 2 | 5 (Primary) | Image was left-cropped: y-axis title and the `0.` of every tick were cut. Reinsert `identity-disjoint-transfer.png` uncropped | Blocker | Done |
| 3 | 6 (Turn) | Replace the chart with the regenerated `activation-robustness.png` (label fix, below) | Blocker | Done |
| 4 | 3 (Intro) | “…as a different claims” → **“are different claims”** | Text | Done |
| 5 | 7 (Conclusion) | Title needs the semicolon: “Predictive signal survives**;** connectivity-specific…” | Text | Done |
| 6 | 6 (Turn) | Add the missing legend line `Open squares = held-out cross-run generalization.` — two open squares were unexplained | Text | Done |
| 7 | 4 (Method) | Add the definition line (see Slide 4 above) | Content gap | Done |
| 8 | 6 (Turn) | `Activation contrast: 0.600 ± 0.016` is pale sand on a pale ground; darken it | Legibility | **Open** |
| 9 | 17, 18 | Delete the empty duplicate divider and the internal compression map | Hygiene | **Open** |
| 10 | 12–15 | Valeria Moraga's legacy slides — agree with her before removing or merging, they are her contribution | Team decision | **Open** |
| 11 | 11 vs 15 | Resolve the two parallel bibliographies (see Slide 11 above) | Team decision | **Open** |

### From the TA review (Andrea, 23 Jul Zoom) — all open

| # | Slide | Fix | Source |
|---|---|---|---|
| 12 | 3 (Intro) | Enlarge the question; step the two prediction blocks down one size | TA instruction 5 |
| 13 | 3 (Intro) | Add the single Avery 2020 anchor line — one citation, no more | TA instruction 4 |
| 14 | 4 (Method) | Add the FC and system-segregation definitions to the definitions band | TA instruction 1, raised by Arefeh |
| 15 | 4 (Method) | Delete `TR = 0.72 s`, `4 s HRF shift`, `312 frames per load`, `2 WM runs`, `360 × 360` | TA instruction 3 |
| 16 | 4 (Method) | Replace text boxes 3–5 with the three-matrix figure — **blocked** on re-rendering `condition-fc-contrast` as a pure plot | TA instruction 2 |
| 17 | 6 (Turn) | Retitle to *Two checks that narrowed what we can claim*; collapse four tiny caveats into two readable lines | TA instruction 7 + Discord consensus |
| 18 | 10 (Backup) | Fifth future-work item: ST-GNN, credited to Goutham Arcod | Discord 23 Jul |
| 19 | — | Settle presenters for slides 5, 6 and 7, and resolve the Goutham/Arefeh clash over slide 4 | TA instruction 10 |
| 20 | — | Rehearse to one minute per slide; Andrea offered tutorial time on Friday | TA instruction 10 |

### Legacy slides to delete, and why

- **12** — Valeria's `Our study aims to… / FC Reconfiguration Explanation???`. Both questions are now
  answered: the aims by Slide 3, the definition by the new Slide 4 line. It also still carries the
  superseded nb08 figures, whose labels render at 3–4 pt and whose rounding (`0.27 / 0.37 / 0.33 /
  0.60`) visually contradicts Slide 6.
- **13** — `Conclusion 1 / 2 / etc` and `L1 / L2` placeholders; superseded by Slide 7.
- **14** — `IMPORTANT CONCEPTS`. **Delete on content grounds, not just tidiness:** it says the result
  *“substantially changes our conclusion,”* which contradicts the narrative framing rule at the top
  of this file. We pre-specified two hypotheses; one held and one was refined. Nothing changed.
- **15** — Valeria's reference slide; fold into Slide 11 per the decision above.
- **17** — empty duplicate of the “Complementary Slides” divider on 16.
- **18** — `INTERNAL SLIDE: Compression map`. A working artefact of this storyboard; it must not
  travel in a deck that gets projected or shared outside the pod.

### Format contract — follow Valeria's grammar, do not invent a second one

Measured from the snapshot PPTX on a **720 × 405 pt** canvas. Any slide we add must match these, so
an edit pastes into the shared deck without restyling. Full values in the snapshot metadata under
`format_contract`.

| Element | Geometry | Type |
|---|---|---|
| Page margin | 24 pt left/right → content width 672 | — |
| Slide title | L 24 · T 18 · W 672 · H 30–42 | 16 pt |
| Section label | T 60 | 11 pt |
| Body | — | 8–9 pt |
| Two-column grid | left L 24 W 326.2 · right L 369.8 W 326.2 · gutter 19.6 | — |
| Card block | W 326.2 · H 55.5 · 63 pt pitch | — |
| Content top | charts and cards from T 82.5 | — |
| Footer band | full width at T 380.5 · H 24.5; title left at L 7.5, “The Gammas” right at L 390, logo centred | 9 pt |

Palette from the theme: ink `#202729`, white `#FFFFFF`, greens `#4BA173` / `#63D297`, greys
`#353744` `#424242` `#616161` `#999999`, alerts `#FF5252` `#FFF176`. The cream page and sand footer
are **shape fills, not theme colours** — copy an existing slide rather than recolouring by hand.
`theme1.xml` declares Arial, but no run sets a font name, so the rendered face comes from the Google
Slides theme; our charts embed Poppins, which is close enough at projection size and is why chart
type must never try to match slide type exactly.

**Chart width — resolved.** The old flat “≥ 460 pt” rule and the deck disagreed; the rule lost,
because it was written against a full-width layout and these slides are two-column. Measured widths
are now recorded in the production rules at the top of this file and accepted deliberately.

### Our optimized deck

[`the-gammas-w3d5-optimized.pptx`](the-gammas-w3d5-optimized.pptx) — **12 slides**, built from the
snapshot so it inherits the theme, layouts, footer and logo unchanged. Everything in it is specified
above. Review, then replace the Google deck or paste slide by slide.

Structural work applied on top of the content edits:

- **Slide 4 rebuilt three times before it was right.** First pass left the figure floating outside
  the numbered flow; second pass put Model and Held-out side by side and their header strips would
  not align; the third folded them into one band. Final shape: row 1 `[1 Cohort] [2 Condition
  frames] [evidence panel]`, row 2 `[3 Model and held-out evaluation]` full width. Numbering now
  matches reading order and there is no dead quadrant.
- **Slide 9 chart un-squashed** — it had been dragged to 451.4 × 196.4 from an uncropped 16:9
  source, a 22 % vertical compression. Height restored to `width × 9/16`.
- **Section labels added** to slides 3–12; slide 5's buried “Analysis” heading deleted, and slide 3's
  inline “Introduction” promoted to the same standard eyebrow as the rest.
- **Definitions split on Arefeh Lali Dehaghi's proposal** — plain-language notion on Slide 3, formula
  and Pearson detail on Slide 4. See the Slide 4 section for why it is a split and not a move.
- **Text boxes this script creates need `word_wrap = True`.** `add_textbox()` ships with wrapping
  off, so the first version of the lengthened figure caption ran straight off the right edge of the
  canvas — and the geometry check passed it, because the *box* was inside the canvas.
- **Slide 2** dummy roles removed. The stock portraits for Kerem Akyurt and Goutham Arcod remain —
  that needs their photographs, not an edit. Arefeh Lali Dehaghi's and Valeria Moraga's personal
  email addresses are on a deck NMA archives publicly; worth asking them before it ships.
- **Slide 7** keeps three half-empty columns. Left alone deliberately: the cards cannot be shortened
  without rescaling their text, and a conclusion slide that stays projected through Q&A is the one
  place where whitespace costs nothing.

**Rendering is not optional before sharing.** The first build passed every geometric check — no
overlaps, no off-canvas shapes, no duplicate shape ids — and still overflowed two cards on the
method slide, because nothing in the toolchain measures rendered text. See the README for the
PowerPoint-via-AppleScript recipe; LibreOffice cannot do it on this machine.

### Chart label defect found and fixed (23 Jul)

`activation-robustness` shipped the reconfiguration predictor as **`dFC pattern`**. In the fMRI
literature `dFC` reads as *dynamic* FC — a claim the delivery checklist explicitly forbids and that
our design cannot support, since we subtract two condition-aggregated **static** matrices. The risk
was live: Valeria's reference slide cites two dynamic-FC papers, so the deck was one question away
from a conflation we had no clean answer for. Renamed to **`FC reconfiguration`** across the five
occurrences in `visuals/src/generate_visuals.py` (`activation-robustness`, `incremental-fc-test`,
`anatomical-context`, `feature-construction`), library regenerated, 18/18 contract tests pass. Of the
four charts used in the deck, only `activation-robustness.png` changes visually.

## Delivery checklist

- **Five presenters, five spoken slides (3–7), one each.** Cover, team and backup carry no timed
  slot. Valeria Moraga opens on Slide 3; Goutham Arcod has Slide 4; **5, 6 and 7 are still unassigned
  and must be settled before rehearsing.**
- **Six presenters:** split Slide 6 across two people — presenter A takes the directional bridge,
  presenter B takes the activation benchmark and the caveats — keeping one slide projected. Do not
  promote a backup slide to create a sixth slot.
- **Define every concept the moment you name it** — functional connectivity, FC reconfiguration,
  system segregation. Andrea's most repeated instruction, and Arefeh asked for it directly.
- **Name the axes out loud before quoting any number from a figure.** Applies to Slides 4, 5, 6 and
  to every backup slide opened in Q&A: *“always make sure that people know what they're looking at.”*
- **Rehearse against the clock until one slide fits one minute.** Andrea offered a rehearsal round
  and Friday tutorial time. Also pre-agree who answers what in Q&A.
- **Nobody's spoken summary may claim more than the slides.** In the 23 Jul Zoom the verbal summary
  drifted into *“working memory performance relies on … adaptive transition towards network states”*
  — that is the directional hypothesis we **refined**, not confirmed: the group shift is real
  (p = 3.45 × 10⁻⁵) but the individual link is weak (r = −0.105, p = .054). Rehearsing together is
  what catches this; each presenter reading their own slide is not enough.
- Aim for 460 pt of chart width; where a two-column layout caps it lower, record the measured width
  in this file rather than letting the rule and the deck disagree. No insets; never two charts on
  one slide.
- Every slide carries its section label; every figure is named aloud before any number is read.
- Say “identity-disjoint same-HCP transfer,” never “independent external validation.”
- Say “split SD,” never “confidence interval,” for repeated-CV `±` values.
- Pair the full-refit permutation only with seed-42 `r = .405`; label the B→A permutation separately.
- Say “we predicted two things; one held, one was refined.” Never “our hypothesis evolved/changed.”
- Do not claim causality, dynamic FC, adaptive benefit, or an FC-specific mechanism. This applies to
  **chart axis labels too**: never abbreviate the reconfiguration predictor as `dFC`, which reads as
  *dynamic* FC. Say “FC reconfiguration” or “FC change” (fixed 23 Jul; the activation chart shipped
  the wrong label to the shared Google deck).
- State the activation caveats out loud on Slide 6: post hoc, unmatched 360 vs 78, and CVR
  uncontrolled.
- Keep Slide 7 visible during Q&A; open backup slides only on demand.
- Rehearse Slide 6 against the clock — it carries two beats and is the likeliest overrun.
- Export a PDF fallback: Poppins may not be installed on the presenting machine.
