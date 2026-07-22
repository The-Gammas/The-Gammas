# The Gammas — evidence-first chart system

## Purpose

The repository stores only charts that encode project data, statistical methods or empirical
results. Titles, hypotheses, cohort descriptions, conclusions, future work and references are
specified in the storyboards but will be composed later with native presentation elements.

Both decks reuse the same chart library:

```text
pipeline/02 canonical cells
        ↓ execute in Pixi
identifier-free temporary chart bundle
        ↓ validate numerical invariants
9 empirical PNG/SVG charts
        ↓
manifest + automated file QA + one contact sheet
        ↙                         ↘
internal-review storyboard       final 5+4 storyboard
```

There is no image-per-slide requirement and no duplicated final-deck asset set.

## Evidence boundary

`pipeline/02_canonical_analysis_and_slides.ipynb` is the only numerical source. The generator stops
before publication unless it reproduces the registered sample sizes, feature counts, prediction,
transfer, segregation, model-comparison and incremental metrics. No participant IDs, tables or
intermediate participant-level arrays are stored in Git.

## Chart library

| Chart | Question answered | Boundary |
|---|---|---|
| `condition-fc-contrast` | What signed FC contrast enters the predictor? | Condition-aggregated FC, not dynamic or causal connectivity. |
| `feature-construction` | How do 360 regions become 78 FC differences? | Task FC may include task-evoked coactivation. |
| `primary-repeated-cv` | Is prediction stable across participant partitions? | Split SD is not a confidence interval. |
| `null-and-holdout` | What do the seed-42 null and fixed holdout show? | Two different estimands; the p belongs only to seed-42. |
| `identity-disjoint-transfer` | Does the B-trained model transfer to A identities? | Same-HCP, not independent-site; kinship unmodelled. |
| `segregation-refinement` | Does the group direction explain individual performance? | A paired mean shift is not an individual mechanism. |
| `anatomical-context` | Where did mean FC change? | Descriptive mean change, not predictive importance. |
| `incremental-fc-test` | Does reconfiguration add beyond 0-back FC? | The 2-SD rule is a split-sensitive heuristic. |
| `activation-robustness` | Is predictive information specific to FC? | Post hoc unmatched 360-versus-78 feature comparison. |

## Visual language

All charts use Poppins, a white background, restrained grids, direct labels and the same 16:9
2560×1440 canvas. Color has a stable semantic role and is never the only distinction.

| Role | Color | Use |
|---|---|---|
| Ink | `#202729` | Text, axes and reference lines. |
| Pale sand | `#EAD6B8` | Open fills and quiet context. |
| Taupe | `#B99470` | Secondary condition or distribution. |
| Brown | `#705C40` | Keylines and methodological emphasis. |
| FC blue | `#0072B2` | FC and FC-based predictions. |
| Activation orange | `#D55E00` | Activation only when compared with FC. |
| Neutral grey | `#B8B8B8` | Null distributions and background references. |

Scales for signed FC changes remain symmetric around zero. The charts avoid 3D, shadows, decorative
gradients, ranking metaphors and red/green winner semantics.

## Storyboard use

- The internal-review storyboard can use all nine charts because its job is scientific inspection.
- The final five-content-slide flow uses only `feature-construction`, `primary-repeated-cv`,
  `identity-disjoint-transfer`, `segregation-refinement` and `activation-robustness` in the timed
  talk. `null-and-holdout` remains optional backup if layout space allows.
- Slides without a named chart are deliberately text/layout slides. A presentation generator must
  not invent an image merely to fill space.

## QA

Each delivery requires:

1. canonical invariant checks;
2. nine valid 2560×1440 PNGs and nine parseable SVGs under 50 MB;
3. matching hashes in `manifest.json`;
4. full-resolution inspection of each PNG;
5. contact-sheet review for palette and narrative coherence;
6. visual-contract tests, existing project tests and `git diff --check`.

The branch remains local until owner approval; no commit or push is part of this iteration.
