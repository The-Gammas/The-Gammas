# AGENTS.md

Working contract for any coding agent (Claude Code, Codex, Cursor, Copilot, Gemini, …) in **The
Gammas** repo. Tool-agnostic, following the open [AGENTS.md](https://agents.md) format. Kept short on
purpose: it holds the **rules** and links out for everything else — it does not duplicate the other
docs. Change a rule here in the same PR that changes the behaviour.

## Orient yourself first (read, don't duplicate)

- [README.md](README.md) — the quick current-state snapshot, **setup & commands**, repo layout, key links.
- [docs/project-plan.md](docs/project-plan.md) — the detailed living plan: current method, evidence,
  open decisions and milestones.
- [CONTRIBUTING.md](CONTRIBUTING.md) — where files go, notebook conventions, the everyday Git flow.
- The newest file in [docs/meetings/](docs/meetings/) — why the current state changed and what the
  team still needs to decide.
- [manuscript/references.md](manuscript/references.md) — the claim-level scientific source record.

### Current-state contract

- `README.md` is the short snapshot; `docs/project-plan.md` is the canonical detailed status.
- Record a new decision in its dated meeting note first, reconcile `docs/project-plan.md`, then update
  the short README table. Do not use proposals, literature reviews or old minutes as a current task
  tracker.
- Dated records preserve what was known at that time. Add a status pointer when they are superseded;
  do not silently rewrite their historical content.
- Keep external feedback distinct from team decisions. A TA/reviewer comment is attributed evidence
  for discussion, not a veto; experiments, robustness checks and an explicit team decision determine
  whether a method or finding stays in scope.
- Before coordinating work, check `git status`, the current README table, the living plan and the
  latest meeting note. If they disagree, stop duplication and reconcile those sources first.

The data (NMA-curated HCP N-back, 360 ROIs) is **not in Git**: it lives under `data/` (gitignored). How to
**download, place and load** it → [`data/README.md`](data/README.md). The shared **A/B data layer** is
`sandbox/jaime/datasets.py` (I/O) → `preprocessing.py` (transforms) → `evaluation.py` (split/QC).
Import it **read-only** from any sandbox — the one exception to "work only in your own folder": use
it, don't edit it without the owner or a PR. The current roles of cohorts A and B live in the project
plan; do not infer them from an older notebook's "finalist" language.

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
