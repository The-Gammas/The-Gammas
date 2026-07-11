# The Gammas — HCP N-back working-memory project

> **Working question:** Does functional connectivity reconfigure between low and high
> working-memory load (0-back → 2-back), and can that reconfiguration predict individual
> working-memory performance?

**Current status — initial shared scaffold (11 July 2026).** The repository is a place to share
work as the question and analysis evolve. It is intentionally small: personal explorations live in
`sandbox/`; only notebooks reviewed by the group move into `pipeline/`.

## Start here

1. Read the [current project plan](docs/project-plan.md).
2. Use the official [HCP task loader with behavioural data](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/fMRI/load_hcp_task_with_behaviour.ipynb) to understand and access the dataset.
3. Work inside your own `sandbox/<name>/` folder.
4. Start notebooks from [`pipeline/00_NOTEBOOK_TEMPLATE.ipynb`](pipeline/00_NOTEBOOK_TEMPLATE.ipynb).
5. Read the short [contribution guide](CONTRIBUTING.md) before pushing.

## Current focus

| Stage | Current state | Lead(s) | Working location |
|---|---|---|---|
| Data ingestion + EV segmentation | **In progress** | Jaime | [`sandbox/jaime/`](sandbox/jaime/) |
| Data dictionary | **In progress** | Jaime | [`sandbox/jaime/02_data_dictionary.ipynb`](sandbox/jaime/02_data_dictionary.ipynb) |
| Functional connectivity | Planned | Valeria + Arefeh | Personal sandboxes first |
| Matrices → graphs | Planned | Goutham | Personal sandbox first |
| Graph metrics | Planned | Kerem + Arefeh | Personal sandboxes first |
| Prediction / testing | Planned | Valeria + Arefeh | Personal sandboxes first |

The stages describe the group's working direction; they do not imply that corresponding notebooks
or outputs already exist.

## Key links

| Resource | Link |
|---|---|
| Group repository | [The-Gammas/The-Gammas](https://github.com/The-Gammas/The-Gammas) |
| Shared project Colab / initial POC | [Open in Colab](https://colab.research.google.com/drive/1Wu9Ke8bqr_UQp8_ZmtLTus-l0Xja3oIq) |
| Live abstract | [Shared Google Doc](https://docs.google.com/document/d/1mRC-UZhOGJ_ovPqXBudEBEPUyIp_AzjkJqvoIsAyouk/edit) |
| NMA fMRI datasets | [Official guide](https://github.com/NeuromatchAcademy/course-content/tree/main/projects/fMRI) |
| NMA project workflow | [Daily project guidance](https://compneuro.neuromatch.io/projects/docs/project_guidance.html) |
| NMA project planner | [Open planner](https://nma-project-planner.vercel.app/) |
| Meeting record | [10 July notes](docs/meetings/2026-07-10.md) |
| Versioned writing | [`manuscript/`](manuscript/) |

## Team

These are short working profiles, not fixed job descriptions. Each member can update their own row.

| Member | Background / interest shared with the group | Current focus |
|---|---|---|
| **Jaime** | Medical doctor + senior data scientist; Python and methodological rigor | Ingestion, EV segmentation, data dictionary |
| **Pratik Bhandari** | Profile to complete with Pratik | Contribution to define |
| **Goutham Arcod** | HCP data exploration and initial proof of concept | Graph construction |
| **Valeria Moraga** | Functional connectivity and literature review | FC and prediction/testing |
| **Arefeh Lali Dehadhi** | Graph-theory framing and scientific writing | FC, graph metrics and testing |
| **Kerem Akyurt** | Previous graph-theory work in cognitive neuroscience | Graph metrics |

## Repository map

```text
pipeline/      group-reviewed, explanatory notebooks; currently only the template
sandbox/       iterative work, one folder per person
data/          local HCP data; contents are ignored by Git
docs/          the living project plan and dated meeting notes
manuscript/    abstract snapshots, references and prior work
```

The rule is simple:

- **Still exploring?** Keep it in `sandbox/<name>/`.
- **Reviewed and useful to the whole group?** Promote a clean explanatory copy to `pipeline/`.
- **Large or subject-level data?** Keep it out of Git and document how to reproduce it.

## Notebook style

Notebooks should show the reasoning, not only the final code. Explain the question, inputs,
sanity checks, processing, visualisations, interpretation, limitations and hand-off. Reusable or
repeated logic may live in a neighbouring `.py` file and be imported by the notebook.

## Setup

### Google Colab

The easiest route is to open an existing notebook in Colab. The template contains a commented
bootstrap cell for cloning this repository after the first version is published.

### Local

```bash
git clone https://github.com/The-Gammas/The-Gammas.git
cd The-Gammas
python3 -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter lab
```

## Data use

The NMA subset derives from the Human Connectome Project. Every user must follow the
[HCP Data Use Terms](https://www.humanconnectome.org/study/hcp-young-adult/document/wu-minn-hcp-consortium-open-access-data-use-terms).
Raw data and subject-level derived files are not versioned in this repository; see
[`data/README.md`](data/README.md).

