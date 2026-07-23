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
- [`the-gammas-w3d5-optimized.pptx`](the-gammas-w3d5-optimized.pptx) — **our proposed deck**, 12
  slides. Built from the current snapshot so it inherits Valeria's theme, layouts, footer and logo
  exactly; every change in it is specified in the final storyboard. Review it, then either replace
  the Google deck or paste slide by slide.
- [`source-snapshots/`](source-snapshots/) — dated, immutable local exports of the shared team deck.
  One folder at a time: the current state, replaced whenever a fresh export is taken.

## Evidence and status

The scientific source of truth is
[`../../pipeline/02_canonical_analysis_and_slides.ipynb`](../../pipeline/02_canonical_analysis_and_slides.ipynb).
Source notebooks remain provenance only. The submitted abstract is a historical record and must not
override the canonical notebook when a result or interpretation differs.

Audience-facing slide copy is written in English. Spanish text in the storyboards is production
guidance, speaker logic or scientific review context and is not intended to appear on screen.

The final deck respects NMA's approximately five-minute format and one-slide-per-person rule
directly: **storyboard Slides 3–7 are the five spoken slots, one per presenter; 1–2 (cover, team) and
8–11 (backup) are never allocated speaking time.** With six presenters, split Slide 6 across two
people rather than promoting a backup slide.

Two narrative rules bind every speaker text:

- We pre-specified **two** hypotheses; the evidence **confirmed one and refined the other**. Never
  say the hypothesis evolved, changed or was replaced.
- The conclusion names both opening hypotheses out loud, so the talk closes the loop it opened.

## Frozen source and format reference

The live deliverable is the team Google deck
([`1A-FC-Hs2…Dk9E`](https://docs.google.com/presentation/d/1A-FC-Hs29PhzQ4ZID4hKFMMbXgLh2YIlnMQiUirDk9E/edit)),
owned by Valeria Moraga. The storyboards are its **spec**; the snapshot is its **frozen state**.

Current snapshot: [`source-snapshots/2026-07-23T17-42-40_CEST_valeria/`](source-snapshots/2026-07-23T17-42-40_CEST_valeria/)
— 19 slides, source modified **2026-07-23 17:05:07 CEST**, downloaded **17:42:40 CEST**.

- Frozen exports: [PDF](source-snapshots/2026-07-23T17-42-40_CEST_valeria/the-gammas-nma-project.pdf)
  · [PPTX](source-snapshots/2026-07-23T17-42-40_CEST_valeria/the-gammas-nma-project.pptx)
  · [provenance, SHA-256 and the measured format contract](source-snapshots/2026-07-23T17-42-40_CEST_valeria/snapshot-metadata.json).
- The `format_contract` block in that metadata records the deck's visual grammar — footer band,
  title and column geometry, type sizes, palette — measured from the PPTX. **Any slide we add must
  follow it**, so edits paste into Valeria's deck without restyling.
- Placeholder biographies, unfinished text and older figures inside the snapshot are not project
  evidence, and it is not a corrected deck: it preserves the defects listed in its `warning` field.
- A snapshot of a shared Google file is only frozen as of the minute it was pulled. Re-export and
  diff before trusting it; on 23 Jul the source moved five times in one afternoon.

## Rendering a deck locally

LibreOffice cannot do it on this machine — it is the Mac App Store build, so it is sandboxed and
`soffice --headless` always dies with *“User installation could not be completed”*, whatever
`-env:UserInstallation` path it is given. Use PowerPoint through AppleScript instead:

```bash
osascript -e 'tell application "Microsoft PowerPoint"
  open POSIX file "/abs/path/deck.pptx"
  delay 3
  save active presentation in POSIX file "/abs/path/deck.pdf" as save as PDF
  close active presentation saving no
end tell'
pdftoppm -png -r 110 /abs/path/deck.pdf /abs/path/out/s
```

This is the only way to see a deck before sharing it, and it is worth the detour: the first build of
the optimized deck looked correct by every geometric check and still overflowed two cards on the
method slide. Nothing measures rendered text — only rendering does.
