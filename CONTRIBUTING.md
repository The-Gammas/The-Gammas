# Contributing — keep it simple

The repository should be usable even if Git is new to you. **GitHub Desktop** is the recommended
interface; command-line Git is equally welcome.

## Three places, three rules

| Place | What belongs there | Editing rule |
|---|---|---|
| `sandbox/<your-name>/` | Draft notebooks, scripts and notes | Edit only your own folder |
| `pipeline/` | Group-reviewed explanatory notebooks | Coordinate with the notebook owner or use a pull request |
| `data/` | Local HCP downloads | Never commit its contents |

Files shared by everyone — `README.md`, `docs/`, `pipeline/` and future common helpers — should be
changed by the agreed integrator or through a small pull request.

## Keeping status coherent

When work changes the project state:

1. Preserve the evidence in the relevant notebook or dated meeting note.
2. Update [`docs/project-plan.md`](docs/project-plan.md), the detailed living status.
3. Update the short table in [`README.md`](README.md).
4. Leave historical minutes, proposals and transcriptions intact; add a pointer to the living plan if
   their old status could now mislead a reader.

Record TA/reviewer comments as attributed feedback until the team evaluates them against the analysis.
Do not turn one person's preference into a method change or discarded finding without supporting
evidence and an explicit team decision.

Before reimplementing an existing stage, share the partial work and compare it with the linked
prototype. A sandbox result is not automatically the final pipeline, but it is also not invisible.

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

### 2. In shared areas (`pipeline/`, `docs/`, common helpers, or `README.md`)
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
3. Copy only the clear, reproducible story into `pipeline/`.
4. Preserve authorship and link back to the originating sandbox notebook.
5. Update the living project plan, then the status table in the main README.
