# Literature review (automated + verified) — reconfiguration → WM-prediction MVP

**Consolidated 2026-07-17.** Merges two passes into one decision-oriented source of truth:
a manual deep-research pass (Claude Desktop, 16 Jul) and an automated fan-out pass with
**adversarial multi-vote verification** (17 Jul). Only findings relevant to our MVP and citations
that survived verification are kept. Provenance is tagged per item:
- **[verified]** — confirmed by ≥2/3 adversarial verifier votes on the source quote (17 Jul pass).
- **[canonical]** — well-established methods reference from the manual pass; standard in the field, not independently re-voted.

> **Status:** the decisions below are implemented in [`../../manuscript/abstract.md`](../../manuscript/abstract.md)
> and [`../../sandbox/jaime/04_goutham_pipeline_on_B.ipynb`](../../sandbox/jaime/04_goutham_pipeline_on_B.ipynb)
> (post-audit pattern-vs-scalar reframe). This file is the **evidence base**; the citation list lives in
> [`../../manuscript/references.md`](../../manuscript/references.md).
>
> **18 Jul pointer:** the evidence and numbers remain useful. "Pattern vs scalar" is an active
> candidate finding, neither a settled headline nor discarded because of one framing comment. The
> team will decide its weight from the method and robustness evidence; current options and next
> actions live in the [project plan](../project-plan.md) and
> [17 July minutes](../meetings/2026-07-17.md).
>
> **21 Jul update:** notebook 08 ([`../../sandbox/jaime/08_activation_vs_reconfiguration.ipynb`](../../sandbox/jaime/08_activation_vs_reconfiguration.ipynb),
> peer-reviewed) supersedes pattern-vs-scalar as the headline. Reconfiguration does not clearly add
> over single-condition 0-back FC (nested delta-R2 +0.034, sd 0.023, under 2 sd); a task-activation
> contrast (2bk-0bk mean BOLD) predicts better (r ~ 0.60 pooled, ~0.48 held-out people and runs) and
> FC adds nothing over it (delta-R2 -0.003). The predictive signal is not specific to connectivity
> reconfiguration. Reconfiguration repeated-CV r ~ 0.366 still stands as a number; the 17 Jul
> analysis below is kept unchanged as the original context.

---

## Bottom line

- Our WM-prediction headline (out-of-sample, consistent with **Avery 2020, r=0.36**) is a **conceptual
  replication** (different model), not a discovery. Own it as such.
- The distinct contribution is a **pattern-vs-scalar dissociation**: the *multivariate* load
  reconfiguration pattern (2bk−0bk fingerprint) **predicts** (repeated-CV r≈0.37; leakage-free cross-run
  r≈0.28), but its *scalar* directional summaries — net between-network integration index (r≈0.04) and
  mean modularity change — **do not**. Difference-score unreliability explains why the scalar summaries
  fail while the pattern, and each single-condition trait fingerprint (r≈0.27), survive.
- Two manual-pass recommendations (**family-aware CV; age/sex confounds**) are **not implementable** on
  the Neuromatch-curated data and are dropped (declared as limitations).

---

## Canonical methods background (from the manual pass; not re-voted)

- **Calibration (general).** Marek 2022 (*Nature*): out-of-sample multivariate brain–behaviour
  effects shrink ~63% vs in-sample; report cross-validated, CI-bounded numbers, never in-sample. **[canonical]**
- **Task-evoked co-activation confound.** Cole 2019 (*NeuroImage*) and Masharipov 2024 (*Commun Biol*
  7:1402): blockwise task FC is inflated by the shared evoked response; FIR / block-mean removal is
  the fix, canonical-HRF regression is inadequate. For our long blocks, cheapest remedies are
  block-mean removal or discarding the first ~6 s per block — or declare the confound. **[canonical]**
- **d′ extreme-rate correction.** Hautus 1995: loglinear rule (add 0.5 to hits/FA, 1 to trial
  totals); implemented/validated in notebook §5 (loglinear ≈ 1/2N clip). **[canonical]**
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
  (rest FC r=0.20) — their 10-fold-CV CPM vs our 5-fold RidgeCV; **our headline is consistent with
  it** — a conceptual replication, not exact. **[verified]** <https://pmc.ncbi.nlm.nih.gov/articles/PMC8004893/>
- Other WM-specific out-of-sample benchmarks: out-of-scanner List-Sorting from N-back FC **r=0.24**
  (rest 0.10) **[verified]** <https://pmc.ncbi.nlm.nih.gov/articles/PMC8413720/>; dynamic-FC CPM WM
  capacity **r≈0.22** **[verified]** <https://pmc.ncbi.nlm.nih.gov/articles/PMC7930367/>; CPM 2-back
  performance up to **r=0.48** **[verified]** <https://pmc.ncbi.nlm.nih.gov/articles/PMC12439485/>.
  → The WM band is ~0.22–0.48; our value sits **inside** it, not "above typical" (corrects the manual
  pass, which calibrated against fluid-intelligence r≈0.38).
- Same-task prediction **is accepted** in the field (Avery; PMC12439485), **not** fatally circular —
  but same-context prediction is inflated vs cross-context (~2×: r=.58 intra → .27 cross in movie
  studies) **[verified]** <https://www.biorxiv.org/content/10.1101/2023.11.14.566767.full.pdf>.
- **Decision (applied):** calibration re-anchored to Avery 2020; same-context inflation declared as a
  limitation, with d′ (net of response bias) as a partial guard.

### Gap 2 — The reconfiguration null is about the scalar summary, not the pattern
- A reconfiguration **magnitude** score *can* predict cognition (Thiele 2022, *Cereb Cortex*: more
  reconfiguration ↔ lower intelligence, rho≈−0.23) — so "reconfiguration doesn't predict" is not a
  safe blanket headline. **[verified]** <https://academic.oup.com/cercor/article/32/19/4172/6523266>
- **Difference-score psychometrics**: a within-subject contrast can be robust yet have ~zero
  between-subject reliability, because subtraction removes the true-score variance shared across
  conditions (worked example: faces−shapes contrast reliability −0.06 while each condition map is
  0.95–0.97, because conditions correlate r=.97). **[verified]**
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC5912348/>
  → This bites the **scalar** summary of reconfiguration (integration index r≈0.04), where subtracting
  two correlated conditions leaves mostly error. It does **not** sink the **multivariate** pattern: a
  ridge over 78 network edges still predicts out-of-sample (leakage-free cross-run r≈0.28), tied with
  each single-condition trait fingerprint (r≈0.27).
- **Decision (applied):** frame the result as a pattern-vs-scalar dissociation — the multivariate
  reconfiguration pattern predicts; its one-number directional summaries do not, explained by
  difference-score reliability. Verified directly in notebook §3b (feature-wise test-retest ≈0.02 vs
  cross-run prediction ≈0.28).

### Gap 3 — Family-structure leakage without family IDs
- Family leakage is **the mildest** leakage type: Δr≈0.00–0.02 for cognition/reasoning in full
  datasets; ~0.04 worst case (twins-only). **[verified]** <https://www.nature.com/articles/s41467-024-46150-w>
- Rigorous HCP work controls it by permuting only within sibling types (Greene 2018) — which **needs
  kinship IDs the curated set does not expose.** **[verified]** <https://www.nature.com/articles/s41467-018-04920-3>
- **Decision (applied):** one limitation sentence citing the Rosenblatt bound (r≈0.35 → ≥~0.33
  corrected; story unchanged). Manual-pass A2 (family-aware CV) dropped — not implementable and barely
  matters.

### Gap 4 — d′ vs accuracy as the HCP-WM target
- The canonical FC→WM paper (Avery 2020) uses **raw 2-back accuracy**, not d′. The verified pass found
  no surviving evidence on HCP-WM d′ reliability (thin — treat with caution).
- **Decision (applied):** lead with **accuracy** (comparable to Avery 0.36); keep **d′ as the
  measurement-clean primary target** (separates sensitivity from response bias). Under the acc_0bk
  control, d′ and accuracy retain comparable partial signal (~0.24 vs ~0.22) — d′ is **not** more
  robust here. Note the ~16 target / ~64 non-target trial count as a d′ reliability caveat.

---

## Not implementable on the curated data (declared as limitations)

- **Age/sex confounds:** the curated set exposes only **synthetic** pseudo-demographics; the data doc
  says do not use them as confounds.
- **Family-aware / leave-families-out CV:** no kinship IDs exposed; also Δr≲0.02 per Rosenblatt 2024.

**Scope:** feature reduction is unnecessary (78 features / 336 subjects is fine for RidgeCV); the
dynamic-FC HMM is deferred (CAPs / k-means is the declared extension); multi-task / rest comparisons
need extra data.

---

## Refuted / discarded (did NOT survive verification — do not cite)

- "HCP WM-from-FC prediction is r≈0.08" — refuted 0-3.
- "Relating task-FC to task signal is circular unless mean evoked response is regressed" — refuted 0-3.
- "Greene 2018 acknowledges same-task FC predicts same-task behaviour better" — 1-2, not confirmed.

*(Two Gap-3 leakage claims were confirmed 2-0 with the safety classifier unavailable; treated as
reliable but flagged.)*
