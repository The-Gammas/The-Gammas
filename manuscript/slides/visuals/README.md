# Empirical chart library

Nine static, evidence-first charts reused by both The Gammas storyboards. This directory contains
only visual evidence derived from project data or statistical results; conceptual diagrams and
slide-layout compositions belong to the later presentation-authoring stage.

## Contract

- `pipeline/02_canonical_analysis_and_slides.ipynb` is the sole numerical source of truth.
- `charts/` contains nine 2560×1440 PNGs and nine matching SVGs.
- `manifest.json` records provenance, visible metrics, limitations, hashes and QA for each chart.
- `qa/charts-contact-sheet.png` supports library-wide coherence review.
- No participant IDs or participant-level numerical tables are written here.

The approved palette and chart roles are documented in
[`../visual-system-design.md`](../visual-system-design.md). Both storyboards link directly to the
same chart paths; there is no duplicated final-deck image set.

## Charts

| Asset | Presentation role |
|---|---|
| `condition-fc-contrast` | Define the signed 2-back minus 0-back FC contrast. |
| `feature-construction` | Show 360 regions → 12 networks → 78 FC features. |
| `primary-repeated-cv` | Show stability across 20 participant-level partitions. |
| `null-and-holdout` | Keep the seed-42 full-refit null distinct from the fixed holdout. |
| `identity-disjoint-transfer` | Show B-only training transferred to all A identities. |
| `segregation-refinement` | Contrast the group mean change with the weak individual link. |
| `anatomical-context` | Describe where mean FC changed, not model importance. |
| `incremental-fc-test` | Test value beyond 0-back FC on matched folds. |
| `activation-robustness` | Compare the unmatched activation and FC representations. |

## Generation

Run from the NeuroAcademy repository root. The authoritative release route re-executes the canonical
notebook cells and ignores the temporary identifier-free chart cache:

```bash
MPLCONFIGDIR=/private/tmp/gammas-mpl-cache \
pixi run python \
  project/fmri/the-gammas/manuscript/slides/visuals/src/generate_visuals.py \
  --force-evidence
```

For renderer-only iteration, omit `--force-evidence`. The generator may then reuse
`/private/tmp/gammas-slide-visual-bundle-v1.pkl` only when its notebook SHA-256 still matches.

Rendering is transactional: canonical invariants, PNG dimensions, SVG parsing, file size and hashes
must pass in staging before delivered files are replaced.

## Scientific reading rules

- Repeated-CV values are mean ± split SD, not confidence intervals.
- B→A is identity-disjoint transfer within HCP, not independent-site validation; kinship is not
  modelled.
- Activation is a post hoc unmatched benchmark: 360 regional features versus 78 network FC
  features. It cannot establish biological superiority.
- Group-mean segregation change and individual predictive association answer different questions.
- The figures support prediction and claim refinement, not causality, dynamic FC or adaptive
  benefit.

## Verification

```bash
MPLCONFIGDIR=/private/tmp/gammas-mpl-cache \
pixi run python -m unittest \
  project/fmri/the-gammas/manuscript/slides/visuals/tests/test_visual_contracts.py -v
```

After generation, inspect every PNG at original resolution and then inspect
`qa/charts-contact-sheet.png`. Automated file QA is recorded in `qa/qa-report.json`; manual visual
review is deliberately not claimed automatically.
