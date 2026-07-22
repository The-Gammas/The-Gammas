<div align="center">

# 🧠 The Gammas — HCP N-back Working-Memory Project

**Neuromatch Academy · CompNeuro 2026 · Pod Ifrit Ras el Hanout · Group 1**

[![Neuromatch CompNeuro 2026](https://img.shields.io/badge/Neuromatch-CompNeuro_2026-5e35b1)](https://compneuro.neuromatch.io/tutorials/intro.html)
[![Course Week 3](https://img.shields.io/badge/course-Week_3_·_W3D5_Fri_24_Jul-1e88e5)](https://compneuro.neuromatch.io/tutorials/Schedule/daily_schedules.html)
[![Dataset HCP N-back](https://img.shields.io/badge/dataset-HCP_N--back_(A%2FB)-c62828)](data/README.md)
[![Atlas Glasser 360](https://img.shields.io/badge/atlas-Glasser_360_·_Cole--Anticevic-00897b)](sandbox/jaime/02_eda_and_data_dictionary.ipynb)
[![Abstract submitted 20 Jul](https://img.shields.io/badge/abstract-submitted_20_Jul-43a047)](https://docs.google.com/document/d/1mRC-UZhOGJ_ovPqXBudEBEPUyIp_AzjkJqvoIsAyouk/edit)

</div>

---

> ### 🎯 Working question
> Does functional connectivity **reconfigure** between low and high working-memory load
> (0-back → 2-back), and can that reconfiguration **predict** individual working-memory performance?
>
> *The Project TA's north star is **prediction on unseen subjects**. Functional connectivity and graph metrics are candidate **features**, not the goal — and the hypothesis stays falsifiable.*

**Status (22 Jul):** the abstract was **submitted 20 Jul** (22:12) and focus is now the **W3D5
presentation** (Fri 24 Jul). At the [22 July Zoom sync](docs/meetings/2026-07-22.md), Jaime, Kerem and
Valeria agreed to close the scientific scope at the evidence already consolidated in
[`pipeline/02_canonical_analysis_and_slides.ipynb`](pipeline/02_canonical_analysis_and_slides.ipynb).
Its calculations and figures are reproducible; Goutham's additional proposals are follow-up ideas,
not presentation blockers. Jaime and Valeria are preparing the first slide version for review with
Andrea and the full team on Thu 23 Jul afternoon. This is the attendees' working baseline; final
story, figure and presenter approval still belongs to the full-team review. Source analyses remain
in `sandbox/` so their provenance is preserved.

> **nb08 update (21 Jul):** the "reconfiguration predicts WM" framing below is refined.
> A task-activation contrast (2bk-0bk mean BOLD) predicts better (r ~ 0.60 pooled, ~0.48 held-out
> people and runs), FC showed no clear incremental gain over it in the tested comparison (nested
> delta-R2 -0.003; note activation uses 360 regional features vs FC's 78 network summaries), and
> reconfiguration does not clearly add over single-condition 0-back FC (nested delta-R2 +0.034, sd
> 0.023, under 2 sd). Under these unmatched representations, the evidence does not establish that
> the predictive signal is specific to connectivity reconfiguration. Full check:
> [`sandbox/jaime/08_activation_vs_reconfiguration.ipynb`](sandbox/jaime/08_activation_vs_reconfiguration.ipynb).

---

## 🔬 The pipeline

Five steps from raw BOLD to a tested prediction. This is the conceptual workflow; the table below
records what currently exists, not a fixed assignment for the final week. The reconfiguration-predicts-WM
direction is **refined by nb08** (see the status note above): a task-activation contrast predicts better
under the current comparison, while FC shows no clear incremental gain. The proposed final narrative
keeps FC reconfiguration primary and presents activation as an unexpected benchmark.

```mermaid
flowchart LR
    A["1 · Ingestion + EV<br/>0-back / 2-back split<br/><b>Jaime</b>"]
    B["2 · Functional connectivity<br/>Pearson per condition<br/><b>Valeria · Arefeh</b>"]
    C["3 · Graph construction<br/>weighted, undirected<br/><b>Goutham</b>"]
    D["4 · Graph metrics<br/>segregation / integration<br/><b>Kerem · Arefeh</b>"]
    E["5 · Prediction / testing<br/>WM performance · held-out subjects<br/>cross-validated · <b>Valeria · Arefeh</b>"]
    A --> B --> C --> D --> E
```

| Stage | State | Lead(s) | Working location |
|---|---|---|---|
| 1 · Ingestion + EV segmentation | ✅ Done | Jaime | Shared A/B layer + [`pipeline/01`](pipeline/01_explore_dataset_b.ipynb) |
| 2 · Functional connectivity | ✅ Canonical evidence consolidated; method caveat retained | Valeria · Arefeh | [`pipeline/02`](pipeline/02_canonical_analysis_and_slides.ipynb) · sources [`04`](sandbox/jaime/04_goutham_pipeline_on_B.ipynb) / [`08`](sandbox/jaime/08_activation_vs_reconfiguration.ipynb) |
| 3 · Matrices → graphs | 🟡 Descriptive network view included; extended graph work remains exploratory | Goutham | [`pipeline/02`](pipeline/02_canonical_analysis_and_slides.ipynb) · source [`09`](sandbox/jaime/09_goutham_pipeline_replication.ipynb) |
| 4 · Graph metrics | 🟡 Segregation direction included; clustering and full graph layer deferred | Kerem · Arefeh | [`pipeline/02`](pipeline/02_canonical_analysis_and_slides.ipynb) · source [`09`](sandbox/jaime/09_goutham_pipeline_replication.ipynb) |
| 5 · Prediction / testing | ✅ Canonical internal and B→A evidence consolidated | Valeria · Arefeh | [`pipeline/02`](pipeline/02_canonical_analysis_and_slides.ipynb) · sources [`04`](sandbox/jaime/04_goutham_pipeline_on_B.ipynb) / [`05`](sandbox/jaime/05_dataset_A_external_validation.ipynb) |

> **W3D5 scope lock (22 Jul Zoom attendees):** start from `pipeline/02`; use notebooks 04, 05, 08 and
> 09 to audit results or reuse figure code, not to open competing stories. Align on the first slide
> draft before adding individual slides or visualisations. Full-team and Andrea review is Thu 23 Jul.

---

## 📊 Evidence map: canonical result and source notebooks

The presentation evidence and figures are consolidated in one canonical notebook. The executed
sandbox notebooks remain the source record for each analysis and make the chronology auditable.

| Result | Number | Notebook |
|---|---|---|
| **Canonical presentation evidence** | FC prediction, B→A transfer, activation benchmark and segregation direction | [`pipeline/02_canonical_analysis_and_slides`](pipeline/02_canonical_analysis_and_slides.ipynb) |
| Reconfiguration predicts WM (canonical; reproduction gate for the rest) | r ≈ 0.366 repeated-CV, permutation p < 0.001 | [`04_goutham_pipeline_on_B`](sandbox/jaime/04_goutham_pipeline_on_B.ipynb) |
| External validation (train B, test held-out A, disjoint identities) | r ≈ 0.398 | [`05_dataset_A_external_validation`](sandbox/jaime/05_dataset_A_external_validation.ipynb) |
| Tangent-space representation (method candidate) | POSTPONE ADOPTION | [`06_tangent_fc_benchmark`](sandbox/jaime/06_tangent_fc_benchmark.ipynb) |
| **Robustness question:** activation predicts more strongly under unmatched representations; reconfiguration does not clearly add over 0-back FC | r ≈ 0.60 vs 0.37 | [`08_activation_vs_reconfiguration`](sandbox/jaime/08_activation_vs_reconfiguration.ipynb) |
| Goutham's pipeline reconciled on our data + brain maps | fingerprint 0.366; ΔSeg direction only (−0.024, not −0.048) | [`09_goutham_pipeline_replication`](sandbox/jaime/09_goutham_pipeline_replication.ipynb) |

`pipeline/02` is the place to reproduce the final evidence path; `08` is the clearest place to audit
the post-submission comparison that changed the conclusion. Foundation (framing, ingestion, EDA,
A/B choice): notebooks 00-03. Full read-in-order guide:
[`sandbox/jaime/README.md`](sandbox/jaime/README.md).

---

## ▶️ Start here

1. Read [AGENTS.md](AGENTS.md) — the working contract for agents and humans (setup, rules, style).
2. Read the [project plan](docs/project-plan.md), then open the
   [canonical evidence notebook](pipeline/02_canonical_analysis_and_slides.ipynb). The latest dated
   context is in the [22 July meeting notes](docs/meetings/2026-07-22.md).
3. **Get the data.** Two cohorts sit behind one loader interface: the current MVP analysis runs on B
   (339 subjects; 336 analytic), while A (100 subjects) is used for external validation. See the
   [project plan](docs/project-plan.md) and [`data/README.md`](data/README.md).
4. Work inside your own `sandbox/<name>/` folder, starting from [`pipeline/00_NOTEBOOK_TEMPLATE.ipynb`](pipeline/00_NOTEBOOK_TEMPLATE.ipynb) — its setup cells wire the data path and import the shared A/B loader for you.
5. Read the short [contribution guide](CONTRIBUTING.md) before opening a PR.

---

## 🗂️ How the repo is organised

```text
pipeline/      shared notebooks; template + onboarding + canonical presentation evidence
sandbox/       iterative work, one folder per person
data/          local HCP data — gitignored except its README, never committed
docs/          the living project plan and dated meeting notes
manuscript/    abstract snapshots, references and prior work
```

- 🧪 **Still exploring?** Keep it in `sandbox/<name>/`.
- ✅ **Reviewed and useful to everyone?** Promote a clean explanatory copy to `pipeline/`.
- 💾 **Large or subject-level data?** Keep it out of Git and document how to reproduce it.

> For anything that could affect others' code, work on a **branch** and open a **pull request** so `main` stays stable. See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 👥 Team

Short working profiles, not fixed job descriptions — each member can update their own row.

| Member | Background / interest | Current focus |
|---|---|---|
| **Jaime** | Medical doctor + data scientist; Python, pipelines and data analysis | Lead the first W3D5 story and co-build the slide draft with Valeria |
| **Pratik Bhandari** | *Profile to complete with Pratik* | Contribution to define |
| **Goutham Arcod** | HCP data exploration and initial proof of concept | Graph construction |
| **Valeria Moraga** | Functional connectivity and literature review | Co-build the first W3D5 slide draft with Jaime |
| **Arefeh Lali Dehadhi** | Graph-theory framing and scientific writing | FC, graph metrics and testing |
| **Kerem Akyurt** | Previous graph-theory work in cognitive neuroscience | Review the shared interpretation and slide story |

---

## 🔗 Key links

| Resource | Link |
|---|---|
| 🎥 Pod Zoom room | Shared in the pod's private channel (kept out of the public repo) |
| 📦 Group repository | [The-Gammas/The-Gammas](https://github.com/The-Gammas/The-Gammas) |
| 🤖 Agent & contributor guide | [AGENTS.md](AGENTS.md) · [CONTRIBUTING.md](CONTRIBUTING.md) |
| 🧪 Shared Colab (initial POC) | [Open in Colab](https://colab.research.google.com/drive/1Wu9Ke8bqr_UQp8_ZmtLTus-l0Xja3oIq) |
| ✍️ Live abstract | [Google Doc](https://docs.google.com/document/d/1mRC-UZhOGJ_ovPqXBudEBEPUyIp_AzjkJqvoIsAyouk/edit) |
| 📚 Official tutorials | [compneuro.neuromatch.io](https://compneuro.neuromatch.io/tutorials/intro.html) |
| 🗓️ Daily schedule (Slot 3) | [Daily schedules](https://compneuro.neuromatch.io/tutorials/Schedule/daily_schedules.html) |
| 🧭 Project guidance | [NMA project docs](https://compneuro.neuromatch.io/projects/docs/project_guidance.html) |
| 🧩 Project planner | [Planner app](https://nma-project-planner.vercel.app/) |
| 🧠 HCP fMRI dataset guide | [NMA fMRI projects](https://github.com/NeuromatchAcademy/course-content/tree/main/projects/fMRI) |

---

<details>
<summary><b>📓 Notebook style</b> (click to expand)</summary>

Notebooks should show the **reasoning**, not only the final code: explain the question, inputs,
sanity checks, processing, visualisations, interpretation, limitations and hand-off. Reusable or
repeated logic may live in a neighbouring `.py` file and be imported by the notebook.

</details>

<details>
<summary><b>⚙️ Setup</b> (click to expand)</summary>

### Google Colab
Open a notebook in Colab and run its setup cell to clone the repo and install requirements. **Note:**
cloning brings the *code* but not the HCP data (~1 GB for A, ~8 GB for B) — you still have to fetch the
data into the session (run the official loader notebook there, or mount Google Drive). See [`data/README.md`](data/README.md).

### Local
Requires a recent Python (`requirements.txt` is known-good on 3.12).
```bash
git clone https://github.com/The-Gammas/The-Gammas.git
cd The-Gammas
python3 -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter lab
```
These steps install the code, **not** the data — see [`data/README.md`](data/README.md) to download it. By
default the loaders read from `./data`; set `GAMMAS_DATA_DIR` to point elsewhere
(e.g. `export GAMMAS_DATA_DIR=/path/to/hcp`).

</details>

---

## 💾 Data use

The NMA subset derives from the **Human Connectome Project**. Every user must follow the
[HCP Data Use Terms](https://www.humanconnectome.org/study/hcp-young-adult/document/wu-minn-hcp-consortium-open-access-data-use-terms).
Raw data and subject-level derived files are **not** versioned here; how to obtain, place and load it → [`data/README.md`](data/README.md).
