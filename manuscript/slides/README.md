# Slides

Presentation storyboards and frozen source material for the NMA W3D5 project presentation.

## Current working files

- [`final-storyboard-5-plus-4.md`](final-storyboard-5-plus-4.md) — **the deck we present.** Five
  spoken slides (intro · method · primary result · the turn · conclusion) plus four backup slides
  opened only in Q&A. Structure benchmarked against the 2025 NMA example decks in
  [`../../../references/nma_project_examples_2025/`](../../../references/nma_project_examples_2025/).
- [`internal-review-storyboard.md`](internal-review-storyboard.md) — detailed scientific narrative for
  internal review, capped at 15 slides. Long-form reference; it is not the presented deck.
- [`visuals/charts/`](visuals/charts/) — one reusable library of nine empirical charts. Both
  storyboards reference these same assets; slides that need only text or layout have no generated
  image.
- [`source-snapshots/`](source-snapshots/) — dated, immutable local exports of shared presentation
  sources used as visual references.
- [`restructure_deck_5plus4.py`](restructure_deck_5plus4.py) — the one-shot migration that moved the
  draft deck from the earlier 9-slide layout to the current 5 spoken + 4 backup architecture. Kept
  for provenance; it is not idempotent and must not be re-run against the current deck.

## Evidence and status

The scientific source of truth is
[`../../pipeline/02_canonical_analysis_and_slides.ipynb`](../../pipeline/02_canonical_analysis_and_slides.ipynb).
Source notebooks remain provenance only. The submitted abstract is a historical record and must not
override the canonical notebook when a result or interpretation differs.

Audience-facing slide copy is written in English. Spanish text in the storyboards is production
guidance, speaker logic or scientific review context and is not intended to appear on screen.

The final deck respects NMA's approximately five-minute format and one-slide-per-person rule
directly: **Slides 1–5 are the five spoken slots, one per presenter; Slides 6–9 are never allocated
speaking time.** With six presenters, split Slide 4 across two people rather than promoting a backup
slide.

Two narrative rules bind every speaker text:

- We pre-specified **two** hypotheses; the evidence **confirmed one and refined the other**. Never
  say the hypothesis evolved, changed or was replaced.
- The conclusion names both opening hypotheses out loud, so the talk closes the loop it opened.

## Frozen visual source

The current snapshot of Valeria's Google Slides draft is stored at
[`source-snapshots/2026-07-22T19-06-12_CEST_valeria/`](source-snapshots/2026-07-22T19-06-12_CEST_valeria/).
It is a visual/template reference only. Placeholder biographies, unfinished text and older figures
inside that deck are not project evidence.

- Source modified: **2026-07-22 17:24:40 CEST**; downloaded: **2026-07-22 19:06:12 CEST**.
- Frozen exports: [PDF](source-snapshots/2026-07-22T19-06-12_CEST_valeria/the-gammas-nma-project.pdf)
  · [PPTX](source-snapshots/2026-07-22T19-06-12_CEST_valeria/the-gammas-nma-project.pptx)
  · [provenance and SHA-256](source-snapshots/2026-07-22T19-06-12_CEST_valeria/snapshot-metadata.json).
