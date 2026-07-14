"""Steps 1-2 — HCP N-back ingestion + EV segmentation (Jaime's sandbox).

This module supports Jaime's exploratory notebooks. It is intentionally local to
``sandbox/jaime/``: its functions and signatures have not yet been proposed as a
shared team API. If the group later promotes parts of this work, the public
interface should be designed from the needs of the reviewed pipeline notebook.

What this module does
---------------------
1. Load the parcellated working-memory (WM) BOLD time series per subject.
2. Use the EV (Explanatory Variable) files to keep only the frames of a given
   load level (0-back vs 2-back), pooling the 4 stimulus categories.
3. Parse the behavioural ``Stats.txt`` into per-subject WM performance scores
   (the prediction target).
4. Build an ROI -> network -> hemisphere table and an exploratory subject-level
   train/test split for discussing a future anti-leakage contract.

Provenance (where every input comes from)
------------------------------------------
- Dataset: NMA-curated subset of the Human Connectome Project (HCP) task fMRI.
- Official access route: the NMA loader notebook at
  ``https://github.com/NeuromatchAcademy/course-content/blob/main/projects/fMRI/``.
  It downloads ``hcp_task.tgz`` from OSF (``https://osf.io/2y3fw/download``) and unpacks it
  to ``./hcp_task/``; it also documents the folder layout and the helper functions this
  module reimplements. Using HCP data requires accepting the HCP Data Use Terms at
  ConnectomeDB (``https://db.humanconnectome.org``).
- Parcellation: Glasser et al. (2016), Nature 536:171-178 — 360 cortical ROIs (HCP-MMP1.0).
- Network assignment: the 12-network Cole-Anticevic partition, Ji et al. (2019),
  NeuroImage 185:35-57. Both references are the ones cited by the official loader notebook
  (its markdown links ``regions.npy`` to Glasser 2016 and the network labels to Ji 2019);
  ``NETWORK_FULL`` below simply de-truncates the 12-char labels stored in ``regions.npy``
  back to those published names.
- Constants (N_SUBJECTS, N_PARCELS, TR, RUNS): copied from the loader notebook.

Base dataset vs. the 339-subject alternative
--------------------------------------------
This module targets **Finalist A** — ``load_hcp_task_with_behaviour`` (100 subjects,
task only, per-subject ``Stats.txt``), living under ``data/hcp_task/``. **Finalist B**
— the ``load_hcp_task`` loader (339 subjects, + resting-state, consolidated
``data/hcp/behavior/wm.csv``) — has a different on-disk layout (``bold{N}`` timeseries,
top-level EV dirs) and **cannot be reached by a path swap**; its loader is implemented
separately in ``datasets.py``, which wraps these A helpers behind a common A/B
interface. Choosing A vs B is an open team decision (see
``03_dataset_comparison.ipynb``).

The companion notebooks (``00`` framing, ``01`` ingestion + EV, ``02`` EDA) are
executed against the real dataset and embed their outputs; scientific
interpretation and the final hand-off remain team decisions.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

# --------------------------------------------------------------------------- #
# Constants (from the official loader)
# --------------------------------------------------------------------------- #
N_SUBJECTS: int = 100
N_PARCELS: int = 360
TR: float = 0.72  # seconds per frame
RUNS: tuple[str, str] = ("LR", "RL")

#: The 8 WM conditions = 2 load levels x 4 stimulus categories.
COND_0BACK: tuple[str, ...] = ("0bk_body", "0bk_faces", "0bk_places", "0bk_tools")
COND_2BACK: tuple[str, ...] = ("2bk_body", "2bk_faces", "2bk_places", "2bk_tools")

#: ``Stats.txt`` labels the body category "BP" (Body Parts), not "body".
STATS_CATEGORIES: tuple[str, ...] = ("BP", "Faces", "Places", "Tools")

#: ``regions.npy`` stores network labels truncated to 12 characters. This maps each
#: truncated form back to the full published name (12-network Cole-Anticevic partition,
#: Ji et al. 2019). The mapping keys were read directly from the dataset's own
#: ``regions.npy`` (via ``np.unique`` on the network column); the values are the
#: corresponding full names the official loader notebook attributes to Ji (2019).
#: Matching on the full name without this mapping would silently drop rows.
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


def get_subjects(hcp_dir: str | Path) -> list[str]:
    """Return the list of subject IDs shipped with the dataset."""
    return np.loadtxt(Path(hcp_dir) / "subjects_list.txt", dtype="str").tolist()


# --------------------------------------------------------------------------- #
# 1. Time series
# --------------------------------------------------------------------------- #
def load_single_timeseries(
    hcp_dir: str | Path, subject: str, experiment: str, run: int,
    remove_mean: bool = True,
) -> np.ndarray:
    """Load the parcellated BOLD time series for one subject/experiment/run.

    Reimplements the official NMA loader's ``load_single_timeseries`` (loader link
    in the module docstring); ``remove_mean`` is exposed here as an explicit flag.

    Args:
        hcp_dir: root of the extracted ``hcp_task`` folder.
        subject: subject ID (e.g. ``"100307"``).
        experiment: task name (``"WM"`` for us).
        run: 0 (LR) or 1 (RL).
        remove_mean: subtract each parcel's temporal mean (the mean BOLD level
            carries no task information and is standard to drop).

    Returns:
        Array ``(N_PARCELS, n_timepoints)`` of BOLD values.
    """
    path = Path(hcp_dir) / "subjects" / subject / experiment / f"tfMRI_{experiment}_{RUNS[run]}" / "data.npy"
    ts = np.load(path)
    if remove_mean:
        ts = ts - ts.mean(axis=1, keepdims=True)
    return ts


# --------------------------------------------------------------------------- #
# 2. EV segmentation
# --------------------------------------------------------------------------- #
def load_condition_frames(hcp_dir: str | Path, subject: str, run: int, level: str) -> np.ndarray:
    """Frame indices belonging to a load level in one run.

    Reimplements the official loader's ``load_evs``: reads the EV ``.txt`` files
    for the 4 stimulus categories of ``level`` and converts each trial's
    (onset, duration) from seconds to frame indices via ``TR`` (``floor`` the
    onset, ``ceil`` the duration), then pools and de-duplicates them.

    Args:
        level: ``"0back"`` or ``"2back"``.

    Returns:
        Sorted, unique array of frame indices for that condition.
    """
    conditions = COND_0BACK if level == "0back" else COND_2BACK
    frames: list[np.ndarray] = []
    for cond in conditions:
        ev_path = Path(hcp_dir) / "subjects" / subject / "WM" / f"tfMRI_WM_{RUNS[run]}" / "EVs" / f"{cond}.txt"
        ev = np.loadtxt(ev_path, ndmin=2)  # rows: (onset, duration, amplitude)
        for onset, duration, _amplitude in ev:
            start = int(np.floor(onset / TR))
            n_frames = int(np.ceil(duration / TR))
            frames.append(np.arange(start, start + n_frames))
    return np.unique(np.concatenate(frames))


def load_condition_timeseries(
    hcp_dir: str | Path, subject: str, level: str, concat_runs: bool = True,
) -> np.ndarray:
    """BOLD time series for one subject restricted to a load level.

    Args:
        level: ``"0back"`` or ``"2back"``.
        concat_runs: concatenate LR+RL along time (doubling the frames available
            for later analysis). If False, only run LR.

    Returns:
        Array ``(N_PARCELS, n_frames)`` — the input step 3 (functional
        connectivity) consumes to build one FC matrix per condition.
    """
    mats: list[np.ndarray] = []
    for run in ([0, 1] if concat_runs else [0]):
        ts = load_single_timeseries(hcp_dir, subject, "WM", run)
        frames = load_condition_frames(hcp_dir, subject, run, level)
        frames = frames[frames < ts.shape[1]]  # guard against rounding past scan end
        mats.append(ts[:, frames])
    return np.concatenate(mats, axis=1)


# --------------------------------------------------------------------------- #
# 3. Behaviour (prediction target)
# --------------------------------------------------------------------------- #
def parse_stats(hcp_dir: str | Path, subject: str, run: int) -> dict[str, float]:
    """Parse one ``Stats.txt`` into a ``{label: value}`` dict.

    The official loaders ship no behaviour reader; ``Stats.txt`` is the per-run
    behavioural summary documented in the loader's folder layout (lines such as
    ``"2-Back Faces Median ACC: 0.9"``). This parser is ours.
    """
    path = Path(hcp_dir) / "subjects" / subject / "WM" / f"tfMRI_WM_{RUNS[run]}" / "EVs" / "Stats.txt"
    out: dict[str, float] = {}
    for line in path.read_text().splitlines():
        if ":" in line:
            key, value = line.rsplit(":", 1)
            try:
                out[key.strip()] = float(value)
            except ValueError:
                pass
    return out


def _mean_metric(run_stats: list[dict[str, float]], load: str, metric: str) -> float:
    """Average one metric (``"Median ACC"`` or ``"Median RT"``) for one load level.

    Averages across the 4 stimulus categories (BP/Faces/Places/Tools) and both
    runs. ``load`` is the ``Stats.txt`` prefix, ``"0-Back"`` or ``"2-Back"``.
    """
    values: list[float] = []
    for stats in run_stats:
        for category in STATS_CATEGORIES:
            values.append(stats[f"{load} {category} {metric}"])
    return float(np.mean(values))


def load_behaviour(hcp_dir: str | Path, subject: str) -> dict[str, float]:
    """Per-subject WM performance, averaged over the 4 categories and both runs.

    Keys returned:
        ``acc_0bk`` / ``acc_2bk``  — mean accuracy at each load
        ``acc_cost``               — acc_2bk - acc_0bk (load cost; < 0 = worse under load)
        ``rt_0bk`` / ``rt_2bk``    — mean median reaction time (ms) at each load
        ``rt_cost``                — rt_2bk - rt_0bk

    ``acc_2bk`` is the recommended target: 0.54-0.99 spread, no missing values, and
    its pooled global accuracy matches correct/(correct+error) from the EV files
    exactly (200/200 runs).

    No signal-detection d' is provided for this dataset: the ``Stats.txt`` Target /
    Non-Target accuracies are internally inconsistent (378/800 = 47% of 2-back
    records have the global accuracy outside [Target, Non-Target], impossible for
    coherent rates — the documented HCP WM accuracy bug). The 339-subject
    ``wm.csv`` passes this invariant, so d' must be derived there if needed.
    """
    run_stats = [parse_stats(hcp_dir, subject, run) for run in (0, 1)]

    acc_0bk = _mean_metric(run_stats, "0-Back", "Median ACC")
    acc_2bk = _mean_metric(run_stats, "2-Back", "Median ACC")
    rt_0bk = _mean_metric(run_stats, "0-Back", "Median RT")
    rt_2bk = _mean_metric(run_stats, "2-Back", "Median RT")

    return {
        "acc_0bk": acc_0bk,
        "acc_2bk": acc_2bk,
        "acc_cost": acc_2bk - acc_0bk,
        "rt_0bk": rt_0bk,
        "rt_2bk": rt_2bk,
        "rt_cost": rt_2bk - rt_0bk,
    }


def behaviour_table(hcp_dir: str | Path, subjects: list[str]) -> pd.DataFrame:
    """Behaviour scores for every subject as a tidy DataFrame."""
    return pd.DataFrame([{"subject": s, **load_behaviour(hcp_dir, s)} for s in subjects])


# --------------------------------------------------------------------------- #
# 4. Region table
# --------------------------------------------------------------------------- #
def build_region_table(hcp_dir: str | Path) -> pd.DataFrame:
    """ROI -> full network name -> hemisphere, for all 360 parcels.

    Reads the same ``regions.npy`` the official loader uses; we additionally
    de-truncate the network labels (see ``NETWORK_FULL``). Columns:
    ``roi_index, name, network_raw, network, hemi`` — ``network`` holds the full
    Cole-Anticevic name and ``network_raw`` the 12-char form for traceability.
    """
    regions = np.load(Path(hcp_dir) / "regions.npy").T
    table = pd.DataFrame({
        "roi_index": range(N_PARCELS),
        "name": regions[0],
        "network_raw": regions[1],
        "hemi": ["Right"] * (N_PARCELS // 2) + ["Left"] * (N_PARCELS // 2),
    })
    table["network"] = table["network_raw"].map(NETWORK_FULL)
    missing = table["network"].isna()
    if missing.any():
        raise ValueError(f"unmapped network label(s): {table.loc[missing, 'network_raw'].unique()}")
    return table


# --------------------------------------------------------------------------- #
# 5. Anti-leakage subject-level split
# --------------------------------------------------------------------------- #
def make_split(subjects: list[str], seed: int = 42, test_frac: float = 0.2, cv_folds: int = 5) -> dict:
    """Build an exploratory subject-level train/test split + development folds.

    The split is by SUBJECT (never by timepoint/run), so no subject appears in
    both train and test. Rationale: NMA's project guidance treats prediction on
    held-out subjects as the gold standard and warns to always split by the unit
    of generalization (here the subject) to avoid leakage.

    Returns a dict ready to serialise to ``artifacts_staging/splits.json``:
        ``{seed, test_frac, cv_folds, n_train, n_test, train, test, cv}``
    where ``cv`` is a list of ``{fold, val}`` and the union of the validation
    folds equals the training set exactly.
    """
    rng = np.random.default_rng(seed)
    ids = np.array(sorted(subjects))
    rng.shuffle(ids)
    n_test = int(round(len(ids) * test_frac))
    test = sorted(ids[:n_test].tolist())
    train = sorted(ids[n_test:].tolist())

    train_shuffled = np.array(train.copy())
    rng.shuffle(train_shuffled)
    folds = [sorted(f.tolist()) for f in np.array_split(train_shuffled, cv_folds)]
    cv = [{"fold": i, "val": folds[i]} for i in range(cv_folds)]

    split = {
        "seed": seed, "test_frac": test_frac, "cv_folds": cv_folds,
        "n_train": len(train), "n_test": len(test),
        "train": train, "test": test, "cv": cv,
    }
    _validate_split(split)
    return split


def _validate_split(split: dict) -> None:
    """Fail loudly if the split could leak or is malformed."""
    train, test = set(split["train"]), set(split["test"])
    assert train.isdisjoint(test), "leak: a subject is in both train and test"
    assert len(train) + len(test) == N_SUBJECTS, "train+test must cover all subjects"
    val_union = sorted(s for f in split["cv"] for s in f["val"])
    assert val_union == sorted(split["train"]), "CV validation folds must partition the train set exactly"


def save_split(split: dict, path: str | Path) -> None:
    """Serialise a split dict to a local JSON staging file."""
    Path(path).write_text(json.dumps(split, indent=2))


def load_split(path: str | Path) -> dict:
    """Load and validate an exploratory subject-level split from ``splits.json``.

    ``make_split`` builds the sandbox candidate and this function reads it back.
    A shared split is not part of the public scaffold until the group reviews it.

    Returns:
        The split dict ``{seed, test_frac, cv_folds, n_train, n_test, train, test, cv}``,
        re-validated on load so a corrupted or hand-edited file fails loudly.
    """
    split = json.loads(Path(path).read_text())
    _validate_split(split)
    return split
