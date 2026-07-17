# Literature review (automated + verified) — reconfiguration → WM-prediction MVP

**Consolidated 2026-07-17.** Merges two passes into one decision-oriented source of truth:
a manual deep-research pass (Claude Desktop, 16 Jul) and an automated fan-out pass with
**adversarial multi-vote verification** (17 Jul). Only findings relevant to our MVP and citations
that survived verification are kept. Provenance is tagged per item:
- **[verified]** — confirmed by ≥2/3 adversarial verifier votes on the source quote (17 Jul pass).
- **[canonical]** — well-established methods reference from the manual pass; not independently re-voted here, but standard in the field.

---

## Bottom line

- Our headline (out-of-sample r≈0.35 predicting 2-back accuracy from N-back FC) is **consistent with
  Avery 2020 (r=0.36)** — a conceptual replication (different model), not a discovery. Own it as such.
- Our genuine, distinct contribution is the **dissociation**: the load-driven reconfiguration
  change-score does **not** predict WM (r≈0.04) while trait/baseline FC does (r≈0.29) — with a
  mechanistic reason (difference-score unreliability). Frame the study around this, not around "FC
  predicts WM".
- Two of the manual pass's recommendations (**family-aware CV; age/sex confounds**) are **not
  implementable** on the Neuromatch-curated data and are dropped.

---

## Settled by the manual pass (kept as background; not re-voted)

- **Calibration (general).** Marek 2022 (*Nature*): out-of-sample multivariate brain–behaviour
  effects shrink ~63% vs in-sample; report cross-validated, CI-bounded numbers, never in-sample. **[canonical]**
- **Task-evoked co-activation confound.** Cole 2019 (*NeuroImage*) and Masharipov 2024 (*Commun Biol*
  7:1402): blockwise task FC is inflated by the shared evoked response; FIR / block-mean removal is
  the fix; canonical-HRF regression is inadequate. For our long blocks, cheapest remedies are
  block-mean removal or discarding the first ~6 s per block — or declare the confound. **[canonical]**
- **d′ extreme-rate correction.** Hautus 1995: use the loglinear rule (add 0.5 to hits/FA, 1 to trial
  totals). Already implemented/validated in notebook §5 (loglinear ≈ 1/2N clip). **[canonical]**
- **Direction framing.** The **task-complexity / integration-for-hard-tasks** account (Cohen &
  D'Esposito 2016 — direct n-back; Shine 2016; Barbey 2018) is the defensible frame, not the
  resting-state segregation-maintenance account (Chan 2014 / Calder 2026, which are rest/aging). **[canonical]**
- **Graph metrics.** Newman modularity + Chan system segregation (segregation), global efficiency +
  participation coefficient (integration); proportional (density-matched) thresholds; weight-conserving
  treatment of negative edges (Rubinov & Sporns 2010/2011). Report 2–3, interpret cautiously. **[canonical]**

---

## Verified findings (17 Jul adversarial pass) — the four gaps

### Gap 1 — Same-task circularity & the correct WM-specific benchmark
- **Avery 2020** predicts 2-back accuracy from same-task N-back FC in novel HCP subjects at **r=0.36**
  (rest FC r=0.20). This is the closest same-task/target design (their 10-fold-CV CPM vs our 5-fold
  RidgeCV); **our r≈0.35 is consistent with it** — a conceptual replication, not exact. **[verified]**
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC8004893/>
- Other WM-specific out-of-sample benchmarks: out-of-scanner List-Sorting from N-back FC **r=0.24**
  (rest 0.10) **[verified]** <https://pmc.ncbi.nlm.nih.gov/articles/PMC8413720/>; dynamic-FC CPM WM
  capacity **r≈0.22** **[verified]** <https://pmc.ncbi.nlm.nih.gov/articles/PMC7930367/>; CPM 2-back
  performance up to **r=0.48** **[verified]** <https://pmc.ncbi.nlm.nih.gov/articles/PMC12439485/>.
  → The WM band is ~0.22–0.48; **0.35 sits inside it, not "above typical"** (corrects the manual pass,
  which calibrated against fluid-intelligence r≈0.38).
- Same-task prediction **is accepted** in the field (Avery; PMC12439485), **not** fatally circular —
  but same-context prediction is inflated vs cross-context (~2×: r=.58 intra → .27 cross in movie
  studies) **[verified]** <https://www.biorxiv.org/content/10.1101/2023.11.14.566767.full.pdf>.
  Rigorous guards: predict out-of-scanner / cross-task behaviour (PMC8413720; PMC12439485).
- **Verdict — CHANGE (cheap):** re-anchor calibration to Avery 2020 (r=0.36); declare same-context
  inflation as a limitation. Our d′ (net of response bias) is a partial guard.

### Gap 2 — Novelty of the reconfiguration change-score null
- A reconfiguration **magnitude** score *can* predict cognition (Thiele 2022, *Cereb Cortex*: more
  reconfiguration ↔ lower intelligence, rho≈−0.23) — so "reconfiguration doesn't predict" is not a
  safe blanket headline. **[verified]** <https://academic.oup.com/cercor/article/32/19/4172/6523266>
- **Difference-score psychometrics** explain our null: a within-subject contrast can be robust yet have
  ~zero between-subject reliability, because subtraction removes the true-score variance shared across
  conditions (worked example: faces−shapes contrast reliability −0.06 while each condition map is
  0.95–0.97, because conditions correlate r=.97). **[verified]**
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC5912348/>
  → This is exactly our case (0bk/2bk FC predict r≈0.29; their difference r≈0.04).
- **Verdict — ADD (cheap):** reframe the null via difference-score reliability (a principled result,
  not "we found reconfiguration fails"). Optional direct evidence: split-half reliability of the
  2bk−0bk fingerprint (a few hours) — see the "our own calculation" step.

### Gap 3 — Family-structure leakage without family IDs
- Family leakage is **the mildest** leakage type: Δr≈0.00–0.02 for cognition/reasoning in full
  datasets; ~0.04 worst case (twins-only). **[verified]** <https://www.nature.com/articles/s41467-024-46150-w>
- Rigorous HCP work controls it by permuting only within sibling types (Greene 2018) — which **needs
  kinship IDs the curated set does not expose.** **[verified]** <https://www.nature.com/articles/s41467-018-04920-3>
- **Verdict — CONFIRM / DECLARE:** one limitation sentence citing the Rosenblatt bound (our r≈0.35
  → ≥~0.33 corrected; story unchanged). **Drops the manual pass's A2 (family-aware CV): not
  implementable and barely matters.**

### Gap 4 — d′ vs accuracy as the HCP-WM target
- The canonical FC→WM paper (Avery 2020) uses **raw 2-back accuracy**, not d′. The verified pass found
  no surviving evidence on HCP-WM d′ reliability (thin — treat with caution).
- **Verdict — NUANCE:** lead with **accuracy** (comparable to Avery 0.36); keep **d′ as the
  measurement-clean primary target** (separates sensitivity from response bias). Under the acc_0bk
  control, d′ and accuracy retain comparable partial signal (~0.24 vs ~0.22) — d′ is **not** more
  robust here. Note the ~16 target / ~64 non-target trial count as a d′ reliability caveat.

---

## Not supported by our data — drop from the plan

- **Age/sex confounds (manual pass A3):** the curated set exposes only **synthetic** pseudo-demographics;
  the data doc says do not use them as confounds. Not implementable.
- **Family-aware / leave-families-out CV (manual pass A2):** no kinship IDs exposed; also Δr≲0.02 per
  Rosenblatt 2024. Declare as a limitation instead.

---

## Decision list for the 1-week MVP

| # | Action | Type | MVP-feasible | Effort |
|---|---|---|---|---|
| 1 | Re-anchor calibration to Avery 2020 (r=0.36); state same-context inflation | CHANGE | yes | ~15 min |
| 2 | Reframe the null via difference-score reliability (+ Thiele 2022 contrast) | ADD | yes | ~20 min |
| 3 | Optional: compute split-half reliability of the 2bk−0bk fingerprint (direct evidence) | ADD | yes | ~2–3 h |
| 4 | Family leakage → one limitation sentence (Rosenblatt bound); drop A2/A3 | CONFIRM | yes | ~10 min |
| 5 | Abstract: lead with accuracy; d′ as measurement-clean primary target | CHANGE | yes | ~15 min |
| 6 | Co-activation confound (Cole/Masharipov): declare; block-mean/6-s trim only if CV refactor stable | IMPROVE | declare: yes / re-run: maybe | 2 h – 2 d |

**Out of scope this week:** feature reduction (78 features / 336 subj is fine for RidgeCV), dynamic-FC
HMM (deferred; CAPs/k-means is the declared extension), re-deriving FC, multi-task/rest comparisons
needing extra data.

---

## Refuted / discarded (did NOT survive verification — do not cite)

- "HCP WM-from-FC prediction is r≈0.08" — refuted 0-3.
- "Relating task-FC to task signal is circular unless mean evoked response is regressed" — refuted 0-3.
- "Greene 2018 acknowledges same-task FC predicts same-task behaviour better" — 1-2, not confirmed.

*(Two Gap-3 leakage claims were confirmed 2-0 with the safety classifier unavailable; treated as
reliable but flagged.)*
