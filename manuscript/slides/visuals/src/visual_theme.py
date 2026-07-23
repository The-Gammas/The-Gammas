"""Shared visual tokens for The Gammas slide figures."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.font_manager import FontProperties, fontManager

COLORS = {
    "ink": "#202729",
    "pale_sand": "#EAD6B8",
    "taupe": "#B99470",
    "brown": "#705C40",
    "fc": "#0072B2",
    "activation": "#D55E00",
    "neutral": "#B8B8B8",
}

PNG_SIZE = (2560, 1440)
# Do NOT shrink this canvas to make type bigger relative to the frame. Every
# renderer positions text in FIGURE FRACTIONS while font sizes are absolute
# points, so a smaller canvas overflows every layout: tried (10.0, 5.625)/256
# on 23 Jul and all nine charts came back with clipped axis labels and
# overlapping captions, while the whole test suite still passed (nothing
# measures rendered text position). Legibility has to come from simplifying
# chart content, not from rescaling the canvas.
FIGSIZE = (16.0, 9.0)
DPI = 160

VISUALS_DIR = Path(__file__).resolve().parents[1]
FONT_DIR = VISUALS_DIR / "fonts"
FONT_FILES = {
    "regular": FONT_DIR / "Poppins-Regular.ttf",
    "medium": FONT_DIR / "Poppins-Medium.ttf",
    "semibold": FONT_DIR / "Poppins-SemiBold.ttf",
}


def register_fonts() -> str:
    """Register bundled Poppins files and report the active font family."""
    available = [path for path in FONT_FILES.values() if path.exists()]
    for path in available:
        fontManager.addfont(path)
    if len(available) == len(FONT_FILES):
        return FontProperties(fname=FONT_FILES["regular"]).get_name()
    return "Arial"


def configure_matplotlib() -> str:
    """Apply the approved slide-safe chart styling."""
    family = register_fonts()
    mpl.rcParams.update(
        {
            "font.family": family,
            "font.size": 20,
            "axes.titlesize": 28,
            "axes.titleweight": 600,
            "axes.labelsize": 20,
            "axes.labelcolor": COLORS["ink"],
            "axes.edgecolor": COLORS["ink"],
            "axes.linewidth": 1.2,
            "xtick.color": COLORS["ink"],
            "ytick.color": COLORS["ink"],
            "xtick.labelsize": 17,
            "ytick.labelsize": 17,
            "text.color": COLORS["ink"],
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.facecolor": "white",
            "savefig.transparent": False,
            "grid.color": COLORS["pale_sand"],
            "grid.linewidth": 0.8,
            "grid.alpha": 0.55,
            "legend.frameon": False,
            "svg.fonttype": "none",
        }
    )
    return family


def new_figure(
    nrows: int = 1,
    ncols: int = 1,
    **kwargs: Any,
) -> tuple[Figure, Any]:
    """Create a standard 16:9 figure and axes."""
    configure_matplotlib()
    return plt.subplots(nrows=nrows, ncols=ncols, figsize=FIGSIZE, **kwargs)

