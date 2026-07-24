# Guía del presentador — W3D5 · The Gammas

> **Qué es esto.** Una guía por diapositiva para que quien presente cada una tenga **todo** el contexto:
> definición de conceptos desde cero, cómo leer cada gráfico, cómo interpretar cada número, qué decir
> (con las frases en inglés listas para pronunciar) y qué preguntas esperar. Un bloque por slide.
> **Fuente de verdad:** el deck final `manuscript/slides/source-snapshots/The Gammas - NMA project.pdf`
> y `pipeline/02_canonical_analysis_and_slides.ipynb` (números). El texto que se proyecta es **inglés**;
> la explicación va en español y la charla se da en inglés.

## Numeración — esta guía coincide con el deck final

El deck final tiene **6 páginas habladas + 5 backups**. **Portada y equipo están fusionados en la página 1**
(por eso la numeración bajó un número respecto al storyboard viejo). Esta guía usa **la numeración del deck
proyectado**:

| Pág / Slide | Contenido | Presenta |
|---|---|---|
| **1** · Portada + Equipo | Título + "Meet the Gammas" | Valeria abre |
| **2** · Introduction | La pregunta + Pattern/Direction + ancla Avery | **Valeria** |
| **3** · Methods | 336 HCP · fingerprint de 78 · benchmark vs 360 activación | **Arefeh** |
| **4** · Results | Primario r=0.366 + transferencia B→A 0.398 (scatter) | **Jaime** |
| **5** · Robustness checks | Dirección matizada + activación 0.60 vs 0.37 + 2 guardrails | **Goutham** |
| **6** · Conclusions | Survives / Refined / Unresolved + gracias | **Kerem** |
| 7–11 · Backups | Divider + direccional + validación + futuro + referencias | según pregunta |

Cinco ponentes, **una slide cada uno (slides 2–6)**. Portada/equipo y backups no consumen minuto.
Reparto cerrado en Discord (24 jul); dos matices vs el borrador de líneas: Goutham lleva **toda** la slide
5 (sus guardrails enlazan con el 0.60/0.37 que cualifican), y Jaime lleva **toda** la slide 4 (0.366 + la
transferencia 0.398). El 0.398 también está impreso en la slide 6 bajo *Survives*, así que Kerem lo remata
como titular de cierre.

## Reglas de entrega comunes (aplican a TODAS las slides)

**Instrucciones de Andrea (vinculantes):**
1. **Define cada concepto al nombrarlo** — FC, reconfiguración, segregación. Su instrucción más repetida; Arefeh la pidió directamente.
2. **Nombra los ejes en voz alta antes de dar ningún número** de un gráfico: *"always make sure people know what they're looking at."*
3. **Menos texto, más visual.** Menos detalle técnico; lo cortado va a Q&A.
4. **Ensayad al minuto.** Andrea ofreció una ronda de ensayo y tutoría el viernes. Acordad quién responde qué en Q&A.
5. **Es sobre el proceso, no el hallazgo:** *"no vais a ganar ningún premio porque el estudio sea mejor o no."* Nadie va a defender un descubrimiento; contáis lo que hicisteis y lo que aprendisteis.

**Guardarraíles de lenguaje (NO digas nunca, en ninguna slide):**
- ❌ "cambiamos / evolucionó la hipótesis" → ✅ "predijimos dos cosas; una se sostuvo, otra se matizó".
- ❌ "intervalo de confianza" para el ±0.024 → ✅ "split SD" (desviación entre particiones).
- ❌ "validación externa independiente" → ✅ "identity-disjoint same-HCP transfer".
- ❌ "dFC" / "dynamic FC" / "true network dynamics" → es FC **estática** agregada por condición.
- ❌ "el modelo A le gana al modelo B" (marcador deportivo) → ✅ "comprobación de especificidad".
- ❌ causalidad, beneficio adaptativo, mecanismo específico de conectividad.

---

# Slide 1 — Portada + Equipo · Valeria abre

**En pantalla:** *"Functional Connectivity Reconfiguration in N-back Working Memory"* · los cinco nombres ·
**The Gammas** · línea de pod/TA (Pod 884 "Ifrit Ras el Hanout" · Megapod Lotus · TA Andrea Buccellato ·
Project TA Azman Akhter). Sin gráfico, sin minuto de habla (se muestra mientras Valeria saluda).

**Lo que debes saber:** El título nombra la **medida**, no un mecanismo. "Reconfiguration" aquí es
literalmente una **resta entre dos matrices de FC** agregadas por condición — no implica dinámica temporal.
Andrea pidió el **nombre del equipo bien visible**: el deck se archiva y lo lee la cohorte del año que viene.

**Pendientes conocidos (housekeeping, no ciencia):**
- Fotos stock y roles de relleno ("Actor/Doctor/…") — a medias; Arefeh, Valeria y Jaime ya tienen foto real, Kerem y Goutham no.
- **Direcciones de email personales** en un deck que se archiva públicamente — buscar y quitar antes de entregar.

**Cómo decirlo:** *"Hi, we're The Gammas. Our project is on functional connectivity reconfiguration in an
N-back working-memory task."* Y pasar a la Introducción (slide 2).

---

# Slide 2 — Introduction: la pregunta y las dos apuestas · **Valeria**

**En pantalla (verbatim):**
- Título: *"Does load-related brain connectivity predict working-memory performance?"*
- Ancla: *"Avery et al. 2020 predicted 2-back accuracy from task FC in the same dataset (r = 0.36). We asked whether the change between loads carries that signal."*
- *"We predicted two things"*
  - **Pattern** — *"A 78-feature FC fingerprint of the 2-back − 0-back change predicts performance."*
  - **Direction** — *"Higher load shifts networks toward integration; larger shifts accompany better performance."*
- *"A distributed pattern and a one-number direction are different claims."*

**Lo que debes saber (desde cero):**

*La tarea N-back.* Dos niveles de dificultad de memoria de trabajo: **0-back** (fácil, "aprieta al ver
esta imagen concreta" — atención pura, casi todos rozan el techo) y **2-back** (difícil, "aprieta si la
imagen actual es igual a la de dos posiciones atrás" — obliga a mantener y actualizar un buffer). El
2-back es donde la gente **se diferencia**, por eso es la condición estrella.

*Las dos apuestas — la clave de esta slide.* No es una hipótesis, son **dos, de naturaleza distinta**:
- **Pattern** es **multivariado y sin signo**: das los 78 números juntos a un modelo y ves si el
  conjunto predice. No exige que ninguno suba o baje en concreto. Analogía: un panel de 78 biomarcadores
  — no importa cada uno por separado, importa si el conjunto es diagnóstico.
- **Direction** es **un solo número, con signo esperado**: la carga debe **bajar** la segregación (más
  integración), y ese cambio, por sí solo, debe predecir quién rinde mejor. Analogía: "la fiebre sube, y
  a más fiebre peor pronóstico" — una variable, una dirección.

*Por qué eran dos y no una.* En la propuesta original (Arefeh, 15 jul) era **una frase** que ya contenía
ambas afirmaciones. Al llegar los datos, una se sostuvo y la otra no. Separarlas no es reescribir la
historia: es hacer explícito lo que siempre fueron: **dos pruebas independientes**. Esto te blinda si
preguntan "¿no era una sola hipótesis de integración?".

*Por qué Avery 2020.* Es el ancla de calibración. Predijo `acc_2bk` desde FC de tarea, **mismos datos**,
a r = 0.36. Cítalo para que, cuando en la slide 4 salga **nuestro 0.366**, la audiencia lo juzgue contra
ese listón publicado, no en el vacío. **Una sola cita aquí, ninguna más** (instrucción de Andrea).

**Cómo decirlo (~1 min):**
> *"Our question: does the way brain connectivity changes with memory load predict how well someone
> performs? A 2020 study by Avery already predicted 2-back accuracy from connectivity in this same
> dataset, at r = 0.36 — we asked whether the **change between loads** carries that signal. We made two
> different predictions. First, a **pattern**: a 78-feature fingerprint of the 2-back-minus-0-back change
> predicts performance — this doesn't need any particular direction, just that the combined pattern
> carries information. Second, a **direction**: higher load pushes networks toward integration, and
> people with bigger shifts perform better — that's a single signed number. These are different kinds of
> claims, so we test them separately."*

**Transición:** *"So how did we actually measure that? Over to the method."*

**Preguntas probables:**
- *"¿No era una sola hipótesis?"* → "The original proposal was one sentence that contained both a pattern and a directional claim; we report them as the two separate tests they always were."
- *"¿Por qué 2-back y no 0-back como objetivo?"* → "0-back is near ceiling — everyone gets it. 2-back is where people differ, so it's where there's something to predict."

**No digas:** que la hipótesis cambió; una segunda cita.

---

# Slide 3 — Methods: de los escáneres a una predicción · **Arefeh**

**En pantalla (verbatim):**
- Título: *"We evaluated a 78-feature FC difference in held-out people"*
- Banda de definiciones (3 líneas):
  - *"Functional connectivity = the Pearson correlation between the time courses of two brain regions. Each node is one of 360 Glasser ROIs."*
  - *"FC reconfiguration = how much each network pair changes its coupling when memory load goes from 0-back to 2-back."*
  - *"System segregation = (mean within-network FC − mean between-network FC) ÷ mean within-network FC, computed per participant per condition (Chan et al. 2014)."*
- **1 · Cohort** — *"Two HCP N-back samples · 360 Glasser ROIs · B (primary): 336 participants — all cross-validation here · A (transfer target): 100 participants with per-subject behaviour — held out for the B→A test"* — **A/B es jerga interna nuestra; defínelas aquí, en su primera aparición, o el público llega al "B→A" de la siguiente slide sin saber qué es A.**
- **2 · Condition frames** — *"0-back and 2-back frames kept separate, with no temporal overlap"*
- **Figura: tres matrices de red** (0-back FC, 2-back FC, y su diferencia). Caption: *"12 Cole-Anticevic networks · 12 within + 66 between = 78 values per person"*
- **3 · Model** — *"StandardScaler + RidgeCV, fitted inside each training fold"*
- **4 · Held-out evaluation** — *"repeated 5-fold CV · fixed holdout · 1000-permutation null · B→A transfer (301 → 100, identity-disjoint)"*
- *"All splits hold out participants; "±" = split SD, not CI."*

**Lo que debes saber (desde cero) — las tres definiciones son tuyas de decir en voz alta:**

*Conectividad funcional (FC).* La **correlación de Pearson** entre las series temporales de dos
regiones. Coges cómo sube y baja la señal de la región A en el tiempo y la de la región B; si van
juntas, correlación alta positiva; si no, cerca de cero. Cada región es un **nodo**; hay **360** (atlas
Glasser).

*Reconfiguración de FC.* Cuánto cambia el acoplamiento de cada par de redes al pasar de 0-back a
2-back. **Foto de 2-back menos foto de 0-back.** (Analogía: prueba de esfuerzo cardiaco — importa el
cambio reposo→esfuerzo, no cada foto por separado.)

*Segregación de sistema (necesita desgrane — 3 piezas):* conectividad media **dentro** de las redes,
menos conectividad media **entre** redes, dividido entre la de dentro (para normalizar). Un número por
persona y condición. **Alto = cerebro modular** (sistemas hablando consigo mismos); **bajo = integrado**
(redes mezclándose). Esta métrica la usará Goutham en la slide 5 — quédate con "alto modular, bajo integrado".

*De 360×360 a 78.* Las matrices completas serían >64.000 pares — imposible con 336 personas sin
sobreajuste. Se agrupan las 360 regiones en **12 redes** (atlas Cole-Anticevic: visual, motora, control
cognitivo, default…) y se promedia: **12** valores dentro de red + **66** entre redes (12×11/2 = 66
parejas sin repetir) = **78 features** por persona por condición.

*El modelo (esto lo domináis, no te extiendas):* ridge con estandarizado, ambos ajustados **dentro** de
cada fold de entrenamiento — nunca con info del test. Es la higiene que evita inflar la CV.

*Las 4 evaluaciones* (cada una sale luego): CV repetida 5-fold ×20 · holdout fijo · null de 1000
permutaciones · transferencia B→A sin identidades compartidas.

**El gráfico (léelo así — no es autoevidente):** tres cuadrículas de 360×360. Cada casilla = un par de
regiones; color = su correlación en esa condición. Escala: azul (negativo) → blanco (≈0) → tierra
(positivo). Panel 1 = 2-back, panel 2 = 0-back, panel 3 = la resta.

⚠️ **Matiz que hay que decir:** los paneles 1 y 2 comparten **una** escala; el panel 3 tiene **la suya**,
~10× más estrecha. Que los tres se vean igual de intensos **no** significa magnitudes iguales — el panel
de la diferencia está estirado para que se vea un cambio que en absoluto es pequeño. Solo el panel 3
lleva colorbar.

**Recortado de la slide (disponible en Q&A):** TR 0.72 s, desplazamiento HRF de 4 s, 312 frames por
condición, 2 runs por persona, matrices intermedias de 360×360. Andrea: *"just say it's HCP, 336
participants, this is the task. That's it."* **Excepción:** el diseño de **2 runs por persona** sí hay
que decirlo si preguntan por los cuadrados abiertos (cross-run) de la slide 5.

**Cómo decirlo (~1 min):**
> *"Quick definitions first. Functional connectivity is just the Pearson correlation between two brain
> regions' time courses — each region is one of 360 Glasser nodes. FC reconfiguration is how much each
> network pair changes its coupling from 0-back to 2-back. And system segregation — we'll need it later —
> is within-network minus between-network connectivity, normalized: high means a modular brain, low means
> an integrated one. Pipeline — and say this out loud, it's two samples, not one: the main cohort, we call it B, is 336
> HCP participants doing the N-back, and every cross-validation, holdout and permutation runs inside it.
> A second, smaller sample — cohort A, 100 people who also have per-subject behaviour — is set aside
> untouched as the transfer target, so when you hear 'B-to-A' later it just means train on the 336, test
> on those held-out 100. We compute a 360-by-360 correlation
> matrix per condition, then summarize it into 12 within- and 66 between-network values — 78 numbers per
> person. **Naming the axes on this figure:** three network matrices — 2-back, 0-back, and their
> difference. The first two share one colour scale; the third has its own, about ten times tighter, so
> the difference is small even though the colours look strong. Reconfiguration is that difference. We feed
> it to a ridge model, fitted strictly inside each training fold, and evaluate only on held-out people."*

**Transición:** *"So did this 78-feature difference actually predict anything? Yes — and it transferred."*

**Preguntas probables:**
- *"¿Por qué 78 y no todos los pares?"* → "64,000 edges for 336 people would overfit; the network summary is the standard dimensionality reduction."
- *"¿No infla la tarea las correlaciones (coactivación)?"* → "Yes, task FC can reflect coactivation, not communication — it's a stated limitation; separating the two is future work (backup slide 10, test 2)."
- *"¿Parámetros de adquisición?"* → TR 0.72 s, HRF shift 4 s, 312 frames/condición, 2 runs — todo listo si lo piden.

**No digas:** "dynamic FC"; que las matrices muestran magnitudes comparables (escalas distintas).

---

# Slide 4 — Results: el patrón predice y transfiere · **Jaime** ✅

> **Tu slide.** Objetivo en ~1 min: contar que **el patrón predice y transfiere**, dejar claro **qué
> fuerza** tiene cada número, y **no sobreafirmar**. Al terminar, se lo pasas a **Goutham** (slide 5).

**En pantalla (verbatim):**
- Título: *"The FC pattern predicted performance—and transferred to a separate cohort"*
- **Primary repeated CV** *"r = 0.366 ± 0.024 · 336 participants · 78 FC features"*
- **B→A transfer** *"r = 0.398; 95% CI [0.25, 0.53]"* · *"301 B → 100 A · 35 shared identities removed"*
- Caveat: *"Identity-disjoint same-HCP transfer—not independent-site validation."*
- Gráfico: dispersión `identity-disjoint-transfer.png` (predicho vs observado, cohorte A).

### 1 · El gráfico — nombra los ejes ANTES de dar un número (regla de Andrea)

- Eje **X** = precisión **real** en 2-back de cada persona del **grupo A** (el test).
- Eje **Y** = precisión **predicha** por un modelo entrenado **solo en el grupo B**, que nunca vio a nadie de A.
- Cada punto = una persona real de A. La nube **sube de izquierda a derecha** → hay señal. Si el modelo
  fuera inútil, sería una nube plana.

### 2 · Los dos números — miden cosas distintas, NO los fundas

| | **0.366 ± 0.024** | **0.398 · IC [0.25, 0.53]** |
|---|---|---|
| Qué es | media de **CV repetida** (5-fold ×20 semillas) | **transferencia B→A** (modelo fijo) |
| El ± / IC | **split SD** = cuánto se mueve según la partición | **IC bootstrap** = incertidumbre poblacional clásica |
| Por qué difieren | el modelo **se reajusta** en cada fold → mides *estabilidad*, no IC | el modelo está **congelado** → puedes remuestrear las 100 de A |

El **0.398 es el número más fuerte** que tenéis: modelo entrenado en una cohorte, probado en **otra**, sin
identidades compartidas (se quitaron las 35 que aparecían en ambas).

### 3 · Calibración con Avery (por qué 0.36–0.40 es un buen número)

0.366 y 0.398 caen **justo en la zona del 0.36 publicado** por Avery en estos mismos datos — o algo por
encima. Es **modesto en absoluto pero a la altura de la literatura**. El criterio de éxito del Project TA
nunca fue una R² alta, sino **superar claramente el azar** — y eso lo demuestra el backup de validación
(slide 9): null de 1000 permutaciones p ≈ .001 + holdout fijo 0.312.

### 4 · El caveat obligatorio — dilo tú, no esperes a que lo pregunten

Es una transferencia entre **dos cohortes del mismo HCP**: más fuerte que barajar tus datos, más débil que
replicar en otro escáner/población. Gradiente: barajar-tus-datos < **transferencia same-HCP (esto)** <
replicación externa real. Decir dónde caes = credibilidad (y te ahorra que te lo saquen como pega).

### 🎤 Tu speech (inglés, ~65 s, listo para decir)

> *"This is our main result. First, the axes: horizontal is each person's **actual** 2-back accuracy in
> cohort A — our test group; vertical is the accuracy our model **predicted** for them, from a model
> trained **only on cohort B** that never saw anyone in A. Each dot is one real participant, and the trend
> clearly rises.*
>
> *Two numbers, and they measure different things. Our primary effect is the repeated cross-validation
> correlation, **r = 0.366** — and that ± 0.024 is a **split standard deviation** across partitions, how
> stable the number is, not a confidence interval. The stronger test: we froze a model trained on B only
> and applied it to A, after removing 35 people who appeared in both cohorts — so nobody is in training and
> test at once. That transfer gives **r = 0.398**, with a bootstrap 95% CI of 0.25 to 0.53.*
>
> *One honest caveat: this is an **identity-disjoint transfer within the same HCP study** — stronger than
> reshuffling your own data, but not an independent-site replication. Still, both numbers sit right on the
> **0.36 Avery** reported in this same data, so this is a real, replicable brain-behavior effect — not a
> fluke."*

**Handoff a Goutham:** *"So the pattern held. But is that signal specifically about connectivity? That's
what the next two checks tackle."*

### Interpretación en profundidad (por si aprietan)

- **Por qué split SD ≠ IC.** En CV repetida el modelo se reentrena en cada fold, así que la dispersión mide
  *sensibilidad a la partición*, no incertidumbre poblacional. El IC clásico solo es legítimo para el modelo
  **fijo** de la transferencia — por eso el IC va con el 0.398, no con el 0.366.
- **Por qué B→A y no A→B.** B es la cohorte grande (336 vs 100): entrenas en la muestra grande y testeas en
  la pequeña; es la dirección de generalización más exigente y con más potencia.
- **Circularidad (misma tarea).** Predecir N-back desde FC de N-back comparte varianza de estado. Está
  **parcialmente controlado**: al sacar la habilidad general (`acc_0bk`) la señal sobrevive, y se ancla en el
  diseño de misma tarea de Avery. Separar coactivación de conectividad = trabajo futuro (slide 10, test 2).
- **¿Por qué parece bajo el número?** En predicción cerebro-conducta un r ≈ 0.35–0.40 es un efecto real y
  publicable; el techo está además limitado por el efecto techo de `acc_2bk` (mucha gente cerca de 1.0).

### Preguntas (probables + trampa) — con respuesta lista

- *"What if it's overfitting or luck?"* → *"Backup: a 1000-permutation null gives p ≈ .001, and a fixed
  holdout of 67 never-seen people gives r = 0.312 — three procedures, same story."* (slide 9)
- *"Isn't 0.366 low?"* → *"For brain–behavior prediction it's a real, publishable effect — Avery got 0.36 in
  the same data. The bar was beating a permutation null, not a high R²."*
- *"Why split SD and not a CI on 0.366?"* → *"The model is refit every fold, so that spread is partition
  sensitivity. We only claim a true CI for the fixed-model B→A transfer."*
- *"Isn't predicting N-back from N-back FC circular?"* → *"It's a same-task association — a stated
  limitation. Partialling out 0-back accuracy the signal survives, and we anchor it in Avery's same-task
  design; cleanly separating coactivation is future work."*
- *"Why train on B and test on A, not the reverse?"* → *"B is the larger cohort — 336 vs 100 — so we train
  on the bigger sample and test on the smaller, the stronger generalization direction."*
- *"Is this an external / independent validation?"* → *"No — identity-disjoint transfer within the same HCP
  study. Stronger than reshuffling, weaker than an independent-site replication."*

**No digas:** "confidence interval" para el 0.366 · "external / independent validation" para la
transferencia · que el modelo "gana" nada (eso es de la slide de Goutham) · "dynamic FC".

**Entrega:** ~1 min, una sola figura y dos números. El único riesgo real es **acelerarte y fundir los dos
números** — respira entre *"0.366, split SD"* y *"0.398, bootstrap CI"*. Ensáyalo cronometrado.

---

# Slide 5 — Robustness checks: dos comprobaciones que acotan lo que se puede afirmar · **Goutham** (la bisagra)

**En pantalla (verbatim):**
- Título: *"Two checks that narrowed what we can claim"*
- *"Repeated-CV correlation (mean ± split SD across 20 partitions)"*
- *"0-back FC 0.274 ± 0.032 · FC reconfiguration 0.366 ± 0.024"*
- *"0-back + reconfiguration 0.333 ± 0.026 · Activation contrast 0.600 ± 0.016"*
- **Direction, as predicted—but only at group level:** *"Segregation fell under load (0.3271 → 0.3035; Δ = −0.0236; p = 3.45 × 10⁻⁵), yet larger shifts did not predict better performance (r = −0.105; p = .054)."*
- *"Open squares = held-out cross-run generalization."*
- Dos líneas de caveat (grandes):
  - *"A specificity check, not a competition: post hoc, 360 activation features vs 78 FC features, and 0-back activation alone predicts as well (0.571), so the benchmark is not load-specific. FC reconfiguration stays the load-specific measure."*
  - *"Activation is a raw BOLD amplitude difference, not a GLM beta. Individual vascular reactivity (CVR) is uncontrolled, and this dataset carries no CVR proxy."*
- **Gráfico:** `activation-robustness.png`.

**Marco mental (dilo así):** no es "perdimos contra la activación", es "hicimos **dos comprobaciones de
solidez**, y las dos nos obligaron a ser más precisos". Dos tiempos: **dirección** y **especificidad**.

**Comprobación 1 — la dirección (responde a la apuesta "Direction" de la slide 2):** a nivel de grupo la
segregación bajó 0.3271 → 0.3035; Δ = −0.0236; p = 3.45×10⁻⁵ (pareado, n=336) — **prácticamente cero de
azar**. La dirección predicha **existe**. Pero ¿predice a un individuo? La correlación entre cuánto cambia
la segregación de una persona y cuánto rinde es **r = −0.105, p = 0.054** — justo en el borde de lo
significativo. **No.**

> **La lección transferible más importante de la charla:** un efecto de grupo aplastante **no** garantiza
> valor predictivo individual. Igual que la tensión sube con la edad en la población (hecho rocoso) pero
> la edad sola no diagnostica a un paciente. Tamaño del efecto ≠ relevancia diagnóstica individual.

**Comprobación 2 — la especificidad (el gráfico):** puntos con barras de error, horizontal, 4 filas. Eje
X = correlación de CV, ~0.2 a 0.7. Cada fila = un conjunto de features distinto, misma receta de modelo:
- **0-back FC** (78) → **0.274**
- **FC reconfiguration** (78) → **0.366** (la protagonista de la slide 4)
- **Combined** (156) → **0.333** — ojo, **más bajo** que reconfiguration sola: juntarlas no ayuda, diluye. Pista de que la reconfiguración ya hace todo el trabajo útil de la FC.
- **Activation** (360) → **0.600**, en naranja/diamante — netamente por encima de toda la FC.

**Cuadrados abiertos** sobre reconfiguration y activation = comprobación aún más estricta (entrenar en una
run, predecir en la otra). A ojo (**lectura aproximada, no cifras impresas**): ~0.24 reconfig vs su 0.366;
~0.47 activation vs su 0.600. Mensaje honesto: la replicación entre runs es más débil para **las dos**.

**Por qué NO es una competición justa (dilo entero):**
1. **360 vs 78** features, sin igualar → más variables casi siempre predicen más, sin significado biológico.
2. **La activación de 0-back sola ya predice 0.571** — casi el 0.600 del contraste. Si con la persona en la condición fácil ya tienes casi toda la predicción, la señal **no es de la carga**; parece un **rasgo estable**.
3. **CVR (reactividad vascular cerebral):** la activación es amplitud BOLD cruda (no un beta de GLM), influida por factores vasculares (rigidez, edad, cafeína) sin nada que ver con actividad neuronal. Este dataset no puede medirlo ni controlarlo. La FC, al ser una **correlación**, cancela buena parte de ese factor de escala.

**El argumento de Goutham (es tu slide — dilo si preguntan "¿por qué os quedáis con la medida más débil?"):**
una **resta** cancela matemáticamente la varianza **estable** (anatomía vascular, amplitud basal, motion
de rasgo) y deja solo lo que **cambió** con la tarea. Por eso es **esperable** que la reconfiguración
replique peor entre runs que una medida cruda — no es un defecto que favorezca a la activación. Que la
activación replique mejor **no** prueba que sea mejor medida cognitiva; puede estar cargada de ruido
estable (vascular) que resulta que correlaciona con el rendimiento. Con 0-back-sola prediciendo 0.571,
la ventaja de activación la impulsa un **rasgo estático**, no la tarea.

⚠️ **Traceability gap:** los números de fiabilidad entre runs que sostienen este argumento (reconfig ≈
0.024, activación ≈ 0.169) viven en `nb08`, **no** en `pipeline/02`, así que **no** tienen test
automático. **No los imprimas en ninguna slide** — mantenlos verbales, en la nota del ponente.

**Cómo decirlo (~1.5–2 min — la slide más larga, ensáyala contra reloj):**
> *"Two checks, both of which narrowed our claim. **First, direction.** At the group level, segregation
> fell under load — from 0.327 to 0.304, p around 3 times ten-to-the-minus-five, essentially zero by
> chance. So the direction we predicted is real. But does it predict individuals? The correlation between
> a person's segregation change and their accuracy is minus 0.105, p = 0.054 — right at the border. So a
> rock-solid group effect does **not** give us individual prediction — same trap as blood pressure rising
> with age in a population but age alone not diagnosing a patient. **Second, specificity — naming the
> axes:** horizontal is cross-validated correlation, and each row is a different feature set. 0-back FC,
> 0.274. Our reconfiguration, 0.366. Both combined, 0.333 — lower, so combining doesn't help. And plain
> regional activation, 360 features, 0.600 — higher than any connectivity. But this is a specificity
> **check, not a competition**: it's post hoc, 360 versus 78 features unmatched, and 0-back activation
> alone already predicts 0.571 — so it isn't even load-specific. Activation is raw BOLD amplitude, which
> vascular reactivity contaminates and we can't control here. A difference score like ours mathematically
> removes that stable variance, so it's expected to look less reliable — that's why we keep it as our
> pre-specified, amplitude-independent measure."*

**Transición:** *"So — what does all this add up to?"* (a la conclusión).

**Preguntas probables:**
- *"Entonces la activación es mejor, ¿deberíais usarla?"* → "It predicts more in this unmatched, post-hoc comparison, but it isn't load-specific and it's confounded by vascular reactivity. We report it as a specificity check, not a replacement."
- *"¿Por qué la combinada baja?"* → "Adding 0-back FC to reconfiguration doesn't add independent signal and slightly dilutes it — reconfiguration alone is doing the work."
- *"¿Qué son los cuadrados?"* → "Cross-run generalization: train on one scan run, test on the other. Both measures drop — reliability across runs is weaker than the main estimate for both." (2 runs por persona — de aquí sale.)
- *"¿No es dFC?"* → "No — this is static FC aggregated per condition, then subtracted. Not dynamic connectivity."

**No digas:** que un modelo "gana"; que la reconfiguración es "la más robusta"; imprimir los números de fiabilidad de nb08.

---

# Slide 6 — Conclusions: qué predijimos y qué hizo la evidencia · **Kerem** · **se queda en pantalla en Q&A**

**En pantalla (verbatim):**
- Título: *"Predictive signal survives; connectivity-specific mechanism remains unresolved"*
- **Survives — the pattern hypothesis:** *"A 78-feature FC difference predicts unseen 2-back accuracy."* · *"The model transfers across identity-disjoint same-HCP cohorts (r = 0.398)."*
- **Refined — the directional hypothesis:** *"Segregation fell under load, but larger shifts did not predict better performance."* · *"Reconfiguration showed no clear gain beyond 0-back FC."* · *"FC added no clear gain over activation under the current unmatched comparison."*
- **Unresolved:** *"Is the predictive information connectivity-specific, or shared with task activation?"* · *"Vascular reactivity (CVR) is not controlled in the activation benchmark."*
- Sin gráfico. Andrea la aprobó sin cambios.

**Lo que debes saber:** son **tres columnas que cierran el bucle de la slide 2**. Survives = la apuesta
Pattern. Refined = la apuesta Direction. Unresolved = lo que honestamente no se sabe. Nombrar las dos
primeras columnas con las etiquetas de la slide 2 es lo que hace que el relato **cierre** en vez de sonar
a retractación. El 0.398 impreso bajo *Survives* es tu titular de cierre — remátalo como *"identity-disjoint
same-HCP transfer"*, nunca "independent".

**Cómo decirlo (~1 min):**
> *"To close the loop we opened. **Survives** — the pattern hypothesis: a 78-feature FC difference
> predicts unseen 2-back accuracy, and it transfers across identity-disjoint cohorts at r = 0.398.
> **Refined** — the directional hypothesis: segregation did fall under load **at the group level**, but
> bigger shifts didn't predict better performance; reconfiguration added no clear gain over
> single-condition FC; and FC added no clear gain over activation in this unmatched comparison.
> **Unresolved:** is the predictive information specific to connectivity, or shared with task activation?
> And vascular reactivity is uncontrolled. So — the predictive signal survives; the connectivity-specific
> mechanism remains unresolved. Thank you — happy to take questions."*

**Preguntas probables:** esta slide **es** tu mapa de Q&A — se queda proyectada. Cada columna apunta a un
backup: Refined→slides 8 y 9, Unresolved→slide 10 (futuro).

**No digas:** que "cambió" la conclusión; que se demostró un mecanismo de conectividad; "independent
validation" (es *identity-disjoint same-HCP*); la integración como confirmada a nivel individual (solo grupo).

---

# Backups (slides 7–11 · solo se abren si preguntan)

*(Slide 7 = portada divisoria "Backup · opened only on demand during Q&A". Sin habla.)*

## Slide 8 — Backup: la dirección en detalle

**En pantalla:** Título *"Group direction was real; the individual link was weak"* · *"Group mean: 0-back
0.3271 → 2-back 0.3035"* · *"Paired change: Δ = −0.0236; p = 3.45 × 10⁻⁵"* · *"Across participants:
r = −0.105; p = .054"* · *"A reliable mean shift does not establish individual predictive relevance."* ·
Gráfico `segregation-refinement.png`.

**El gráfico (2 paneles):** izquierda, dos **violines** (0-back / 2-back) = la distribución completa de
segregación de las 336 personas, no solo la media; una línea con dos puntos blancos une las medias y
muestra la caída 0.3271 → 0.3035. Derecha, **dispersión**: X = cuánto cambió la segregación de cada
persona, Y = su precisión en 2-back; línea vertical punteada en 0 (izquierda = se integró más). La
tendencia es casi plana. **Efecto de grupo real, vínculo individual débil** — la misma lección de la
slide 5 con la imagen completa.

**Cuándo abrirla:** "¿qué significa que la hipótesis direccional se 'matizó'?".

**Ojo:** no reuses la magnitud **−0.048** del abstract enviado — esa tenía otra convención de atlas; la
canónica es −0.0236 (mismo signo, mitad de magnitud).

## Slide 9 — Backup: las comprobaciones del resultado primario

**En pantalla:** Título *"The checks behind the primary result"* · *"Fixed holdout: r = 0.312 in 67
unseen participants"* · *"Full-refit null (seed 42): r = 0.405; p = 1/1001 ≈ .001"* · *"B→A A-label
permutation, fixed B predictions: p = 1/1001 ≈ .001"* · *"Reconfiguration over 0-back FC: ΔR² = +0.0344 ±
0.0225 → no clear gain"* · *"FC over activation: ΔR² = −0.0030 ± 0.0065 → no clear gain"* · *"The
permutation p belongs only to seed-42 r = 0.405; the holdout is a separate split."* · Gráfico
`null-and-holdout.png`.

**El gráfico (2 paneles):** izquierda, **histograma** = barajar 1000 veces las etiquetas de rendimiento
(reajustando el modelo, partición fija) → distribución de "esto es el azar con este pipeline"; una línea
vertical marca el r real 0.405, a la derecha de casi toda la nube → solo 1 de 1001 fue tan extrema →
p ≈ .001. Derecha, **holdout fijo**: 67 personas nunca tocadas, r = 0.312.

⚠️ El p de una-entre-mil pertenece **solo** al 0.405 de la semilla 42 — no al 0.312 del holdout ni al
0.366 de la CV repetida. Tres procedimientos distintos, misma historia, no intercambiables.

**Los dos ΔR² ("no clear gain"):** regla heurística de "2 SD" (el incremento es menor que el doble de su
variabilidad). **No es un test formal** de superioridad/equivalencia — dilo si preguntan.

**Cuándo abrirla:** "¿cómo sabéis que no es azar / y el holdout?".

*Munición extra (en `pipeline/02`, no en slide):* también controlaron parcialmente por precisión en
0-back (para descartar "habilidad general") y repitieron con **d′** (sensibilidad de teoría de detección
de señales) en la cohorte B. Si preguntan "¿controlasteis por habilidad general?" → sí.

## Slide 10 — Backup: trabajo futuro

**En pantalla:** Título *"Five tests could resolve the remaining question"* · 5 ítems + criterio de
decisión (*"FC must add reliable held-out value beyond activation and single-condition FC."*).

**Los 5, qué ataca cada uno:** (1) igualar dimensionalidad activación/FC en CV anidada; (2) separar
coactivación de acoplamiento con un estimador prefijado; (3) generalización a otro sitio/sesión con
parentesco modelado; (4) correr el modelo de activación sobre **reposo** — si el reposo predice tan bien
como la tarea, la señal es **independiente de tarea** (ejecutable ya: cohorte B trae 4 runs de reposo);
(5) **ST-GNN** (propuesta de Goutham, ya construyéndola) — modelar la transición como grafo dinámico y
que el modelo **aprenda** la reorganización en vez de resumirla en una resta ("ver la película, no dos
fotos").

**Cuándo abrirla:** "¿y ahora qué / cómo resolveríais lo de activación vs FC?".

## Slide 11 — Backup: referencias y guardarraíles

**En pantalla:** Título *"References and statistical guardrails"* · bibliografía (Avery 2020, Chan 2014,
Murphy 2020, Masharipov 2024, Hedge 2018, Logothetis 2008) + definiciones de guardarraíl (r = 0.366 ±
0.024 = media ± split SD de 20 particiones; seed-42 r = 0.405, p ≈ .001 = null de refit completo; B→A
r = 0.398, IC [0.25, 0.53] = transferencia identity-disjoint).

**Cómo presentarla (Andrea):** el último ponente la muestra ~5 segundos, dice "estas son las referencias",
y pasa a preguntas. **No se lee en voz alta.** Chan sostiene la fórmula de segregación; Hedge sostiene el
argumento de Goutham (slide 5); Logothetis enmarca el límite de CVR como limitación **ya conocida** del
campo, no un hallazgo propio.

**Las tres cifras a memorizar (sostienen toda la charla):** 0.366 ± 0.024 · seed-42 0.405, p ≈ .001 · B→A
0.398, IC [0.25, 0.53].
