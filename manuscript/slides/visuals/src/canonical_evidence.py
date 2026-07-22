"""Execute and validate the canonical presentation evidence in memory."""

from __future__ import annotations

import argparse
import json
import os
from collections.abc import Mapping
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

import numpy as np
from sklearn.metrics import r2_score

ANALYTIC_CELLS = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22)

EXPECTED = {
    "n_b": 336,
    "n_a": 100,
    "n_rois": 360,
    "n_networks": 12,
    "n_fc_features": 78,
    "repeated_cv_r": 0.366,
    "repeated_cv_sd": 0.024,
    "holdout_r": 0.312,
    "holdout_n": 67,
    "seed42_r": 0.405,
    "primary_p": 1 / 1001,
    "transfer_r": 0.398,
    "transfer_ci_low": 0.25,
    "transfer_ci_high": 0.53,
    "transfer_train_n": 301,
    "transfer_test_n": 100,
    "shared_removed_n": 35,
    "segregation_0": 0.3271,
    "segregation_2": 0.3035,
    "segregation_delta": -0.0236,
    "segregation_p": 3.45e-05,
    "segregation_individual_r": -0.105,
    "segregation_individual_p": 0.054,
    "method_0back_r": 0.274,
    "method_reconfig_r": 0.366,
    "method_combined_r": 0.333,
    "method_activation_r": 0.600,
    "increment_reconfig_mean": 0.0344,
    "increment_reconfig_sd": 0.0225,
    "increment_fc_mean": -0.0030,
    "increment_fc_sd": 0.0065,
}

METHOD_KEYS = (
    "0-back FC (78)",
    "reconfig FC (78)",
    "0bk + reconfig (156)",
    "activation contrast (360)",
)

NETWORK_LABELS = {
    "Auditory": "Auditory",
    "Cingulo-Oper": "Cingulo-op.",
    "Default": "Default",
    "Dorsal-atten": "Dorsal attn.",
    "Frontopariet": "Frontoparietal",
    "Language": "Language",
    "Orbito-Affec": "Orbito-aff.",
    "Posterior-Mu": "Posterior multi.",
    "Somatomotor": "Somatomotor",
    "Ventral-Mult": "Ventral multi.",
    "Visual1": "Visual 1",
    "Visual2": "Visual 2",
}


@contextmanager
def _working_directory(path: Path) -> Iterator[None]:
    previous = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)


@contextmanager
def _temporary_environment(name: str, value: str) -> Iterator[None]:
    previous = os.environ.get(name)
    os.environ[name] = value
    try:
        yield
    finally:
        if previous is None:
            os.environ.pop(name, None)
        else:
            os.environ[name] = previous


def execute_canonical(notebook: Path, n_perm: int = 1000) -> dict[str, object]:
    """Execute the canonical notebook's analytical cells in one namespace."""
    notebook = notebook.resolve()
    document = json.loads(notebook.read_text(encoding="utf-8"))
    repository = notebook.parents[1]
    namespace: dict[str, object] = {"__name__": "__slide_visuals__"}
    with (
        _working_directory(repository),
        _temporary_environment("GAMMAS_NPERM", str(n_perm)),
        _temporary_environment("MPLBACKEND", "Agg"),
    ):
        for index in ANALYTIC_CELLS:
            source = "".join(document["cells"][index]["source"])
            exec(
                compile(source, f"{notebook}:cell-{index}", "exec"),
                namespace,
            )
    return namespace


def canonical_metrics(namespace: Mapping[str, object]) -> dict[str, float | int]:
    """Extract presentation metrics from the canonical notebook namespace."""
    feat_b = namespace["featB"]
    feat_a = namespace["featA"]
    reconfig = np.asarray(namespace["reconfig"])
    activation = np.asarray(namespace["act_contrast"])
    methods = namespace["r_methods"]
    ci_ext = np.asarray(namespace["ci_ext"])
    seg0 = np.asarray(namespace["seg0"])
    seg2 = np.asarray(namespace["seg2"])
    dseg = np.asarray(namespace["dseg"])
    return {
        "n_b": int(feat_b["n"]),
        "n_a": int(feat_a["n"]),
        "n_rois": int(activation.shape[1]),
        "n_networks": int(np.unique(feat_b["net"]).size),
        "n_fc_features": int(reconfig.shape[1]),
        "repeated_cv_r": float(namespace["r_recon_mean"]),
        "repeated_cv_sd": float(namespace["r_recon_sd"]),
        "holdout_r": float(namespace["r_heldout"]),
        "holdout_n": len(namespace["te_idx"]),
        "seed42_r": float(namespace["r_seed42"]),
        "primary_p": float(namespace["p_recon"]),
        "transfer_r": float(namespace["r_ext"]),
        "transfer_ci_low": float(ci_ext[0]),
        "transfer_ci_high": float(ci_ext[1]),
        "transfer_train_n": len(namespace["b_only_idx"]),
        "transfer_test_n": len(namespace["yA"]),
        "shared_removed_n": len(namespace["shared"]),
        "segregation_0": float(seg0.mean()),
        "segregation_2": float(seg2.mean()),
        "segregation_delta": float(dseg.mean()),
        "segregation_p": float(namespace["p_seg"]),
        "segregation_individual_r": float(namespace["r_dseg"]),
        "segregation_individual_p": float(namespace["p_dseg"]),
        "method_0back_r": float(methods[METHOD_KEYS[0]][0]),
        "method_reconfig_r": float(methods[METHOD_KEYS[1]][0]),
        "method_combined_r": float(methods[METHOD_KEYS[2]][0]),
        "method_activation_r": float(methods[METHOD_KEYS[3]][0]),
        "increment_reconfig_mean": float(namespace["d_recon"]),
        "increment_reconfig_sd": float(namespace["s_recon"]),
        "increment_fc_mean": float(namespace["d_fc"]),
        "increment_fc_sd": float(namespace["s_fc"]),
    }


def _tolerance(name: str) -> float:
    if name in {"n_b", "n_a", "n_rois", "n_networks", "n_fc_features",
                "holdout_n", "transfer_train_n", "transfer_test_n",
                "shared_removed_n"}:
        return 0.0
    if name in {"segregation_0", "segregation_2", "segregation_delta",
                "increment_reconfig_mean", "increment_reconfig_sd",
                "increment_fc_mean", "increment_fc_sd"}:
        return 0.00006
    if name in {"primary_p", "segregation_p"}:
        return 0.000006
    return 0.0006


def validate_canonical(namespace: Mapping[str, object]) -> dict[str, float | int]:
    """Assert that all presentation metrics match the approved evidence."""
    metrics = canonical_metrics(namespace)
    for name, expected in EXPECTED.items():
        observed = metrics[name]
        if name in {"transfer_ci_low", "transfer_ci_high"}:
            assert round(float(observed), 2) == expected, (
                f"{name} drifted at display precision: observed={observed!r}, "
                f"expected={expected!r}"
            )
            continue
        tolerance = _tolerance(name)
        difference = abs(float(observed) - float(expected))
        assert difference <= tolerance, (
            f"{name} drifted: observed={observed!r}, expected={expected!r}, "
            f"tolerance={tolerance}"
        )
    return metrics


def _network_blocks(matrix: np.ndarray, networks: np.ndarray) -> np.ndarray:
    societies = np.unique(networks)
    indices = [np.where(networks == society)[0] for society in societies]
    result = np.zeros((len(societies), len(societies)))
    for row, idx_row in enumerate(indices):
        for column, idx_column in enumerate(indices):
            block = matrix[np.ix_(idx_row, idx_column)]
            if row == column:
                triangle = np.triu_indices(len(idx_row), k=1)
                result[row, column] = block[triangle].mean()
            else:
                result[row, column] = block.mean()
    return result


def chart_bundle(namespace: Mapping[str, object]) -> dict[str, object]:
    """Collect identifier-free chart arrays after the evidence gate passes."""
    metrics = validate_canonical(namespace)
    feat_b = namespace["featB"]
    networks = np.asarray(feat_b["net"])
    societies = np.unique(networks)
    fc0_group = np.asarray(feat_b["FC0_group"])
    fc2_group = np.asarray(feat_b["FC2_group"])
    delta_fc = fc2_group - fc0_group
    network_0 = _network_blocks(fc0_group, networks)
    network_2 = _network_blocks(fc2_group, networks)
    network_delta = _network_blocks(delta_fc, networks)
    upper_mask = np.tril(np.ones_like(network_delta, dtype=bool), k=-1)
    network_unique = np.ma.masked_where(upper_mask, network_delta)
    assert network_unique.count() == 78

    off_diagonal = delta_fc.copy()
    np.fill_diagonal(off_diagonal, np.nan)
    roi_reconfiguration = np.nanmean(off_diagonal, axis=1)
    coords = np.load(namespace["B"].atlas, allow_pickle=True)["coords"]

    cv_predict = namespace["cv_predict"]
    pearsonr = namespace["pearsonr"]
    reconfig = np.asarray(namespace["reconfig"])
    y = np.asarray(namespace["y"])
    repeated_values = np.array(
        [pearsonr(cv_predict(reconfig, y, seed), y)[0] for seed in range(20)]
    )

    fp0 = np.asarray(namespace["fp0"])
    activation = np.asarray(namespace["act_contrast"])
    delta_reconfig = np.array([
        r2_score(y, cv_predict(np.hstack([fp0, reconfig]), y, seed))
        - r2_score(y, cv_predict(fp0, y, seed))
        for seed in range(20)
    ])
    delta_fc_over_activation = np.array([
        r2_score(y, cv_predict(np.hstack([reconfig, activation]), y, seed))
        - r2_score(y, cv_predict(activation, y, seed))
        for seed in range(20)
    ])

    method_values = namespace["r_methods"]
    method_means = np.array([method_values[name][0] for name in METHOD_KEYS])
    method_sds = np.array([method_values[name][1] for name in METHOD_KEYS])

    return {
        "metrics": metrics,
        "network_labels": [NETWORK_LABELS.get(str(name), str(name)) for name in societies],
        "network_0": network_0,
        "network_2": network_2,
        "network_delta": network_delta,
        "network_unique": network_unique,
        "fingerprint_delta_mean": reconfig.mean(axis=0),
        "coords": coords,
        "roi_reconfiguration": roi_reconfiguration,
        "shared_vmax": float(max(np.abs(network_delta).max(),
                                  np.abs(roi_reconfiguration).max())),
        "repeated_cv_values": repeated_values,
        "null_reconfiguration": np.asarray(namespace["null_recon"]),
        "holdout_observed": y[np.asarray(namespace["te_idx"], dtype=int)],
        "holdout_predicted": np.asarray(namespace["pred_heldout"]),
        "dprime_metrics": dict(namespace["res"]["reconfig_dprime"]),
        "transfer_observed": np.asarray(namespace["yA"]),
        "transfer_predicted": np.asarray(namespace["pred_A"]),
        "transfer_bootstrap": np.asarray(namespace["boot_ext"]),
        "segregation_0": np.asarray(namespace["seg0"]),
        "segregation_2": np.asarray(namespace["seg2"]),
        "segregation_delta": np.asarray(namespace["dseg"]),
        "accuracy_2back": y,
        "method_names": METHOD_KEYS,
        "method_means": method_means,
        "method_sds": method_sds,
        "cross_run_reconfig": float(namespace["xr_recon"]),
        "cross_run_activation": float(namespace["xr_act"]),
        "delta_reconfig": delta_reconfig,
        "delta_fc_over_activation": delta_fc_over_activation,
        "activation_metrics": dict(namespace["res"]["activation"]),
    }


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-only", action="store_true")
    parser.add_argument("--n-perm", type=int, default=1000)
    return parser.parse_args()


def main() -> None:
    """Run the canonical evidence gate from the command line."""
    args = _parse_args()
    visuals = Path(__file__).resolve().parents[1]
    notebook = visuals.parents[2] / "pipeline" / "02_canonical_analysis_and_slides.ipynb"
    namespace = execute_canonical(notebook, n_perm=args.n_perm)
    metrics = validate_canonical(namespace)
    print("canonical evidence PASS")
    for name, value in metrics.items():
        print(f"{name}: {value}")
    if not args.check_only:
        chart_bundle(namespace)
        print("chart bundle PASS")


if __name__ == "__main__":
    main()
