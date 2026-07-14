"""Split + QC for the HCP working-memory finalists (Jaime's sandbox).

**Category: evaluation setup + quality control.** :func:`make_split` builds the leakage-safe
subject-level train/test + CV split; :func:`validate_dataset` produces the aggregate QC the
A/B decision rests on. Downstream of :mod:`datasets` + :mod:`preprocessing`.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

import datasets as ds
import preprocessing as pp


# --------------------------------------------------------------------------- #
# Subject-level split (leakage-safe)
# --------------------------------------------------------------------------- #
def make_split(spec: ds.DatasetSpec, seed: int = 42, test_frac: float = 0.2,
               cv_folds: int = 5) -> dict:
    """Subject-level train/test + CV split over a dataset's analytic cohort — ours, N-agnostic.

    Split by SUBJECT (never timepoint/run) so none appears in both sets; prediction on
    held-out subjects is NMA's project-guidance gold standard and the leakage-safe unit of
    generalization. Works for A (100) or B (336). Returns ``{seed, test_frac, cv_folds,
    n_total, n_train, n_test, train, test, cv}``; the CV validation folds partition ``train``
    exactly.
    """
    rng = np.random.default_rng(seed)
    ids = np.array(sorted(ds.load_subjects(spec)))
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
        "n_total": len(ids), "n_train": len(train), "n_test": len(test),
        "train": train, "test": test, "cv": cv,
    }
    _validate_split(split)
    return split


def _validate_split(split: dict) -> None:
    """Fail loudly if the split could leak or is malformed.

    Explicit raises, not ``assert``: this is the module's core leakage guarantee and must
    survive ``python -O`` (which strips asserts).
    """
    train, test = set(split["train"]), set(split["test"])
    if not train.isdisjoint(test):
        raise ValueError("leak: a subject is in both train and test")
    n_total = split.get("n_total", len(train) + len(test))  # N-agnostic: A (100) or B (336)
    if len(train) + len(test) != n_total:
        raise ValueError("train+test must cover all subjects")
    val_union = sorted(s for f in split["cv"] for s in f["val"])
    if val_union != sorted(split["train"]):
        raise ValueError("CV validation folds must partition the train set exactly")


def save_split(split: dict, path: str | Path) -> None:
    """Serialise a split dict to a local JSON staging file."""
    Path(path).write_text(json.dumps(split, indent=2))


def load_split(path: str | Path) -> dict:
    """Load and re-validate a subject-level split from ``splits.json``.

    Re-validated on load, so a corrupted or hand-edited file fails loudly.
    """
    split = json.loads(Path(path).read_text())
    _validate_split(split)
    return split


# --------------------------------------------------------------------------- #
# Aggregate QC (the evidence the A/B decision rests on)
# --------------------------------------------------------------------------- #
def validate_dataset(spec: ds.DatasetSpec) -> dict:
    """Aggregate QC for one dataset, probing a single representative subject for shapes.

    Returns a flat dict (easy to tabulate side by side) covering subject counts, WM run
    shape, frames per load, condition overlap, ROI/network counts, resting-state
    availability and behavioural spread/missingness. No subject identifiers are returned.
    """
    all_subjects = ds.load_subjects(spec, require_behaviour=False)
    analytic = ds.load_subjects(spec, require_behaviour=True)
    probe = analytic[0]

    ts_shape = ds.load_timeseries(spec, probe, run=0).shape
    frames_0 = pp.condition_frames(spec, probe, run=0, level="0back")
    frames_2 = pp.condition_frames(spec, probe, run=0, level="2back")
    concat_0 = pp.condition_timeseries(spec, probe, "0back").shape[1]
    concat_2 = pp.condition_timeseries(spec, probe, "2back").shape[1]

    regions = pp.region_table(spec)
    beh = pp.behaviour_table(spec)
    acc2 = beh["acc_2bk"].dropna()

    rest_files = ds.list_rest_runs(spec, probe)
    rest_runs = len(rest_files)
    rest_shape = ds.load_rest_timeseries(spec, probe).shape if rest_files else None

    return {
        "dataset": spec.name,
        "loader": spec.loader,
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
