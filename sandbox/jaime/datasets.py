"""Common A/B loader for the HCP working-memory finalists (Jaime's sandbox).

Purpose
-------
Give the two candidate datasets **one shared output schema** so the team can compare
them on equal footing and pick one. This module does not choose; it makes the choice
auditable (see ``03_dataset_comparison.ipynb``).

- **Finalist A** — ``load_hcp_task_with_behaviour``: 100 subjects, task only, per-subject
  ``Stats.txt``. Its loaders already live in :mod:`ingestion`; this module **reuses them
  unchanged** (A stays byte-for-byte identical to the earlier notebooks).
- **Finalist B** — ``load_hcp_task``: 339 subjects, adds real resting-state and a
  consolidated ``wm.csv``. Its WM ingestion did not exist yet; it is implemented here.

Every public function takes a :class:`DatasetSpec` and returns the same objects for A and
B: condition-restricted BOLD (``360 x n_frames``), a tidy behaviour table, the ROI table
and an aggregate QC dict.

Finalist B specifics (verified against the official ``load_hcp_task.ipynb`` and the data)
----------------------------------------------------------------------------------------
- Timeseries live in ``subjects/<id>/timeseries/bold{N}_Atlas_MSMAll_Glasser360Cortical.npy``.
  The official ``EXPERIMENTS['WM']['runs'] == [7, 8]`` maps the two WM runs to **bold7 and
  bold8**. The loader pairs run index 0 with the ``tfMRI_WM_RL`` EVs and run 1 with
  ``tfMRI_WM_LR`` (``['RL', 'LR'][run]``) -> **bold7 = WM-RL, bold8 = WM-LR**. This is the
  reverse of A, where run 0 is LR; the asymmetry is kept so each series is segmented with
  its own EVs.
- Behaviour is the consolidated ``hcp/behavior/wm.csv`` (``Subject`` = 0..338, matching the
  on-disk integer IDs), not per-subject ``Stats.txt``. 336 of 339 subjects have complete
  2-back behaviour; subjects 81, 143 and 329 lack it and are dropped from the analytic set.
- ``regions.npy`` is structurally identical to A (same 12 truncated Cole-Anticevic labels),
  so :func:`ingestion.build_region_table` applies to both.

Scope
-----
This ends at delivering condition-restricted signals, behaviour, ROI table and QC for
either dataset. Functional connectivity, graph metrics, target choice (``acc_2bk`` vs a
future ``d'``) and prediction remain downstream team decisions.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

import ingestion as ing

#: Run index -> phase-encoding direction. A and B disagree on which run is index 0.
RUN_LABELS: dict[str, tuple[str, str]] = {"A": ("LR", "RL"), "B": ("RL", "LR")}

#: Finalist B: run index -> ``bold{N}`` file number for the WM task (official EXPERIMENTS).
B_WM_BOLD: tuple[int, int] = (7, 8)

#: Subjects present in B's task folder but without complete 2-back behaviour in ``wm.csv``.
B_INCOMPLETE_SUBJECTS: tuple[str, ...] = ("81", "143", "329")


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
    root = Path(data_dir)
    task = root / "hcp_task"
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
# Subjects
# --------------------------------------------------------------------------- #
def list_subjects(spec: DatasetSpec, require_behaviour: bool = True) -> list[str]:
    """Analytic subject IDs (as strings) for a dataset.

    Args:
        require_behaviour: if True, drop subjects without a usable 2-back score
            (A: all 100 qualify; B: 336 of 339, excluding 81/143/329).
    """
    if spec.kind == "A":
        return ing.get_subjects(spec.task_dir)
    ids = sorted((p.name for p in (spec.task_dir / "subjects").iterdir() if p.is_dir()),
                 key=int)
    if require_behaviour:
        ids = [s for s in ids if s not in B_INCOMPLETE_SUBJECTS]
    return ids


# --------------------------------------------------------------------------- #
# Timeseries + EV segmentation
# --------------------------------------------------------------------------- #
def _b_timeseries_path(spec: DatasetSpec, subject: str, run: int) -> Path:
    bold = B_WM_BOLD[run]
    return (spec.task_dir / "subjects" / subject / "timeseries"
            / f"bold{bold}_Atlas_MSMAll_Glasser360Cortical.npy")


def load_single_timeseries(spec: DatasetSpec, subject: str, run: int,
                           remove_mean: bool = True) -> np.ndarray:
    """One WM run as ``(N_PARCELS, n_timepoints)``. ``run`` is 0 or 1.

    A delegates to :mod:`ingestion`; B reimplements the official ``load_hcp_task``
    bold-file loading (WM = ``bold7``/``bold8``).
    """
    if spec.kind == "A":
        return ing.load_single_timeseries(spec.task_dir, subject, "WM", run, remove_mean)
    ts = np.load(_b_timeseries_path(spec, subject, run))
    if remove_mean:
        ts = ts - ts.mean(axis=1, keepdims=True)
    return ts


def load_condition_frames(spec: DatasetSpec, subject: str, run: int, level: str) -> np.ndarray:
    """Sorted unique frame indices for a load level in one run (``"0back"``/``"2back"``).

    A delegates to :mod:`ingestion`; B reimplements the official ``load_evs``
    (run -> ``tfMRI_WM_{['RL','LR'][run]}``).
    """
    if spec.kind == "A":
        return ing.load_condition_frames(spec.task_dir, subject, run, level)
    conditions = ing.COND_0BACK if level == "0back" else ing.COND_2BACK
    ev_dir = (spec.task_dir / "subjects" / subject / "EVs"
              / f"tfMRI_WM_{RUN_LABELS['B'][run]}")
    frames: list[np.ndarray] = []
    for cond in conditions:
        ev = np.loadtxt(ev_dir / f"{cond}.txt", ndmin=2)  # (onset, duration, amplitude)
        for onset, duration, _amp in ev:
            start = int(np.floor(onset / ing.TR))
            n_frames = int(np.ceil(duration / ing.TR))
            frames.append(np.arange(start, start + n_frames))
    return np.unique(np.concatenate(frames))


def load_condition_timeseries(spec: DatasetSpec, subject: str, level: str,
                              runs: tuple[int, ...] = (0, 1)) -> np.ndarray:
    """BOLD restricted to one load level, ``(N_PARCELS, n_frames)``.

    The object step 3 (functional connectivity) consumes, one FC matrix per condition.

    Args:
        runs: acquisition runs to include, concatenated along time. Default ``(0, 1)``
            gives 312 frames; pass ``(0,)`` or ``(1,)`` for a single run (156 frames) —
            the per-run access an LR/RL reliability check needs. Direction: :func:`run_label`.
    """
    mats: list[np.ndarray] = []
    for run in runs:
        ts = load_single_timeseries(spec, subject, run)
        frames = load_condition_frames(spec, subject, run, level)
        frames = frames[frames < ts.shape[1]]  # guard against rounding past scan end
        mats.append(ts[:, frames])
    return np.concatenate(mats, axis=1)


def run_label(spec: DatasetSpec, run: int) -> str:
    """Phase-encoding direction (``"LR"``/``"RL"``) of an acquisition run.

    A run 0 is LR; B run 0 is RL — the datasets order the runs oppositely.
    """
    return RUN_LABELS[spec.kind][run]


# --------------------------------------------------------------------------- #
# Behaviour (prediction target)
# --------------------------------------------------------------------------- #
def load_behaviour_table(spec: DatasetSpec) -> pd.DataFrame:
    """Per-subject WM performance with a shared schema for A and B.

    Columns: ``subject, acc_0bk, acc_2bk, acc_cost, rt_0bk, rt_2bk, rt_cost``. Accuracy is
    a 0-1 rate; RT is the median in ms. Both datasets average over the 4 stimulus
    categories and both runs. For B, subjects without 2-back rows carry ``NaN`` in the
    2-back columns (kept here; filtered by :func:`list_subjects`).
    """
    if spec.kind == "A":
        return ing.behaviour_table(spec.task_dir, ing.get_subjects(spec.task_dir))

    wm = pd.read_csv(spec.behaviour)
    wm["load"] = wm["ConditionName"].str[:3]  # "0BK" / "2BK"
    subjects = sorted(wm["Subject"].unique())
    # reindex to a common subject list so incomplete subjects (missing 2-back) stay
    # aligned as NaN instead of shortening one column.
    acc = (wm.pivot_table(index="Subject", columns="load", values="ACC", aggfunc="mean")
             .reindex(index=subjects, columns=["0BK", "2BK"]))
    rt = (wm.pivot_table(index="Subject", columns="load", values="MEDIAN_RT", aggfunc="mean")
            .reindex(index=subjects, columns=["0BK", "2BK"]))
    out = pd.DataFrame({
        "subject": [str(s) for s in subjects],
        "acc_0bk": acc["0BK"].to_numpy(),
        "acc_2bk": acc["2BK"].to_numpy(),
        "rt_0bk": rt["0BK"].to_numpy(),
        "rt_2bk": rt["2BK"].to_numpy(),
    })
    out["acc_cost"] = out["acc_2bk"] - out["acc_0bk"]
    out["rt_cost"] = out["rt_2bk"] - out["rt_0bk"]
    return out[["subject", "acc_0bk", "acc_2bk", "acc_cost", "rt_0bk", "rt_2bk", "rt_cost"]]


def load_signal_detection_table(spec: DatasetSpec) -> pd.DataFrame:
    """Per-subject hit / false-alarm rates for 0-back and 2-back — the inputs a d' needs.

    Ours, B-only, from ``wm.csv``: ``hit = ACC_TARGET``, ``fa = 1 - ACC_NONTARGET``,
    averaged over the 4 categories and both runs. Does **not** compute d' — the
    extreme-rate correction (e.g. loglinear) is a prespecified team choice. A raises:
    its ``Stats.txt`` Target/Non-Target accuracies are internally inconsistent (the
    documented HCP WM bug), so signal detection is not defensible for A.

    Columns: ``subject, hit_0bk, fa_0bk, hit_2bk, fa_2bk``.
    """
    if spec.kind == "A":
        raise NotImplementedError(
            "Signal detection is B-only: A's Stats.txt Target/Non-Target accuracies are "
            "internally inconsistent (HCP WM bug). Use acc_2bk for A."
        )
    wm = pd.read_csv(spec.behaviour)
    wm["load"] = wm["ConditionName"].str[:3]  # "0BK" / "2BK"
    subjects = sorted(wm["Subject"].unique())
    hit = (wm.pivot_table(index="Subject", columns="load", values="ACC_TARGET", aggfunc="mean")
             .reindex(index=subjects, columns=["0BK", "2BK"]))
    cr = (wm.pivot_table(index="Subject", columns="load", values="ACC_NONTARGET", aggfunc="mean")
            .reindex(index=subjects, columns=["0BK", "2BK"]))
    return pd.DataFrame({
        "subject": [str(s) for s in subjects],
        "hit_0bk": hit["0BK"].to_numpy(),
        "fa_0bk": 1 - cr["0BK"].to_numpy(),
        "hit_2bk": hit["2BK"].to_numpy(),
        "fa_2bk": 1 - cr["2BK"].to_numpy(),
    })


# --------------------------------------------------------------------------- #
# Region table
# --------------------------------------------------------------------------- #
def build_region_table(spec: DatasetSpec) -> pd.DataFrame:
    """ROI -> full network name -> hemisphere. Both datasets ship the same ``regions.npy``."""
    return ing.build_region_table(spec.task_dir)


# --------------------------------------------------------------------------- #
# Subject-level split (leakage-safe)
# --------------------------------------------------------------------------- #
def make_split(spec: DatasetSpec, seed: int = 42, test_frac: float = 0.2,
               cv_folds: int = 5) -> dict:
    """Subject-level train/test + CV split over a dataset's analytic cohort — N-agnostic.

    Thin wrapper over :func:`ingestion.make_split` on :func:`list_subjects`, so the same
    leakage-safe split works for A (100) or B (336) without a hard-coded subject count.
    """
    return ing.make_split(list_subjects(spec), seed=seed, test_frac=test_frac, cv_folds=cv_folds)


# --------------------------------------------------------------------------- #
# Aggregate QC (the evidence the A/B decision rests on)
# --------------------------------------------------------------------------- #
def validate_dataset(spec: DatasetSpec) -> dict:
    """Aggregate QC for one dataset, probing a single representative subject for shapes.

    Returns a flat dict (easy to tabulate side by side) covering subject counts, WM run
    shape, frames per load, condition overlap, ROI/network counts, resting-state
    availability and behavioural spread/missingness. No subject identifiers are returned.
    """
    all_subjects = list_subjects(spec, require_behaviour=False)
    analytic = list_subjects(spec, require_behaviour=True)
    probe = analytic[0]

    ts_shape = load_single_timeseries(spec, probe, run=0).shape
    frames_0 = load_condition_frames(spec, probe, run=0, level="0back")
    frames_2 = load_condition_frames(spec, probe, run=0, level="2back")
    concat_0 = load_condition_timeseries(spec, probe, "0back").shape[1]
    concat_2 = load_condition_timeseries(spec, probe, "2back").shape[1]

    regions = build_region_table(spec)
    beh = load_behaviour_table(spec)
    acc2 = beh["acc_2bk"].dropna()

    rest_runs, rest_shape = 0, None
    if spec.rest_dir is not None:
        rest_probe = spec.rest_dir / "subjects" / probe / "timeseries"
        rest_files = sorted(rest_probe.glob("bold*.npy")) if rest_probe.exists() else []
        rest_runs = len(rest_files)
        if rest_files:
            rest_shape = np.load(rest_files[0]).shape

    return {
        "dataset": spec.name,
        "n_subjects_total": len(all_subjects),
        "n_subjects_analytic": len(analytic),
        "wm_run_shape": ts_shape,
        "frames_0back_per_run": len(frames_0),
        "frames_2back_per_run": len(frames_2),
        "frames_0back_concat": concat_0,
        "frames_2back_concat": concat_2,
        "cond_overlap": int(np.intersect1d(frames_0, frames_2).size),
        "n_parcels": len(regions),
        "n_networks": regions["network"].nunique(),
        "rest_runs_per_subject": rest_runs,
        "rest_run_shape": rest_shape,
        "acc_2bk_n": int(acc2.size),
        "acc_2bk_mean": round(float(acc2.mean()), 3),
        "acc_2bk_min": round(float(acc2.min()), 3),
        "acc_2bk_max": round(float(acc2.max()), 3),
        "behaviour_missing_2bk": int(beh["acc_2bk"].isna().sum()),
    }
