# docs — process, decisions and data reference

What was done, why, and on what evidence. The scientific write-up and its bibliography live in
[`../manuscript/`](../manuscript/); reviewed analysis notebooks in [`../pipeline/`](../pipeline/);
per-person exploration in [`../sandbox/`](../sandbox/).

**Boundary rule between the two prose folders:** *if a teammate would read it to KNOW what happened,
it goes in `docs/`; if they would reuse it to WRITE a paper, it goes in `manuscript/`.*

## Contents

| Path | What it is |
|---|---|
| [`final-report.md`](final-report.md) | **Source of truth.** Question, data, method, results, limitations, reproduction, repository map, decision timeline, authorship. Its §5 is the canonical results table: a number quoted anywhere else without a protocol, an `n` and a source cell is superseded by it. |
| [`data-dictionary.md`](data-dictionary.md) | Files, variables, cohort roles and the shared A/B loader layer. Sole authority on anything about the data. |
| [`meetings/`](meetings/) | Six dated minutes, `YYYY-MM-DD.md`. Provenance of every team decision; one-row-per-meeting index in [`final-report.md`](final-report.md) §11. |
| [`reviews/`](reviews/) | Dated literature syntheses, `YYYY-MM-DD_topic.md`, including a *do-not-cite* list of refuted figures. Why this method and not another. Distinct from the citation list, which lives in [`../manuscript/references.md`](../manuscript/references.md). |
| [`archive/`](archive/) | Frozen record: documents that stopped being current on a known date, kept under that date. |

## Status

The project closed at W3D5, **24 Jul 2026**. [`final-report.md`](final-report.md) states the current
position; `archive/` and `meetings/` record what was believed when. There is no living plan in this
folder any more — anything dated before 24 Jul is history, not status.

## The frozen record: `archive/`

Archived documents are moved, dated and banner-marked, never condensed or rewritten: they are the
decision trail, and editing them would destroy the only evidence of what was believed at the time.
Their bodies keep the internal links they had before archiving, which point at pre-archive paths and
are not maintained.

| File | Frozen at | Kept because |
|---|---|---|
| [`2026-07-22_project-plan.md`](archive/2026-07-22_project-plan.md) | 22 Jul 2026 | The living plan that ran the project until the W3D5 scope freeze at `pipeline/02`. It carries the reasoning behind the cohort choice, the dataset-A pilot and every open item as it stood. |
| [`2026-07-10_goutham-poc.md`](archive/2026-07-10_goutham-poc.md) | 10 Jul 2026 | Goutham Arcod's Triple-Network proof-of-concept, the origin of the method the project ended up testing. Kept unaltered, including its attribution. |

Pre-submission manuscript material is archived separately in
[`../manuscript/archive/`](../manuscript/archive/).

## Where does a new document go?

- Meeting minutes → `meetings/`
- A literature review or research synthesis → `reviews/`
- A new citation → [`../manuscript/references.md`](../manuscript/references.md)
- A correction to a result → [`final-report.md`](final-report.md); the superseded text is archived
  under its date, never rewritten in place
- Anything a reader would reuse to write a paper → [`../manuscript/`](../manuscript/)
