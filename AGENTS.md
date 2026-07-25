# AGENTS.md

Working contract for any coding agent (Claude Code, Codex, Cursor, Copilot, Gemini, …) in **The
Gammas** repo. Tool-agnostic, following the open [AGENTS.md](https://agents.md) format. Kept short on
purpose: it holds the **rules** and links out for everything else — it does not duplicate the other
docs. Change a rule here in the same PR that changes the behaviour.

**The project closed at W3D5, 24 July 2026.** What remains is a finished, reproducible record, not a
live plan.

## Orient yourself first (read, don't duplicate)

- [docs/final-report.md](docs/final-report.md) — **the source of truth**: question, data, method, the
  canonical results table, limitations, repository map and open threads.
- [README.md](README.md) — the front door: headline result, the deliverable, **setup & commands**, repo layout.
- [CONTRIBUTING.md](CONTRIBUTING.md) — where files go, notebook conventions, the everyday Git flow.
- [manuscript/references.md](manuscript/references.md) — the claim-level scientific source record.

### Current-state contract

- [`docs/final-report.md`](docs/final-report.md) is the single source of truth for results and
  conclusions. A number quoted anywhere else without a protocol, an `n` and a source cell is
  superseded by it; `pipeline/02_canonical_analysis_and_slides.ipynb` is where every number is computed.
- [`docs/archive/`](docs/archive/) and [`docs/meetings/`](docs/meetings/) are the **frozen record**: what
  was believed and decided at a given date. Read them for provenance, never as a current task tracker,
  and never rewrite their historical content — add a pointer instead.
- New work that changes a conclusion updates the final report in the same PR, with the evidence in a
  notebook. Do not leave a result living only in prose.
- Keep external feedback distinct from team decisions. A TA/reviewer comment is attributed evidence
  for discussion, not a veto; experiments, robustness checks and an explicit team decision determine
  whether a method or finding stays in scope.
- Before coordinating work, check `git status` and the final report. If a document disagrees with it,
  the final report wins — reconcile rather than duplicate.

The data (NMA-curated HCP N-back, 360 ROIs) is **not in Git**: it lives under `data/` (gitignored). How to
**download, place and load** it → [`data/README.md`](data/README.md). The shared **A/B data layer** is the
`gammas/` package at the repo root: `datasets.py` (config + I/O) → `preprocessing.py` (condition
segmentation, behaviour) → `connectivity.py` (FC representations) → `evaluation.py` (splits, CV,
permutation nulls). It is shared code, not anyone's sandbox: import it from anywhere, change it only
through a branch + PR, and run `python -m unittest discover -s tests` after touching it. The roles of
cohorts A and B (B primary, A the identity-disjoint transfer target) are fixed in
[`docs/data-dictionary.md`](docs/data-dictionary.md); do not infer them from an older notebook's
"finalist" language.

## Rules for agents

**Do**
- Work only inside your own `sandbox/<name>/`; keep `main` stable — anything shared goes via a branch + PR.
- Cite the source of any claim (meeting notes, the shared Doc, a paper in `manuscript/references.md`).
- Notebooks: embed figures inside the `.ipynb`; explain the reasoning, not only the code.
- Share partial work before starting a stage that already has a prototype; comparison and review are
  preferable to two silent implementations of the same baseline.

**Don't**
- Don't edit another person's `sandbox/<name>/`, `pipeline/`, or shared docs without a PR / the owner.
- Don't commit data, subject-level files, real subject IDs, or notebook outputs containing them.
- Don't `git push --force` or rewrite `main` history without the repo owner's explicit go-ahead.

**Ask before:** installing packages, `git push`, opening/merging PRs, deleting or moving shared files.
Reading files, running notebooks locally, and `git status` / `git diff` need no permission.

> CI runs a hygiene check on push/PR (blocks committed data or oversized files, validates notebooks) —
> see [`.github/workflows/ci.yml`](.github/workflows/ci.yml).

## Make it your own

Don't edit this shared file for personal preferences. Add a **nearest-file override** instead: an
`AGENTS.md` inside your own `sandbox/<name>/` (the closest file wins — [spec](https://agents.md)), or a
private, gitignored `AGENTS.local.md`. Agents that look for their own filename (`CLAUDE.md`,
`GEMINI.md`, …) can hold a single line: `See AGENTS.md`.
