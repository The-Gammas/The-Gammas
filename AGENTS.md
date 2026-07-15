# AGENTS.md

Working contract for any coding agent (Claude Code, Codex, Cursor, Copilot, Gemini, …) in **The
Gammas** repo. Tool-agnostic, following the open [AGENTS.md](https://agents.md) format. Kept short on
purpose: it holds the **rules** and links out for everything else — it does not duplicate the other
docs. Change a rule here in the same PR that changes the behaviour.

## Orient yourself first (read, don't duplicate)

- [README.md](README.md) — what the project is, **setup & commands**, repo layout, key links.
- [docs/project-plan.md](docs/project-plan.md) — the living plan, the dataset, and **how to obtain it**.
- [CONTRIBUTING.md](CONTRIBUTING.md) — where files go, notebook conventions, the everyday Git flow.
- [docs/meetings/](docs/meetings/) · [manuscript/references.md](manuscript/references.md) — decisions and sources.

The data (NMA-curated HCP N-back, 360 ROIs) is **not in Git**: it lives under `data/` (gitignored). How to
**download, place and load** it → [`data/README.md`](data/README.md). The shared **A/B data layer**
(`sandbox/jaime/datasets.py` ← `preprocessing.py` ← `evaluation.py`) is imported **read-only** from any sandbox —
the one exception to "work only in your own folder": use it, don't edit it without the owner or a PR.

## Rules for agents

**Do**
- Work only inside your own `sandbox/<name>/`; keep `main` stable — anything shared goes via a branch + PR.
- Cite the source of any claim (meeting notes, the shared Doc, a paper in `manuscript/references.md`).
- Notebooks: embed figures inside the `.ipynb`; explain the reasoning, not only the code.

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
