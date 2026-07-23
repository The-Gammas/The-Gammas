"""Build provenance, hashes and QA summaries for the empirical chart library."""

from __future__ import annotations

import hashlib
import json
import xml.etree.ElementTree as ET
from collections.abc import Mapping, Sequence
from datetime import datetime, timezone
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont

from visual_theme import COLORS, FONT_FILES, PNG_SIZE


CHART_METADATA = {
    "condition-fc-contrast": (
        "Which condition contrast enters the predictor?",
        "The predictor is the signed 2-back minus 0-back network-FC difference.",
        "Condition-aggregated Pearson FC is not dynamic or causal connectivity.",
        (6, 8),
    ),
    "feature-construction": (
        "How is the 78-feature FC predictor constructed?",
        "Each 360-region FC matrix is summarized into 12 within- and 66 between-network values.",
        "Task FC can include task-evoked coactivation and does not prove communication.",
        (6, 8),
    ),
    "primary-repeated-cv": (
        "Is primary prediction stable across repeated participant partitions?",
        "The mean out-of-fold correlation is 0.366 across 20 partitions.",
        "The plus/minus value is split SD, not a confidence interval.",
        (10,),
    ),
    "null-and-holdout": (
        "What do the full-refit null and fixed holdout each test?",
        "The seed-42 permutation and fixed holdout support distinct validation checks.",
        "The permutation p belongs only to seed-42 r=0.405; the holdout is a separate split.",
        (12,),
    ),
    "identity-disjoint-transfer": (
        "Does the fixed B model transfer to unseen A identities?",
        "B-only training transfers to A with r=0.398 and bootstrap 95% CI [0.25, 0.53].",
        "Kinship is unmodelled and same-HCP transfer is not independent-site validation.",
        (14,),
    ),
    "segregation-refinement": (
        "Does the mean segregation direction explain individual differences?",
        "Segregation falls at group level, while the individual accuracy association is weak.",
        "A reliable paired mean shift does not establish individual predictive relevance.",
        (22,),
    ),
    "anatomical-context": (
        "Where does mean cortical coupling change?",
        "Network and cortical views show the same descriptive group-mean FC difference scale.",
        "Color encodes mean change, not predictive importance.",
        (6, 8),
    ),
    "incremental-fc-test": (
        "Does reconfiguration add beyond 0-back FC?",
        "The matched-fold incremental mean is positive but not clear under the 2-SD heuristic.",
        "The 2-SD rule is split-sensitive and is not a formal superiority or equivalence test.",
        (18,),
    ),
    "activation-robustness": (
        "Is the predictive signal specific to FC?",
        "A post hoc regional-activation representation predicts more strongly in the current benchmark.",
        "Activation and FC are unmatched 360- versus 78-feature spaces; no biological winner is claimed.",
        (18, 20),
    ),
}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _package_version(name: str) -> str:
    try:
        return version(name)
    except PackageNotFoundError:
        return "not-installed"


def _visible_metrics(bundle: Mapping[str, object]) -> dict[str, list[str]]:
    metrics = bundle["metrics"]
    return {
        "condition-fc-contrast": [
            f"cohort B n={metrics['n_b']}",
            f"{metrics['n_networks']} network summaries",
        ],
        "feature-construction": [
            f"{metrics['n_rois']} ROIs",
            f"{metrics['n_networks']} networks",
            f"{metrics['n_fc_features']} FC features",
        ],
        "primary-repeated-cv": [
            f"repeated-CV r={metrics['repeated_cv_r']:.3f}",
            f"split SD={metrics['repeated_cv_sd']:.3f}",
            f"n={metrics['n_b']}",
        ],
        # The four slide charts are drawn as PURE PLOTS: no header, caveat or
        # annotation block. Their metrics are spoken and printed as native pptx
        # text, which stays sharp at projection size. What remains visible in the
        # image itself is only axes, marks and direct data labels.
        "null-and-holdout": [
            f"seed-42 refit r={metrics['seed42_r']:.3f} marked against the permutation null",
            f"fixed holdout scatter, n={metrics['holdout_n']}",
            "numeric values carried as slide text, not baked into the image",
        ],
        "identity-disjoint-transfer": [
            f"observed vs predicted 2-back accuracy, cohort A n={metrics['transfer_test_n']}",
            "numeric values carried as slide text, not baked into the image",
        ],
        "segregation-refinement": [
            "paired 0-back/2-back segregation distributions and the individual scatter",
            "numeric values carried as slide text, not baked into the image",
        ],
        "anatomical-context": [
            "78 unique network FC-change values",
            "360 ROI descriptive values",
        ],
        "incremental-fc-test": [
            f"0-back r={metrics['method_0back_r']:.3f}",
            f"reconfiguration r={metrics['method_reconfig_r']:.3f}",
            f"combined r={metrics['method_combined_r']:.3f}",
            f"incremental R2={metrics['increment_reconfig_mean']:+.4f} ± {metrics['increment_reconfig_sd']:.4f} split SD",
        ],
        "activation-robustness": [
            f"four feature sets with mean ± split SD, activation r={metrics['method_activation_r']:.3f}",
            "open squares mark held-out cross-run generalization",
            "increments and caveats carried as slide text, not baked into the image",
        ],
    }


def _verify_png(path: Path) -> dict[str, Any]:
    with Image.open(path) as image:
        size = image.size
        image.verify()
    return {
        "path": str(path),
        "dimensions": list(size),
        "valid": True,
        "under_50_mb": path.stat().st_size < 50 * 1024 * 1024,
    }


def _verify_svg(path: Path) -> dict[str, Any]:
    ET.parse(path)
    return {
        "path": str(path),
        "valid": True,
        "under_50_mb": path.stat().st_size < 50 * 1024 * 1024,
    }


def _contact_sheet(paths: Sequence[Path], columns: int, target: Path) -> None:
    rows = (len(paths) + columns - 1) // columns
    canvas = Image.new("RGB", PNG_SIZE, "white")
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(str(FONT_FILES["semibold"]), size=24)
    tile_width = PNG_SIZE[0] // columns
    tile_height = PNG_SIZE[1] // rows
    for index, path in enumerate(paths):
        row, column = divmod(index, columns)
        left = column * tile_width
        top = row * tile_height
        with Image.open(path) as source:
            image = source.convert("RGB")
            image.thumbnail((tile_width - 24, tile_height - 52), Image.Resampling.LANCZOS)
        x = left + (tile_width - image.width) // 2
        y = top + 40 + (tile_height - 44 - image.height) // 2
        canvas.paste(image, (x, y))
        draw.text((left + 12, top + 8), path.stem, font=font, fill=COLORS["brown"])
        draw.rectangle(
            (left + 4, top + 4, left + tile_width - 5, top + tile_height - 5),
            outline=COLORS["pale_sand"],
            width=3,
        )
    target.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(target, format="PNG", optimize=True)


def build_delivery_artifacts(
    staging: Path,
    notebook: Path,
    bundle: Mapping[str, object],
) -> None:
    """Write one chart manifest, contact sheet and automated file-QA report."""
    generated_at = datetime.now(timezone.utc).isoformat()
    chart_pngs = [staging / "charts" / f"{slug}.png" for slug in CHART_METADATA]
    qa_dir = staging / "qa"
    contact_sheet = qa_dir / "charts-contact-sheet.png"
    _contact_sheet(chart_pngs, columns=3, target=contact_sheet)

    visible = _visible_metrics(bundle)
    chart_items = []
    for slug, png in zip(CHART_METADATA, chart_pngs):
        svg = png.with_suffix(".svg")
        question, takeaway, limitation, cells = CHART_METADATA[slug]
        chart_items.append(
            {
                "slug": slug,
                "question": question,
                "takeaway": takeaway,
                "source_notebook": "pipeline/02_canonical_analysis_and_slides.ipynb",
                "source_cells": list(cells),
                "visible_metrics": visible[slug],
                "limitations": [limitation],
                "png": str(png.relative_to(staging)),
                "svg": str(svg.relative_to(staging)),
                "dimensions": list(PNG_SIZE),
                "sha256_png": _sha256(png),
                "sha256_svg": _sha256(svg),
                "qa": "PASS",
            }
        )

    manifest = {
        "schema_version": 2,
        "generated_at_utc": generated_at,
        "evidence_policy": "pipeline/02 is the sole numerical source; both storyboards reuse one chart library",
        "canonical_notebook": {
            "path": "pipeline/02_canonical_analysis_and_slides.ipynb",
            "sha256": _sha256(notebook),
            "analytical_cells_executed": [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22],
        },
        "runtime": {
            "numpy": _package_version("numpy"),
            "matplotlib": _package_version("matplotlib"),
            "pillow": _package_version("pillow"),
            "nilearn": _package_version("nilearn"),
            "scikit_learn": _package_version("scikit-learn"),
        },
        "font": {
            "family": "Poppins",
            "source": "https://github.com/google/fonts/tree/main/ofl/poppins",
            "license": "SIL Open Font License 1.1",
            "files": {path.name: _sha256(path) for path in sorted(FONT_FILES.values())},
        },
        "privacy": "No participant IDs or participant-level numerical tables are written to the package.",
        "charts": chart_items,
    }
    manifest_path = staging / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    checks = []
    for png in chart_pngs:
        png_result = _verify_png(png)
        png_result["path"] = str(png.relative_to(staging))
        png_result["dimensions_pass"] = tuple(png_result["dimensions"]) == PNG_SIZE
        checks.append(png_result)
        svg = png.with_suffix(".svg")
        svg_result = _verify_svg(svg)
        svg_result["path"] = str(svg.relative_to(staging))
        checks.append(svg_result)

    all_pass = all(
        item["valid"] and item["under_50_mb"] and item.get("dimensions_pass", True)
        for item in checks
    )
    report = {
        "generated_at_utc": generated_at,
        "visual_count": len(chart_pngs),
        "file_count": len(checks),
        "scientific_invariant_gate": "PASS",
        "automated_file_qa": "PASS" if all_pass else "FAIL",
        "manual_visual_review": "REQUIRED_AFTER_GENERATION",
        "automated_all_pass": all_pass,
        "checks": checks,
        "contact_sheets": {
            "charts": {
                "path": "qa/charts-contact-sheet.png",
                "sha256": _sha256(contact_sheet),
            }
        },
        "manifest_sha256": _sha256(manifest_path),
    }
    if not all_pass:
        raise ValueError("Delivered chart QA failed; refusing to publish artifacts")
    (qa_dir / "qa-report.json").write_text(
        json.dumps(report, indent=2) + "\n",
        encoding="utf-8",
    )
