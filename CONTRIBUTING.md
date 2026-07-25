# Contributing — keep it simple

The repository should be usable even if Git is new to you. **GitHub Desktop** is the recommended
interface; command-line Git is equally welcome.

## Where things go

| Place | What belongs there | Editing rule |
|---|---|---|
| `sandbox/<your-name>/` | Draft notebooks, scripts and notes | Edit only your own folder |
| `pipeline/` | Group-reviewed explanatory notebooks | Coordinate with the notebook owner or use a pull request |
| `gammas/` | The shared A/B data layer, imported by every notebook | Pull request, and `python -m unittest discover -s tests` must pass |
| `tests/` | Unit tests for `gammas/`, no data required | Pull request; add a test with the behaviour it protects |
| `data/` | Local HCP downloads | Never commit its contents |

`gammas/` sits at the repo root rather than in `src/` because we never install this repo: notebooks add
the root to `sys.path` and import from there, which keeps Colab and GitHub Desktop working with no
`pip install -e .` step. If it ever becomes an installed package, move it to `src/gammas/` then.

## The Git flow — two zones

1. **Pull** or sync the latest `main`, then work in `sandbox/<your-name>/`, saving with descriptive
   filenames.
2. **Inside your own sandbox, commit and push straight to `main`.** Short message describing what
   changed. If you break your own folder, nobody else is affected. Optional branch
   (`sandbox/<your-name>-<topic>`) for a wild experiment or shared exploration.
3. **In shared areas — `pipeline/`, `gammas/`, `tests/`, `docs/`, `README.md` — never commit directly to
   `main`.** Branch with a descriptive lowercase name (`refactor/jaime-repo-structure`), push it, open a
   pull request, and get one teammate to review before merging.

If Git blocks you, share the Colab/Drive notebook with the group and ask the repo owner to add it.
Contributing to the analysis matters more than mastering Git on day one.

## Tests — what deserves one

The suite runs in under a second, needs no project data, and uses `unittest` from the standard library —
no pytest, no fixtures, no plugins. `make test` runs it.

**Write a test when a bug would be silent.** That is what the existing ones protect: the train-only
tangent reference and the subject-level split with its CV folds (a leak would raise every score), the
4 s HRF default (wrong value → r = 0.152 instead of 0.366, no error), and the statistics the conclusions
rest on. **Don't** write one for anything needing the 9 GB of HCP data — that is what the reproduction
gate in `pipeline/02` cell 10 is for — nor for plotting, thin wrappers over NumPy or scikit-learn, or a
function whose failure mode is an obvious exception.

**Prefer a predictable outcome over a recorded one:** a value you can derive by hand
(`(0.8 − 0.2) / 0.8`), a mathematical property (held-out rows must not move a fitted reference), or a
clear separation (real association → p < 0.01, noise → p > 0.05). Snapshots of last run's output rot.

## Sandboxes

Each member has one folder for work that is still being explored: visible to the group, not part of the
shared pipeline, kept as the record of how an idea developed. Some hold working prototypes — check the
originating sandbox and the [final report](docs/final-report.md) before rebuilding a stage.

- An **empty sandbox folder** means space was assigned and the work was delivered outside the
  repository (shared documents, slides, meetings) — not that nothing was contributed.
- A **README inside your folder is welcome, not required.** Add one when it helps a reader navigate
  more than a couple of files.

## Keeping the record coherent

[`docs/final-report.md`](docs/final-report.md) is the source of truth for results and conclusions;
[`docs/archive/`](docs/archive/) and [`docs/meetings/`](docs/meetings/) are the frozen record of what was
believed and decided at each date.

1. Put the evidence in a notebook first — a result that lives only in prose does not count.
2. If it changes a conclusion, update the final report in the same pull request.
3. Leave historical minutes, proposals and archived plans intact; add a pointer if their old status
   could now mislead a reader.
4. Record TA/reviewer comments as attributed feedback until the team evaluates them against the
   analysis. One person's preference is not a method change without evidence and an explicit team
   decision.

## Notebook conventions

- Begin with author, date, status and a concrete question.
- Pair short markdown explanations with small code cells.
- Record inputs, key shapes, checks, findings, limitations and the next hand-off.
- Keep only outputs that help a reader understand the result, and never a subject identifier.

## Promoting work into `pipeline/`

1. Explore freely in your sandbox, then review the work with at least one teammate.
2. **Move** the notebook with `git mv` — do not copy it. Git history is the audit trail, and a copy
   leaves two versions that drift apart.
3. Clean it up in place: fix the paths it inherited from the sandbox, run it top to bottom, and drop
   outputs that do not help a reader.
4. Preserve authorship, and update [`pipeline/README.md`](pipeline/README.md) and the final report if
   the promotion changes what the canonical evidence path is.
