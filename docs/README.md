# docs — project documentation

Process and decision artifacts for The Gammas. The scientific write-up and its bibliography live in
[`../manuscript/`](../manuscript/); exploratory notebooks in [`../sandbox/`](../sandbox/); reviewed
pipeline notebooks in [`../pipeline/`](../pipeline/).

| Path | What goes here |
|---|---|
| [`project-plan.md`](project-plan.md) | The living plan: question, methods, accepted decisions, open items. Update when the team accepts a decision. |
| [`data-dictionary.md`](data-dictionary.md) | Data reference: files, variables, the shared A/B loader layer. |
| [`meetings/`](meetings/) | Dated meeting minutes, `YYYY-MM-DD.md`. |
| [`reviews/`](reviews/) | Dated literature reviews / research syntheses, `YYYY-MM-DD_topic.md`. Analyses that use the literature to inform decisions — distinct from the citation list, which lives in [`../manuscript/references.md`](../manuscript/references.md). |

## Status hierarchy

1. [`../README.md`](../README.md) gives the short current snapshot.
2. [`project-plan.md`](project-plan.md) is the canonical detailed status.
3. The latest file in [`meetings/`](meetings/) records the evidence and discussion behind changes.
4. Dated reviews and proposals preserve their original analytical context; they do not override the
   living plan.

When a decision changes, update the dated evidence first, then the project plan, then the root README.
Do not rewrite an old meeting note to make it look current.

**Where does a new document go?**

- Meeting minutes → `meetings/`
- A literature review or research synthesis → `reviews/`
- A new citation → [`../manuscript/references.md`](../manuscript/references.md)
- A decision the team accepted → `project-plan.md`
- A quick status-table change → `project-plan.md` first, then `../README.md`
