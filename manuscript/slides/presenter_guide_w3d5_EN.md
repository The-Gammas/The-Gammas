# Presenter Guide — W3D5 · The Gammas

> **What this is.** A per-slide guide so whoever presents a slide has the full context: concepts from
> scratch, how to read each figure, how to interpret each number, what to say (with a ready delivery
> script), and what questions to expect. One block per slide.
> **A note on how to use it.** I put this together from the final deck, Andrea's review and our Discord
> discussion — it's a shared aid, not a script anyone has to follow word-for-word. Please correct anything
> I got wrong. Numbers are all checked against `pipeline/02`.
> **Source of truth:** the final deck `manuscript/slides/The Gammas - NMA project.pdf`
> and `pipeline/02_canonical_analysis_and_slides.ipynb`. On-screen copy is English; the talk is in English.

## Numbering — this guide matches the final deck

The final deck is **6 spoken pages + 5 backups**. **Cover and team are merged into page 1** (that's why the
numbering dropped by one vs the old storyboard). This guide uses **the projected-deck numbering**:

| Page / Slide | Content | Presenter |
|---|---|---|
| **1** · Cover + Team | Title + "Meet the Gammas" | Valeria opens |
| **2** · Introduction | The question + Pattern/Direction + Avery anchor | **Valeria** |
| **3** · Methods | 336 HCP · 78-feature fingerprint · benchmark vs 360 activation | **Arefeh** |
| **4** · Results | Primary r=0.366 + B→A transfer 0.398 (scatter) | **Jaime** |
| **5** · Robustness checks | Direction refined + activation 0.60 vs 0.37 + 2 guardrails | **Goutham** |
| **6** · Conclusions | Survives / Refined / Unresolved + thanks | **Kerem** |
| 7–11 · Backups | Divider + directional + validation + future + references | on demand |

Five presenters, **one slide each (slides 2–6)**. Cover/team and backups take no speaking slot. Split
locked on Discord (24 Jul); two tweaks vs the draft lines: Goutham takes the **whole** slide 5 (his
guardrails lead into the 0.60/0.37 numbers they qualify), and Jaime takes the **whole** slide 4 (0.366 +
the 0.398 transfer). The 0.398 is also printed on slide 6 under *Survives*, so Kerem lands it as the
closing headline.

## Common delivery rules (apply to EVERY slide)

**From Andrea's review (she was clear about these):**
1. **Define every concept as you name it** — FC, reconfiguration, segregation. Her most repeated point; Arefeh asked for it directly.
2. **Name the axes out loud before any number** from a figure: *"always make sure people know what they're looking at."*
3. **Less text, more visual.** Trim technical detail; cut material goes to Q&A.
4. **Rehearse to the minute.** Andrea offered a rehearsal round and Friday tutorial time. Let's pre-agree who fields which questions.
5. **It's about the process, not the finding:** *"you won't get any prize if the study is better or not."* Nobody is defending a discovery; we tell what we did and what we learned.

**Language guardrails we agreed on — worth avoiding on any slide:**
- Not "we changed / the hypothesis evolved" → "we predicted two things; one held, one was refined".
- Not "confidence interval" for the ±0.024 → "split SD" (spread across partitions).
- Not "independent external validation" → "identity-disjoint same-HCP transfer".
- Not "dFC" / "dynamic FC" / "true network dynamics" → it's **static** FC aggregated per condition.
- Not "model A beats model B" (scoreboard) → "specificity check".
- No causality, adaptive benefit, or connectivity-specific mechanism claims.

---

# Slide 1 — Cover + Team · Valeria opens

**On screen:** *"Functional Connectivity Reconfiguration in N-back Working Memory"* · the five names ·
**The Gammas** · pod/TA line (Pod 884 "Ifrit Ras el Hanout" · Megapod Lotus · TA Andrea Buccellato ·
Project TA Azman Akhter). No figure, no speaking slot (shown while Valeria greets).

**What to know:** The title names the **measure**, not a mechanism. "Reconfiguration" here is literally a
**difference between two condition-averaged FC matrices** — no temporal dynamics implied. Andrea asked for
the **team name prominent**: the deck is archived and read by next year's cohort.

**Known housekeeping (not science):**
- Stock photos and filler roles ("Actor/Doctor/…") — partly done; Arefeh, Valeria and Jaime have real photos, Kerem and Goutham don't yet.
- **Personal email addresses** on a deck that gets archived publicly — worth finding and removing before submission.

**Delivery:** *"Hi, we're The Gammas. Our project is on functional connectivity reconfiguration in an
N-back working-memory task."* Move to the Introduction (slide 2).

---

# Slide 2 — Introduction: the question and the two predictions · **Valeria**

**On screen (verbatim):**
- Title: *"Does load-related brain connectivity predict working-memory performance?"*
- Anchor: *"Avery et al. 2020 predicted 2-back accuracy from task FC in the same dataset (r = 0.36). We asked whether the change between loads carries that signal."*
- *"We predicted two things"*
  - **Pattern** — *"A 78-feature FC fingerprint of the 2-back − 0-back change predicts performance."*
  - **Direction** — *"Higher load shifts networks toward integration; larger shifts accompany better performance."*
- *"A distributed pattern and a one-number direction are different claims."*

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
making explicit what they always were: **two independent tests**. This covers us if someone asks "wasn't
it a single integration hypothesis?".

*Why Avery 2020.* It's the calibration anchor. It predicted `acc_2bk` from task FC, **same dataset**, at
r = 0.36. Cite it so that when **our 0.366** appears on slide 4, the audience judges it against that
published bar, not in a vacuum. **One citation here, no more** (Andrea's instruction).

**Delivery (~1 min):**
> *"Our question: does the way brain connectivity changes with memory load predict how well someone
> performs? A 2020 study by Avery already predicted 2-back accuracy from connectivity in this same
> dataset, at r = 0.36 — we asked whether the **change between loads** carries that signal. We made two
> different predictions. First, a **pattern**: a 78-feature fingerprint of the 2-back-minus-0-back change
> predicts performance — this doesn't need any particular direction, just that the combined pattern
> carries information. Second, a **direction**: higher load pushes networks toward integration, and people
> with bigger shifts perform better — that's a single signed number. These are different kinds of claims,
> so we test them separately."*

**Transition:** *"So how did we actually measure that? Over to the method."*

**Likely questions:**
- *"Wasn't it one hypothesis?"* → "The original proposal was one sentence containing both a pattern and a directional claim; we report them as the two separate tests they always were."
- *"Why 2-back, not 0-back, as the target?"* → "0-back is near ceiling — everyone gets it. 2-back is where people differ, so it's where there's something to predict."

**Avoid:** saying the hypothesis changed; a second citation.

---

# Slide 3 — Methods: from scans to a held-out prediction · **Arefeh**

**On screen (verbatim):**
- Title: *"We evaluated a 78-feature FC difference in held-out people"*
- Definitions band (3 lines):
  - *"Functional connectivity = the Pearson correlation between the time courses of two brain regions. Each node is one of 360 Glasser ROIs."*
  - *"FC reconfiguration = how much each network pair changes its coupling when memory load goes from 0-back to 2-back."*
  - *"System segregation = (mean within-network FC − mean between-network FC) ÷ mean within-network FC, computed per participant per condition (Chan et al. 2014)."*
- **1 · Cohort** — *"Two HCP N-back samples · 360 Glasser ROIs · B (primary): 336 participants — all cross-validation here · A (transfer target): 100 participants with per-subject behaviour — held out for the B→A test"* — **A/B is our internal shorthand; define both here, at first mention, or the audience meets "B→A" on the next slide with no referent.**
- **2 · Condition frames** — *"0-back and 2-back frames kept separate, with no temporal overlap"*
- **Figure: three network matrices** (0-back FC, 2-back FC, and their difference). Caption: *"12 Cole-Anticevic networks · 12 within + 66 between = 78 values per person"*
- **3 · Model** — *"StandardScaler + RidgeCV, fitted inside each training fold"*
- **4 · Held-out evaluation** — *"repeated 5-fold CV · fixed holdout · 1000-permutation null · B→A transfer (301 → 100, identity-disjoint)"*
- *"All splits hold out participants; "±" = split SD, not CI."*

**What to know (from scratch) — the three definitions are yours to say out loud:**

*Functional connectivity (FC).* The **Pearson correlation** between two regions' time courses. Take how
region A's signal rises and falls over time and region B's; if they move together, high positive
correlation; if unrelated, near zero. Each region is a **node**; there are **360** (Glasser atlas).

*FC reconfiguration.* How much each network pair changes its coupling from 0-back to 2-back. **2-back
picture minus 0-back picture.** (Analogy: a cardiac stress test — what matters is the rest→exercise
change, not either snapshot alone.)

*System segregation (needs unpacking — 3 pieces):* mean **within**-network connectivity, minus mean
**between**-network connectivity, divided by the within (to normalize). One number per person per
condition. **High = modular brain** (systems talking to themselves); **low = integrated** (networks
mixing). Goutham will use this on slide 5 — remember "high modular, low integrated".

*From 360×360 to 78.* The full matrices would be >64,000 pairs — impossible with 336 people without heavy
overfitting. So the 360 regions are grouped into **12 networks** (Cole-Anticevic atlas: visual, motor,
cognitive control, default…) and averaged: **12** within-network values + **66** between-network (12×11/2
= 66 unique pairs) = **78 features** per person per condition.

*The model (you all know this — don't dwell):* ridge with standardization, both fit **inside** each
training fold — never using test info. That's the hygiene that stops CV from inflating.

*The 4 evaluations* (each appears later): repeated 5-fold CV ×20 · fixed holdout · 1000-permutation null ·
B→A transfer with no shared identities.

*Figure (in the deck): Slide 3 — 0-back FC, 2-back FC, and their difference (78-network summary). Panels 1–2 share one colour scale; panel 3 has its own, about 10× tighter.*

**The figure (read it this way — it's not self-evident):** three 360×360 grids. Each cell = a region
pair; colour = its correlation in that condition. Scale: blue (negative) → white (≈0) → tan (positive).
Panel 1 = 2-back, panel 2 = 0-back, panel 3 = the difference.

⚠️ **Say this:** panels 1 and 2 share **one** scale; panel 3 has **its own**, ~10× tighter. Three
equally intense-looking panels do **not** mean equal magnitudes — the difference panel is stretched to
make a genuinely small change visible. Only panel 3 carries a colorbar.

**Cut from the slide (available in Q&A):** TR 0.72 s, 4 s HRF shift, 312 frames per condition, 2 runs per
person, the 360×360 intermediates. Andrea: *"just say it's HCP, 336 participants, this is the task. That's
it."* **Exception:** the **2-runs-per-person** design does need saying if anyone asks about the open
(cross-run) squares on slide 5.

**Delivery (~1 min):**
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

**Transition:** *"So did this 78-feature difference actually predict anything? Yes — and it transferred."*

**Likely questions:**
- *"Why 78 and not all pairs?"* → "64,000 edges for 336 people would overfit; the network summary is the standard dimensionality reduction."
- *"Doesn't the task inflate correlations (coactivation)?"* → "Yes, task FC can reflect coactivation, not communication — it's a stated limitation; separating them is future work (backup slide 10, test 2)."
- *"Acquisition parameters?"* → TR 0.72 s, HRF shift 4 s, 312 frames/condition, 2 runs — ready if asked.

**Avoid:** "dynamic FC"; implying the matrices show comparable magnitudes (different scales).

---

# Slide 4 — Results: the pattern predicts and transfers · **Jaime** ✅

> **Your slide.** Goal in ~1 min: tell that **the pattern predicts and transfers**, make clear **how
> strong** each number is, and **don't overclaim**. When done, hand to **Goutham** (slide 5).

**On screen (verbatim):**
- Title: *"The FC pattern predicted performance—and transferred to a separate cohort"*
- **Primary repeated CV** *"r = 0.366 ± 0.024 · 336 participants · 78 FC features"*
- **B→A transfer** *"r = 0.398; 95% CI [0.25, 0.53]"* · *"301 B → 100 A · 35 shared identities removed"*
- Caveat: *"Identity-disjoint same-HCP transfer—not independent-site validation."*
- Figure: scatter `identity-disjoint-transfer.png` (predicted vs observed, cohort A).

*Figure (in the deck): Slide 4 — B→A transfer: predicted (y) vs observed (x) 2-back accuracy in cohort A; each dot is one person.*

### 1 · The figure — name the axes BEFORE any number (Andrea's rule)

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

The **0.398 is your strongest number**: a model trained on one cohort, tested on **another**, with no
shared identities (the 35 that appeared in both were removed).

### 3 · Calibration with Avery (why 0.36–0.40 is a good number)

0.366 and 0.398 land **right in the region of the published 0.36** from Avery in this same data — or a
touch above. **Modest in absolute terms but on par with the literature.** The Project TA's success
criterion was never a high R², but **clearly beating chance** — which the validation backup (slide 9) shows:
1000-permutation null p ≈ .001 + fixed holdout 0.312.

### 4 · The mandatory caveat — say it yourself, don't wait to be asked

It's a transfer between **two cohorts of the same HCP**: stronger than reshuffling your own data, weaker
than replicating at another scanner/population. Gradient: reshuffle-your-own-data < **same-HCP transfer
(this)** < true external replication. Saying where you land = credibility (and it spares you the gotcha).

### 🎤 Your speech (English — verbatim, line by line)

```
This is our main result, and we evaluated it in two ways.
In the scatterplot, each dot is one person.
The X axis is their actual 2-back accuracy,
and the Y axis is what our model predicted.
The cloud trends upward, so there's signal.

Now, our two results.
The primary one, an r of 0.366, we got from cross-validation inside our large sample, cohort B, 336 subjects.
The 0.024 next to it is the spread across partitions.

Then we ran a transfer test with a frozen model, trained on B and applied to another cohort, A, 100 different people from the other HCP dataset.
We also removed 35 IDs that were in both.
That transfer, the one you see in the plot, gives an r of 0.398.

It's important to remember that our results are consistent with the published benchmark, Avery's 0.36, within the same HCP study.
And under permutation, the effect is unlikely to be due to chance.
```

**Handoff to Goutham:** *"So the pattern held. But is that signal specifically about connectivity? That's
what the next two checks tackle."*

### Interpretation in depth (if they push)

- **Why split SD ≠ CI.** In repeated CV the model is retrained each fold, so the spread measures *partition
  sensitivity*, not population uncertainty. The classic CI is only legitimate for the **fixed** transfer
  model — that's why the CI goes with 0.398, not 0.366.
- **Why B→A and not A→B.** B is the larger cohort (336 vs 100): you train on the big sample and test on the
  small one; it's the more demanding, higher-powered generalization direction.
- **Circularity (same task).** Predicting N-back from N-back FC shares state variance. It's **partly
  controlled**: partialling out general ability (`acc_0bk`) the signal survives, and it's anchored in
  Avery's same-task design. Separating coactivation from connectivity = future work (slide 10, test 2).
- **Why does the number look low?** In brain–behavior prediction r ≈ 0.35–0.40 is a real, publishable
  effect; the ceiling is also capped by the ceiling effect on `acc_2bk` (many people near 1.0).

### Questions (likely + trap) — with ready answers

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

**Avoid:** "confidence interval" for 0.366 · "external / independent validation" for the transfer · saying
the model "wins" anything (that's Goutham's slide) · "dynamic FC".

**Delivery:** ~1 min, one figure and two numbers. The only real risk is **rushing and merging the two
numbers** — breathe between *"0.366, split SD"* and *"0.398, bootstrap CI"*. Rehearse it against the clock.

---

# Slide 5 — Robustness checks: two checks that narrowed what we can claim · **Goutham** (the hinge)

**On screen (verbatim):**
- Title: *"Two checks that narrowed what we can claim"*
- *"Repeated-CV correlation (mean ± split SD across 20 partitions)"*
- *"0-back FC 0.274 ± 0.032 · FC reconfiguration 0.366 ± 0.024"*
- *"0-back + reconfiguration 0.333 ± 0.026 · Activation contrast 0.600 ± 0.016"*
- **Direction, as predicted—but only at group level:** *"Segregation fell under load (0.3271 → 0.3035; Δ = −0.0236; p = 3.45 × 10⁻⁵), yet larger shifts did not predict better performance (r = −0.105; p = .054)."*
- *"Open squares = held-out cross-run generalization."*
- Two caveat lines (large):
  - *"A specificity check, not a competition: post hoc, 360 activation features vs 78 FC features, and 0-back activation alone predicts as well (0.571), so the benchmark is not load-specific. FC reconfiguration stays the load-specific measure."*
  - *"Activation is a raw BOLD amplitude difference, not a GLM beta. Individual vascular reactivity (CVR) is uncontrolled, and this dataset carries no CVR proxy."*
- **Figure:** `activation-robustness.png`.

*Figure (in the deck): Slide 5 — cross-validated r by feature set: 0-back FC, FC reconfiguration, combined FC, activation. Open squares = cross-run generalization.*

**Framing (say it this way):** not "we lost to activation", but "we ran **two robustness checks**, and both
made us more precise". Two beats: **direction** and **specificity**.

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

**Open squares** over the reconfiguration and activation rows = an even stricter check (train on one run,
predict on the other). By eye (**approximate, not printed numbers**): ~0.24 reconfig vs its 0.366; ~0.47
activation vs its 0.600. Honest message: cross-run replication is weaker for **both** measures.

**Why it's NOT a fair competition (say all of it):**
1. **360 vs 78** features, unmatched → more features almost always predict more, with no biological meaning.
2. **0-back activation alone already predicts 0.571** — nearly the 0.600 of the contrast. If the person just sitting in the easy condition already gives you almost all the prediction, the signal is **not about load**; it looks like a **stable trait**.
3. **CVR (cerebral vascular reactivity):** activation is raw BOLD amplitude (not a GLM beta), influenced by vascular factors (vessel stiffness, age, caffeine) unrelated to neural activity. This dataset can't measure or control it. FC, being a **correlation**, cancels much of that shared scale factor.

**Goutham's argument (it's your slide — say it if asked "why keep the weaker measure?"):** a **difference
score** mathematically cancels the **stable** variance (vascular anatomy, baseline amplitude, trait-level
motion) and leaves only what **changed** with the task. So it's **expected** that reconfiguration replicates
worse across runs than a raw measure — not a defect that favors activation. Activation replicating better
does **not** prove it's a better cognitive measure; it may be loaded with stable (vascular) noise that
happens to correlate with performance. With 0-back-alone predicting 0.571, the activation advantage is
driven by a **static trait**, not the task.

⚠️ **Traceability gap:** the between-run reliability numbers behind this argument (reconfig ≈ 0.024,
activation ≈ 0.169) live in `nb08`, **not** in `pipeline/02`, so they have **no automated check**. **Don't
print them on a slide** — keep them verbal, in the speaker note.

**Delivery (~1.5–2 min — the longest slide; rehearse against the clock):**
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

**Transition:** *"So — what does all this add up to?"* (to the conclusion).

**Likely questions:**
- *"So activation is better — should you use it?"* → "It predicts more in this unmatched, post-hoc comparison, but it isn't load-specific and it's confounded by vascular reactivity. We report it as a specificity check, not a replacement."
- *"Why does the combined one drop?"* → "Adding 0-back FC to reconfiguration doesn't add independent signal and slightly dilutes it — reconfiguration alone is doing the work."
- *"What are the squares?"* → "Cross-run generalization: train on one scan run, test on the other. Both measures drop — reliability across runs is weaker than the main estimate for both." (2 runs per person — that's where this comes from.)
- *"Isn't this dFC?"* → "No — this is static FC aggregated per condition, then subtracted. Not dynamic connectivity."

**Avoid:** saying a model "wins"; calling reconfiguration "the most robust"; printing the nb08 reliability numbers.

---

# Slide 6 — Conclusions: what we predicted and what the evidence did to it · **Kerem** · **keep projected in Q&A**

**On screen (verbatim):**
- Title: *"Predictive signal survives; connectivity-specific mechanism remains unresolved"*
- **Survives — the pattern hypothesis:** *"A 78-feature FC difference predicts unseen 2-back accuracy."* · *"The model transfers across identity-disjoint same-HCP cohorts (r = 0.398)."*
- **Refined — the directional hypothesis:** *"Segregation fell under load, but larger shifts did not predict better performance."* · *"Reconfiguration showed no clear gain beyond 0-back FC."* · *"FC added no clear gain over activation under the current unmatched comparison."*
- **Unresolved:** *"Is the predictive information connectivity-specific, or shared with task activation?"* · *"Vascular reactivity (CVR) is not controlled in the activation benchmark."*
- No figure. Andrea approved it with no changes.

**What to know:** three columns that **close the loop opened on slide 2**. Survives = the Pattern
prediction. Refined = the Direction prediction. Unresolved = what we honestly don't know. Naming the first
two columns with slide 2's labels is what makes the story **close** rather than sound like a retraction.
The 0.398 printed under *Survives* is your closing headline — land it as *"identity-disjoint same-HCP
transfer"*, never "independent".

**Delivery (~1 min):**
> *"To close the loop we opened. **Survives** — the pattern hypothesis: a 78-feature FC difference
> predicts unseen 2-back accuracy, and it transfers across identity-disjoint cohorts at r = 0.398.
> **Refined** — the directional hypothesis: segregation did fall under load **at the group level**, but
> bigger shifts didn't predict better performance; reconfiguration added no clear gain over
> single-condition FC; and FC added no clear gain over activation in this unmatched comparison.
> **Unresolved:** is the predictive information specific to connectivity, or shared with task activation?
> And vascular reactivity is uncontrolled. So — the predictive signal survives; the connectivity-specific
> mechanism remains unresolved. Thank you — happy to take questions."*

**Likely questions:** this slide **is** your Q&A map — keep it projected. Each column points to a backup:
Refined→slides 8 and 9, Unresolved→slide 10 (future work).

**Avoid:** saying the conclusion "changed"; that a connectivity mechanism was demonstrated; "independent
validation" (it's *identity-disjoint same-HCP*); integration as confirmed at the individual level (group only).

---

# Backups (slides 7–11 · open only if asked)

*(Slide 7 = the "Backup · opened only on demand during Q&A" divider. No speaking.)*

## Slide 8 — Backup: the directional result in full

**On screen:** Title *"Group direction was real; the individual link was weak"* · *"Group mean: 0-back
0.3271 → 2-back 0.3035"* · *"Paired change: Δ = −0.0236; p = 3.45 × 10⁻⁵"* · *"Across participants:
r = −0.105; p = .054"* · *"A reliable mean shift does not establish individual predictive relevance."* ·
Figure `segregation-refinement.png`.

*Figure (in the deck): Slide 8 — group segregation shift (violins, left) and the weak individual link (scatter, right).*

**The figure (2 panels):** left, two **violins** (0-back / 2-back) = the full segregation distribution of
the 336 people, not just the mean; a line with two white dots connects the means and shows the 0.3271 →
0.3035 drop. Right, **scatter**: X = each person's segregation change, Y = their 2-back accuracy; a dotted
vertical line at 0 (left = integrated more). The trend is almost flat. **Real group effect, weak
individual link** — slide 5's lesson with the full picture.

**When to open:** "what does 'the directional hypothesis was refined' actually mean?".

**Note:** don't reuse the **−0.048** magnitude from the submitted abstract — that used a different atlas
convention; the canonical one is −0.0236 (same sign, half the magnitude).

## Slide 9 — Backup: the checks behind the primary result

**On screen:** Title *"The checks behind the primary result"* · *"Fixed holdout: r = 0.312 in 67 unseen
participants"* · *"Full-refit null (seed 42): r = 0.405; p = 1/1001 ≈ .001"* · *"B→A A-label permutation,
fixed B predictions: p = 1/1001 ≈ .001"* · *"Reconfiguration over 0-back FC: ΔR² = +0.0344 ± 0.0225 → no
clear gain"* · *"FC over activation: ΔR² = −0.0030 ± 0.0065 → no clear gain"* · *"The permutation p belongs
only to seed-42 r = 0.405; the holdout is a separate split."* · Figure `null-and-holdout.png`.

*Figure (in the deck): Slide 9 — permutation null with the real r marked (left) and the fixed holdout scatter (right).*

**The figure (2 panels):** left, **histogram** = shuffle the performance labels 1000 times (refitting the
model, fixed partition) → the distribution of "what chance looks like with this pipeline"; a vertical line
marks the real r = 0.405, to the right of almost the whole cloud → only 1 of 1001 was that extreme →
p ≈ .001. Right, **fixed holdout**: 67 never-touched people, r = 0.312.

⚠️ The one-in-a-thousand p belongs **only** to the seed-42 r = 0.405 — not to the 0.312 holdout nor the
0.366 repeated-CV. Three different procedures, same story, not interchangeable.

**The two ΔR² ("no clear gain"):** a "2-SD" heuristic (the increment is smaller than twice its own
variability). **Not a formal** superiority/equivalence test — say so if asked.

**When to open:** "how do you know it's not chance / and the holdout?".

*Extra ammunition (in `pipeline/02`, not on a slide):* we also partial out 0-back accuracy (to rule out
"general ability") and repeat with **d′** (signal-detection sensitivity) in cohort B. If asked "did you
control for general ability?" → yes.

## Slide 10 — Backup: future work

**On screen:** Title *"Five tests could resolve the remaining question"* · 5 items + decision criterion
(*"FC must add reliable held-out value beyond activation and single-condition FC."*).

**The 5, what each attacks:** (1) match activation/FC dimensionality in nested CV; (2) separate
coactivation from coupling with a prespecified estimator; (3) independent-site / repeat-session
generalization with kinship modelled; (4) run the activation model on **resting-state** — if rest predicts
as well as task, the signal is **task-independent** (runnable now: cohort B ships 4 rest runs); (5)
**ST-GNN** (Goutham's proposal, already building it) — model the transition as a dynamic graph and let the
model **learn** the reorganization rather than summarize it in one difference ("watch the film, not two
snapshots").

**When to open:** "what next / how would you resolve the activation-vs-FC question?".

## Slide 11 — Backup: references and statistical guardrails

**On screen:** Title *"References and statistical guardrails"* · bibliography (Avery 2020, Chan 2014,
Murphy 2020, Masharipov 2024, Hedge 2018, Logothetis 2008) + guardrail definitions (r = 0.366 ± 0.024 =
mean ± split SD over 20 partitions; seed-42 r = 0.405, p ≈ .001 = full-refit null; B→A r = 0.398, CI
[0.25, 0.53] = identity-disjoint transfer).

**How to present it (Andrea):** the last presenter shows it for ~5 seconds, says "these are the references
we used", and moves to questions. **Don't read it aloud.** Chan backs the segregation formula; Hedge backs
Goutham's argument (slide 5); Logothetis frames the CVR limit as a **known** field limitation, not a
finding of ours.

**Three numbers to memorize (they carry the whole talk):** 0.366 ± 0.024 · seed-42 0.405, p ≈ .001 · B→A
0.398, CI [0.25, 0.53].
