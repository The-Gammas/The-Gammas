<div align="center">

# 🧠 The Gammas

### Does functional-connectivity reconfiguration under working-memory load predict individual performance?

HCP N-back · Neuromatch Academy CompNeuro 2026 · Pod Ifrit Ras el Hanout · Group 1

[![Project closed 24 Jul 2026](https://img.shields.io/badge/project-closed_24_Jul_2026-455a64)](docs/final-report.md)
[![Dataset HCP N-back](https://img.shields.io/badge/dataset-HCP_N--back_(A%2FB)-c62828)](data/README.md)
[![Atlas Glasser 360](https://img.shields.io/badge/atlas-Glasser_360_·_Cole--Anticevic-00897b)](docs/data-dictionary.md)
[![Tests](https://img.shields.io/badge/tests_·_no_data_needed-43a047)](tests/)
[![License MIT + CC BY 4.0](https://img.shields.io/badge/license-MIT_·_CC--BY--4.0-1e88e5)](LICENSE)

</div>

## What we found

The 78-feature reconfiguration fingerprint (2-back − 0-back functional connectivity, 12 Cole-Anticevic
networks) **predicts 2-back accuracy in held-out participants**: repeated-CV **r = +0.366 ± 0.024**
(n = 336, permutation p < 0.001), transferring to the identity-disjoint cohort A at **r = +0.398**
(95% CI [+0.25, +0.53]).

The directional prediction was **refined rather than confirmed**. Segregation does drop under load at
group level (Δ = −0.0236, p = 3.45e-05), but a larger drop does not predict better performance. And a
regional activation contrast predicts more strongly (r = 0.600) under unmatched representations — so
whether the predictive signal is *specific to connectivity* remains open.

> **📕 [`docs/final-report.md`](docs/final-report.md) is the source of truth.** Any number quoted
> elsewhere without a protocol, an `n` and a source cell is superseded by it. Everything dated before
> 24 Jul 2026 — the submitted abstract, the minutes, the folder READMEs — records what was known then.

## Start here

The minimum path is four documents, about 40 minutes:

1. **[`docs/final-report.md`](docs/final-report.md)** — question, data, method, canonical results table, limitations, open threads.
2. **[The presented deck](manuscript/slides/The%20Gammas%20-%20NMA%20project.pdf)** — the same story in 11 slides, as delivered on 24 July 2026.
3. **[`presenter_guide_w3d5.md`](manuscript/slides/presenter_guide_w3d5.md)** — how each figure and number is meant to be read, plus the likely questions.
4. **[`docs/data-dictionary.md`](docs/data-dictionary.md)** — the single authority on files, variables and the two cohorts.

Then, depending on why you came:

| I want to… | Go to |
|---|---|
| **Re-run the analysis** | [`data/README.md`](data/README.md) for the data, then `make reproduce` (~8 min) |
| **Reuse the code** | [`gammas/`](gammas/) and [`tests/`](tests/) · `make test` runs in under a second |
| **Read the abstract** | [`manuscript/abstract.md`](manuscript/abstract.md) — as submitted 20 Jul, plus the corrected draft |
| **Contribute** | [CONTRIBUTING.md](CONTRIBUTING.md) (where things go, branches, tests) · [AGENTS.md](AGENTS.md) (working contract) |
| **Continue the science** | [final report §10](docs/final-report.md) — five open threads with their provenance |

## Evidence map

Every number on the slides traces to
[`pipeline/02_canonical_analysis_and_slides.ipynb`](pipeline/02_canonical_analysis_and_slides.ipynb),
which runs top to bottom and self-checks against the canonical `r = 0.366` at cell 10. The executed
sandbox notebooks stay as the dated source record, so the chronology remains auditable.

| Result | Number | Where |
|---|---|---|
| **Canonical evidence and figures** | all of the below, one notebook | [`pipeline/02`](pipeline/02_canonical_analysis_and_slides.ipynb) |
| Reconfiguration predicts WM | r ≈ 0.366, perm p < 0.001 | source [`sandbox/jaime/04`](sandbox/jaime/04_goutham_pipeline_on_B.ipynb) |
| Identity-disjoint B→A transfer *(same HCP study, not an external cohort)* | r ≈ 0.398 | source [`sandbox/jaime/05`](sandbox/jaime/05_dataset_A_external_validation.ipynb) |
| **The result that changed the conclusion:** activation predicts more strongly; reconfiguration adds nothing clear over 0-back FC | 0.600 vs 0.366 | source [`sandbox/jaime/08`](sandbox/jaime/08_activation_vs_reconfiguration.ipynb) |
| Tangent-space representation evaluated | **POSTPONE ADOPTION** | [`pipeline/03`](pipeline/03_method_benchmark_tangent_fc.ipynb) |
| Goutham's pipeline reconciled + brain maps | fingerprint 0.366; ΔSeg −0.024, not −0.048 | [`pipeline/04`](pipeline/04_goutham_pipeline_reconciliation.ipynb) |

## How the repo is organised

```text
gammas/        shared A/B data layer: datasets → preprocessing → connectivity → evaluation
               + contributed.py — methods designed by teammates, under their authorship
tests/         unit tests for the layer, no data required
pipeline/      group-reviewed notebooks: EDA, canonical evidence, two benchmarks
docs/          final report, data dictionary, meeting minutes, writing guide, archive/
manuscript/    abstract, references, proposal, literature review, the presented deck, archive/
sandbox/       per-person exploration, one folder per member — the audit trail
data/          local HCP data — gitignored except its README, never committed
```

Area indexes: [`pipeline/`](pipeline/README.md) · [`manuscript/`](manuscript/README.md) ·
[`data/`](data/README.md) · [`sandbox/jaime/`](sandbox/jaime/README.md) · full map with the source of
truth for each fact: [final report §9](docs/final-report.md)

*Rule of thumb: if a teammate would read it to **know what happened** it goes in `docs/`; if they would
reuse it to **write a paper**, `manuscript/`.*

> Shared areas change through a **branch + pull request** so `main` stays stable, and
> `sandbox/<name>/` belongs to that person alone. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Team

Valeria Moraga · Kerem Akyurt · Goutham Arcod · Jaime Alonso Pineda Moreno · Arefeh Lali Dehaghi,
with Pratik Bhandari as a pod member and, by recorded decision, not an author.

Commit history is **not** a proxy for contribution here — several members delivered through shared
documents, slides and meetings. Author order, CRediT roles and the evidence behind each:
[AUTHORS.md](AUTHORS.md). Methods contributed by a teammate stay under their name in
[`gammas/contributed.py`](gammas/contributed.py) and keep their own copy in their sandbox.

<details>
<summary><b>⚙️ Setup</b></summary>

**Google Colab.** Open a notebook and run its setup cell to clone the repo and install requirements.
Cloning brings the *code*, not the HCP data (~1 GB for A, ~8 GB for B) — fetch that into the session
separately. See [`data/README.md`](data/README.md).

**Local** (`requirements.txt` is known-good on Python 3.12):

```bash
git clone https://github.com/The-Gammas/The-Gammas.git
cd The-Gammas
python3 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
make test                                            # sanity check, no data needed
```

Loaders read from `./data` by default; set `GAMMAS_DATA_DIR` to point elsewhere.

Notebooks at any depth import the shared layer the same way — it locates the package rather than
guessing a relative hop:

```python
ROOT = next(p for p in (Path.cwd(), *Path.cwd().parents) if (p / "gammas").is_dir())
sys.path.insert(0, str(ROOT))
from gammas import datasets as ds, preprocessing as pp, evaluation as ev
```

`make reproduce` re-runs the analysis end to end once you have the data.

</details>

## Data use and licence

The NMA subset derives from the **Human Connectome Project**; every user must follow the
[HCP Data Use Terms](https://www.humanconnectome.org/study/hcp-young-adult/document/wu-minn-hcp-consortium-open-access-data-use-terms).
Raw data and subject-level derived files are **not** versioned here — see
[`data/README.md`](data/README.md) to obtain and place them.

Code under the **MIT License**, text and figures under **CC BY 4.0** ([LICENSE](LICENSE)). If you reuse
this work, cite it with [CITATION.cff](CITATION.cff) and credit the authors in [AUTHORS.md](AUTHORS.md).
Conduct: we keep the [NMA Code of Conduct](https://docs.neuromatch.io/p/vIfHFwWpiwsIOa/Code-of-Conduct).
