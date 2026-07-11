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

## Everyday flow

1. **Pull** or sync the latest `main`.
2. Work in `sandbox/<your-name>/`.
3. Save with a descriptive filename.
4. **Commit** with a short message describing what changed.
5. **Push**.

If Git blocks you, share the Colab/Drive notebook with the group and ask an integrator to add it.
Contributing to the analysis matters more than mastering Git on day one.

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
5. Update the status table in the main README.

