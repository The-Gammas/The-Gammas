# Presenter Guide — W3D5 · The Gammas

> **What this is.** A per-slide reading guide for the archived deck: every concept from scratch, how to
> read each figure, how to interpret each number, and the questions we expected with the answers we
> prepared. It is what makes the deck legible to someone who was not in the room, so it does not repeat
> the slide text — read it next to the deck.
> **Source of truth:** the deck `manuscript/slides/The Gammas - NMA project.pdf` — 11 pages, 6 spoken
> (cover/team merged into page 1) + 5 backups — and `pipeline/02_canonical_analysis_and_slides.ipynb`.
> Numbering below is the projected deck's; every number is checked against `pipeline/02`.

## Language guardrails (they bind any text that reuses these numbers)

- Not "we changed / the hypothesis evolved" → "we predicted two things; one held, one was refined".
- Not "confidence interval" for the ±0.024 → "split SD" (spread across partitions).
- Not "independent external validation" → "identity-disjoint same-HCP transfer".
- Not "dFC" / "dynamic FC" / "true network dynamics" → it's **static** FC aggregated per condition.
- Not "model A beats model B" (scoreboard) → "specificity check".
- No causality, adaptive benefit, or connectivity-specific mechanism claims.
- Define every concept where it is first named (FC, reconfiguration, segregation), and name a figure's
  axes before quoting any number off it.

---

# Slide 1 — Cover + team · Valeria

Title *"Functional Connectivity Reconfiguration in N-back Working Memory"*, the five names, no figure.
The title names the **measure**, not a mechanism: "reconfiguration" is literally a **difference between
two condition-averaged FC matrices** — no temporal dynamics implied.

---

# Slide 2 — Introduction: the question and the two predictions · **Valeria**

Asks *"Does load-related brain connectivity predict working-memory performance?"*, anchors on Avery et
al. 2020 (r = 0.36, same dataset) and states the two predictions — **Pattern** (a 78-feature FC
fingerprint of the 2-back − 0-back change predicts performance) and **Direction** (higher load shifts
networks toward integration; larger shifts accompany better performance).

**What to know (from scratch):**

*The N-back task.* Two working-memory difficulty levels: **0-back** (easy — "press when you see this
specific target image"; pure attention, almost everyone is near ceiling) and **2-back** (hard — "press
when the current image matches the one two positions back"; you must hold and update a buffer). 2-back is
where people **differ**, so it's the condition of interest.

*The two predictions — the key point of this slide.* Not one hypothesis, two, of different natures:
- **Pattern** is **multivariate and sign-free**: give the 78 numbers together to a model and see if the
  set predicts. It doesn't require any one of them to go up or down. Analogy: a 78-biomarker panel — you
  don't care about each one alone, you care whether the set is diagnostic.
- **Direction** is **a single signed number**: load must **lower** segregation (more integration), and
  that shift alone must predict who performs better. Analogy: "fever rises, and higher fever means worse
  prognosis" — one variable, one direction.

*Why two and not one.* The original proposal (Arefeh, 15 Jul) was **one sentence** that already held both
claims. When the data came in, one held and one didn't. Splitting them isn't rewriting history — it's
making explicit what they always were: **two independent tests**.

*Why Avery 2020.* It's the calibration anchor. It predicted `acc_2bk` from task FC, **same dataset**, at
r = 0.36. Cite it so that when **our 0.366** appears on slide 4, the audience judges it against that
published bar, not in a vacuum. **One citation here, no more.**

**Likely questions:**
- *"Wasn't it one hypothesis?"* → "The original proposal was one sentence containing both a pattern and a directional claim; we report them as the two separate tests they always were."
- *"Why 2-back, not 0-back, as the target?"* → "0-back is near ceiling — everyone gets it. 2-back is where people differ, so it's where there's something to predict."

**Avoid:** saying the hypothesis changed; a second citation.

---

# Slide 3 — Methods: from scans to a held-out prediction · **Arefeh**

Four steps (cohort · condition frames · model · held-out evaluation), a definitions band, and the figure
of three network matrices. **A/B is internal shorthand — the slide defines both cohorts here, at first
mention, or the audience meets "B→A" on the next slide with no referent.**

**What to know (from scratch) — the three definitions carry this slide:**

*Functional connectivity (FC).* The **Pearson correlation** between two regions' time courses. Take how
region A's signal rises and falls over time and region B's; if they move together, high positive
correlation; if unrelated, near zero. Each region is a **node**; there are **360** (Glasser atlas).

*FC reconfiguration.* How much each network pair changes its coupling from 0-back to 2-back. **2-back
picture minus 0-back picture.** (Analogy: a cardiac stress test — what matters is the rest→exercise
change, not either snapshot alone.)

*System segregation (needs unpacking — 3 pieces):* mean **within**-network connectivity, minus mean
**between**-network connectivity, divided by the within (to normalize). One number per person per
condition. **High = modular brain** (systems talking to themselves); **low = integrated** (networks
mixing). Slide 5 uses it — remember "high modular, low integrated".

*From 360×360 to 78.* The full matrices would be >64,000 pairs — impossible with 336 people without heavy
overfitting. So the 360 regions are grouped into **12 networks** (Cole-Anticevic atlas: visual, motor,
cognitive control, default…) and averaged: **12** within-network values + **66** between-network (12×11/2
= 66 unique pairs) = **78 features** per person per condition.

*The model and the four evaluations.* Ridge with standardization, both fit **inside** each training fold
— never using test info; that's the hygiene that stops CV from inflating. Evaluated four ways, each of
which appears later: repeated 5-fold CV ×20 · fixed holdout · 1000-permutation null · B→A transfer with
no shared identities.

**The figure (read it this way — it's not self-evident):** three 360×360 grids. Each cell = a region
pair; colour = its correlation in that condition. Scale: blue (negative) → white (≈0) → tan (positive).
Panel 1 = 2-back, panel 2 = 0-back, panel 3 = the difference.

⚠️ Panels 1 and 2 share **one** scale; panel 3 has **its own**, ~10× tighter. Three equally
intense-looking panels do **not** mean equal magnitudes — the difference panel is stretched to make a
genuinely small change visible. Only panel 3 carries a colorbar.

**Likely questions:**
- *"Why 78 and not all pairs?"* → "64,000 edges for 336 people would overfit; the network summary is the standard dimensionality reduction."
- *"Doesn't the task inflate correlations (coactivation)?"* → "Yes, task FC can reflect coactivation, not communication — it's a stated limitation; separating them is future work (backup slide 10)."
- *"Acquisition parameters?"* → TR 0.72 s, 4 s HRF shift, 312 frames per condition, **2 runs per person**
  (that last one is where the open cross-run squares on slide 5 come from); full detail in
  [`docs/data-dictionary.md`](../../docs/data-dictionary.md).

**Avoid:** "dynamic FC"; implying the matrices show comparable magnitudes (different scales).

---

# Slide 4 — Results: the pattern predicts and transfers · **Jaime**

Two numbers — primary repeated CV **r = 0.366 ± 0.024** (336 participants, 78 FC features) and the
**B→A transfer r = 0.398, 95% CI [0.25, 0.53]** (301 B → 100 A, 35 shared identities removed) — over the
scatter `identity-disjoint-transfer.png`, with the caveat line *"identity-disjoint same-HCP transfer, not
independent-site validation"*.

### 1 · The figure — name the axes before any number

- **X** = each person's **actual** 2-back accuracy in **cohort A** (the test set).
- **Y** = the accuracy **predicted** by a model trained **only on cohort B** that never saw anyone in A.
- Each dot = one real person in A. The cloud **rises left to right** → there's signal. If the model were
  useless, it'd be a flat cloud.

### 2 · The two numbers — they measure different things, do NOT conflate them

| | **0.366 ± 0.024** | **0.398 · CI [0.25, 0.53]** |
|---|---|---|
| What it is | **repeated-CV** mean (5-fold ×20 seeds) | **B→A transfer** (fixed model) |
| The ± / CI | **split SD** = how much it moves by partition | **bootstrap CI** = classic population uncertainty |
| Why they differ | model is **refit** each fold → measures *stability*, not a CI | model is **frozen** → you can resample A's 100 people |

The **0.398 is the strongest number**: a model trained on one cohort, tested on **another**, with no
shared identities (the 35 that appeared in both were removed).

### 3 · Calibration, and the caveat to state unprompted

0.366 and 0.398 land **right in the region of the published 0.36** from Avery in this same data — modest
in absolute terms, on par with the literature. The Project TA's success criterion was never a high R² but
**clearly beating chance**, which is what the validation backup (slide 9) shows.

The transfer is between **two cohorts of the same HCP**. Gradient: reshuffle-your-own-data <
**same-HCP transfer (this)** < true external replication. Saying where you land is credibility, and it
spares you the gotcha.

### Questions (likely + trap) — with ready answers

- *"What if it's overfitting or luck?"* → *"A 1000-permutation null gives p ≈ .001, and a fixed holdout of
  67 never-seen people gives r = 0.312 — three procedures, same story."* (slide 9)
- *"Isn't 0.366 low?"* → *"For brain–behavior prediction r ≈ 0.35–0.40 is a real, publishable effect —
  Avery got 0.36 in the same data, and the bar was beating a permutation null, not a high R². The ceiling
  is also capped by the ceiling effect on `acc_2bk`, with many people near 1.0."*
- *"Why split SD and not a CI on 0.366?"* → *"In repeated CV the model is refit every fold, so that spread
  is partition sensitivity, not population uncertainty. A classic CI is only legitimate for the frozen
  transfer model — which is why it goes with 0.398."*
- *"Isn't predicting N-back from N-back FC circular?"* → *"It's a same-task association that shares state
  variance — a stated limitation. Partialling out 0-back accuracy the signal survives, and we anchor it in
  Avery's same-task design; cleanly separating coactivation from coupling is future work (slide 10)."*
- *"Why train on B and test on A, not the reverse?"* → *"B is the larger cohort — 336 vs 100 — so we train
  on the bigger sample and test on the smaller: the more demanding, higher-powered direction."*
- *"Is this an external / independent validation?"* → *"No — identity-disjoint transfer within the same HCP
  study. Stronger than reshuffling, weaker than an independent-site replication."*

**Avoid:** "confidence interval" for 0.366 · "external / independent validation" for the transfer · saying
the model "wins" anything · "dynamic FC".

---

# Slide 5 — Robustness checks: two checks that narrowed what we can claim · **Goutham** (the hinge)

Four repeated-CV correlations, the group-level segregation result and the figure
`activation-robustness.png`, under two large caveat lines. **Framing:** not "we lost to activation", but
"two robustness checks, both of which made us more precise". Two beats: **direction** and **specificity**.

**Check 1 — direction (answers the "Direction" prediction from slide 2):** at group level, segregation
fell 0.3271 → 0.3035; Δ = −0.0236; p = 3.45×10⁻⁵ (paired, n=336) — **essentially zero by chance**. The
predicted direction **exists**. But does it predict an individual? The correlation between a person's
segregation change and their accuracy is **r = −0.105, p = 0.054** — right at the significance border. So
**no.**

> **The most transferable lesson of the talk:** an overwhelming group effect does **not** guarantee
> individual predictive value. Just as blood pressure rises with age across a population (rock-solid) but
> age alone doesn't diagnose a patient. Effect size ≠ individual diagnostic relevance.

**Check 2 — specificity (the figure):** dot-and-error-bar plot, horizontal, 4 rows. X = CV correlation,
~0.2 to 0.7. Each row = a different feature set, same model recipe:
- **0-back FC** (78) → **0.274**
- **FC reconfiguration** (78) → **0.366** (the star of slide 4)
- **Combined** (156) → **0.333** — note, **lower** than reconfiguration alone: combining doesn't help, it dilutes. A hint that reconfiguration is already doing all the useful FC work.
- **Activation** (360) → **0.600**, in orange/diamond — clearly above any FC.

**Open squares** over the reconfiguration and activation rows = a stricter check: train on one run, predict
the other (this is where the 2-runs-per-person design matters). Reconfiguration **0.246** against its
0.366, activation **0.475** against its 0.600 — cross-run replication is weaker for **both** measures
(`pipeline/02` cell 20, `cross_run_r`).

**Why it's NOT a fair competition (say all of it):**
1. **360 vs 78** features, unmatched → more features almost always predict more, with no biological meaning.
2. **0-back activation alone already predicts 0.571** — nearly the 0.600 of the contrast. If the person just sitting in the easy condition already gives you almost all the prediction, the signal is **not about load**; it looks like a **stable trait**.
3. **CVR (cerebral vascular reactivity):** activation is raw BOLD amplitude (not a GLM beta), influenced by vascular factors (vessel stiffness, age, caffeine) unrelated to neural activity. This dataset can't measure or control it. FC, being a **correlation**, cancels much of that shared scale factor.

**Goutham's argument (the answer to "why keep the weaker measure?"):** a **difference score**
mathematically cancels the **stable** variance (vascular anatomy, baseline amplitude, trait-level motion)
and leaves only what **changed** with the task. So it's **expected** that reconfiguration replicates worse
across runs than a raw measure — not a defect that favors activation. Activation replicating better does
**not** prove it's a better cognitive measure; it may be loaded with stable (vascular) noise that happens
to correlate with performance. With 0-back-alone predicting 0.571, the activation advantage is driven by a
**static trait**, not the task.

The between-run reliability behind that argument — reconfiguration **0.024** vs activation **0.169** — is
computed in `pipeline/02` cell 20 (`between_run_reliability`) and tabulated with its protocol in
[`docs/final-report.md` §5](../../docs/final-report.md). It was kept off the slide, not out of the record.

**Likely questions:**
- *"So activation is better — should you use it?"* → "It predicts more in this unmatched, post-hoc comparison, but it isn't load-specific and it's confounded by vascular reactivity. We report it as a specificity check, not a replacement."
- *"Why does the combined one drop?"* → "Adding 0-back FC to reconfiguration doesn't add independent signal and slightly dilutes it — reconfiguration alone is doing the work."
- *"Isn't this dFC?"* → "No — this is static FC aggregated per condition, then subtracted. Not dynamic connectivity."

**Avoid:** saying a model "wins"; calling reconfiguration "the most robust".

---

# Slide 6 — Conclusions: what we predicted and what the evidence did to it · **Kerem**

Three columns — *Survives* / *Refined* / *Unresolved* (the wording itself is in
[`docs/final-report.md` §6](../../docs/final-report.md)), no figure. They **close the loop opened on
slide 2**: Survives = the Pattern prediction, Refined = the Direction prediction. Reusing slide 2's labels
is what makes the story **close** rather than sound like a retraction. The 0.398 under *Survives* is the
closing headline — land it as *"identity-disjoint same-HCP transfer"*, never "independent". The slide
doubles as the Q&A map and stays projected: Refined→slides 8 and 9, Unresolved→slide 10.

**Avoid:** saying the conclusion "changed"; that a connectivity mechanism was demonstrated; integration as
confirmed at the individual level (it is group-level only).

---

# Backups (slides 7–11 · opened only if asked)

*(Slide 7 = the "Backup · opened only on demand during Q&A" divider.)*

## Slide 8 — the directional result in full

*"Group direction was real; the individual link was weak"* — the group means, the paired change, the
across-participant correlation, and the figure `segregation-refinement.png`. Opened when asked what "the
directional hypothesis was refined" actually means.

**The figure (2 panels):** left, two **violins** (0-back / 2-back) = the full segregation distribution of
the 336 people, not just the mean; a line with two white dots connects the means and shows the 0.3271 →
0.3035 drop. Right, **scatter**: X = each person's segregation change, Y = their 2-back accuracy; a dotted
vertical line at 0 (left = integrated more). The trend is almost flat. **Real group effect, weak
individual link** — slide 5's lesson with the full picture.

**Note:** don't reuse the **−0.048** magnitude from the submitted abstract — that used a different atlas
convention; the canonical one is −0.0236 (same sign, half the magnitude).

## Slide 9 — the checks behind the primary result

The fixed holdout (r = 0.312 in 67 unseen participants), the full-refit null (seed 42: r = 0.405,
p = 1/1001 ≈ .001), the B→A label permutation, the two incremental ΔR², and the figure
`null-and-holdout.png`. Opened on "how do you know it's not chance?".

**The figure (2 panels):** left, **histogram** = shuffle the performance labels 1000 times (refitting the
model, fixed partition) → the distribution of "what chance looks like with this pipeline"; a vertical line
marks the real r = 0.405, to the right of almost the whole cloud → only 1 of 1001 was that extreme →
p ≈ .001. Right, **fixed holdout**: 67 never-touched people, r = 0.312.

⚠️ The one-in-a-thousand p belongs **only** to the seed-42 r = 0.405 — not to the 0.312 holdout nor the
0.366 repeated-CV. Three different procedures, same story, not interchangeable.

**The two ΔR² ("no clear gain"):** reconfiguration over 0-back FC +0.0344 ± 0.0225, FC over activation
−0.0030 ± 0.0065, judged by a "2-SD" heuristic (the increment is smaller than twice its own variability).
**Not a formal** superiority/equivalence test — say so if asked.

*Not on a slide, but ready:* asked "did you control for general ability?" the answer is yes — `pipeline/02`
partials out 0-back accuracy and repeats the whole thing with **d′** in cohort B.

## Slides 10 and 11 — future work · references

Slide 10 lists five tests that could resolve the activation-vs-FC question, plus the decision criterion
(*"FC must add reliable held-out value beyond activation and single-condition FC."*); the five are kept
current in [`docs/final-report.md` §10](../../docs/final-report.md). Slide 11 holds the bibliography and
the guardrail definitions (±0.024 = split SD over 20 partitions · seed-42 r = 0.405, p ≈ .001 = full-refit
null · B→A 0.398, CI [0.25, 0.53] = identity-disjoint transfer); which reference backs which claim is
annotated in [`manuscript/references.md`](../references.md).
