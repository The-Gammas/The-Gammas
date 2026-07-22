"""Generate the reusable evidence-first chart library for both storyboards."""

from __future__ import annotations

import argparse
import hashlib
import os
import pickle
import tempfile
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.figure import Figure
from nilearn import plotting
from PIL import Image

from artifact_qa import build_delivery_artifacts
from canonical_evidence import (
    canonical_metrics,
    chart_bundle,
    execute_canonical,
)
from visual_theme import COLORS, PNG_SIZE, configure_matplotlib

VISUALS = Path(__file__).resolve().parents[1]
REPOSITORY = VISUALS.parents[2]
NOTEBOOK = REPOSITORY / "pipeline" / "02_canonical_analysis_and_slides.ipynb"

QUESTION_MATRIX_KEYS = ("network_2", "network_0", "network_delta")
QUESTION_MATRIX_TITLES = ("2-back FC", "0-back FC", "2-back - 0-back")
QUESTION_OPERATORS = ("minus", "equals")
FEATURE_MATRIX_TITLES = (
    "0-back FC\n12x12 summary of 360x360",
    "2-back FC\n12x12 summary of 360x360",
)
FC_DIVERGING = LinearSegmentedColormap.from_list(
    "gammas_fc_diverging", [COLORS["fc"], "#FFFFFF", COLORS["taupe"]]
)


def metric_labels(namespace: Mapping[str, object]) -> dict[str, str]:
    """Format labels while keeping every statistical estimand distinct."""
    metrics = canonical_metrics(namespace)
    return {
        "repeated_cv": (
            f"r = {metrics['repeated_cv_r']:.3f} ± "
            f"{metrics['repeated_cv_sd']:.3f} split SD"
        ),
        "primary_null": (
            f"seed 42 r = {metrics['seed42_r']:.3f}; "
            "full-refit p = 1/1001"
        ),
        "transfer": (
            f"r = {metrics['transfer_r']:.3f}; bootstrap 95% CI "
            f"[{metrics['transfer_ci_low']:.2f}, {metrics['transfer_ci_high']:.2f}]"
        ),
    }


def _figure() -> Figure:
    configure_matplotlib()
    return plt.figure(figsize=(16, 9), constrained_layout=False)


def _header(
    fig: Figure,
    number: int,
    label: str,
    context: str | None = None,
) -> None:
    fig.text(
        0.055,
        0.935,
        f"FIGURE {number:02d}  ·  {label.upper()}",
        fontsize=14,
        fontweight=600,
        color=COLORS["brown"],
        va="top",
    )
    if context:
        fig.text(0.055, 0.892, context, fontsize=16, color=COLORS["ink"], va="top")
    fig.add_artist(
        plt.Line2D(
            [0.055, 0.945],
            [0.855, 0.855],
            transform=fig.transFigure,
            color=COLORS["pale_sand"],
            linewidth=2.0,
        )
    )


def _caveat(fig: Figure, text: str) -> None:
    fig.text(
        0.055,
        0.035,
        text,
        fontsize=13,
        color=COLORS["brown"],
        va="bottom",
    )


def _clean_axis(ax: Any, grid: str | None = None) -> None:
    ax.spines[["top", "right"]].set_visible(False)
    if grid:
        ax.grid(axis=grid, zorder=0)
    ax.set_axisbelow(True)


def _linear_trend(ax: Any, observed: np.ndarray, predicted: np.ndarray, color: str) -> None:
    slope, intercept = np.polyfit(observed, predicted, 1)
    grid = np.linspace(observed.min(), observed.max(), 100)
    ax.plot(grid, intercept + slope * grid, color=color, linewidth=3.0, zorder=3)


def render_master_01(bundle: Mapping[str, object], _: Path) -> Figure:
    """Show the two condition summaries and their signed difference."""
    fig = _figure()
    _header(fig, 1, "The predictive contrast", "Group-mean network FC; cohort B, n=336")
    grid = fig.add_gridspec(1, 3, left=0.055, right=0.94, bottom=0.12, top=0.81, wspace=0.18)
    matrices = [bundle[key] for key in QUESTION_MATRIX_KEYS]
    titles = QUESTION_MATRIX_TITLES
    limits = [
        max(np.abs(matrices[0]).max(), np.abs(matrices[1]).max()),
        max(np.abs(matrices[0]).max(), np.abs(matrices[1]).max()),
        np.abs(matrices[2]).max(),
    ]
    for index, (matrix, title, limit) in enumerate(zip(matrices, titles, limits)):
        ax = fig.add_subplot(grid[0, index])
        image = ax.imshow(matrix, cmap=FC_DIVERGING, vmin=-limit, vmax=limit)
        ax.set_title(title, pad=18)
        ax.set_xticks([])
        ax.set_yticks([])
        if index < 2:
            ax.text(
                1.03,
                0.5,
                r"$-$" if QUESTION_OPERATORS[index] == "minus" else "=",
                transform=ax.transAxes,
                fontsize=38,
                fontweight=600,
                color=COLORS["brown"],
                ha="center",
                va="center",
            )
        if index == 2:
            colorbar = fig.colorbar(image, ax=ax, fraction=0.05, pad=0.04)
            colorbar.set_label(r"Mean $\Delta$FC", fontsize=16)
            colorbar.ax.tick_params(labelsize=14)
    _caveat(fig, "Condition-aggregated Pearson FC difference; not dynamic or causal connectivity.")
    return fig



def render_master_04(bundle: Mapping[str, object], _: Path) -> Figure:
    """Trace real FC matrices into the 78-feature load difference."""
    fig = _figure()
    _header(fig, 2, "From regional FC to a 78-feature difference", "Actual cohort-B group summaries")
    grid = fig.add_gridspec(
        1,
        4,
        left=0.045,
        right=0.955,
        bottom=0.15,
        top=0.74,
        width_ratios=[1.05, 1.05, 1.0, 1.20],
        wspace=0.24,
    )
    fc0 = bundle["network_0"]
    fc2 = bundle["network_2"]
    condition_limit = max(np.abs(fc0).max(), np.abs(fc2).max())
    for index, (matrix, title) in enumerate(
        zip((fc0, fc2), FEATURE_MATRIX_TITLES)
    ):
        ax = fig.add_subplot(grid[0, index])
        ax.imshow(matrix, cmap=FC_DIVERGING, vmin=-condition_limit, vmax=condition_limit)
        ax.set_title(title, fontsize=16, pad=14)
        ax.set_xticks([])
        ax.set_yticks([])
    delta = bundle["network_unique"]
    delta_limit = np.abs(bundle["network_delta"]).max()
    ax_delta = fig.add_subplot(grid[0, 2])
    ax_delta.imshow(delta, cmap=FC_DIVERGING, vmin=-delta_limit, vmax=delta_limit)
    ax_delta.set_title("Unique network dFC\n12 + 66 blocks", fontsize=18, pad=14)
    ax_delta.set_xticks([])
    ax_delta.set_yticks([])
    ax_vector = fig.add_subplot(grid[0, 3])
    values = np.asarray(bundle["fingerprint_delta_mean"])[None, :]
    limit = np.abs(values).max()
    ax_vector.imshow(values, aspect="auto", cmap=FC_DIVERGING, vmin=-limit, vmax=limit)
    ax_vector.set_title("78-feature fingerprint\n2-back - 0-back", fontsize=18, pad=14)
    ax_vector.set_yticks([])
    ax_vector.set_xticks([0, 11, 77], ["1", "12", "78"])
    for position in (0.265, 0.515, 0.745):
        fig.text(position, 0.47, r"$\longrightarrow$", fontsize=34,
                 color=COLORS["brown"], ha="center")
    _caveat(fig, "Every participant contributes one 78-value difference; no frame or run is treated as a person.")
    return fig



def render_master_06(bundle: Mapping[str, object], _: Path) -> Figure:
    """Show repeated-CV stability without presenting split SD as a CI."""
    values = np.asarray(bundle["repeated_cv_values"])
    metrics = bundle["metrics"]
    rng = np.random.default_rng(42)
    jitter = rng.uniform(-0.09, 0.09, len(values))
    fig = _figure()
    _header(fig, 3, "Primary prediction across 20 partitions", "Repeated five-fold CV; cohort B, n=336")
    ax = fig.add_axes([0.12, 0.19, 0.76, 0.58])
    ax.scatter(values, jitter, s=150, color=COLORS["fc"], alpha=0.78, edgecolor="white", linewidth=1.2)
    mean = metrics["repeated_cv_r"]
    sd = metrics["repeated_cv_sd"]
    ax.errorbar(mean, 0.23, xerr=sd, fmt="o", color=COLORS["brown"],
                markersize=12, capsize=8, elinewidth=4, label="Mean ± split SD")
    ax.axvline(mean, color=COLORS["fc"], linewidth=2.2, linestyle="--")
    ax.text(mean + 0.006, -0.23, f"mean r = {mean:.3f}", fontsize=23, fontweight=600)
    ax.set_xlim(min(values.min() - 0.03, 0.30), max(values.max() + 0.03, 0.43))
    ax.set_ylim(-0.31, 0.35)
    ax.set_yticks([])
    ax.set_xlabel("Out-of-fold Pearson r")
    ax.legend(loc="upper left", fontsize=18)
    _clean_axis(ax, grid="x")
    _caveat(fig, "±0.024 is SD across overlapping split partitions, not a confidence interval.")
    return fig


def render_master_07(bundle: Mapping[str, object], _: Path) -> Figure:
    """Keep the primary full-refit null and fixed holdout distinct."""
    metrics = bundle["metrics"]
    null = np.asarray(bundle["null_reconfiguration"])
    observed = np.asarray(bundle["holdout_observed"])
    predicted = np.asarray(bundle["holdout_predicted"])
    fig = _figure()
    _header(fig, 4, "Null and fixed holdout", "Two checks; two distinct estimands")
    grid = fig.add_gridspec(1, 2, left=0.07, right=0.94, bottom=0.18, top=0.76, wspace=0.28)
    ax_null = fig.add_subplot(grid[0, 0])
    ax_null.hist(null, bins=28, color=COLORS["neutral"], edgecolor="white", linewidth=0.8)
    ax_null.axvline(metrics["seed42_r"], color=COLORS["fc"], linewidth=4)
    ax_null.text(0.03, 0.95, "Full model refit ×1000", transform=ax_null.transAxes,
                 fontsize=18, fontweight=600, va="top")
    ax_null.text(0.03, 0.83, "seed 42 r = 0.405\np = 1/1001 ≈ .001",
                 transform=ax_null.transAxes, fontsize=18, va="top")
    ax_null.set_xlabel("Permutation-null Pearson r")
    ax_null.set_ylabel("Permutations")
    _clean_axis(ax_null, grid="y")
    ax_holdout = fig.add_subplot(grid[0, 1])
    ax_holdout.scatter(observed, predicted, s=85, color=COLORS["fc"], alpha=0.68,
                       edgecolor="white", linewidth=0.8)
    _linear_trend(ax_holdout, observed, predicted, COLORS["fc"])
    ax_holdout.set_xlabel("Observed 2-back accuracy")
    ax_holdout.set_ylabel("Predicted 2-back accuracy")
    ax_holdout.set_title("Fixed holdout · n=67 · r=0.312", fontsize=22, pad=14)
    _clean_axis(ax_holdout, grid="both")
    _caveat(fig, "The full-refit permutation p belongs only to seed-42 r=0.405; the holdout is a separate fixed split.")
    return fig


def render_master_08(bundle: Mapping[str, object], _: Path) -> Figure:
    """Show identity-disjoint same-HCP transfer with its own uncertainty."""
    metrics = bundle["metrics"]
    observed = np.asarray(bundle["transfer_observed"])
    predicted = np.asarray(bundle["transfer_predicted"])
    fig = _figure()
    _header(fig, 5, "Identity-disjoint transfer B to A", "Train: 301 B-only · Test: 100 A · 35 shared identities removed")
    ax = fig.add_axes([0.10, 0.15, 0.60, 0.64])
    ax.scatter(observed, predicted, s=92, color=COLORS["fc"], alpha=0.67,
               edgecolor="white", linewidth=0.9)
    _linear_trend(ax, observed, predicted, COLORS["fc"])
    ax.set_xlabel("Observed 2-back accuracy · cohort A")
    ax.set_ylabel("Predicted 2-back accuracy")
    _clean_axis(ax, grid="both")
    fig.text(0.75, 0.68, f"r = {metrics['transfer_r']:.3f}", fontsize=34, fontweight=600)
    fig.text(0.75, 0.56,
             f"bootstrap 95% CI\n[{metrics['transfer_ci_low']:.2f}, {metrics['transfer_ci_high']:.2f}]",
             fontsize=22, linespacing=1.4)
    fig.text(0.75, 0.40, "A-label permutation\nfixed B prediction\np = 1/1001 ≈ .001",
             fontsize=19, linespacing=1.35, color=COLORS["brown"])
    _caveat(fig, "Same task and HCP source; kinship is unmodelled. This is not independent-site validation.")
    return fig


def render_master_09(bundle: Mapping[str, object], _: Path) -> Figure:
    """Separate the group segregation shift from the individual association."""
    seg0 = np.asarray(bundle["segregation_0"])
    seg2 = np.asarray(bundle["segregation_2"])
    delta = np.asarray(bundle["segregation_delta"])
    accuracy = np.asarray(bundle["accuracy_2back"])
    metrics = bundle["metrics"]
    fig = _figure()
    _header(fig, 6, "Group direction ≠ individual differences", "Chan-style system segregation; cohort B, n=336")
    grid = fig.add_gridspec(1, 2, left=0.07, right=0.94, bottom=0.17, top=0.77, wspace=0.30)
    ax_group = fig.add_subplot(grid[0, 0])
    parts = ax_group.violinplot([seg0, seg2], positions=[0, 1], widths=0.72,
                                showmeans=False, showmedians=False, showextrema=False)
    for index, body in enumerate(parts["bodies"]):
        body.set_facecolor(COLORS["pale_sand"] if index == 0 else COLORS["taupe"])
        body.set_edgecolor(COLORS["brown"])
        body.set_alpha(0.88)
    ax_group.plot([0, 1], [seg0.mean(), seg2.mean()], color=COLORS["ink"], linewidth=3, marker="o",
                  markersize=11, markerfacecolor="white", markeredgewidth=2)
    ax_group.set_xticks([0, 1], ["0-back", "2-back"])
    ax_group.set_ylabel("System segregation")
    ax_group.set_title("Group mean fell under load", pad=14)
    ax_group.text(0.5, 0.07, "0.3271 to 0.3035\ndelta = −0.0236 · paired p = 3.45e-05",
                  transform=ax_group.transAxes, ha="center", fontsize=18, fontweight=600)
    _clean_axis(ax_group, grid="y")
    ax_individual = fig.add_subplot(grid[0, 1])
    ax_individual.scatter(delta, accuracy, s=70, color=COLORS["fc"], alpha=0.55,
                          edgecolor="white", linewidth=0.7)
    _linear_trend(ax_individual, delta, accuracy, COLORS["fc"])
    ax_individual.axvline(0, color=COLORS["ink"], linestyle=":", linewidth=1.8)
    ax_individual.set_xlabel("Segregation change · 2-back − 0-back")
    ax_individual.set_ylabel("2-back accuracy")
    ax_individual.set_title(
        f"Individual link was weak · r={metrics['segregation_individual_r']:.3f}, "
        f"p={metrics['segregation_individual_p']:.3f}",
        fontsize=20,
        pad=14,
    )
    _clean_axis(ax_individual, grid="both")
    _caveat(fig, "A reliable mean shift does not establish that larger shifts predict better individual performance.")
    return fig


def render_master_10(bundle: Mapping[str, object], _: Path) -> Figure:
    """Map group-mean coupling change without implying feature importance."""
    fig = _figure()
    grid = fig.add_gridspec(1, 2, left=0.105, right=0.93, bottom=0.14, top=0.78,
                           width_ratios=[0.95, 1.55], wspace=0.18)
    ax_matrix = fig.add_subplot(grid[0, 0])
    limit = bundle["shared_vmax"]
    image = ax_matrix.imshow(bundle["network_unique"], cmap=FC_DIVERGING, vmin=-limit, vmax=limit)
    labels = bundle["network_labels"]
    ax_matrix.set_xticks(range(12), labels=labels, rotation=52, ha="right", fontsize=11.5)
    ax_matrix.set_yticks(range(12), labels=labels, fontsize=11.5)
    ax_matrix.set_title("78 unique network dFC values", fontsize=20, pad=14)
    colorbar = fig.colorbar(image, ax=ax_matrix, fraction=0.046, pad=0.04)
    colorbar.set_label(r"Mean $\Delta$FC", fontsize=15)
    ax_brain = fig.add_subplot(grid[0, 1])
    plotting.plot_markers(
        np.asarray(bundle["roi_reconfiguration"]),
        np.asarray(bundle["coords"]),
        node_size=34,
        node_cmap=FC_DIVERGING,
        node_vmin=-limit,
        node_vmax=limit,
        display_mode="lzr",
        axes=ax_brain,
        colorbar=True,
        title=None,
    )
    ax_brain.set_title("Mean dFC per Glasser ROI", fontsize=22, pad=14)
    _header(fig, 7, "Where mean cortical coupling changed", "Same symmetric scale across network and cortical views")
    _caveat(fig, "Descriptive group mean only; color does not encode regional predictive importance.")
    return fig


def render_master_11(bundle: Mapping[str, object], _: Path) -> Figure:
    """Compare FC representations and matched-fold incremental value."""
    means = np.asarray(bundle["method_means"])[:3]
    sds = np.asarray(bundle["method_sds"])[:3]
    labels = ["0-back FC", "FC reconfiguration", "Combined FC\n(0-back + dFC)"]
    delta = np.asarray(bundle["delta_reconfig"])
    fig = _figure()
    _header(fig, 8, "Does reconfiguration add beyond 0-back FC?", "Same estimator and repeated participant folds")
    left = fig.add_axes([0.155, 0.18, 0.40, 0.57])
    positions = np.arange(3)
    left.errorbar(means, positions, xerr=sds, fmt="o", color=COLORS["fc"],
                  markersize=12, capsize=7, elinewidth=3)
    for y_position, mean, sd in zip(positions, means, sds):
        left.text(mean + sd + 0.008, y_position, f"{mean:.3f} ± {sd:.3f}",
                  va="center", fontsize=17)
    left.set_yticks(positions, labels)
    left.invert_yaxis()
    left.set_xlabel("Repeated-CV Pearson r · mean ± split SD")
    left.set_xlim(0.20, 0.42)
    _clean_axis(left, grid="x")
    right = fig.add_axes([0.72, 0.24, 0.22, 0.46])
    right.scatter(np.ones_like(delta), delta, s=85, color=COLORS["taupe"], alpha=0.72,
                  edgecolor="white", linewidth=0.8)
    right.axhline(0, color=COLORS["ink"], linewidth=1.8, linestyle=":")
    right.errorbar([1], [delta.mean()], yerr=[delta.std()], fmt="o", color=COLORS["brown"],
                   markersize=12, capsize=8, elinewidth=3)
    right.set_xlim(0.7, 1.3)
    right.set_xticks([1], ["20 matched\npartitions"])
    right.set_ylabel(r"Incremental $R^2$")
    right.set_title(
        "Matched-fold increment\n"
        f"combined - 0-back: {delta.mean():+.4f} ± {delta.std():.4f}",
        fontsize=16.5,
        pad=12,
    )
    _clean_axis(right, grid="y")
    fig.text(0.83, 0.105, "2-SD heuristic: no clear gain", ha="center",
             fontsize=16, fontweight=600, color=COLORS["brown"])
    _caveat(fig, "The 2-SD decision rule is a split-sensitivity heuristic, not a formal superiority or equivalence test.")
    return fig


def render_master_12(bundle: Mapping[str, object], _: Path) -> Figure:
    """Place activation beside FC without implying biological superiority."""
    means = np.asarray(bundle["method_means"])
    sds = np.asarray(bundle["method_sds"])
    labels = [
        "0-back FC\n78 features",
        "dFC pattern\n78 features",
        "Combined FC\n156 features",
        "Activation\n360 features",
    ]
    colors = [COLORS["fc"], COLORS["fc"], COLORS["fc"], COLORS["activation"]]
    fig = _figure()
    _header(fig, 9, "Post hoc robustness benchmark", "Repeated five-fold CV · mean ± split SD across 20 partitions")
    ax = fig.add_axes([0.14, 0.20, 0.56, 0.56])
    positions = np.arange(4)
    for position, mean, sd, color in zip(positions, means, sds, colors):
        marker = "D" if color == COLORS["activation"] else "o"
        face = "white" if marker == "D" else color
        ax.errorbar(mean, position, xerr=sd, fmt=marker, color=color, markerfacecolor=face,
                    markeredgewidth=2.5, markersize=12, capsize=7, elinewidth=3)
        if color == COLORS["activation"]:
            ax.text(mean, position - 0.20, f"{mean:.3f} ± {sd:.3f}",
                    va="bottom", ha="center", fontsize=17)
        else:
            ax.text(mean + sd + 0.015, position, f"{mean:.3f} ± {sd:.3f}",
                    va="center", fontsize=17)
    ax.scatter([bundle["cross_run_reconfig"], bundle["cross_run_activation"]], [1, 3],
               marker="s", s=130, facecolor="white", edgecolor=COLORS["ink"], linewidth=2.2,
               label="Cross-run feature generalization · seed 42")
    ax.set_yticks(positions, labels)
    ax.invert_yaxis()
    ax.set_xlim(0.16, 0.69)
    ax.set_xlabel("Cross-validated Pearson r")
    ax.text(
        0.98,
        0.96,
        "open squares: cross-run\nfeature generalization · seed 42",
        transform=ax.transAxes,
        ha="right",
        va="top",
        fontsize=13,
        color=COLORS["brown"],
        bbox={"facecolor": "white", "edgecolor": COLORS["pale_sand"], "pad": 7},
    )
    _clean_axis(ax, grid="x")
    fig.text(0.75, 0.72, "MATCHED-FOLD INCREMENTS", fontsize=17, fontweight=600,
             color=COLORS["brown"])
    fig.text(
        0.75,
        0.61,
        "Reconfiguration over 0-back\n"
        r"incremental $R^2$ = +0.0344 ± 0.0225" "\n"
        "2-SD heuristic: no clear gain",
        fontsize=15.5,
        linespacing=1.45,
        va="top",
    )
    fig.text(
        0.75,
        0.40,
        "FC over activation\n"
        r"incremental $R^2$ = -0.0030 ± 0.0065" "\n"
        "2-SD heuristic: no clear gain",
        fontsize=15.5,
        linespacing=1.45,
        va="top",
    )
    fig.text(0.75, 0.20, "Activation = mean BOLD\n2-back - 0-back", fontsize=15,
             color=COLORS["activation"], linespacing=1.35, va="top")
    _caveat(fig, "Post hoc and unmatched: 360 regional activation features vs 78 network FC features; no biological winner claim.")
    return fig



CHART_SPECS: dict[str, Callable[[Mapping[str, object], Path], Figure]] = {
    "condition-fc-contrast": render_master_01,
    "feature-construction": render_master_04,
    "primary-repeated-cv": render_master_06,
    "null-and-holdout": render_master_07,
    "identity-disjoint-transfer": render_master_08,
    "segregation-refinement": render_master_09,
    "anatomical-context": render_master_10,
    "incremental-fc-test": render_master_11,
    "activation-robustness": render_master_12,
}


def _save_figure(fig: Figure, base: Path) -> tuple[Path, Path]:
    png = base.with_suffix(".png")
    svg = base.with_suffix(".svg")
    png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(png, dpi=160, metadata={"Software": "The Gammas evidence-first visual generator"})
    fig.savefig(svg, format="svg", metadata={"Creator": "The Gammas evidence-first visual generator"})
    plt.close(fig)
    with Image.open(png) as image:
        if image.size != PNG_SIZE:
            raise ValueError(f"{png.name}: expected {PNG_SIZE}, observed {image.size}")
        image.verify()
    return png, svg



def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _load_or_compute_bundle(force: bool) -> tuple[dict[str, object], str]:
    cache = Path(tempfile.gettempdir()) / "gammas-slide-visual-bundle-v1.pkl"
    notebook_hash = _sha256(NOTEBOOK)
    if cache.exists() and not force:
        with cache.open("rb") as stream:
            cached = pickle.load(stream)
        if cached.get("notebook_sha256") == notebook_hash:
            return cached["bundle"], "temporary cache"
    namespace = execute_canonical(NOTEBOOK, n_perm=1000)
    bundle = chart_bundle(namespace)
    with cache.open("wb") as stream:
        pickle.dump({"notebook_sha256": notebook_hash, "bundle": bundle}, stream)
    return bundle, "fresh canonical execution"


def render_all(bundle: Mapping[str, object], staging: Path) -> None:
    """Render the nine empirical charts and their delivery metadata."""
    chart_dir = staging / "charts"
    chart_dir.mkdir(parents=True, exist_ok=True)
    for slug, renderer in CHART_SPECS.items():
        fig = renderer(bundle, staging)
        _save_figure(fig, chart_dir / slug)
    build_delivery_artifacts(
        staging=staging,
        notebook=NOTEBOOK,
        bundle=bundle,
    )


def _publish(staging: Path) -> None:
    for folder_name in ("charts", "qa"):
        source = staging / folder_name
        destination = VISUALS / folder_name
        destination.mkdir(parents=True, exist_ok=True)
        for path in source.iterdir():
            os.replace(path, destination / path.name)
    os.replace(staging / "manifest.json", VISUALS / "manifest.json")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force-evidence",
        action="store_true",
        help="Ignore the temporary identifier-free chart cache and rerun the canonical notebook.",
    )
    return parser.parse_args()


def main() -> None:
    """Run the evidence gate and publish a complete static visual set."""
    args = _parse_args()
    bundle, source = _load_or_compute_bundle(force=args.force_evidence)
    print(f"evidence source: {source}")
    with tempfile.TemporaryDirectory(prefix="gammas-slide-render-") as temporary:
        staging = Path(temporary)
        render_all(bundle, staging)
        _publish(staging)
    print("rendered 9 reusable empirical charts")


if __name__ == "__main__":
    main()
