# The Gammas — detailed internal-review storyboard

## Communication job

Al terminar, la audiencia de NMA debe entender que el patrón multivariado de cambio de FC entre
0-back y 2-back predice rendimiento y se transfiere entre dos cohortes HCP sin identidades
compartidas, pero que la hipótesis direccional y la especificidad de conectividad no quedan
establecidas; el benchmark regional de activación obliga a refinar la conclusión.

> **Relación con el deck hablado.** Este documento es la versión **larga de revisión interna** (15
> slides). El deck que se presenta el viernes es
> [`final-storyboard-5-plus-4.md`](final-storyboard-5-plus-4.md): **5 slides habladas + 4 de
> backup**, alineado con la estructura de los decks de equipos NMA 2025 en
> [`../../../references/nma_project_examples_2025/`](../../../references/nma_project_examples_2025/).
> Los cambios estructurales que ese deck aplica sobre este: el título deja de ser pre-roll mudo y se
> funde con la intro y la línea de equipo (slides 1–2 → 1); las slides 9–12 se comprimen en **una
> sola slide bisagra** con el dot plot de activación como única figura, y la figura de segregación
> baja a backup; el null y el holdout fijo bajan a backup para que la slide de resultado primario
> lleve una figura dominante; y la conclusión nombra en voz alta las dos hipótesis de apertura.
> Mapa completo → sección *Compression map* del deck final.

## Global production rules

- **Audiencia visible:** participantes y tutores de NMA; la redacción que aparece en pantalla va en
  inglés natural y directo.
- **Arco:** hypothesis → test → primary evidence → transfer → directional refinement → robustness
  surprise → refined conclusion.
- **Lenguaje estadístico:** `±` significa siempre desviación estándar entre 20 particiones de CV,
  nunca intervalo de confianza. Solo la transferencia B→A lleva bootstrap 95% CI.
- **Nulls distintos:** el null primario de refit completo pertenece solo a seed-42 `r=.405`; el p
  de transferencia, cuando se muestre, se etiqueta como permutación de labels A con predicciones
  B→A fijas (`1/1001 ≈ .001`).
- **Guardrail de inferencia:** no describir la FC de tarea como dinámica, causal, adaptativa ni
  específica de conectividad. “Reconfiguration” nombra aquí una diferencia entre dos matrices FC
  agregadas por condición.
- **Framing del relato (obligatorio en cualquier texto hablado):** no cambiamos la hipótesis al ver
  los datos. Pre-especificamos **dos** hipótesis; la evidencia **confirmó una y matizó la otra**.
  Decir *“predijimos dos cosas: una se sostuvo, la otra resultó más estrecha de lo esperado”*. Nunca
  decir que la hipótesis *evolucionó*, *cambió* o *fue reemplazada* — describiría mal la secuencia
  inferencial real.
- **Densidad:** una afirmación central por slide; máximo tres unidades visuales; toda limitación que
  cambie la lectura debe verse en pantalla, no quedar solo en las notas.
- **Charts:** usar únicamente los nueve assets empíricos de `visuals/charts/`. Cuando una slide no
  tenga chart asignado, resolverla después con tipografía o elementos nativos; no generar una imagen
  de relleno.

## Slide 1 — The question

**Purpose:** Abrir con la pregunta falsable y con el contraste de carga que estructura todo el
relato.

**Audience-facing title:** Can a load-related FC change predict working-memory performance?

**Visible copy:**

Small kicker: `THE GAMMAS · NMA COMPUTATIONAL NEUROSCIENCE 2026 · HCP N-BACK PROJECT`

> We asked whether the brain-wide functional-connectivity difference from 0-back to 2-back carries
> information about individual 2-back accuracy in unseen participants.

Small footer: `HCP N-back · low vs high working-memory load · prediction by participant`

**Layout:** Kicker pequeño arriba, seguido del título; una sola frase central de gran tamaño; abajo,
una línea visual 0-back → 2-back → predicted accuracy. Mantener esta slide deliberadamente limpia.

**Chart:** [`visuals/charts/condition-fc-contrast.png`](visuals/charts/condition-fc-contrast.png).
Usar las matrices reales y su diferencia como evidencia del contraste; añadir la pregunta
predictiva como texto nativo, sin flechas que sugieran causalidad temporal.

**Speaker notes and transition:** “Partimos de una pregunta predictiva, no causal. Si la diferencia
entre condiciones contiene información individual, debe generalizar a personas que el modelo no ha
visto.” Transición: “Eso nos llevó a formular dos expectativas distintas: una multivariada y otra
direccional.”

**Evidence/provenance:** `pipeline/02_canonical_analysis_and_slides.ipynb`, celdas 0 y 11;
`docs/project-plan.md`, “Working question”.

**Scientific caveat:** La diferencia 2-back − 0-back resume dos condiciones de una misma tarea; no
es una medida de dinámica temporal.

## Slide 2 — The original hypothesis had two parts

**Purpose:** Separar desde el principio la hipótesis predictiva del relato direccional, para que el
resultado posterior no parezca contradictorio.

**Audience-facing title:** Prediction and direction are separate hypotheses

**Visible copy:**

- **Pattern hypothesis:** the 2-back − 0-back FC fingerprint predicts 2-back accuracy in unseen
  participants.
- **Directional hypothesis:** higher load shifts the network toward integration, and larger shifts
  accompany better performance.

Bottom line: `These are separate tests: distributed pattern vs one-number direction.`

**Layout:** Dos columnas asimétricas: a la izquierda un vector de múltiples características; a la
derecha un único eje segregation ↔ integration. La línea inferior une ambas con “separate tests”.

**Chart:** No pre-rendered chart. Construir después una comparación tipográfica nativa:
“78-feature pattern” frente a “one segregation scalar”.

**Speaker notes and transition:** Explicar que un patrón puede predecir aunque una media direccional
no lo haga. Transición: “Para probar ambas partes necesitábamos una cohorte amplia para estimar y
otra que no reutilizara identidades para la transferencia.”

**Evidence/provenance:** `docs/project-plan.md`, “Original working hypothesis and current result”;
`pipeline/02`, celdas 0 y 21.

**Scientific caveat:** La hipótesis direccional era más fuerte que la hipótesis predictiva: impone
un signo y reduce una estructura multivariada a un escalar.

## Slide 3 — Two HCP cohorts serve different roles

**Purpose:** Fijar muestra, unidad de generalización y relación entre cohortes antes de mostrar
resultados.

**Audience-facing title:** One cohort estimates the model; the other tests transfer

**Visible copy:**

- **Cohort B:** 339 participants; 336 with complete 2-back behaviour — primary analysis.
- **Cohort A:** 100 participants — transfer test only.
- **Shared representation:** 360 Glasser cortical regions grouped into 12 networks; two WM runs.

Visible caveat: `Both cohorts come from HCP; transfer is not independent-site validation.`

**Layout:** Dos bloques horizontales B y A conectados por una flecha de entrenamiento→test. La
caveat va como pie visible, no como asterisco.

**Chart:** No pre-rendered chart. Mostrar B y A como dos bloques de texto nativos con sus conteos y
roles; no usar un diagrama de flujo ni mostrar IDs.

**Speaker notes and transition:** Aclarar que tres participantes de B quedan fuera por conducta
2-back incompleta. Reservar para la slide 8 el filtrado de identidades solapadas. Transición: “En
cada persona convertimos la señal de tarea en una representación compacta y reproducible.”

**Evidence/provenance:** `pipeline/02`, celdas 5–8; `sandbox/jaime/datasets.py` y
`sandbox/jaime/preprocessing.py`; `docs/project-plan.md`, “Dataset roles”.

**Scientific caveat:** Cohortes hermanas del mismo recurso HCP comparten adquisición y población;
por eso la prueba mide transferencia de cohorte, no generalización de sitio.

## Slide 4 — From task frames to a 78-feature FC difference

**Purpose:** Hacer transparente la transformación analítica sin convertir la slide en un diagrama de
software.

**Audience-facing title:** Each participant contributed a 78-feature load contrast

**Visible copy:**

`312 HRF-shifted frames per condition (two runs pooled) → Pearson FC → 12 within-network + 66 between-network means`

Large equation:

> **FC reconfiguration = fingerprint(2-back) − fingerprint(0-back)**

Footer: `78 features per participant`

**Layout:** Flujo único de izquierda a derecha, con la ecuación ocupando el tercio inferior. No usar
tarjetas repetidas ni un pipeline de ingeniería demasiado detallado.

**Chart:** [`visuals/charts/feature-construction.png`](visuals/charts/feature-construction.png).
Colocarlo como visual dominante; ya contiene las matrices reales, el resumen 12×12 y el vector de
78 características. No reconstruir el pipeline con formas adicionales.

**Speaker notes and transition:** Explicar que el desplazamiento HRF es de 4 s, que los dos runs se
concatenan para aportar 312 frames a cada condición y que la diferencia mantiene 78 características.
Transición: “Con las características fijadas, la pregunta clave pasa a ser cómo evaluar sin que una
persona aparezca a ambos lados del test.”

**Evidence/provenance:** `pipeline/02`, celdas 7–8; `sandbox/jaime/connectivity.py`,
`network_fingerprint`; `sandbox/jaime/preprocessing.py`, `condition_frames` y
`condition_timeseries`.

**Scientific caveat:** Pearson FC sobre ventanas de tarea puede incluir coactivación evocada por la
tarea; no demuestra comunicación entre regiones.

## Slide 5 — Every estimate holds out participants

**Purpose:** Definir los cuatro esquemas de evaluación y evitar mezclar sus números más adelante.

**Audience-facing title:** We tested prediction at the participant level

**Visible copy:**

1. **Repeated CV:** 5-fold CV across 20 shuffled partitions.
2. **Fixed holdout:** one 80/20 subject split.
3. **Permutation test:** labels shuffled and the full pipeline refit.
4. **Transfer:** train on B-only identities; test on A.

Visible key: `Repeated-CV “±” = SD across partitions, not a confidence interval.`

**Layout:** Una secuencia vertical de cuatro pasos con el “visible key” en una franja inferior. Dar
más peso visual al repeated CV y a transfer.

**Chart:** No pre-rendered chart. Usar una lista nativa de cuatro checks y resaltar en texto que la
unidad de separación es la persona y que scaler + RidgeCV se reajustan dentro de cada fold.

**Speaker notes and transition:** Señalar que StandardScaler y RidgeCV se ajustan dentro de cada
fold. Explicar que la unidad de separación es la persona, nunca el run ni el frame. Transición:
“Primero veamos el estimador más estable del efecto principal.”

**Evidence/provenance:** `pipeline/02`, celdas 3–5 y 11–12; `sandbox/jaime/evaluation.py`,
`make_split` y `ridge_pipeline`.

**Scientific caveat:** Las 20 particiones cuantifican sensibilidad al split; no producen 20 muestras
independientes ni un CI poblacional.

## Slide 6 — Primary evidence

**Purpose:** Presentar el efecto principal con su estimando canónico y sin asociarle indebidamente el
p de otra realización.

**Audience-facing title:** The distributed FC change predicted unseen performance

**Visible copy:**

> **Repeated 5-fold CV: r = 0.366**

> **SD across 20 partitions: 0.024**

Supporting line: `Prediction target: 2-back accuracy · 336 participants · 78 FC features`

**Layout:** Número principal grande a la izquierda; a la derecha, distribución o puntos de los 20
valores de r. Debajo, la línea de método.

**Chart:** [`visuals/charts/primary-repeated-cv.png`](visuals/charts/primary-repeated-cv.png).
Usarlo completo; la media y la split SD ya están diferenciadas y no deben redibujarse como CI.

**Speaker notes and transition:** “Este es nuestro tamaño de efecto principal: la media sobre 20
particiones. Todavía no le hemos asignado un p; el p se calculó sobre la realización seed 42 y lo
mostramos separado.” Transición: “Dos comprobaciones inferenciales sitúan ese efecto —null y
holdout— y d′ aporta un compañero de medición B-only.”

**Evidence/provenance:** `pipeline/02`, celdas 9–12; valor reproducido por notebooks fuente 04, 08 y
09.

**Scientific caveat:** Correlación predictiva no equivale a varianza explicada ni a utilidad clínica;
el diseño es asociacional y de una sola tarea.

## Slide 7 — Null, holdout and measurement companion

**Purpose:** Mostrar dos checks complementarios y dejar d′ en su papel correcto de
compañero de medición B-only, manteniendo separados los estimandos.

**Audience-facing title:** Two additional checks supported the predictive signal

**Visible copy:**

- **Full-refit permutation:** seed-42 CV **r = 0.405; p = 1/1001 ≈ 0.001**.
- **Fixed 80/20 holdout:** **r = 0.312** in 67 unseen participants.
- **B-only measurement companion — d′:** repeated-CV **r = 0.352 ± 0.026**; partial | 0-back
  accuracy **r = 0.249**.

Small qualifications: `For accuracy, partial | 0-back accuracy = 0.219.`
`d′ “±” is split SD; canonical 02 shows no d′-specific permutation p, bootstrap CI or transfer test.`

**Layout:** Dos bandas primarias — permutation y holdout — ocupan la mayor parte. d′ queda en una
franja secundaria rotulada “B-only measurement companion”, visualmente subordinada.

**Chart:** [`visuals/charts/null-and-holdout.png`](visuals/charts/null-and-holdout.png). El chart
contiene únicamente el null de refit completo y el holdout fijo. Mantener d′ como cifras textuales
secundarias; no generar un tercer panel.

**Speaker notes and transition:** Explicar que el null primario permuta etiquetas y reajusta el
pipeline 1000 veces; por eso **p≈.001 se pronuncia junto a r=.405, no junto a r=.366**. d′ es B-only,
separa sensibilidad de sesgo de respuesta y sirve como compañero de medición, no como tercer check
inferencial equivalente: el notebook canónico no le calcula null propio, CI ni transferencia.
Transición: “La comprobación más exigente que podemos hacer con estos datos es entrenar en personas
B que no aparecen en A.”

**Evidence/provenance:** `pipeline/02`, celdas 11–14; `sandbox/jaime/preprocessing.py`,
`signal_detection_table`.

**Scientific caveat:** d′ no puede calcularse limpiamente en A por campos target/non-target
inconsistentes; la transferencia usa accuracy. En canonical 02 no hay p de permutación, bootstrap CI
ni transferencia específicos de d′.

## Slide 8 — Transfer

**Purpose:** Elevar la evidencia de generalización sin llamarla validación externa independiente.

**Audience-facing title:** The B-trained model transferred to identity-disjoint cohort A

**Visible copy:**

> **r = 0.398 · bootstrap 95% CI [0.25, 0.53]**

`A-label permutation with fixed B-trained predictions: p = 1/1001 ≈ 0.001`

`Train: 301 B-only participants · Test: all 100 A participants · 35 shared identities removed`

Visible caveat: `Identity-disjoint same-HCP transfer — not independent-site validation.`
`This transfer-label test is separate; the primary full-refit null belongs only to seed-42 r = 0.405.`

**Layout:** Scatter predicho vs observado en dos tercios; en el lateral, los conteos train/test y el
guardrail de identidad. La caveat ocupa el pie visible.

**Chart:** [`visuals/charts/identity-disjoint-transfer.png`](visuals/charts/identity-disjoint-transfer.png).
Usarlo como panel dominante; conserva el bootstrap 95% CI, la permutación de labels A y los conteos
de identidades sin introducir barras de split SD.

**Speaker notes and transition:** Subrayar que el modelo se ajusta solo en los 301 sujetos B cuyas
identidades reales no están en A. Este p no es el null primario: permuta 1000 veces los labels de A
con la predicción B→A fija y usa la corrección +1, por lo que `p=1/1001≈.001`. El único null de refit
completo de la historia principal pertenece a seed-42 `r=.405`. Transición: “La predicción se
sostiene; ahora preguntamos si la dirección biológica que esperábamos también se sostiene.”

**Evidence/provenance:** `pipeline/02`, celdas 15–16 y figura 9C; notebook fuente
`sandbox/jaime/05_dataset_A_external_validation.ipynb`.

**Scientific caveat:** La posible estructura familiar no está modelada y ambas cohortes provienen
del mismo HCP; la CI cuantifica incertidumbre sobre A, no heterogeneidad entre sitios.

## Slide 9 — Directional refinement

**Purpose:** Mostrar que existe un cambio medio de segregación, pero que no explica de forma clara
las diferencias individuales.

**Audience-facing title:** Segregation fell under load, but the individual link was weak

**Visible copy:**

- **Group mean:** 0-back **0.3271** → 2-back **0.3035**.
- **Paired change:** **Δ = −0.0236; p = 3.45 × 10⁻⁵**.
- **Across participants:** corr(ΔSegregation, accuracy) **r = −0.105; p = 0.054**.

Bottom line: `Higher load reduced segregation on average; larger reductions did not convincingly predict better performance.`

**Layout:** Izquierda: paired slope/violin 0-back vs 2-back. Derecha: cifra del cambio y pequeño
scatter individual. El bottom line atraviesa la base.

**Chart:** [`visuals/charts/segregation-refinement.png`](visuals/charts/segregation-refinement.png).
Conservar juntos el cambio grupal y el scatter individual, porque su contraste es el argumento de la
slide; no sustituirlos por barras agregadas.

**Speaker notes and transition:** Separar verbalmente el test pareado de grupo y la correlación entre
personas. No recuperar el valor −0.048 del abstract enviado. Transición: “La dirección media existe,
pero no es el mecanismo individual simple que habíamos anticipado.”

**Evidence/provenance:** `pipeline/02`, celdas 21–22 y figura 9D; notebook fuente
`sandbox/jaime/09_goutham_pipeline_replication.ipynb`.

**Scientific caveat:** System segregation es un resumen escalar Chan-style; no es Newman modularity
y no reemplaza el patrón multivariado de 78 características.

## Slide 10 — Anatomical context, not predictive importance

**Purpose:** Dar una lectura espacial del cambio de acoplamiento sin convertirla en explicación del
modelo.

**Audience-facing title:** Mean FC changes were distributed—but they do not show model importance

**Visible copy:**

> Red: stronger mean coupling at 2-back · Blue: weaker mean coupling at 2-back

`78 unique network-level ΔFC values · 360 descriptive ROI summaries`

Visible caveat: `Group-mean change shows where coupling differs, not which regions drive prediction.`

**Layout:** Mitad izquierda: triángulo superior 12×12 de ΔFC; mitad derecha: proyección cortical.
Misma escala divergente en ambos paneles.

**Chart:** [`visuals/charts/anatomical-context.png`](visuals/charts/anatomical-context.png). Usar la
escala divergente común y mantener visible que es una media descriptiva, no importancia predictiva.

**Speaker notes and transition:** Explicar que esta figura reutiliza la misma ΔFC de las slides
previas; no crea una métrica adicional. Transición: “El mapa demuestra distribución espacial, pero
la pregunta de especificidad exige comparar la reconfiguración con una base más simple.”

**Evidence/provenance:** `pipeline/02`, celdas 25–26.

**Scientific caveat:** La media grupal no identifica pesos del modelo, causalidad ni importancia por
región; tampoco demuestra que el efecto sea exclusivo de conectividad.

## Slide 11 — The incremental claim did not survive

**Purpose:** Probar explícitamente el “beyond single-condition FC” del relato original y mostrar por
qué se retira.

**Audience-facing title:** Reconfiguration did not clearly add beyond 0-back FC

**Visible copy:**

- 0-back FC (78): **r = 0.274 ± 0.032**.
- Reconfiguration FC (78): **r = 0.366 ± 0.024**.
- 0-back + reconfiguration (156): **r = 0.333 ± 0.026**.
- Matched-fold increment: **ΔR² = +0.0344; SD = 0.0225 → no clear gain**.

Footer: `All “±” values are SD across the same 20 CV partitions.`

**Layout:** Forest/dot plot de tres r repetidos; debajo, una sola línea para ΔR². No usar barras
agrupadas ni sugerir una prueba de superioridad no realizada.

**Chart:** [`visuals/charts/incremental-fc-test.png`](visuals/charts/incremental-fc-test.png). Usarlo
completo; el panel izquierdo compara los tres modelos y el derecho muestra la variabilidad del
incremento emparejado sin presentarla como un test formal.

**Speaker notes and transition:** “El modelo de diferencia predice, pero añadirlo al 0-back no mejora
de forma clara el R² fuera de muestra. La regla de 2 SD es una heurística de estabilidad, no un test
formal.” Transición: “Entonces probamos un benchmark regional más simple y obtuvimos la sorpresa del
proyecto.”

**Evidence/provenance:** `pipeline/02`, celdas 17–18; notebook fuente
`sandbox/jaime/08_activation_vs_reconfiguration.ipynb`.

**Scientific caveat:** Comparar r de modelos por separado no demuestra valor incremental; la
conclusión procede del ΔR² emparejado por fold y debe conservar su carácter heurístico.

## Slide 12 — Robustness surprise

**Purpose:** Introducir el benchmark post hoc que cambia la interpretación, sin reemplazar el
proyecto ni convertirlo en una competición biológica equitativa.

**Audience-facing title:** A regional activation benchmark predicted more strongly

**Visible copy:**

- **Activation contrast (360 regional features): r = 0.600 ± 0.016**.
- **FC reconfiguration (78 network features): r = 0.366 ± 0.024**.
- **Seed-42 cross-run feature generalization:** **0.475 vs 0.246** in held-out people, against the
  shared subject-level `acc_2bk` outcome.
- FC added over activation: **ΔR² = −0.0030; SD = 0.0065 → no clear gain**.

Visible caveat: `Post hoc and unmatched: 360 regional activation features vs 78 network FC features.`
`Activation = mean BOLD(2-back) − mean BOLD(0-back), not a GLM beta.`
`Cross-run separates features and people, not the behavioural outcome by run.`

**Layout:** Dos filas comparativas grandes, activation en naranja y FC en azul; la generalización de
features cross-run aparece como diamantes con “seed 42 / shared outcome” escrito al lado; ΔR² queda
como conclusión inferior. Las caveats deben estar dentro del área principal.

**Chart:** [`visuals/charts/activation-robustness.png`](visuals/charts/activation-robustness.png).
Usarlo como evidencia principal y conservar dentro del chart el mismatch 360 vs 78, los incrementos
emparejados y la ausencia de una metáfora de ganador.

**Speaker notes and transition:** Explicar que el contraste regional es la diferencia de mean BOLD
entre condiciones, no un beta GLM, y fue un benchmark de robustez posterior a la hipótesis original.
La cifra cross-run es una única estimación seed 42: entrena con features de un run y se aplica a las
features del otro en personas held-out para predecir el mismo `acc_2bk` agregado por participante.
La activación también conserva asociación tras controles de accuracy 0-back
(partial r=.412) y DVARS (partial r=.580), pero esos controles no prueban ausencia de artefacto:
en particular, ninguno de los dos captura reactividad cerebrovascular (CVR), y el dataset actual no
tiene proxy de CVR — punto señalado por Goutham Arcod (22 jul, Discord), con apoyo en Logothetis
(2008): el BOLD es un proxy hemodinámico, no una medida directa de disparo neural.
Transición: “La sorpresa no borra la predicción FC; limita lo que podemos afirmar sobre su
especificidad.”

**Evidence/provenance:** `pipeline/02`, celdas 17–20; notebook fuente
`sandbox/jaime/08_activation_vs_reconfiguration.ipynb`.

**Scientific caveat:** El centrado por run hace que 0-back, 2-back y su contraste de activación sean
fuertemente colineales; el contraste no es un rasgo independiente de carga. La comparación no está
igualada en número ni escala de características. La cifra cross-run demuestra separación de
features/runs y de personas con un outcome compartido, no un test conductual completamente
independiente entre runs. Los controles de habilidad y movimiento no capturan reactividad
cerebrovascular (CVR); el contraste de activación podría reflejar en parte variación vascular
entre sujetos, no solo señal neural — hueco no testeado, no descartado.

## Slide 13 — Refined conclusion

**Purpose:** Resolver la pregunta inicial con tres niveles explícitos: qué sobrevive, qué se matiza y
qué queda sin resolver, nombrando las dos hipótesis pre-especificadas de la apertura.

**Audience-facing title:** Prediction survives; connectivity-specific mechanism remains unresolved

**Visible copy:**

**What survives — the pattern hypothesis**

- A 78-feature FC difference predicts 2-back accuracy in unseen participants.
- The model transfers across identity-disjoint same-HCP cohorts.

**What was refined — the directional hypothesis**

- Mean system segregation does decrease at higher load, as predicted.
- But larger segregation reductions did not convincingly predict better performance.
- Reconfiguration showed no clear incremental gain over 0-back FC.

**What remains unresolved**

- Whether the predictive information is connectivity-specific rather than shared with task
  activation.

**Layout:** Tres zonas verticales “survives / refined / unresolved”; la tercera ocupa algo más de
espacio para preparar los experimentos. Evitar estilo de dashboard; usar jerarquía tipográfica plana.
Las dos primeras cabeceras nombran explícitamente las hipótesis de la Slide 1 para cerrar el bucle.

**Chart:** No pre-rendered chart. Resolver después con tres bloques tipográficos nativos —Survives,
Refined, Unresolved— y sin reutilizar miniaturas de resultados.

**Speaker notes and transition:** Esta es la conclusión que debe quedar en Q&A. Pronunciar “same-HCP
transfer”, nunca “independent external validation”. Transición: “La incertidumbre restante sugiere
experimentos concretos que podrían decidir entre explicaciones.”

**Evidence/provenance:** Síntesis de `pipeline/02`, celdas 27–30; `docs/project-plan.md`, “Original
working hypothesis and current result”.

**Scientific caveat:** El análisis observacional de una sola tarea no identifica mecanismo causal ni
especificidad biológica.

## Slide 14 — Decisive next experiments

**Purpose:** Cerrar el relato científico con pruebas que cambien la conclusión, no con una lista
genérica de extensiones.

**Audience-facing title:** Four experiments could resolve the remaining question

**Visible copy:**

1. **Match the representations:** compare activation and FC with equalized dimensionality and nested,
   participant-level CV.
2. **Separate coactivation from coupling:** use a prespecified task-connectivity estimator and the
   same target, folds and null.
3. **Test real generalization:** repeat the model in an independent-site cohort with repeat-session
   and family-aware evaluation.
4. **Control for vascular reactivity (CVR):** regress a CVR proxy (or scanner-gain covariate) out of
   the activation contrast before re-testing whether it still predicts performance.

Closing line: `Decision criterion: FC must add reliable held-out value beyond activation and single-condition FC.`

**Layout:** Cuatro pasos numerados con una pregunta decisiva debajo de cada uno: fairness, estimator,
generalization, vascular confound. La closing line queda visible mientras empieza el Q&A.

**Chart:** No pre-rendered chart. Presentar las cuatro pruebas como una lista numerada nativa y cerrar
con el criterio de decisión; no generar un diagrama de flujo.

**Speaker notes and transition:** Explicar que cada experimento ataca una limitación distinta: no
equivalencia de representaciones, contaminación por coactivación, falta de generalización de sitio y
confusión vascular no controlada (CVR, señalada por Goutham el 22 jul).
Transición a referencias: “Hasta entonces, la conclusión calibrada es predictiva y asociacional.”

**Evidence/provenance:** `pipeline/02`, tabla claim→result→limitation; `manuscript/references.md`,
Masharipov 2024 para el problema de FC de tarea, Hedge 2018 para fiabilidad de diferencias y
Logothetis 2008 para el proxy hemodinámico del BOLD; `docs/project-plan.md`, limitaciones de cohortes.

**Scientific caveat:** Son experimentos propuestos, no resultados del pipeline adoptado; no deben
aparecer en pasado ni como trabajo ya realizado.

## Slide 15 — References / backup

**Purpose:** Dejar la trazabilidad científica y un recordatorio estadístico disponible durante las
preguntas.

**Audience-facing title:** References and statistical guardrails

**Visible copy:**

**Selected references**

- Avery et al. (2020), *J. Cognitive Neuroscience* — HCP task-FC prediction of 2-back accuracy.
- Chan et al. (2014), *PNAS* — system-segregation metric.
- Murphy et al. (2020), *Nature Communications* — selective, not uniformly beneficial, integration.
- Masharipov et al. (2024), *Communications Biology* — task coactivation can inflate condition FC.
- Hedge et al. (2018), *Behavior Research Methods* — reliability limits of difference scores.
- Logothetis (2008), *Nature* — BOLD is a hemodynamic proxy, confounded by vascular variables.

**Backup labels**

- `r = 0.366 ± 0.024` = mean ± SD across 20 repeated-CV partitions.
- `seed-42 r = 0.405; permutation p = 1/1001 ≈ 0.001` = the primary statistic and its full-refit null.
- `B→A r = 0.398; bootstrap 95% CI [0.25, 0.53]` = identity-disjoint same-HCP transfer;
  A-label permutation with fixed B-trained predictions: `p = 1/1001 ≈ 0.001`.

**Layout:** Dos columnas: referencias a la izquierda; guardrails a la derecha. Tipografía menor que
en las slides narrativas, pero legible como backup proyectado.

**Chart:** No pre-rendered chart. Usar referencias y guardrails como texto nativo; no añadir
miniaturas, porque duplicarían evidencia ya disponible en las slides anteriores.

**Speaker notes and transition:** Mantener esta slide para Q&A si surge una duda sobre procedencia,
definición de segregación o diferencia SD/CI. No leerla en la exposición principal.

**Evidence/provenance:** `manuscript/references.md`; `pipeline/02`, celdas 12, 16, 22 y 30.

**Scientific caveat:** Avery es calibración conceptual, no réplica exacta; Chan/Murphy aportan marco,
no validación directa del pipeline; Masharipov justifica una limitación metodológica; Logothetis
enmarca la confusión vascular (CVR) de la Slide 12 como hueco citado, no resultado propio.

## QA checklist

- [x] **Factual consistency:** 15 slides exactas; B=339/336, A=100, 360 ROIs, 12 redes, 78
  características, 4 s HRF, 312 frames por condición con dos runs pooled y todos los resultados
  coinciden con `pipeline/02`.
- [x] **Statistical labeling:** repeated-CV `r=.366 ± .024` está separado del null; `p=1/1001≈.001` se
  empareja con seed-42 `r=.405`; el p B→A está rotulado por separado como permutación de labels A con
  predicción B fija (`1/1001≈.001`); el único 95% CI narrativo es el bootstrap B→A `[.25,.53]`.
- [x] **d′ boundary:** d′ queda como compañero de medición B-only, con split SD explícita y sin
  atribuirle p, CI o transferencia específicos no calculados en canonical 02.
- [x] **Transfer wording:** siempre “identity-disjoint same-HCP transfer”; nunca independent-site
  validation.
- [x] **Directional result:** `.3271 → .3035`, `Δ=-.0236`, paired `p=3.45e-05`; vínculo individual
  `r=-.105`, `p=.054`.
- [x] **Robustness boundary:** activation se marca como post hoc y no igualada (360 regional vs 78
  network FC features), se define como contraste de mean BOLD y no beta GLM; cross-run se etiqueta
  seed 42, held-out people y outcome conductual compartido; no se afirma especificidad de conectividad.
- [x] **Narrative continuity:** cada transición abre la pregunta de la slide siguiente y el cierre
  responde las dos hipótesis pre-especificadas con survives / refined / unresolved / decisive
  experiments.
- [x] **Framing del relato:** ningún texto hablado describe la hipótesis como evolucionada, cambiada
  o reemplazada; el cierre nombra la hipótesis de patrón (se sostiene) y la direccional (se matiza).
- [x] **Slide density:** una afirmación central por slide; las slides 7, 11, 12 y 15 son las únicas
  deliberadamente densas y funcionan como evidencia o backup, no como texto corrido.
- [x] **Scope and language:** no se incorporan análisis fuera del pipeline adoptado; no se describe
  la FC de tarea como dinámica, causal o adaptativa.
