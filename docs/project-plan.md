# Living project plan

**Last reviewed:** 14 July 2026  
**Stage:** Week 2 — question refinement; hypothesis and dataset choice still open

This is a working plan, not a claim that every stage has been implemented. NMA projects are
iterative: the question, methods and division of work may change as the group learns from the data.

## Working question

> Does functional connectivity reconfigure between low and high working-memory load
> (0-back → 2-back), and can that reconfiguration predict individual working-memory performance?

The Project TA's north star is prediction on unseen subjects. Functional connectivity and graph
metrics are candidate features, not the final goal. The hypothesis should remain falsifiable.

## Dataset

NMA-curated HCP task-fMRI subset: 360 Glasser cortical regions, two WM runs (LR/RL), eight WM conditions
(0-back / 2-back × four stimulus categories). **Which subset is not yet decided** — two finalists:

- **Finalist A** — `load_hcp_task_with_behaviour`: 100 subjects, task + per-subject behaviour (`Stats.txt`).
- **Finalist B** — `load_hcp`: 339 subjects, task + resting-state + consolidated behaviour (`wm.csv`).

Comparison and trade-offs: [`sandbox/jaime/00`](../sandbox/jaime/00_framing_and_dataset_choice.ipynb) and
[`docs/data-dictionary.md`](data-dictionary.md). Official loader:
[HCP task with behaviour](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/fMRI/load_hcp_task_with_behaviour.ipynb).

## Working stages

| Stage | Purpose | Lead(s) | Status |
|---|---|---|---|
| 1. Ingestion + EV segmentation | Understand the files and separate low/high load frames | Jaime | In progress in `sandbox/jaime/` |
| 2. Functional connectivity | Estimate FC for each load condition | Valeria + Arefeh | Planned |
| 3. Graph construction | Represent FC as weighted, undirected graphs | Goutham | Planned |
| 4. Graph metrics | Explore segregation and integration | Kerem + Arefeh | Planned |
| 5. Prediction / testing | Predict WM performance in unseen subjects | Valeria + Arefeh | Planned |

## Confirmed direction

- Require a dataset with behaviour (both finalists have it); behaviour is the prediction target.
- Compare low and high working-memory load (0-back vs 2-back).
- Use functional rather than directed/effective connectivity.
- Treat graphs as weighted and undirected unless later evidence changes the choice.
- Keep prediction on held-out subjects as the main evaluation principle.
- Do not chase additional datasets during the short course timeline.

## Open now

- **Dataset: Finalist A (100) vs Finalist B (339, + resting-state)** — see the Dataset section above
- Final wording of the falsifiable hypothesis
- Primary behavioural target
- Whether the resting-state objective should be dropped or reframed
- Exact FC preprocessing and estimation choices
- Graph thresholding and treatment of negative edges
- Graph metrics and level of aggregation
- Prediction model, validation scheme and available confounds

## Course milestones

| Date | Milestone |
|---|---|
| 13 July | Extended proposal session: refine question and start coordinated analysis |
| 17 July | Abstract submission |
| 24 July | Final project story / presentation |

## Sources

This plan is distilled from two team sources — keep both in sync as they evolve:

- the [10 July meeting](meetings/2026-07-10.md) notes and its transcript, and
- the shared **"Ideas" Google Doc** (owner: Valeria; tabs *Ideas · Data Understanding · Literature
  Related · Main Tasks · Abstract*) — its *Main Tasks* tab is the "proposed path" that maps to the
  working stages above. See [`../manuscript/README.md`](../manuscript/README.md) for how the Doc's tabs
  map into the repo.

New decisions should update this plan; detailed discussion can stay in dated meeting notes.

