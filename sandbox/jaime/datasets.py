"""Config + raw loaders for the HCP working-memory finalists (Jaime's sandbox).

**Category: loaders / I-O.** Defines the two datasets (:class:`DatasetSpec`, :func:`spec_a`,
:func:`spec_b`), the shared constants, and the raw reads from disk (subject lists,
parcellated BOLD). Both finalists sit behind one spec so the downstream modules never
branch on the dataset. Layering:

    datasets (this file: config + I/O)  <-  preprocessing (raw -> analysis-ready)  <-  evaluation (split + QC)

- **Finalist A** = ``load_hcp_task_with_behaviour`` (100 subj, ``hcp_task/``, per-subject ``Stats.txt``).
- **Finalist B** = ``load_hcp`` (339 subj, ``hcp_task_339/`` + ``hcp_rest/`` + ``hcp/behavior/wm.csv``).

On disk both finalists live under loader-named group dirs (``data/A_load_hcp_task_with_behaviour/``,
``data/B_load_hcp/``); the loaders resolve that or the legacy flat layout — see :func:`spec_a` / :func:`spec_b`.

Provenance: NMA-curated HCP task fMRI; the loaders reimplement the official
``load_hcp_task_with_behaviour`` / ``load_hcp`` notebooks (B is ``load_hcp`` — **not** the
similarly-named ``load_hcp_task``, a different 100-subj, behaviour-free set we never used). Glasser 360 parcellation
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

#: Loader provenance + on-disk grouping. Each finalist's files live under a loader-named
#: group dir (``data/<group>/…``); the loaders fall back to the legacy flat layout
#: (``data/hcp_task/…``) so grouped data, flat data, or a fresh flat download all read the same.
LOADER_A: str = "load_hcp_task_with_behaviour"
LOADER_B: str = "load_hcp"
GROUP_A: str = f"A_{LOADER_A}"  # -> "A_load_hcp_task_with_behaviour"
GROUP_B: str = f"B_{LOADER_B}"  # -> "B_load_hcp"

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
        loader: the official NMA loader this dataset comes from (``LOADER_A`` / ``LOADER_B``);
            surfaced in QC so every table carries its provenance.
        task_dir: root holding ``subjects/`` (WM timeseries + EVs) and ``regions.npy``.
        behaviour: A -> same as ``task_dir`` (per-subject ``Stats.txt``); B -> ``wm.csv``.
        rest_dir: resting-state root (B only), else ``None``.
        atlas: ROI-geometry ``.npz`` (B only: ``coords`` + surface ``labels_R/L``), else ``None``.
        n_expected: sanity-check subject count (100 for A, 339 for B).
    """

    kind: str
    name: str
    loader: str
    task_dir: Path
    behaviour: Path
    rest_dir: Path | None
    atlas: Path | None
    n_expected: int


def _resolve(data_dir: Path, group: str, subpath: str) -> Path:
    """Locate a dataset subpath, preferring the loader-grouped layout over the legacy flat one.

    Tries ``data_dir/<group>/<subpath>`` first, then ``data_dir/<subpath>``; returns the grouped
    target when neither exists, so a missing-data error points at the current layout. Keeps the
    loaders working whether the data is grouped, flat, or a fresh flat download.
    """
    grouped = data_dir / group / subpath
    if grouped.exists():
        return grouped
    flat = data_dir / subpath
    return flat if flat.exists() else grouped


def spec_a(data_dir: str | Path) -> DatasetSpec:
    """Finalist A spec — loader ``load_hcp_task_with_behaviour``, task+behaviour in ``hcp_task``."""
    task = _resolve(Path(data_dir), GROUP_A, "hcp_task")
    return DatasetSpec("A", "Finalist A (100 subj, task-only)", LOADER_A, task, task, None, None, 100)


def spec_b(data_dir: str | Path) -> DatasetSpec:
    """Finalist B spec — loader ``load_hcp``; task in ``hcp_task_339``, behaviour ``hcp/behavior/wm.csv``."""
    root = Path(data_dir)
    return DatasetSpec(
        "B",
        "Finalist B (339 subj, +resting-state)",
        LOADER_B,
        _resolve(root, GROUP_B, "hcp_task_339"),
        _resolve(root, GROUP_B, "hcp/behavior/wm.csv"),
        _resolve(root, GROUP_B, "hcp_rest"),
        _resolve(root, GROUP_B, "hcp_atlas_339.npz"),
        339,
    )


# --------------------------------------------------------------------------- #
# Loaders
# --------------------------------------------------------------------------- #
def load_subjects(spec: DatasetSpec, require_behaviour: bool = True) -> list[str]:
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
    if run not in (0, 1):
        raise ValueError(f"run must be 0 or 1, got {run!r}")
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


def list_rest_runs(spec: DatasetSpec, subject: str) -> list[Path]:
    """Resting-state run files for a subject, sorted (Finalist B only; empty for A).

    Owns the rest-state path layout (``rest_dir/subjects/<s>/timeseries/bold*.npy``) so QC
    and downstream callers never rebuild it. A ships no resting-state data, hence empty.
    """
    if spec.rest_dir is None:
        return []
    ts_dir = spec.rest_dir / "subjects" / subject / "timeseries"
    return sorted(ts_dir.glob("bold*.npy")) if ts_dir.exists() else []


def load_rest_timeseries(spec: DatasetSpec, subject: str, run: int = 0) -> np.ndarray:
    """One resting-state run as ``(N_PARCELS, n_timepoints)``; ``run`` indexes
    :func:`list_rest_runs` order. Raw read (no mean removal) — rest is only probed for
    availability/shape in QC, not part of this data layer's analysis path.
    """
    return np.load(list_rest_runs(spec, subject)[run])
