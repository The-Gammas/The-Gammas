# The Gammas — condensed final storyboard (9 slides)

## Production-wide rules

- **Document status:** presentation-ready scientific flow for Friday. Slides 3–7 are the five core
  content slides; Slides 8–9 remain hidden support.
- **Visible language:** concise English. **Production language:** Spanish.
- **Visual system:** 16:9 (720 × 405 pt), Poppins, restrained taupe/brown/pale-mint Neuromatch palette, generous margins, large takeaway titles, a simple footer/page marker, and one principal evidence visual per slide.
- **Template hygiene:** the template supplies visual grammar only. Remove every placeholder, old result image, fake biography, stock portrait, source comment, comment-author record, speaker note and hidden review artifact; do not invent people, figures, or results. Keep the frozen snapshot unchanged.
- **Statistical guardrail:** repeated-CV `±` is SD across 20 overlapping split partitions, never a confidence interval. The seed-42 full-refit permutation and the B→A fixed-prediction label permutation are distinct tests.
- **Density fallback:** never shrink narrative type to force a layout. On Slide 4, move the fixed
  holdout and null details to notes/backup before reducing type. On Slide 6, let the dot plot carry
  the four model values and keep only the two ΔR² decisions plus the unmatched/mean-BOLD guardrail
  as prose.
- **Empirical assets:** reuse only the evidence in `visuals/charts/`. Slides without an assigned chart
  are built later with native text/layout; no separate diagram image is required.

## Slide 1 — Title

- **Status:** Pre-roll; no allocated speaking beat.
- **Audience-facing title:** *Does load-related brain connectivity predict working-memory performance?*
- **Visible copy:**

  `THE GAMMAS · NMA COMPUTATIONAL NEUROSCIENCE 2026`

  `HCP N-back · participant-level prediction`

- **Layout:** Título grande sobre fondo limpio; un único subtítulo pequeño y pie discreto.
- **Chart:** No pre-rendered chart. Mantener la portada tipográfica y mínima; no convertir la
  pregunta en un diagrama.
- **Template mapping:** Valeria source slide 1 (title composition), shortened substantially.
- **Speaker note / transition:** “Abrimos con una pregunta predictiva, no causal.” Dejarla como pre-roll y pasar directamente a la pregunta e hipótesis.
- **Evidence / provenance:** Detailed internal-review storyboard, Slides 1–2; canonical pipeline framing cited there.
- **Scientific caveat:** “Reconfiguration” es una diferencia entre dos FC agregadas por condición, no conectividad dinámica.

## Slide 2 — Introduction

- **Status:** Spoken introduction.
- **Audience-facing title:** *A distributed pattern and a directional shift are different hypotheses*
- **Visible copy:**

  **Question**  `Can 2-back − 0-back FC predict 2-back accuracy in unseen participants?`

  **Pattern hypothesis**  `A 78-feature FC fingerprint predicts performance.`

  **Directional hypothesis**  `Higher load shifts networks toward integration; larger shifts accompany better performance.`

  `Distributed pattern ≠ one-number direction.`

- **Layout:** Izquierda, pregunta y vector de 78 rasgos; derecha, eje único `segregation ↔ integration`; frase final uniendo ambos.
- **Chart:** No pre-rendered chart. Resolver la distinción pattern/scalar con texto y formas nativas
  simples; no generar una ilustración independiente.
- **Template mapping:** Valeria source slides 3–4: balance text/right-space plus sparse hypothesis composition; remove unfinished bullet.
- **Speaker note / transition:** “La predicción multivariada puede sobrevivir aunque el escalar direccional falle. Ahora fijamos cómo representamos y evaluamos esa diferencia.”
- **Evidence / provenance:** Detailed internal-review storyboard, Slides 1–2; `pipeline/02_canonical_analysis_and_slides.ipynb` cells 0, 11, 21 and `docs/project-plan.md` as cited there.
- **Scientific caveat:** La hipótesis direccional es más restrictiva: exige un signo y comprime una estructura multivariada a un escalar.

## Slide 3 — Core 1: Method

- **Status:** Spoken core.
- **Audience-facing title:** *We evaluated a 78-feature FC difference in held-out people*
- **Visible copy:**

  `Cohort B: 336 complete participants → primary model`

  `Two pooled WM runs · 312 HRF-shifted frames / condition`

  `Pearson FC: 360 regions → 12 networks → 78 features`

  `FC reconfiguration = fingerprint(2-back) − fingerprint(0-back)`

  `Repeated 5-fold CV · fixed holdout · full-refit permutation · B→A transfer`

  `All splits hold out participants; “±” = split SD, not CI.`

- **Layout:** Flujo horizontal compacto: B cohort → 0/2-back matrices → 12-network triangle/vector → cuatro esquemas de evaluación. La banda inferior lleva el guardrail estadístico.
- **Chart:** [`visuals/charts/feature-construction.png`](visuals/charts/feature-construction.png).
  Usarlo como único visual empírico. Cohortes y evaluación se presentan como texto lateral, sin
  pictogramas ni diagrama de flujo.
- **Template mapping:** Native 16:9 process role, borrowing the rhythm of Valeria source slide 5 but replacing every graph-construction/graph-metric stage.
- **Speaker note / transition:** “Scaler y RidgeCV se ajustan dentro de cada fold; nunca se separan runs o frames de la misma persona. B estima el modelo; A nos permite comprobar transferencia sin identidades compartidas.”
- **Evidence / provenance:** Detailed internal-review storyboard, Slides 3–5: B=339 / 336 complete, A=100, 360 regions, 12 networks, 78 features, 4-s HRF shift, 312 frames; `pipeline/02` and sandbox modules cited there.
- **Scientific caveat:** FC de tarea basada en Pearson puede reflejar coactivación evocada por tarea; no demuestra comunicación interregional ni causalidad.

## Slide 4 — Core 2: Primary prediction and transfer

- **Status:** Spoken core.
- **Audience-facing title:** *The FC pattern predicted performance—and transferred across identity-disjoint cohorts*
- **Visible copy:**

  **Primary repeated CV**  `r = 0.366 ± 0.024`

  `336 participants · 78 FC features · 2-back accuracy`

  **Fixed holdout**  `r = 0.312 in 67 unseen participants`

  **Full-refit null (seed 42)**  `r = 0.405; p = 1/1001 ≈ .001`

  **B→A transfer**  `r = 0.398; bootstrap 95% CI [0.25, 0.53]`

  `301 B-only → 100 A · 35 shared identities removed`

  `Identity-disjoint same-HCP transfer—not independent-site validation.`

- **Layout:** Un campo de evidencia con transferencia dominante e inset de repeated-CV; holdout y
  null quedan como comprobaciones compactas y subordinadas, con etiquetas de estimando distintas.
- **Chart:** [`visuals/charts/identity-disjoint-transfer.png`](visuals/charts/identity-disjoint-transfer.png)
  como panel dominante y [`visuals/charts/primary-repeated-cv.png`](visuals/charts/primary-repeated-cv.png)
  como inset compacto. Mantener
  [`visuals/charts/null-and-holdout.png`](visuals/charts/null-and-holdout.png) como backup: si no cabe
  a tipografía legible, mostrar sus cifras en texto y no insertar el tercer chart.
- **Template mapping:** Valeria source slide 7 (evidence chart + explanation), con gráfico antiguo y placeholders sustituidos por evidencia canónica.
- **Speaker note / transition:** “El efecto primario es la media CV, `.366 ± .024`; el p de refit completo pertenece solo al seed-42 `.405`. La transferencia usa modelos B-only y A sin identidades compartidas; no es validación en otro sitio. Con la predicción establecida, examinamos la dirección que habíamos propuesto.”
- **Evidence / provenance:** Detailed internal-review storyboard, Slides 6–8; canonical `pipeline/02` cells 9–16 and panel 9C as cited there.
- **Scientific caveat:** La SD resume sensibilidad a 20 particiones solapadas, no incertidumbre poblacional. La CI bootstrap cuantifica A; cohortes HCP hermanas no constituyen generalización entre sitios.

## Slide 5 — Core 3: Directional refinement

- **Status:** Spoken core.
- **Audience-facing title:** *Segregation fell under load, but the individual link was weak*
- **Visible copy:**

  `Group mean: 0-back 0.3271 → 2-back 0.3035`

  `Paired change: Δ = −0.0236; p = 3.45 × 10⁻⁵`

  `Across participants: r = −0.105; p = .054`

  `A mean load effect did not convincingly predict who performed better.`

- **Layout:** Izquierda, distribución emparejada 0-back/2-back; derecha, scatter individual y las dos estadísticas; conclusión a todo el ancho en el pie.
- **Chart:** [`visuals/charts/segregation-refinement.png`](visuals/charts/segregation-refinement.png).
  Usarlo completo: la coexistencia del cambio grupal y el vínculo individual débil es la evidencia
  central de la slide.
- **Template mapping:** Native sparse-result role using Valeria source slide 8’s unexpected-finding composition.
- **Speaker note / transition:** “Separar el cambio medio pareado de la asociación entre personas. La dirección media existe, pero no respalda el mecanismo individual simple que esperábamos. Probamos entonces si el patrón FC aporta algo inequívocamente específico.”
- **Evidence / provenance:** Detailed internal-review storyboard, Slide 9; `pipeline/02` cells 21–22 and figure 9D as cited there.
- **Scientific caveat:** System segregation es un resumen escalar tipo Chan, no modularidad de Newman; no sustituye el patrón multivariado de 78 rasgos.

## Slide 6 — Core 4: Robustness surprise

- **Status:** Spoken core; required to support the refined final conclusion.
- **Audience-facing title:** *A post hoc regional activation benchmark predicted more strongly*
- **Visible copy:**

  `Repeated-CV correlation (mean ± split SD across 20 partitions)`

  `0-back FC                         r = 0.274 ± 0.032`

  `FC reconfiguration                r = 0.366 ± 0.024`

  `0-back + reconfiguration          r = 0.333 ± 0.026`

  `Activation contrast                r = 0.600 ± 0.016`

  `Matched-fold increments (split-sensitive 2-SD heuristic; no formal superiority test)`

  `Reconfiguration over 0-back  ΔR² = +0.0344 ± 0.0225 → no clear gain`

  `FC over activation                ΔR² = −0.0030 ± 0.0065 → no clear gain`

  `Post hoc, unmatched comparison: 360 regional activation vs 78 network FC features.`

  `Activation = mean BOLD(2-back) − mean BOLD(0-back), not a GLM beta.`

- **Layout:** Una comparativa de cuatro filas; debajo, dos anotaciones ΔR² emparejadas. Activation y FC se distinguen solo con color sobrio; los caveats visibles ocupan el tercio inferior.
- **Chart:** [`visuals/charts/activation-robustness.png`](visuals/charts/activation-robustness.png).
  Es el único chart de la slide y ya contiene la comparación de cuatro modelos y los dos checks
  incrementales. No añadir `incremental-fc-test.png`, porque duplicaría cifras en el formato final.
- **Template mapping:** Valeria source slide 8 (sparse unexpected finding), reconstruida para el benchmark y sus guardrails.
- **Speaker note / transition:** “Es una prueba post hoc de robustez, no una competición biológica justa: las representaciones difieren en número y escala de rasgos. Los dos ΔR² se calculan por folds emparejados y su regla 2-SD es una heurística de sensibilidad al split, no un test formal de superioridad. La activación no borra el hallazgo predictivo FC; impide afirmar que el mecanismo sea específico de conectividad.”
- **Evidence / provenance:** Detailed internal-review storyboard, Slides 11–12; `pipeline/02` cells 17–20 and `sandbox/jaime/08_activation_vs_reconfiguration.ipynb` as cited there.
- **Scientific caveat:** Activación y FC no están igualadas (360 vs 78); el contraste está fuertemente ligado a condiciones de la misma tarea. Los incrementos emparejados solo muestran sensibilidad entre particiones, no superioridad formal. No afirmar superioridad biológica, mecanismo FC-específico ni beneficio adaptativo.

## Slide 7 — Core 5: Final spoken conclusion

- **Status:** Spoken core; **keep visible for Q&A**.
- **Audience-facing title:** *Predictive signal survives; connectivity-specific mechanism remains unresolved*
- **Visible copy:**

  **Survives**

  `A 78-feature FC difference predicts unseen 2-back accuracy.`

  `The model transfers across identity-disjoint same-HCP cohorts.`

  **Refined**

  `Larger segregation reductions did not convincingly predict better performance.`

  `Reconfiguration showed no clear gain beyond 0-back FC.`

  `FC added no clear gain over activation under the current unmatched comparison.`

  **Unresolved**

  `Is predictive information connectivity-specific rather than shared with task activation?`

- **Layout:** Tres columnas tipográficas “Survives / Refined / Unresolved”, con la última ligeramente más ancha. No añadir una figura nueva.
- **Chart:** No pre-rendered chart. La conclusión se resuelve con tres bloques tipográficos nativos;
  no reutilizar miniaturas de resultados.
- **Template mapping:** Valeria source slide 9 (conclusion/limitations), sustituyendo L1/L2 y todo placeholder.
- **Speaker note / transition:** “Esta es la frase final: *predictive signal survives; connectivity-specific mechanism remains unresolved.* Mantener esta slide durante preguntas; las dos siguientes solo se abren como soporte.”
- **Evidence / provenance:** Detailed internal-review storyboard, Slide 13; synthesis of canonical `pipeline/02` cells 27–30 and `docs/project-plan.md` as cited there.
- **Scientific caveat:** Estudio observacional de una única tarea: no identifica causalidad, conectividad dinámica, beneficio adaptativo ni especificidad biológica.

## Slide 8 — Future work (support)

- **Status:** Hidden/support; open only if discussion needs next steps.
- **Audience-facing title:** *Three tests could resolve the remaining question*
- **Visible copy:**

  `1. Match activation and FC dimensionality in nested participant-level CV.`

  `2. Separate task coactivation from coupling with a prespecified estimator.`

  `3. Test independent-site, repeat-session, family-aware generalization.`

  `Decision criterion: FC must add reliable held-out value beyond activation and single-condition FC.`

- **Layout:** Tres pasos numerados convergen en una pregunta final sí/no de valor incremental FC.
- **Chart:** No pre-rendered chart. Usar una lista numerada nativa y una línea final con el criterio
  de decisión; no generar un diagrama de flujo.
- **Template mapping:** Native process/support layout, retaining Valeria palette and footer; do not use a blank/placeholder source slide.
- **Speaker note / transition:** “No leer en la exposición principal. Cada experimento ataca respectivamente comparabilidad, coactivación y generalización.”
- **Evidence / provenance:** Detailed internal-review storyboard, Slide 14; its cited `pipeline/02` claim–result–limitation table and selected literature anchors.
- **Scientific caveat:** Son propuestas futuras, no análisis ya realizados; la conectividad de tarea puede contener coactivación y la transferencia actual depende de la misma tarea/HCP.

## Slide 9 — References and guardrails (support)

- **Status:** Hidden/support; Q&A only.
- **Audience-facing title:** *References and statistical guardrails*
- **Visible copy:**

  `Avery et al. (2020) · Distributed patterns of FC predict WM · J. Cognitive Neuroscience · PMC8004893`

  `Chan et al. (2014) · Decreased segregation of brain systems · PNAS`

  `Murphy et al. (2020) · Multimodal network dynamics underpinning WM · Nature Communications · 10.1038/s41467-020-15541-0`

  `Masharipov et al. (2024) · Task-modulated FC methods · Communications Biology · 10.1038/s42003-024-07088-3`

  `Hedge et al. (2018) · The reliability paradox · Behavior Research Methods · 10.3758/s13428-017-0935-1`

  `Full annotated bibliography: manuscript/references.md`

  `r = 0.366 ± 0.024 = mean ± split SD across 20 repeated-CV partitions.`

  `seed-42 r = 0.405; p ≈ .001 (1/1001) = full-refit permutation.`

  `B→A r = 0.398; 95% CI [0.25, 0.53] = identity-disjoint same-HCP transfer.`

- **Layout:** Dos columnas: referencias seleccionadas a la izquierda, guardrails estadísticos a la derecha; tamaño menor pero legible.
- **Chart:** No pre-rendered chart. Mantener referencias y guardrails como texto; no añadir
  miniaturas que dupliquen evidencia.
- **Template mapping:** Valeria source slide 11 (dense references), limitado a anclas seleccionadas y marcado como backup.
- **Speaker note / transition:** “Mantener oculta; usarla para procedencia, definición de segregación, SD vs CI o tipos de null.”
- **Evidence / provenance:** Detailed internal-review storyboard, Slide 15; `manuscript/references.md` and canonical pipeline cells listed there.
- **Scientific caveat:** Las referencias proporcionan marco o limitaciones; no convierten el análisis en réplica exacta ni validación causal.

## Compression map: detailed 15-slide internal-review version → final 9 slides

| Final slide | Internal slides compressed | Reason |
|---|---|---|
| 1 | 1 | Title held as pre-roll. |
| 2 | 1–2 | Question and two-part hypothesis form one introduction beat. |
| 3 | 3–5 | Cohorts, feature construction, and participant-level evaluation are one method story. |
| 4 | 6–8 | Primary CV, null/holdout, and transfer are one prediction-evidence story with labels kept distinct. |
| 5 | 9–10 | Directional refinement is retained; anatomy is omitted because it does not change the claim. |
| 6 | 11–12 | Incremental FC and activation benchmark combine into the specificity/robustness surprise. |
| 7 | 13 | Final spoken conclusion remains projected for Q&A. |
| 8 | 14 | Future work becomes hidden support. |
| 9 | 15 | References and statistical guardrails become hidden support. |

## Delivery checklist

- **Six presenters:** Slide 1 is silent pre-roll. Presenter 1 owns only the visible spoken introduction on Slide 2; Presenters 2–6 each own exactly one scientific slide (Slides 3–7). Slides 8–9 are not allocated in the timed talk.
- **Five presenters:** Slide 1 remains silent and Slide 2 is not shown. Build a visible five-person variant of Slide 3 titled *Can a 78-feature FC difference predict unseen performance?* Add the question and `pattern ≠ one-number direction` as its top introduction band, with the method pipeline below. Presenter 1 owns this single Introduction + Method slide; Presenters 2–5 own Slides 4–7. Thus both the introduction and final conclusion remain visible while every presenter owns exactly one projected spoken slide.
- Say “identity-disjoint same-HCP transfer,” never “independent external validation.”
- Say “split SD,” never “confidence interval,” for repeated-CV `±` values.
- Pair the full-refit permutation only with seed-42 `r = .405`; label B→A permutation separately if asked.
- Do not claim causality, dynamic FC, adaptive benefit, or FC-specific mechanism. Keep Slide 7 visible; leave Slides 8–9 hidden unless discussion requires them.
