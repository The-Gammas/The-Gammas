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

Files shared by everyone — `README.md`, `docs/`, `pipeline/`, `gammas/` and `tests/` — should be
changed by the agreed integrator or through a small pull request.

**`docs/` or `manuscript/`?** If a teammate would read it to **know what happened**, it goes in `docs/`.
If they would reuse it to **write a paper**, it goes in `manuscript/`. Process and record on one side,
prose for external readers on the other.

**Why `gammas/` sits at the repo root and not in `src/`.** The `src/` layout is the standard advice for
installable packages, because it forces tests to run against the *installed* code. We never install this
repo: notebooks add the root to `sys.path` and import from there, which keeps Colab and GitHub Desktop
working with no `pip install -e .` step. Flat is the right call *for a research compendium*. If this ever
becomes a package someone installs, move it to `src/gammas/` then — not before.

## Tests — what deserves one

The suite runs in under a second and needs no project data. Keep it that way: it is only useful if
people actually run it before a pull request.

**Write a test when a bug would be silent.** The tests that exist protect exactly that: the
train-only tangent reference (a leak would raise every score), the subject-level split and its CV folds
(same), the 4 s HRF default (wrong value → r = 0.152 instead of 0.366, no error), and the statistics the
conclusions rest on. Each of those can fail while producing a perfectly plausible number.

**Don't write a test for:** anything that needs the 9 GB of HCP data — that is what the reproduction gate
in `pipeline/02` cell 10 is for; plotting; thin wrappers over NumPy or scikit-learn; or a function whose
failure mode is an obvious exception. We are not chasing a coverage number, and a suite nobody runs
protects nothing.

**Prefer a predictable outcome over a recorded one.** Assert against a value you can derive by hand
(`(0.8 − 0.2) / 0.8`), a mathematical property (held-out rows must not move a fitted reference), or a
clear separation (real association → p < 0.01, noise → p > 0.05). Snapshots of last run's output rot.

`make test` runs them. No pytest, no fixtures, no plugins — `unittest` from the standard library.

## Sandboxes

Each member has one folder for work that is still being explored. It is visible to the group but not
part of the shared pipeline, and it stays as the record of how an idea developed.

Some sandboxes contain working prototypes. **Before rebuilding a stage, check the originating sandbox
and the [final report](docs/final-report.md), then share partial work so the team can compare
implementations.** A sandbox result is not automatically the final pipeline, but it is also not
invisible.

- An **empty sandbox folder** means space was assigned and the work was delivered outside the
  repository (shared documents, slides, meetings) — not that nothing was contributed.
- A **README inside your folder is welcome, not required.** Add one when it helps a reader navigate
  more than a couple of files.

## Keeping the record coherent

The project closed at W3D5 (24 Jul 2026). [`docs/final-report.md`](docs/final-report.md) is the source
of truth for results and conclusions; [`docs/archive/`](docs/archive/) and
[`docs/meetings/`](docs/meetings/) are the frozen record of what was believed and decided at each date.

1. Put the evidence in a notebook first — a result that lives only in prose does not count.
2. If it changes a conclusion, update the final report in the same pull request.
3. Leave historical minutes, proposals and archived plans intact; add a pointer if their old status
   could now mislead a reader.

Record TA/reviewer comments as attributed feedback until the team evaluates them against the analysis.
Do not turn one person's preference into a method change or discarded finding without supporting
evidence and an explicit team decision.

## Everyday flow

1. **Pull** or sync the latest `main`.
2. Work in `sandbox/<your-name>/`.
3. Save with a descriptive filename.
4. **Commit** with a short message describing what changed.
5. **Push**.

If Git blocks you, share the Colab/Drive notebook with the group and ask an integrator to add it.
Contributing to the analysis matters more than mastering Git on day one.

## Branching strategy

To keep the `main` branch stable (and prevent our group chat from devolving into a support desk for tragic merge conflicts), we follow a simple branching model based on where you are working:

### 1. In your personal sandbox (`sandbox/<your-name>/`)
- **Direct pushes allowed:** Your sandbox is your sovereign territory. If you break it, you only make your own life miserable. Direct pushes to `main` are perfectly fine here.
- **Optional branches:** If you're planning a wild experiment or want to collaborate without Git-stepping on a teammate's toes, feel free to spin up a branch: `sandbox/<your-name>-<topic>`.

### 2. In shared areas (`pipeline/`, `gammas/`, `tests/`, `docs/`, or `README.md`)
- **No direct commits to `main`:** Committing directly to `main` in these folders is a crime punishable by buying the next round of virtual coffees. All shared changes must go through a Pull Request (PR).
- **Branch naming:** Keep it professional-ish. Avoid names like `temp`, `stuff`, or `please-work-v4`. Use descriptive, lowercase branch names:
  - `feature/<name>-<topic>` (e.g., `feature/jaime-ingestion`)
  - `fix/<name>-<topic>` (e.g., `fix/goutham-matrix-bug`)
  - `docs/<name>-<topic>` (e.g., `docs/arefeh-meeting-notes`)
- **Review & Merge:** 
  1. Push your branch and open a PR on GitHub.
  2. Bribe/request at least one teammate (ideally the stage lead) to review your code.
  3. Once approved, merge it (or ask an integrator to do the honors).

## Notebook conventions

- Begin with author, date, status and a concrete question.
- Pair short markdown explanations with small code cells.
- Record inputs, key shapes, checks, findings, limitations and the next hand-off.
- Personal notebooks may keep small useful outputs. Remove subject identifiers and large/noisy output.
- Group notebooks in `pipeline/` keep only outputs that help a reader understand the result.

## Promoting work into `pipeline/`

1. Explore freely in your sandbox.
2. Review the work with at least one teammate.
3. **Move** the notebook with `git mv` — do not copy it. Git history is the audit trail, and a copy
   leaves two versions that drift apart.
4. Clean it up in place: fix the paths it inherited from the sandbox, run it top to bottom, and drop
   outputs that do not help a reader.
5. Preserve authorship, and update [`pipeline/README.md`](pipeline/README.md) and the final report if
   the promotion changes what the canonical evidence path is.
