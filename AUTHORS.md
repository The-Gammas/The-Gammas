# Authors and contributions

**Project:** *Adaptive Functional Network Reconfiguration for Predicting Individual Working-Memory
Performance* · HCP N-back · Neuromatch Academy CompNeuro 2026 · Pod Ifrit Ras el Hanout, Group 1.
**Author list fixed:** [20 Jul 2026 minutes, §1.3](docs/meetings/2026-07-20.md) · **project closed:**
W3D5, 24 Jul 2026.

## Why this file exists

Commit history is not a proxy for contribution in this repository, and here that is demonstrable
rather than diplomatic:

1. **Valeria Moraga authored files she never committed.** Every commit touching `sandbox/valeria/` was
   pushed by Jaime — the first one says so in its own message
   ([`5cf8f9a`](https://github.com/The-Gammas/The-Gammas/commit/5cf8f9a), *"…hypotheses By Valeria"*).
   `git log -- sandbox/valeria/` returns zero commits authored by her.
2. **Arefeh Lali Dehaghi and Kerem Akyurt own pipeline stages and hold no sandbox content.**
   `sandbox/arefeh/` and `sandbox/kerem/` contain only a `.gitkeep`; the
   [10 Jul work split](docs/meetings/2026-07-10.md) assigns them stages 3–6 and 5, and both presented
   at W3D5 ([presenter guide](manuscript/slides/presenter_guide_w3d5.md), slides 3 and 6). An empty
   sandbox folder means the work was delivered outside the repository — shared documents, slides,
   meetings — not that nothing was contributed.
3. **Pratik Bhandari's absence from the author list is a recorded decision, not an omission.** See
   [Pod members who are not authors](#pod-members-who-are-not-authors).

Roles below use the [CRediT taxonomy](https://credit.niso.org/). Each role carries a link to the file,
commit or minutes that evidence it. Narrative detail of who did what is in
[`docs/final-report.md` §12](docs/final-report.md#12--authorship-and-contributions).

## Authors

Listed in the order fixed on 20 Jul 2026 and used in the submitted abstract.

| # | Author | CRediT roles | Evidence |
|---|---|---|---|
| 1 | **Valeria Moraga** | Conceptualization · Writing – original draft · Writing – review & editing | Research-question development: [`sandbox/valeria/research-question-development.pdf`](sandbox/valeria/research-question-development.pdf), committed by Jaime as [`5cf8f9a`](https://github.com/The-Gammas/The-Gammas/commit/5cf8f9a); condensed into [`manuscript/research-proposal.md`](manuscript/research-proposal.md) (source contribution declared at L20 and L258). Abstract drafting, merge and submission: [`manuscript/abstract.md`](manuscript/abstract.md) (SUBMITTED block, 20 Jul 22:12) and [`sandbox/valeria/Abstract_v1.pdf`](sandbox/valeria/Abstract_v1.pdf). Deck ownership: [`manuscript/slides/README.md`](manuscript/slides/README.md) §History. Presented the introduction (slide 2). |
| 2 | **Kerem Akyurt** | Investigation · Writing – review & editing | Graph-metrics ownership in the [10 Jul work split](docs/meetings/2026-07-10.md) §3 (stage 5) and the graph layer as feature enrichment, [15 Jul minutes](docs/meetings/2026-07-15.md) §Proposed. Raised the A+B cohort merge and its ~35 shared identities ([15 Jul](docs/meetings/2026-07-15.md), *Set aside*), the overlap later quantified in [`docs/final-report.md` §3](docs/final-report.md). Reviewed the shared interpretation and froze the W3D5 scope, [22 Jul minutes](docs/meetings/2026-07-22.md). Presented the conclusions (slide 6). |
| 3 | **Goutham Arcod** | Methodology · Software · Investigation | The analysis method — FC per condition → 2bk−0bk → 12-network fingerprint → cross-validated prediction — in [`sandbox/goutham/per_analysis.ipynb`](sandbox/goutham/per_analysis.ipynb), commit [`5071ccd`](https://github.com/The-Gammas/The-Gammas/commit/5071ccd); clustering and entropy work in [`sandbox/goutham/FCM_entropy.ipynb`](sandbox/goutham/FCM_entropy.ipynb), commit [`f886169`](https://github.com/The-Gammas/The-Gammas/commit/f886169). His `get_brain_profile` is reimplemented as [`gammas.connectivity.network_fingerprint`](gammas/connectivity.py) (attribution in the docstring) and his `measure_system_segregation` runs verbatim in [`pipeline/02`](pipeline/02_canonical_analysis_and_slides.ipynb) and [`pipeline/04`](pipeline/04_goutham_pipeline_reconciliation.ipynb). Raised the CVR caveat on the activation comparator ([`manuscript/references.md`](manuscript/references.md) L163–167). Presented the robustness checks (slide 5). |
| 4 | **Jaime Alonso Pineda Moreno** | Data curation · Software · Formal analysis · Validation · Visualization · Project administration · Writing – original draft | Data ingestion, EV segmentation and the data dictionary assigned in the [10 Jul work split](docs/meetings/2026-07-10.md) §3 (stages 1–2); shared A/B layer [`gammas/`](gammas/) and [`tests/`](tests/), [`docs/data-dictionary.md`](docs/data-dictionary.md), [`data/README.md`](data/README.md). Cohort choice and port of the pipeline to B, identity-disjoint B→A transfer, activation robustness check, tangent benchmark, canonical assembly: [`pipeline/`](pipeline/) and [`sandbox/jaime/`](sandbox/jaime/). Deck build, [presenter guide](manuscript/slides/presenter_guide_w3d5.md) and [`docs/final-report.md`](docs/final-report.md). Presented the results (slide 4). |
| 5 | **Arefeh Lali Dehaghi** | Conceptualization · Writing – original draft | The project hypothesis in the form the analysis tested: [15 Jul minutes](docs/meetings/2026-07-15.md) §*Hypothesis (Arefeh's, refined)*, carried into [`docs/final-report.md` §2](docs/final-report.md). Drafted the Abstract tab of the team document ([`manuscript/README.md`](manuscript/README.md) L13–14; [10 Jul minutes](docs/meetings/2026-07-10.md) §11). FC and graph-metric stages in the [10 Jul work split](docs/meetings/2026-07-10.md) §3 (stages 3–6 and 5). Presented the methods (slide 3). |

## Pod members who are not authors

**Pratik Bhandari** was a member of the pod and is not an author. This is a recorded team decision, not
an oversight: [20 Jul minutes §1.3](docs/meetings/2026-07-20.md) — *"**Authors (5):** … **Pratik is not
on the author list.**"* — reproduced in the submitted abstract
([`manuscript/abstract.md`](manuscript/abstract.md), SUBMITTED block). His sandbox folder
`sandbox/pratik/` is kept, empty, as part of the record that the pod had six members.

## Ownership of teammate material

`sandbox/goutham/` and `sandbox/valeria/` are their authors' own contribution. Their content has never
been edited or rewritten by anyone else. The only changes ever applied were housekeeping: one PDF
renamed to kebab-case with no byte of content altered, and the removal of placeholder `.gitkeep` files
from folders that now hold work. Technical caveats about that material are documented outside their
files — in [`docs/final-report.md`](docs/final-report.md) and
[`pipeline/04`](pipeline/04_goutham_pipeline_reconciliation.ipynb) — never by editing it.

## Name spellings

The canonical spelling is the one in the [20 Jul minutes](docs/meetings/2026-07-20.md) and the
submitted abstract. Earlier files carry variants; they refer to the same person and are not corrected
where the file is a frozen dated record.

| Canonical | Also appears as | Where |
|---|---|---|
| Arefeh Lali Dehaghi | Arefeh Lali Dehadhi | `README.md` L139, [22 Jul minutes](docs/meetings/2026-07-22.md) L9 |
| Goutham Arcod | `gouthamarcot` (GitHub handle) | commits [`5071ccd`](https://github.com/The-Gammas/The-Gammas/commit/5071ccd), [`f886169`](https://github.com/The-Gammas/The-Gammas/commit/f886169) |
| Jaime Alonso Pineda Moreno | `jpimore`, `Jaime` (GitHub handle / commit name) | commit history |

## Citing this work

Machine-readable metadata: [`CITATION.cff`](CITATION.cff). Licensing: MIT for code, CC BY 4.0 for
documentation, text and figures — see [`LICENSE`](LICENSE).
