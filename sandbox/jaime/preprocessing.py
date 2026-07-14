"""Preprocessing: raw HCP loads -> analysis-ready objects (Jaime's sandbox).

**Category: preprocessing.** Turns the raw reads from :mod:`datasets` into the objects the
FC and behaviour steps consume: condition-restricted BOLD, per-subject behaviour and
signal-detection tables, and the ROI -> network table. Downstream of :mod:`datasets`,
upstream of :mod:`evaluation`.

Not here on purpose: the actual **processing / modelling** (functional connectivity, graph
metrics, prediction) is the team's downstream work, not part of this data layer.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

import datasets as ds


# --------------------------------------------------------------------------- #
# EV segmentation
# --------------------------------------------------------------------------- #
def condition_frames(spec: ds.DatasetSpec, subject: str, run: int, level: str) -> np.ndarray:
    """Sorted, unique frame indices for a load level in one run.

    Reimplements the official loader's ``load_evs``: pools the 4 stimulus categories of
    ``level``; onset/duration -> frames via ``floor(onset/TR)`` / ``ceil(duration/TR)``. A
    reads EVs inside ``WM/tfMRI_WM_{run}/EVs``; B reads ``EVs/tfMRI_WM_{['RL','LR'][run]}``.

    Args:
        level: ``"0back"`` or ``"2back"``.
    """
    conditions = ds.COND_0BACK if level == "0back" else ds.COND_2BACK
    if spec.kind == "A":
        ev_dir = (spec.task_dir / "subjects" / subject / "WM"
                  / f"tfMRI_WM_{ds.RUN_LABELS['A'][run]}" / "EVs")
    else:
        ev_dir = (spec.task_dir / "subjects" / subject / "EVs"
                  / f"tfMRI_WM_{ds.RUN_LABELS['B'][run]}")
    frames: list[np.ndarray] = []
    for cond in conditions:
        ev = np.loadtxt(ev_dir / f"{cond}.txt", ndmin=2)  # (onset, duration, amplitude)
        for onset, duration, _amp in ev:
            start = int(np.floor(onset / ds.TR))
            n_frames = int(np.ceil(duration / ds.TR))
            frames.append(np.arange(start, start + n_frames))
    return np.unique(np.concatenate(frames))


def condition_timeseries(spec: ds.DatasetSpec, subject: str, level: str,
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
        ts = ds.load_timeseries(spec, subject, run)
        frames = condition_frames(spec, subject, run, level)
        frames = frames[frames < ts.shape[1]]  # guard against rounding past scan end
        mats.append(ts[:, frames])
    return np.concatenate(mats, axis=1)


def run_label(spec: ds.DatasetSpec, run: int) -> str:
    """Phase-encoding direction (``"LR"``/``"RL"``) of an acquisition run.

    A run 0 is LR; B run 0 is RL — the datasets order the runs oppositely.
    """
    return ds.RUN_LABELS[spec.kind][run]


# --------------------------------------------------------------------------- #
# Behaviour (prediction target)
# --------------------------------------------------------------------------- #
def _parse_stats(spec: ds.DatasetSpec, subject: str, run: int) -> dict[str, float]:
    """Parse one Finalist-A ``Stats.txt`` into a ``{label: value}`` dict.

    Ours — the official loaders ship no behaviour reader. Per-run summary; lines such as
    ``"2-Back Faces Median ACC: 0.9"``.
    """
    path = (spec.task_dir / "subjects" / subject / "WM"
            / f"tfMRI_WM_{ds.RUN_LABELS['A'][run]}" / "EVs" / "Stats.txt")
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
    """Average one Finalist-A metric across the 4 stimulus categories and both runs.

    Args:
        load: ``Stats.txt`` prefix, ``"0-Back"`` or ``"2-Back"``.
        metric: ``"Median ACC"`` or ``"Median RT"``.
    """
    values: list[float] = []
    for stats in run_stats:
        for category in ds.STATS_CATEGORIES:
            values.append(stats[f"{load} {category} {metric}"])
    return float(np.mean(values))


def _behaviour_a(spec: ds.DatasetSpec) -> pd.DataFrame:
    """Finalist-A behaviour table, parsed and aggregated from per-subject ``Stats.txt``."""
    rows: list[dict[str, float]] = []
    for subject in ds.list_subjects(spec):
        run_stats = [_parse_stats(spec, subject, run) for run in (0, 1)]
        acc_0bk = _mean_metric(run_stats, "0-Back", "Median ACC")
        acc_2bk = _mean_metric(run_stats, "2-Back", "Median ACC")
        rt_0bk = _mean_metric(run_stats, "0-Back", "Median RT")
        rt_2bk = _mean_metric(run_stats, "2-Back", "Median RT")
        rows.append({
            "subject": subject,
            "acc_0bk": acc_0bk, "acc_2bk": acc_2bk, "acc_cost": acc_2bk - acc_0bk,
            "rt_0bk": rt_0bk, "rt_2bk": rt_2bk, "rt_cost": rt_2bk - rt_0bk,
        })
    return pd.DataFrame(rows)


def behaviour_table(spec: ds.DatasetSpec) -> pd.DataFrame:
    """Per-subject WM performance with a shared schema for A and B.

    Columns: ``subject, acc_0bk, acc_2bk, acc_cost, rt_0bk, rt_2bk, rt_cost``. Accuracy is
    a 0-1 rate; RT is the median in ms. Both datasets average over the 4 stimulus
    categories and both runs. A parses per-subject ``Stats.txt``; B reads the consolidated
    ``wm.csv``, where subjects without 2-back rows carry ``NaN`` in the 2-back columns
    (kept here; filtered by :func:`datasets.list_subjects`). ``acc_2bk`` is the recommended
    target: A's ``Stats.txt`` Target/Non-Target fields are inconsistent (HCP WM bug), so no
    d' for A — see :func:`signal_detection_table`.
    """
    if spec.kind == "A":
        return _behaviour_a(spec)

    wm = pd.read_csv(spec.behaviour)
    wm["load"] = wm["ConditionName"].str[:3]  # "0BK" / "2BK"
    subjects = sorted(wm["Subject"].unique())
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


def signal_detection_table(spec: ds.DatasetSpec) -> pd.DataFrame:
    """Per-subject hit / false-alarm rates for 0-back and 2-back — the inputs a d' needs.

    Ours, B-only, from ``wm.csv``: ``hit = ACC_TARGET``, ``fa = 1 - ACC_NONTARGET``,
    averaged over the 4 categories and both runs. Does **not** compute d' — the extreme-rate
    correction (e.g. loglinear) is a prespecified team choice. A raises: its ``Stats.txt``
    Target/Non-Target accuracies are internally inconsistent (the documented HCP WM bug).

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
def region_table(spec: ds.DatasetSpec) -> pd.DataFrame:
    """ROI -> network -> hemisphere for all 360 parcels.

    Reads the official ``regions.npy`` (same for A and B); our addition is de-truncating the
    12-char network labels via ``NETWORK_FULL``. Columns: ``roi_index, name, network_raw,
    network, hemi``.
    """
    regions = np.load(spec.task_dir / "regions.npy").T
    table = pd.DataFrame({
        "roi_index": range(ds.N_PARCELS),
        "name": regions[0],
        "network_raw": regions[1],
        "hemi": ["Right"] * (ds.N_PARCELS // 2) + ["Left"] * (ds.N_PARCELS // 2),
    })
    table["network"] = table["network_raw"].map(ds.NETWORK_FULL)
    missing = table["network"].isna()
    if missing.any():
        raise ValueError(f"unmapped network label(s): {table.loc[missing, 'network_raw'].unique()}")
    return table
