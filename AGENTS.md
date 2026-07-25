# AGENTS.md

Working contract for any coding agent in **The Gammas** repo — a finished, reproducible record of an
NMA CompNeuro 2026 pod project (HCP N-back, closed 24 Jul 2026), not a live plan.

[`docs/final-report.md`](docs/final-report.md) is the source of truth for every result and conclusion.
Where files go, what deserves a test, notebook conventions and the Git flow are in
[CONTRIBUTING.md](CONTRIBUTING.md) — read it, this file does not repeat it. What it does not cover:

- **Never edit another person's `sandbox/<name>/`.** Shared areas (`gammas/`, `tests/`, `pipeline/`,
  `docs/`, `README.md`) change through a branch + PR, never a direct commit to `main`.
- **Never commit data, subject-level files, real subject IDs, or notebook outputs containing them.**
- **Never `git push --force` or rewrite `main` history** without the repo owner's explicit go-ahead.
- **Cite the source of any claim** (a meeting minute, a notebook cell, a paper in
  [`manuscript/references.md`](manuscript/references.md)) — do not assert a number from memory.
- The roles of cohorts A and B (B primary, A the identity-disjoint transfer target) are fixed in
  [`docs/data-dictionary.md`](docs/data-dictionary.md); do not infer them from older "finalist" language.

**Ask before:** installing packages, `git push`, opening or merging PRs, deleting or moving shared
files. Reading files, running notebooks locally and `git status` / `git diff` need no permission.

Personal preferences go in a gitignored `AGENTS.local.md`, not in this shared file.
