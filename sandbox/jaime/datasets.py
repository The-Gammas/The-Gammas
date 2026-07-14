"""Config + raw loaders for the HCP working-memory finalists (Jaime's sandbox).

**Category: loaders / I-O.** Defines the two datasets (:class:`DatasetSpec`, :func:`spec_a`,
:func:`spec_b`), the shared constants, and the raw reads from disk (subject lists,
parcellated BOLD). Both finalists sit behind one spec so the downstream modules never
branch on the dataset. Layering:

    datasets (this file: config + I/O)  <-  preprocessing (raw -> analysis-ready)  <-  evaluation (split + QC)

- **Finalist A** = ``load_hcp_task_with_behaviour`` (100 subj, ``hcp_task/``, per-subject ``Stats.txt``).
- **Finalist B** = ``load_hcp_task`` (339 subj, ``hcp_task_339/`` + ``hcp_rest/`` + ``hcp/behavior/wm.csv``).

Provenance: NMA-curated HCP task fMRI; the loaders reimplement the official
``load_hcp_task_with_behaviour`` / ``load_hcp_task`` notebooks. Glasser 360 parcellation
(Glasser et al. 2016); 12-network Cole-Anticevic partition (Ji et al. 2019). Using HCP data
requires accepting the HCP Data Use Terms. B's WM runs are ``bold7`` (RL) / ``bold8`` (LR),
verified against the official ``EXPERIMENTS['WM']['runs'] == [7, 8]``; note A run 0 is LR but
B run 0 is RL.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

# --------------------------------------------------------------------------- #
# Constants (from the official loaders)
# --------------------------------------------------------------------------- #
N_PARCELS: int = 360
TR: float = 0.72  # seconds per frame

#: The 8 WM conditions = 2 load levels x 4 stimulus categories.
COND_0BACK: tuple[str, ...] = ("0bk_body", "0bk_faces", "0bk_places", "0bk_tools")
COND_2BACK: tuple[str, ...] = ("2bk_body", "2bk_faces", "2bk_places", "2bk_tools")

#: ``Stats.txt`` (Finalist A) labels the body category "BP" (Body Parts), not "body".
STATS_CATEGORIES: tuple[str, ...] = ("BP", "Faces", "Places", "Tools")

#: Run index -> phase-encoding direction. A and B order the two runs oppositely.
RUN_LABELS: dict[str, tuple[str, str]] = {"A": ("LR", "RL"), "B": ("RL", "LR")}

#: Finalist B: run index -> ``bold{N}`` file number for the WM task (official EXPERIMENTS).
B_WM_BOLD: tuple[int, int] = (7, 8)

#: Finalist B: task subjects without complete 2-back behaviour in ``wm.csv``.
B_INCOMPLETE_SUBJECTS: tuple[str, ...] = ("81", "143", "329")

#: ``regions.npy`` stores network labels truncated to 12 chars; map them back to the full
#: published Cole-Anticevic names (Ji et al. 2019). Keys read from the dataset's own
#: ``regions.npy``; matching on the full name without this would silently drop rows.
NETWORK_FULL: dict[str, str] = {
    "Visual1": "Visual1",
    "Visual2": "Visual2",
    "Somatomotor": "Somatomotor",
    "Cingulo-Oper": "Cingulo-Opercular",
    "Language": "Language",
    "Default": "Default",
    "Frontopariet": "Frontoparietal",
    "Auditory": "Auditory",
    "Dorsal-atten": "Dorsal-attention",
    "Posterior-Mu": "Posterior-Multimodal",
    "Ventral-Mult": "Ventral-Multimodal",
    "Orbito-Affec": "Orbito-Affective",
}


# --------------------------------------------------------------------------- #
# Dataset config
# --------------------------------------------------------------------------- #
@dataclass(frozen=True)
class DatasetSpec:
    """Everything the loaders need to locate one dataset on disk.

    Attributes:
        kind: ``"A"`` or ``"B"`` — selects the path layout and behaviour source.
        name: human-readable label for tables and figures.
        task_dir: root holding ``subjects/`` (WM timeseries + EVs) and ``regions.npy``.
        behaviour: A -> same as ``task_dir`` (per-subject ``Stats.txt``); B -> ``wm.csv``.
        rest_dir: resting-state root (B only), else ``None``.
        n_expected: sanity-check subject count (100 for A, 339 for B).
    """

    kind: str
    name: str
    task_dir: Path
    behaviour: Path
    rest_dir: Path | None
    n_expected: int


def spec_a(data_dir: str | Path) -> DatasetSpec:
    """Finalist A spec rooted at ``<data_dir>/hcp_task``."""
    task = Path(data_dir) / "hcp_task"
    return DatasetSpec("A", "Finalist A (100 subj, task-only)", task, task, None, 100)


def spec_b(data_dir: str | Path) -> DatasetSpec:
    """Finalist B spec: task in ``hcp_task_339``, behaviour in ``hcp/behavior/wm.csv``."""
    root = Path(data_dir)
    return DatasetSpec(
        "B",
        "Finalist B (339 subj, +resting-state)",
        root / "hcp_task_339",
        root / "hcp" / "behavior" / "wm.csv",
        root / "hcp_rest",
        339,
    )


# --------------------------------------------------------------------------- #
# Loaders
# --------------------------------------------------------------------------- #
def list_subjects(spec: DatasetSpec, require_behaviour: bool = True) -> list[str]:
    """Analytic subject IDs (as strings) for a dataset.

    Args:
        require_behaviour: if True, drop subjects without a usable 2-back score
            (A: all 100 qualify; B: 336 of 339, excluding 81/143/329).
    """
    if spec.kind == "A":
        return np.loadtxt(spec.task_dir / "subjects_list.txt", dtype="str").tolist()
    ids = sorted((p.name for p in (spec.task_dir / "subjects").iterdir() if p.is_dir()), key=int)
    if require_behaviour:
        ids = [s for s in ids if s not in B_INCOMPLETE_SUBJECTS]
    return ids


def load_timeseries(spec: DatasetSpec, subject: str, run: int,
                    remove_mean: bool = True) -> np.ndarray:
    """One WM run as ``(N_PARCELS, n_timepoints)``. ``run`` is 0 or 1.

    Reimplements the official loader's ``load_single_timeseries``. A reads
    ``WM/tfMRI_WM_{LR,RL}/data.npy`` (run 0 = LR); B reads ``timeseries/bold{7,8}...`` and
    maps run 0 -> bold7 (RL), run 1 -> bold8 (LR).
    """
    if spec.kind == "A":
        path = (spec.task_dir / "subjects" / subject / "WM"
                / f"tfMRI_WM_{RUN_LABELS['A'][run]}" / "data.npy")
    else:
        path = (spec.task_dir / "subjects" / subject / "timeseries"
                / f"bold{B_WM_BOLD[run]}_Atlas_MSMAll_Glasser360Cortical.npy")
    ts = np.load(path)
    if remove_mean:
        ts = ts - ts.mean(axis=1, keepdims=True)
    return ts
