"""Contract tests for the presentation visual asset generator."""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

VISUALS = Path(__file__).resolve().parents[1]
SRC = VISUALS / "src"
MANIFEST = VISUALS / "manifest.json"
QA_REPORT = VISUALS / "qa" / "qa-report.json"
INTERNAL_STORYBOARD = VISUALS.parent / "internal-review-storyboard.md"
FINAL_STORYBOARD = VISUALS.parent / "final-storyboard-5-plus-4.md"
sys.path.insert(0, str(SRC))

from canonical_evidence import validate_canonical  # noqa: E402
import generate_visuals as visuals  # noqa: E402
from generate_visuals import CHART_SPECS, metric_labels  # noqa: E402
from visual_theme import COLORS, PNG_SIZE  # noqa: E402


EXPECTED_CHART_SLUGS = (
    "condition-fc-contrast",
    "feature-construction",
    "primary-repeated-cv",
    "null-and-holdout",
    "identity-disjoint-transfer",
    "segregation-refinement",
    "anatomical-context",
    "incremental-fc-test",
    "activation-robustness",
)


class ThemeContractTests(unittest.TestCase):
    """Keep the exported figures aligned with the approved visual system."""

    def test_palette_is_explicit_and_bounded(self) -> None:
        """Use only the approved semantic color roots."""
        self.assertEqual(
            set(COLORS),
            {
                "ink",
                "pale_sand",
                "taupe",
                "brown",
                "fc",
                "activation",
                "neutral",
            },
        )
        self.assertEqual(len(set(COLORS.values())), 7)

    def test_png_contract_is_16_by_9(self) -> None:
        """Export every visual on the same Google Slides canvas."""
        self.assertEqual(PNG_SIZE, (2560, 1440))
        self.assertEqual(PNG_SIZE[0] / PNG_SIZE[1], 16 / 9)


def canonical_namespace_fixture() -> dict[str, object]:
    """Minimal namespace matching the canonical notebook's public variables."""
    method_values = {
        "0-back FC (78)": (0.274, 0.032),
        "reconfig FC (78)": (0.366, 0.024),
        "0bk + reconfig (156)": (0.333, 0.026),
        "activation contrast (360)": (0.600, 0.016),
    }
    return {
        "featB": {"n": 336, "net": np.arange(12)},
        "featA": {"n": 100},
        "reconfig": np.zeros((336, 78)),
        "act_contrast": np.zeros((336, 360)),
        "r_recon_mean": 0.366,
        "r_recon_sd": 0.024,
        "r_heldout": 0.312,
        "te_idx": np.arange(67),
        "r_seed42": 0.405,
        "p_recon": 1 / 1001,
        "r_ext": 0.398,
        "ci_ext": np.array([0.25, 0.53]),
        "b_only_idx": np.arange(301),
        "yA": np.zeros(100),
        "shared": set(range(35)),
        "seg0": np.full(336, 0.3271),
        "seg2": np.full(336, 0.3035),
        "dseg": np.full(336, -0.0236),
        "p_seg": 3.45e-05,
        "r_dseg": -0.105,
        "p_dseg": 0.054,
        "r_methods": method_values,
        "d_recon": 0.0344,
        "s_recon": 0.0225,
        "d_fc": -0.0030,
        "s_fc": 0.0065,
    }


class CanonicalEvidenceTests(unittest.TestCase):
    """Reject visual generation when canonical evidence drifts."""

    def test_canonical_gate_rejects_wrong_primary_r(self) -> None:
        """Stop when the main repeated-CV result no longer reproduces."""
        namespace = canonical_namespace_fixture()
        namespace["r_recon_mean"] = 0.20
        with self.assertRaisesRegex(AssertionError, "repeated_cv_r"):
            validate_canonical(namespace)

    def test_canonical_gate_accepts_expected_metrics(self) -> None:
        """Accept the approved presentation evidence."""
        metrics = validate_canonical(canonical_namespace_fixture())
        self.assertAlmostEqual(metrics["repeated_cv_r"], 0.366, places=3)
        self.assertEqual(metrics["n_b"], 336)

    def test_canonical_gate_validates_bootstrap_ci_at_display_precision(self) -> None:
        """Compare the transfer CI with its approved two-decimal display."""
        namespace = canonical_namespace_fixture()
        namespace["ci_ext"] = np.array([0.2478, 0.5281099063850812])
        metrics = validate_canonical(namespace)
        self.assertEqual(round(metrics["transfer_ci_low"], 2), 0.25)
        self.assertEqual(round(metrics["transfer_ci_high"], 2), 0.53)


class RendererContractTests(unittest.TestCase):
    """Keep the empirical chart library aligned with both storyboards."""

    def test_chart_registry_is_exact_and_semantic(self) -> None:
        """Generate only the nine empirical views approved for reuse."""
        self.assertEqual(tuple(CHART_SPECS), EXPECTED_CHART_SLUGS)

    def test_metric_labels_keep_estimands_separate(self) -> None:
        """Never relabel split SD as CI or merge the two null tests."""
        labels = metric_labels(canonical_namespace_fixture())
        self.assertIn("split SD", labels["repeated_cv"])
        self.assertIn("seed 42", labels["primary_null"])
        self.assertIn("bootstrap 95% CI", labels["transfer"])
        self.assertNotIn("CI", labels["repeated_cv"])

    def test_question_visual_encodes_the_signed_contrast(self) -> None:
        """Read the first visual literally as 2-back minus 0-back."""
        self.assertEqual(
            getattr(visuals, "QUESTION_MATRIX_KEYS", None),
            ("network_2", "network_0", "network_delta"),
        )
        self.assertEqual(
            getattr(visuals, "QUESTION_OPERATORS", None),
            ("minus", "equals"),
        )

    def test_feature_visual_names_network_summaries_precisely(self) -> None:
        """Do not label a displayed 12-by-12 summary as a 360-by-360 matrix."""
        self.assertEqual(
            getattr(visuals, "FEATURE_MATRIX_TITLES", None),
            (
                "0-back FC\n12x12 summary of 360x360",
                "2-back FC\n12x12 summary of 360x360",
            ),
        )

    def test_activation_renderer_builds_without_an_implicit_legend(self) -> None:
        """Render slide 12 without assuming Matplotlib created a legend."""
        bundle = {
            "method_means": np.array([0.274, 0.366, 0.333, 0.600]),
            "method_sds": np.array([0.032, 0.024, 0.026, 0.016]),
            "cross_run_reconfig": 0.246,
            "cross_run_activation": 0.476,
        }
        figure = visuals.render_master_12(bundle, Path("."))
        self.addCleanup(plt.close, figure)
        self.assertEqual(len(figure.axes), 1)


class StoryboardContractTests(unittest.TestCase):
    """Keep the two narrative flows explicit without forcing one image per slide."""

    def test_every_slide_declares_chart_or_no_pre_rendered_chart(self) -> None:
        """Give the future deck author one unambiguous visual instruction per slide."""
        internal = INTERNAL_STORYBOARD.read_text(encoding="utf-8")
        final = FINAL_STORYBOARD.read_text(encoding="utf-8")
        self.assertEqual(internal.count("\n## Slide "), 15)
        self.assertEqual(internal.count("\n**Chart:**"), 15)
        self.assertEqual(final.count("\n## Slide "), 9)
        self.assertEqual(final.count("\n- **Chart:**"), 9)
        self.assertNotIn("**Visualization:**", internal)
        self.assertNotIn("**Visualization:**", final)

    def test_every_storyboard_chart_reference_exists(self) -> None:
        """Reuse delivered evidence assets instead of stale slide compositions."""
        for storyboard in (INTERNAL_STORYBOARD, FINAL_STORYBOARD):
            source = storyboard.read_text(encoding="utf-8")
            for slug in EXPECTED_CHART_SLUGS:
                reference = f"visuals/charts/{slug}.png"
                if reference in source:
                    self.assertTrue((VISUALS / "charts" / f"{slug}.png").is_file())
            self.assertNotIn("visuals/master/", source)
            self.assertNotIn("visuals/final-5-plus-4/", source)

    def test_final_robustness_slide_is_required_core(self) -> None:
        """Keep the evidence that motivates the refined conclusion in the Friday flow."""
        source = FINAL_STORYBOARD.read_text(encoding="utf-8")
        self.assertIn(
            "**Status:** Spoken core; required to support the refined final conclusion.",
            source,
        )


class DeliveredAssetContractTests(unittest.TestCase):
    """Require a complete, traceable and self-consistent visual delivery."""

    def test_manifest_has_all_visuals(self) -> None:
        """Record exactly the nine empirical charts as QA-passed."""
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertNotIn("master", manifest)
        self.assertNotIn("final_5_plus_4", manifest)
        self.assertEqual(
            tuple(item["slug"] for item in manifest["charts"]),
            EXPECTED_CHART_SLUGS,
        )
        self.assertTrue(all(item["qa"] == "PASS" for item in manifest["charts"]))

    def test_manifest_hashes_match_delivered_chart_files(self) -> None:
        """Detect any PNG or SVG changed after scientific and visual QA."""
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        for item in manifest["charts"]:
            for extension in ("png", "svg"):
                path = VISUALS / item[extension]
                observed = hashlib.sha256(path.read_bytes()).hexdigest()
                self.assertEqual(observed, item[f"sha256_{extension}"], path.name)

    def test_qa_report_and_chart_contact_sheet_exist(self) -> None:
        """Preserve file-level checks and one library-wide coherence view."""
        report = json.loads(QA_REPORT.read_text(encoding="utf-8"))
        self.assertTrue(report["automated_all_pass"])
        self.assertEqual(report["manual_visual_review"], "REQUIRED_AFTER_GENERATION")
        self.assertEqual(report["visual_count"], 9)
        self.assertEqual(report["file_count"], 18)
        self.assertEqual(set(report["contact_sheets"]), {"charts"})
        self.assertTrue((VISUALS / "qa" / "charts-contact-sheet.png").is_file())

    def test_obsolete_slide_image_directories_are_absent(self) -> None:
        """Do not retain diagrams or duplicated final-slide compositions."""
        self.assertFalse((VISUALS / "master").exists())
        self.assertFalse((VISUALS / "final-5-plus-4").exists())

    def test_poppins_copy_avoids_known_missing_glyphs(self) -> None:
        """Keep exported labels free of glyphs absent from bundled Poppins."""
        source = (SRC / "generate_visuals.py").read_text(encoding="utf-8")
        for glyph in ("→", "Δ", "′", "⁻", "⁵"):
            self.assertNotIn(glyph, source)


if __name__ == "__main__":
    unittest.main()
