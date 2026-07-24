# Guía del presentador — W3D5 · The Gammas

> **Qué es esto.** Una guía por diapositiva para que quien presente cada una tenga **todo** el contexto:
> definición de conceptos desde cero, cómo leer cada gráfico, cómo interpretar cada número, qué decir
> (con las frases en inglés listas para pronunciar) y qué preguntas esperar. Un bloque por slide.
> **Cada slide incluye además un bloque `🔍 Aclaraciones en profundidad`** — las dudas que surgieron
> revisando el deck, resueltas para el Q&A difícil. Las slides de resultados (5 y 6) llevan también un
> bloque `🎤 Dominio total` con guion ampliado, cifras a memorizar y preguntas trampa con respuesta.
> **Fuente de verdad:** `manuscript/slides/final-storyboard-5-plus-4.md` (spec, ya con las notas de
> Andrea del 23 jul) y `pipeline/02_canonical_analysis_and_slides.ipynb` (números). El texto que se
> proyecta es **inglés**; la explicación va en español y la charla se da en inglés.

## Coherencia con el deck en vivo — leer antes de usar

Esta guía describe el **estado objetivo** del storyboard (post-Andrea). Al 23 jul 17:42 el deck en vivo
(19 slides) tenía estas ediciones **pendientes de aplicar**; si abres Google Slides y ves la versión
vieja, es esto lo que falta:

- **Slide 3:** pregunta más grande, predicciones un paso menores, + línea de Avery 2020.
- **Slide 4:** banda de 3 definiciones, quitar detalle de adquisición, sustituir 3 cajas por la figura de matrices.
- **Slide 6:** nuevo título *"Two checks that narrowed what we can claim"*, 4 caveats → 2 grandes.
- **Slide 10:** cuarto test → quinto test (ST-GNN).

Si presentas antes de aplicarlas, sigue **el deck que se proyecta**, no esta guía, en esos puntos.

## Reparto (23 jul, Zoom + Discord)

| Slide | Presenta | Estado |
|---|---|---|
| 3 · Intro | **Valeria Moraga** | Confirmado (pidió ir primera) |
| 4 · Método | **Goutham Arcod** | Discord: "methodology is yours" — **conflicto**: en Zoom pareció que Arefeh también lo quería. Resolver antes de ensayar. |
| 5 · Resultado primario | *abierto* (Goutham propuso a Jaime) | — |
| 6 · El giro | *abierto* | La bisagra; que no caiga en quien menos ha ensayado |
| 7 · Conclusión | *abierto* | Andrea la aprobó sin cambios |

Cinco presentadores, cinco slides habladas (3–7), una cada uno. Portada, equipo y backups no consumen
minuto. Con seis, la slide 6 se parte en dos (puente direccional / benchmark de activación).

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

# Slide 1 — Portada

**En pantalla:** *"Functional Connectivity Reconfiguration in N-back Working Memory"* · los cinco
nombres · **The Gammas**. Sin gráfico, sin minuto de habla (se muestra mientras se saluda).

**Lo que debes saber:** El título nombra la **medida**, no un mecanismo. "Reconfiguration" aquí es
literalmente una **resta entre dos matrices de FC** agregadas por condición — no implica dinámica
temporal. Andrea pidió el **nombre del equipo bien visible**: el deck se archiva y lo lee la cohorte
del año que viene.

**Cómo decirlo:** *"Hi, we're The Gammas. Our project is on functional connectivity reconfiguration
in an N-back working-memory task."* Y pasar a la slide 2/3.

---

# Slide 2 — Equipo

**En pantalla:** *"Meet our team"* · cinco nombres · línea de pod/TA (Pod 884 "Ifrit Ras el Hanout" ·
Megapod Lotus · TA Andrea Buccellato · Project TA Azman Akhter). Sin ciencia.

**Pendientes conocidos (housekeeping, no ciencia):**
- Fotos stock y roles de relleno ("Actor/Doctor/…") — a medias; Arefeh, Valeria y Jaime ya tienen foto real, Kerem y Goutham no.
- **Direcciones de email personales** en un deck que se archiva públicamente — buscar y quitar antes de entregar.

**Cómo decirlo:** presentación de 10 segundos, solo nombres. Sin más.

---

# Slide 3 — Intro: la pregunta y las dos apuestas · **Valeria**

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
a r = 0.36. Cítalo para que, cuando en la slide 5 salga **nuestro 0.366**, la audiencia lo juzgue contra
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

### 🔍 Aclaraciones en profundidad (dudas del ponente)

**¿De dónde salen las dos hipótesis? ¿Bifurcación o HARKing?**
No hubo bifurcación de una hipótesis "grande" ni "adivinar a posteriori". La propuesta original (Arefeh,
15 jul) era **una sola frase direccional escrita *antes* del análisis** que ya contenía dos afirmaciones
lógicamente separables: que el *patrón* predice (parte débil, sin signo) y que la *dirección* predice a
nivel individual (parte fuerte, con signo). Presentarlas desdobladas es **descomponer una hipótesis
compuesta en sus dos condiciones de verificación**, no reescribir la historia. Lo que os blinda del
HARKing (*hypothesizing after results are known*): el resultado incómodo va **en vuestra contra** (la
dirección se quedó a nivel de grupo y encima apareció la activación). Nadie que "adivinara a posteriori"
elegiría una hipótesis que su propio análisis desinfla. Ancla clínica: un score preespecificado con dos
componentes (troponina *y* ECG) — reportar que uno pesó y el otro no es cumplir el protocolo, no cambiar
la hipótesis.
> Q&A: *"The original proposal was one directional sentence written before analysis; it always contained
> two separable claims, and we report honestly that one held and one was refined."*

**Patrón vs. dirección, de forma objetiva (no metáfora) — el objeto matemático de cada uno:**

| | **Pattern** | **Direction** |
|---|---|---|
| Qué es | vector de **78 números** por persona, usado *entero* en ridge | **1 escalar** por persona (Δ segregación 0→2) |
| Qué exige | nada de signo; solo que el conjunto prediga | signo concreto (↓ segregación) **y** predecir a nivel individual |
| Cómo se testea | ¿predice `acc_2bk` en no vistos? → 0.366 | ¿corr(Δsegregación, acc_2bk)? → −0.105 |
| Veredicto | **sobrevive** | **se matiza** (grupo sí, individuo no) |

En una línea: **multivariado-sin-signo (78) vs. univariado-con-signo (1)**. Analogías: patrón = panel de
78 biomarcadores en un modelo; dirección = *"a más fiebre, peor pronóstico"* (una variable, un signo).

**Benchmark de Avery 2020 — qué es y en qué os diferenciáis:**
Avery et al. (2020, *J Cogn Neurosci*) predijo `acc_2bk` desde FC de tarea con **CPM (Connectome-based
Predictive Modeling)**, r ≈ 0.36. Se cita como **ancla de calibración**, no como rival. Dos diferencias:
1. **Método/representación.** Avery = CPM: correlaciona cada arista con la conducta, **selecciona** las
   significativas (positivas/negativas), las suma y ajusta un modelo lineal, sobre **una sola condición**
   de FC. Vosotros = **ridge sobre un fingerprint de 78 redes de una *diferencia* (2bk−0bk)** — sin
   selección de aristas, y sobre un *contraste* entre condiciones, no una condición.
2. **Validación.** Avery valida en individuos nuevos (sanos y con deterioro de memoria). Vosotros añadís
   la **transferencia entre cohortes B→A identity-disjoint** (0.398).

Titular: igualáis/superáis ligeramente a Avery prediciendo desde el *cambio* entre condiciones, no desde
una condición. (La diferencia "seleccionar aristas" vs. "promediar a redes" reaparece en la Slide 4.)

---

# Slide 4 — Método: de los escáneres a una predicción · **Goutham**

**En pantalla (verbatim):**
- Título: *"We evaluated a 78-feature FC difference in held-out people"*
- Banda de definiciones (3 líneas):
  - *"Functional connectivity = the Pearson correlation between the time courses of two brain regions. Each node is one of 360 Glasser ROIs."*
  - *"FC reconfiguration = how much each network pair changes its coupling when memory load goes from 0-back to 2-back."*
  - *"System segregation = (mean within-network FC − mean between-network FC) ÷ mean within-network FC, computed per participant per condition (Chan et al. 2014)."*
- **1 · Cohort** — *"336 participants · HCP N-back working-memory task · 360 Glasser ROIs"*
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
(redes mezclándose). Esta métrica la usarás en la slide 6 — quédate con "alto modular, bajo integrado".

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
que decirlo si preguntan por los cuadrados abiertos (cross-run) de la slide 6.

**Cómo decirlo (~1 min):**
> *"Quick definitions first. Functional connectivity is just the Pearson correlation between two brain
> regions' time courses — each region is one of 360 Glasser nodes. FC reconfiguration is how much each
> network pair changes its coupling from 0-back to 2-back. And system segregation — we'll need it later —
> is within-network minus between-network connectivity, normalized: high means a modular brain, low means
> an integrated one. Pipeline: 336 HCP participants doing the N-back. We compute a 360-by-360 correlation
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

### 🔍 Aclaraciones en profundidad (dudas del ponente)

**¿Qué es "la foto de un estado"? (reconfiguración, con precisión):**
"La foto" = **una matriz de conectividad 360×360** para una persona y una condición: la correlación de
Pearson entre las series BOLD de cada par de las 360 ROIs Glasser. Tres precisiones que evitan la
confusión típica:
- **No** es una matriz BOLD cruda (eso sería la serie temporal, 360×~405 frames).
- **No** es una serie de matrices en el tiempo (eso sería FC *dinámica* — que **no** hacéis).
- **Sí** es una única matriz **estática** de correlaciones por condición; el tiempo ya está colapsado
  dentro de la correlación.

**Reconfiguración = foto(2-back) − foto(0-back)**, casilla a casilla, y luego resumida a 78. (Prueba de
esfuerzo cardiaco: importa el cambio reposo→esfuerzo, no cada foto por separado.)

**¿Qué dataframes, train/test y limpieza de IDs?**
Dataset = **B (`load_hcp`)**. 339 sujetos → se excluyen **3** (81, 143, 329) por no tener condición
2-back → **336 analíticos**. Split **por sujeto** (evita fuga), seed 42 → **269 train / 67 test**; CV
5-fold ×20 semillas; scaler y α de ridge ajustados **solo en train** por fold. La transferencia externa
(Slide 5) entrena en B y testea en A **quitando las 35 identidades solapadas** de B → ~301 B → 100 A,
*identity-disjoint*. Ahí es donde la "limpieza de IDs" es crítica: se elimina a mano el solape de
identidades entre las dos cohortes. Target siempre `acc_2bk`.

**¿De dónde salen las 78 features (de las ~64.000)?**
Aritmética pura. Matriz 360×360 → pares únicos = 360×359/2 = **64.620** aristas → con 336 personas eso es
p≫n (sobreajuste garantizado). Se agrupan las 360 ROIs en **12 redes Cole-Anticevic** y se promedia:
**12** valores dentro de red + **66** entre redes (12×11/2) = **78**. Es decir, **78 = 12 + 66**.

**Cole-Anticevic: ¿quién la aplicó, qué evidencia, movimiento válido o error? ¿Avery igual?**
Es un **atlas estándar publicado** (12 redes sobre los 360 nodos Glasser; partición Ji et al. 2019),
cargado por el framework oficial NMA/HCP (`regions.npy`) — **material canónico reutilizado**, no una
decisión ad hoc del equipo. Fue un **movimiento válido, no un error**: teóricamente alineado con la
hipótesis *entre-redes* (si la pregunta es entre sistemas, promediar a sistemas está a favor), y
estadísticamente correcto (78 features con n=336 es **p<n**, protege del sobreajuste). Matiz honesto:
promediar es compresión **con pérdida** (descarta señal de grano fino a nivel de arista); por eso
*"igualar la dimensionalidad activación/FC"* figura como **test 1 de la Slide 10 (trabajo futuro)**.
**¿Avery hace lo mismo? No exactamente:** Avery controla el p≫n **seleccionando aristas** (CPM),
vosotros **promediando a redes** — dos estrategias estándar distintas para el mismo problema (agregar
vs. seleccionar), con interpretaciones distintas (sistemas vs. conexiones concretas).

---

# Slide 5 — Resultado primario: el patrón predice y transfiere · *abierto*

**En pantalla (verbatim):**
- Título: *"The FC pattern predicted performance—and transferred to a separate cohort"*
- **B→A transfer** *"r = 0.398; bootstrap 95% CI [0.25, 0.53]"* · *"301 B-only → 100 A · 35 shared identities removed"*
- **Primary repeated CV** *"r = 0.366 ± 0.024 · 336 participants · 78 FC features"*
- *"Identity-disjoint same-HCP transfer—not independent-site validation."*
- **Gráfico:** dispersión `identity-disjoint-transfer.png`.

**El gráfico (nombra los ejes primero):** eje X = **precisión real en 2-back** de cada persona del
**grupo A** (test). Eje Y = **precisión predicha** por un modelo entrenado **solo en el grupo B**, que
nunca vio a nadie de A. Cada punto = una persona de A. La línea sube de izquierda a derecha: la
tendencia. Si el modelo fuera inútil, nube plana; en cambio, pendiente clara hacia arriba.

**Lo que debes saber — los dos números miden cosas distintas, no los mezcles:**
- **0.366 ± 0.024** = media de CV repetida. El ± es **split SD**, NO intervalo de confianza: repites 20
  veces el partir en 5 bloques, 0.366 es la media, 0.024 es cuánto se mueve según la partición. Habla de
  **estabilidad frente al azar de partición**.
- **0.398, IC 95% [0.25, 0.53]** = transferencia B→A. Aquí el modelo está **fijo** (entrenado una vez),
  así que se puede hacer **bootstrap** sobre las 100 personas de A → sí es incertidumbre poblacional
  clásica. Se quitaron 35 identidades compartidas para que nadie esté en train y test a la vez
  ("identity-disjoint").

*Calibración con Avery:* 0.366 y 0.398 caen justo en la zona del 0.36 publicado — o algo por encima. Es
**modesto en absoluto pero a la altura de la literatura**. El criterio de éxito del Project TA no era una
R² alta, sino **superar claramente el azar**; eso es lo que la slide 9 demuestra en detalle.

⚠️ Es transferencia entre **dos cohortes del mismo HCP** — más fuerte que barajar, más débil que
replicar en otro sitio/escáner. Nunca lo llames validación externa independiente.

**Cómo decirlo (~1 min):**
> *"Naming the axes: horizontal is each person's **actual** 2-back accuracy in cohort A; vertical is the
> accuracy our model **predicted** for them — a model trained only on cohort B that never saw these
> people. Each dot is one person, and the trend clearly rises. Two numbers. Our primary effect is the
> repeated cross-validation mean, r = 0.366 — and that plus-minus is a split standard deviation across
> partitions, not a confidence interval. Then we trained on B only and applied it to A, removing 35
> shared identities: r = 0.398, with a bootstrap 95% CI of 0.25 to 0.53. This is identity-disjoint
> transfer within the same HCP study — not independent-site validation, but it's the same ballpark as
> the 0.36 Avery reported."*

**Transición:** *"So the prediction held. But we ran two more checks — and they narrowed what we can claim."*

**Preguntas probables:**
- *"¿Y si es sobreajuste / suerte?"* → backup slide 9: null de 1000 permutaciones (p ≈ .001) + holdout fijo (r = 0.312, 67 personas nunca vistas).
- *"¿0.366 no es bajo?"* → "For brain-behavior prediction it's a real, publishable effect — Avery got 0.36 in the same data. The TA's bar was beating a permutation null, not a high R²."
- *"¿Por qué split SD y no IC en el 0.366?"* → "The model is refit each fold, so the spread is partition sensitivity, not population uncertainty. We only claim a true CI for the fixed-model transfer."

**No digas:** "intervalo de confianza" para 0.366; "validación externa".

### 🔍 Aclaraciones en profundidad (dudas del ponente)

**¿Hay que decir el matiz de la transferencia, y con esas palabras? — Sí, siempre.**
Sí: dilo literalmente y no lo ocultes. Es lo que demuestra que sabéis **qué fuerza** tiene el resultado y
te ahorra que te lo saquen como pega. La frase, proyectada y hablada:
> *"This is an identity-disjoint transfer between two cohorts of the same HCP study. It is not a
> validation in a different hospital, with a different scanner, on a different population. It is stronger
> than just reshuffling the data you already had, but weaker than a true external replication."*

Es un **gradiente de fuerza**: barajar-tus-datos (débil) < transferencia entre cohortes del mismo estudio
(lo vuestro) < replicación externa con otro escáner/población (fuerte). Decir dónde caéis es honestidad
epistémica. Ancla clínica: validar un score en otro subgrupo del mismo hospital vs. validarlo en otro
país — ambos valen, pero no son lo mismo, y decir cuál es cuál es lo que te hace creíble.

### 🎤 Dominio total (para el ponente — prob. Jaime)

**Cifras a clavar (sin mirar):** 0.366 ± 0.024 (CV repetida, ± = split SD) · 0.398, IC 95% [0.25, 0.53]
(B→A, bootstrap) · Avery 0.36 (ancla) · backup si aprietan: null seed-42 0.405 p≈.001, holdout fijo 0.312
(67 no vistos).

**El guion frase a frase — qué carga cada una:**
1. *Nombra los ejes primero* (regla de Andrea): X = precisión **real** en A; Y = precisión **predicha**
   por un modelo entrenado **solo en B**. Cada punto = una persona de A. Pendiente al alza = señal.
2. *Los dos números miden cosas distintas — nunca los fundas.* **0.366 ± 0.024**: el ± es **split SD**
   (el modelo se reajusta en cada fold → mide sensibilidad a la partición, no incertidumbre poblacional).
   **0.398 [0.25, 0.53]**: aquí el modelo está **fijo** → el bootstrap sobre las 100 personas de A sí es
   un IC clásico.
3. *Cierra con la calibración Avery:* 0.366/0.398 caen en la zona del 0.36 publicado → modesto en
   absoluto, **a la altura de la literatura**.

**Preguntas trampa (con respuesta lista):**
- *"0.366 es bajísimo, ¿no?"* → *"For brain–behavior prediction it's a real, publishable effect — Avery
  got 0.36 in the same data. The TA's success criterion was beating a permutation null, not a high R²."*
- *"¿Por qué split SD y no IC en el 0.366?"* → *"The model is refit every fold, so that spread is
  partition sensitivity. We only claim a true confidence interval for the fixed-model B→A transfer."*
- *"¿No es circular predecir N-back desde FC de N-back?"* → *"It's a same-task association — a stated
  limitation. We partly control it: partialling out 0-back accuracy (general ability) the signal
  survives, and we anchor it in Avery's same-task design. Cleanly separating task coactivation from
  connectivity is future work (backup 10, test 2)."*
- *"¿Y si es sobreajuste o suerte?"* → backup 9: null de 1000 permutaciones **p≈.001** + holdout fijo
  **0.312** en 67 personas nunca vistas.
- *"¿Por qué entrenar en B y testear en A, y no al revés?"* → *"B is the larger cohort (336 vs 100), so
  we train on the bigger sample and test on the smaller — the stronger generalization direction."*

**Entrega:** ~1 min. Es una slide de **un solo gráfico y dos números**; el riesgo es acelerarte y fundir
los dos números. Respira entre "0.366 split SD" y "0.398 IC". Transición ensayada a la 6: *"So the
prediction held — but we ran two checks, and they narrowed what we can claim."*

---

# Slide 6 — El giro: dos comprobaciones que acotan lo que se puede afirmar · *abierto* (la bisagra)

**En pantalla (verbatim):**
- Título: *"Two checks that narrowed what we can claim"* (retitulado 23 jul — el anterior sonaba a marcador)
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

**Comprobación 1 — la dirección (responde a la apuesta "Direction" de la slide 3):** a nivel de grupo la
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
- **FC reconfiguration** (78) → **0.366** (la protagonista de la slide 5)
- **Combined** (156) → **0.333** — ojo, **más bajo** que reconfiguration sola: juntarlas no ayuda, diluye. Pista de que la reconfiguración ya hace todo el trabajo útil de la FC.
- **Activation** (360) → **0.600**, en naranja/diamante — netamente por encima de toda la FC.

**Cuadrados abiertos** sobre reconfiguration y activation = comprobación aún más estricta (entrenar en una
run, predecir en la otra). A ojo (**lectura aproximada, no cifras impresas**): ~0.24 reconfig vs su 0.366;
~0.47 activation vs su 0.600. Mensaje honesto: la replicación entre runs es más débil para **las dos**.

**Por qué NO es una competición justa (dilo entero):**
1. **360 vs 78** features, sin igualar → más variables casi siempre predicen más, sin significado biológico.
2. **La activación de 0-back sola ya predice 0.571** — casi el 0.600 del contraste. Si con la persona en la condición fácil ya tienes casi toda la predicción, la señal **no es de la carga**; parece un **rasgo estable**.
3. **CVR (reactividad vascular cerebral):** la activación es amplitud BOLD cruda (no un beta de GLM), influida por factores vasculares (rigidez, edad, cafeína) sin nada que ver con actividad neuronal. Este dataset no puede medirlo ni controlarlo. La FC, al ser una **correlación**, cancela buena parte de ese factor de escala.

**El argumento de Goutham (aceptado — dilo si preguntan "¿por qué os quedáis con la medida más débil?"):**
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

### 🔍 Aclaraciones en profundidad (dudas del ponente)

**Activación vs. reconfiguración — la lectura neuroanatómica/fisiológica (por qué la activación predice
más).** Lo primero es qué mide cada una, *físicamente*:
- **Reconfiguración (FC):** una propiedad **relacional** — cómo cambia el *acoplamiento entre pares* de
  regiones con la carga. Es una **diferencia** (2bk−0bk) resumida en 78.
- **Activación:** una propiedad **por región** — cuánta *señal BOLD media* hay en cada una de las 360
  regiones, sin mirar conectividad. Diferencia de amplitud 2bk−0bk → 360 features.

Gana la activación (0.600 vs 0.366) por **tres razones acumuladas, y ninguna es "la conectividad
sobra":**
1. **Más features (comparación no igualada):** 360 vs 78. Más variables ≈ más capacidad predictiva, sin
   implicación biológica → por eso es *specificity check*, no competición.
2. **Fiabilidad (psicometría):** la activación media por región es un **rasgo estable y fiable**; la
   reconfiguración es una **resta de dos correlaciones**, dominada por ruido (**paradoja de fiabilidad**
   de Hedge 2018: restar dos medidas fiables da una diferencia poco fiable). Menos fiable → techo
   predictivo más bajo, por pura medición. *(Los números exactos de fiabilidad viven en nb08 y NO se
   imprimen — mantenlos verbales; ver traceability gap arriba.)*
3. **No es específica de la carga:** la activación de **0-back sola** ya predice **0.571** ≈ el 0.600 del
   contraste. Si con la persona en la condición fácil ya tienes casi toda la predicción, la señal habla
   de un **rasgo estable de la persona**, no de la memoria de trabajo.

**La salvedad neuroanatómica seria — CVR.** La activación aquí es amplitud BOLD **cruda** (no un beta de
GLM), contaminable por **reactividad vascular cerebral**: rigidez de vasos, edad, cafeína — *vascular, no
neuronal*. Este dataset no puede medirla. La **FC, al ser una correlación**, cancela buena parte de ese
factor de escala compartido. Por eso *no* vale "la activación gana, la conectividad sobra": la activación
puede estar ganando **en parte por estar contaminada con algo que no es cognición**. Ancla clínica:
activación = temperatura absoluta de cada órgano (fiable, pero contaminada por cuánto abriga el paciente
= CVR); reconfiguración = el *cambio* de temperatura al hacer ejercicio (cancela el abrigo basal, pero más
ruidoso). Que el termómetro absoluto "prediga mejor" no significa que mida mejor la respuesta cognitiva.

### 🎤 Dominio total (para el ponente — prob. Jaime)

**Es la bisagra y la slide más larga (~1.5–2 min). Ensáyala contra reloj.** Marco mental que debes
transmitir: *no es "perdimos contra la activación", son **dos comprobaciones de solidez** que nos
obligaron a afinar.*

**Estructura en dos tiempos (dilos en este orden):**
- **Check 1 · Dirección** → responde a la apuesta "Direction". Grupo: segregación 0.3271 → 0.3035,
  Δ=−0.0236, **p=3.45×10⁻⁵** (real). Individuo: corr(Δsegregación, acc) = **−0.105, p=0.054** (débil).
  Lección transferible: **un efecto de grupo aplastante ≠ valor predictivo individual** (la tensión sube
  con la edad en la población, pero la edad sola no diagnostica).
- **Check 2 · Especificidad** → las 4 filas: 0-back 0.274 · reconfig 0.366 · combinada 0.333 (¡baja!) ·
  activación 0.600. Y el porqué no es competición justa (features 360 vs 78; 0-back-sola 0.571; CVR).

**Cifras a clavar:** 0.274 / 0.366 / 0.333 / 0.600 · dirección grupo Δ=−0.0236 p=3.45×10⁻⁵ · individuo
−0.105 p=0.054 · activación 0-back-sola 0.571.

**Preguntas trampa (con respuesta lista):**
- *"Entonces la activación es mejor, ¿deberíais usarla?"* → *"It predicts more in this unmatched, post-hoc
  comparison, but it isn't load-specific and it's confounded by vascular reactivity. We report it as a
  specificity check, not a replacement."*
- *"¿Por qué la combinada (0.333) baja respecto a reconfig sola (0.366)?"* → *"Adding 0-back FC to
  reconfiguration adds no independent signal and slightly dilutes it — reconfiguration alone is doing the
  work."*
- *"¿Por qué os quedáis con la medida más débil en número bruto?"* (el argumento de Goutham) → *"A
  difference score mathematically cancels everything stable between conditions — vascular anatomy, baseline
  amplitude, trait motion — leaving only what changed with the task. So a subtraction is *expected* to
  replicate less across runs than a raw measure; that's not a defect. We keep reconfiguration because,
  by construction, it's the most amplitude-independent, load-specific measure."*
- *"¿Esto no es dinámica de red?"* → *"No — static FC aggregated per condition, then subtracted. Not
  dynamic connectivity."* (Es lo primero que caza un evaluador del campo.)
- *"¿Qué son los cuadrados abiertos?"* → cross-run (entrenar en una run, testear en la otra); **las dos**
  medidas bajan → sale del diseño de **2 runs por persona**.

**Entrega:** el mayor riesgo es que suene a marcador deportivo. Ancla siempre en *"specificity check"* y
cierra con *"reconfiguration stays our pre-specified, amplitude-independent measure."* Transición a la 7:
*"So — what does all this add up to?"*

---

# Slide 7 — Conclusión: qué predijimos y qué hizo la evidencia · *abierto* · **se queda en pantalla en Q&A**

**En pantalla (verbatim):**
- Título: *"Predictive signal survives; connectivity-specific mechanism remains unresolved"*
- **Survives — the pattern hypothesis:** *"A 78-feature FC difference predicts unseen 2-back accuracy."* · *"The model transfers across identity-disjoint same-HCP cohorts."*
- **Refined — the directional hypothesis:** *"Segregation fell under load, but larger shifts did not predict better performance."* · *"Reconfiguration showed no clear gain beyond 0-back FC."* · *"FC added no clear gain over activation under the current unmatched comparison."*
- **Unresolved:** *"Is the predictive information connectivity-specific, or shared with task activation?"* · *"Vascular reactivity (CVR) is not controlled in the activation benchmark."*
- Sin gráfico. Andrea la aprobó sin cambios.

**Lo que debes saber:** son **tres columnas que cierran el bucle de la slide 3**. Survives = la apuesta
Pattern. Refined = la apuesta Direction. Unresolved = lo que honestamente no se sabe. Nombrar las dos
primeras columnas con las etiquetas de la slide 3 es lo que hace que el relato **cierre** en vez de sonar
a retractación.

**Cómo decirlo (~1 min):**
> *"To close the loop we opened. **Survives** — the pattern hypothesis: a 78-feature FC difference
> predicts unseen 2-back accuracy, and it transfers across identity-disjoint cohorts. **Refined** — the
> directional hypothesis: segregation did fall under load, but bigger shifts didn't predict better
> performance; reconfiguration added no clear gain over single-condition FC; and FC added no clear gain
> over activation in this unmatched comparison. **Unresolved:** is the predictive information specific to
> connectivity, or shared with task activation? And vascular reactivity is uncontrolled. So — the
> predictive signal survives; the connectivity-specific mechanism remains unresolved. Thank you — happy
> to take questions."*

**Preguntas probables:** esta slide **es** tu mapa de Q&A — se queda proyectada. Cada columna apunta a un
backup: Refined→slides 8 y 9, Unresolved→slide 10 (futuro).

**No digas:** que "cambió" la conclusión; que se demostró un mecanismo de conectividad.

---

# Backups (solo se abren si preguntan)

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
slide 6 con la imagen completa.

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
argumento de Goutham (slide 6); Logothetis enmarca el límite de CVR como limitación **ya conocida** del
campo, no un hallazgo propio.

**Las tres cifras a memorizar (sostienen toda la charla):** 0.366 ± 0.024 · seed-42 0.405, p ≈ .001 · B→A
0.398, IC [0.25, 0.53].
