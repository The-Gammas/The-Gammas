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
  projection size. The four slide charts are drawn at 26–30 pt on the 1152 pt canvas and placed
  **470 pt wide**, so their type lands at **≈ 10.6 pt on screen** — never two charts on one slide,
  never an inset.
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

- **Status:** Spoken · Presenter 1.
- **Audience-facing title:** *Does load-related brain connectivity predict working-memory performance?*
- **Visible copy:**

  **We predicted two things**

  **Pattern**  `A 78-feature FC fingerprint of the 2-back − 0-back change predicts performance.`

  **Direction**  `Higher load shifts networks toward integration; larger shifts accompany better performance.`

  `A distributed pattern and a one-number direction are different claims.`

- **Layout:** Large question, then the two predictions as two labelled blocks with the reconciling
  line beneath. The team roster is **not** here — it lives on Slide 2, which frees the vertical space
  the two hypotheses need.
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

- **Status:** Spoken · Presenter 2.
- **Audience-facing title:** *We evaluated a 78-feature FC difference in held-out people*
- **Definition line — required, set directly under the title:**

  `FC reconfiguration = how much each network pair changes its coupling when memory load goes from 0-back to 2-back.`

  Added 23 Jul. The deck's own title word was never defined in plain language on any spoken slide;
  the schematic supplied only the formula, which is not the same thing for an audience seeing the
  design for the first time. Raised by **Valeria Moraga** on her source slide 7 (“FC Reconfiguration
  Explanation???”), and she was right — the gap was real. The sentence is a plain restatement of
  `pipeline/02` §4, so it adds no claim.

- **Visible copy — seven schematic boxes, left to right:**

  `1 · Cohort` — `336 participants · HCP N-back · 2 WM runs · 360 Glasser ROIs · TR 0.72 s`

  `2 · Condition frames` — `4 s HRF shift · 312 frames per load · no 0-back/2-back overlap`

  `3 · FC per condition` — `360 × 360 Pearson correlation, computed for 0-back and 2-back`

  `4 · Network fingerprint` — `12 within + 66 between = 78 values over Cole-Anticevic networks`

  `5 · Reconfiguration` — `fingerprint(2-back) − fingerprint(0-back) → 336 × 78`

  `6 · Model` — `StandardScaler + RidgeCV, fitted inside each training fold`

  `7 · Held-out evaluation` — `repeated 5-fold CV · fixed holdout · 1000-permutation null · B→A transfer (301 → 100, identity-disjoint)`

  `All splits hold out participants; “±” = split SD, not CI.`

- **Layout:** Boxes 1–4 across the top row, boxes 5–6 on a second row, box 7 as a full-width terminal
  band. Rounded rectangles with connectors; box label in semibold, detail line beneath in a lighter
  weight.
- **Chart:** No pre-rendered chart. **Native pptx shapes** — this is deliberate. The chart library
  validates every visible number against the live notebook namespace and admits only data-derived
  evidence; a conceptual box-and-arrow pipeline has no array to validate. Native vector text is also
  immune to the downscale that makes generated charts illegible. The previously assigned
  `feature-construction` chart is **removed from the deck**: it covered only step 4 and rendered its
  labels at ~3.6 pt. It remains in the library, referenced by the internal-review storyboard.
- **Template mapping:** The pipeline flow proposed on Valeria source slide 5, with every
  graph-construction and graph-metric stage replaced by what we actually ran.
- **Speaker note / transition:** “Un solo recorrido: de los escáneres a una predicción en personas no
  vistas. Scaler y RidgeCV se ajustan **dentro** de cada fold; nunca se separan runs o frames de la
  misma persona. B estima el modelo; A comprueba transferencia sin identidades compartidas.”
- **Evidence / provenance:** `pipeline/02` §3–§4 and §5–§6. `TR = 0.72 s` from
  [`datasets.py:37`](../../sandbox/jaime/datasets.py); HRF delay, frame counts and the 78-block
  summary from `preprocessing.py` and `connectivity.py`. Counts must be copied from
  `visuals/manifest.json`, not retyped from memory — this schematic is the one place in the deck
  where a number has no automated test behind it.
- **Scientific caveat:** Pearson task FC can reflect task-evoked coactivation; it does not
  demonstrate interregional communication or causality.

## Slide 5 — Primary result: the FC pattern predicts, and it transfers

- **Status:** Spoken · Presenter 3.
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
- **Speaker note / transition:** “El efecto primario es la media de CV repetida, `.366 ± .024`. La
  transferencia usa modelos entrenados solo en B y aplicados a A sin identidades compartidas: no es
  validación en otro sitio. Si preguntan por el holdout fijo o por el null, están en backup.
  Transición: establecida la predicción, toca revisar lo que **no** salió como esperábamos.”
- **Evidence / provenance:** `pipeline/02` §5–§6 and panels 9B/9C; `manifest.json` →
  `identity-disjoint-transfer` (cell 14).
- **Scientific caveat:** The SD summarizes sensitivity across 20 overlapping partitions, not
  population uncertainty. Sibling HCP cohorts are not cross-site generalization; kinship is
  unmodelled.

## Slide 6 — The turn: the signal survives, but it is not specific to connectivity

- **Status:** Spoken core; required to support the refined final conclusion. Presenter 4 — this is
  the hinge of the talk.
- **Audience-facing title:** *The prediction held—but a simpler regional signal predicted better*
- **Visible copy:**

  `Repeated-CV correlation (mean ± split SD across 20 partitions)`

  `0-back FC  0.274 ± 0.032    ·    FC reconfiguration  0.366 ± 0.024`

  `0-back + reconfiguration  0.333 ± 0.026    ·    Activation contrast  0.600 ± 0.016`

  **Direction, as predicted—but only at group level**
  `Segregation fell under load (0.3271 → 0.3035; Δ = −0.0236; p = 3.45 × 10⁻⁵), yet larger shifts did not predict better performance (r = −0.105; p = .054).`

  `Open squares = held-out cross-run generalization.`

  `0-back activation alone predicts as well (0.571) — the benchmark is not load-specific.`

  `No biological winner is claimed. Post hoc, unmatched: 360 regional activation vs 78 network FC features.`

  `Activation = mean BOLD(2-back) − mean BOLD(0-back), not a GLM beta. Vascular reactivity (CVR) not controlled.`

- **Layout:** The activation comparison chart is the **only** figure. The directional result is a
  single highlighted text block, not a second figure. Caveats occupy a compact lower band. If it does
  not fit at legible type, cut caveat wording — never add a second chart.
- **Chart:** [`visuals/charts/activation-robustness.png`](visuals/charts/activation-robustness.png)
  only, placed at ≥ 460 pt. Do **not** add `incremental-fc-test.png` (duplicates the numbers) and do
  **not** add `segregation-refinement.png` here — that figure is backup Slide 8.
- **Template mapping:** Valeria source slide 8 (sparse unexpected finding), rebuilt for the benchmark
  and its guardrails.
- **Speaker note / transition:** “El giro en dos tiempos. **Uno:** la dirección que predijimos
  existe — la segregación baja con la carga — pero como predictor individual es débil, así que la
  hipótesis direccional queda **matizada**, no confirmada. **Dos:** al probar si la señal era
  específica de conectividad, un contraste de activación regional mucho más simple predijo mejor. Es
  una prueba **post hoc**, no una competición biológica justa: 360 rasgos frente a 78, sin igualar
  dimensionalidad. La activación **no borra** el resultado FC; impide afirmar que el mecanismo sea
  específico de conectividad. Y nuestros controles (DVARS, acc_0bk) no capturan reactividad
  cerebrovascular, así que ese hueco queda declarado.”
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

- **Status:** Spoken · Presenter 5. **Keep projected during Q&A.**
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

- **Audience-facing title:** *Four tests could resolve the remaining question*
- **Visible copy:**

  `1. Match activation and FC dimensionality in nested participant-level CV.`

  `2. Separate task coactivation from coupling with a prespecified estimator.`

  `3. Test independent-site, repeat-session, family-aware generalization.`

  `4. Run the activation model on resting-state amplitude: if rest predicts 2-back accuracy as well as task frames, the signal is task-independent.`

  `Decision criterion: FC must add reliable held-out value beyond activation and single-condition FC.`

- **Chart:** No pre-rendered chart. Native numbered list plus the decision criterion.
- **Speaker note:** “Cada experimento ataca respectivamente comparabilidad, coactivación,
  generalización e independencia de tarea. El cuarto es **propuesta de Goutham Arcod (23 jul)** y es
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
| 10 (backup) | 14 | Future work, now four tests. |
| 11 (backup) | 15 | References and the statistical guardrail definitions. |

Internal-review Slide 10 (anatomical context) stays out of both decks: it does not change any claim.
`condition-fc-contrast`, `anatomical-context`, `feature-construction`, `primary-repeated-cv` and
`incremental-fc-test` remain in the chart library as unassigned assets, still referenced by the
internal-review storyboard.

## Google deck reconciliation — review of 23 Jul

Reviewed against **fresh PDF exports** of the live team deck (Drive file `1A-FC-Hs2…Dk9E`,
**18 slides**), text extracted and all pages rasterised. The frozen copy in
`source-snapshots/2026-07-22T19-06-12_CEST_valeria/` predates this content — it is the 15-slide
version from 22 Jul and does **not** contain the transcribed spoken slides. Today's state is frozen
in `source-snapshots/2026-07-23T15-39-22_CEST_valeria/`.

The deck was being **edited live during the review**: `modifiedTime` advanced three times within the
hour (12:26:42Z → 13:20:29Z → 13:35:54Z), and six of the corrections below were applied by Jaime
while the review was still running. Re-export and diff before trusting any row here.

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
  slot.
- **Six presenters:** split Slide 6 across two people — presenter A takes the directional bridge,
  presenter B takes the activation benchmark and the caveats — keeping one slide projected. Do not
  promote a backup slide to create a sixth slot.
- No chart below 460 pt wide; no insets; never two charts on one slide.
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
