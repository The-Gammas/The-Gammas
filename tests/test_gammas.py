"""Synthetic checks for the FC representations and the HRF-delayed segmentation.

Covers only the logic a silent bug would make invisible in the benchmark: the train-only
tangent reference (leakage), the paired reconfiguration, chunked log extraction, the
fingerprint layout and the delayed EV conversion. No project data required.

Run: ``pixi run python -m unittest discover -s <this directory>``
"""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

import connectivity as fc  # noqa: E402
import datasets as ds  # noqa: E402
import preprocessing as pp  # noqa: E402


def spd_stack(rng: np.random.Generator, n: int, n_roi: int) -> np.ndarray:
    """Well-conditioned SPD matrices for transform tests."""
    factors = rng.normal(size=(n, n_roi, n_roi))
    return factors @ np.swapaxes(factors, -1, -2) + n_roi * np.eye(n_roi)


class TangentTests(unittest.TestCase):

    def setUp(self) -> None:
        self.rng = np.random.default_rng(7)
        self.logs = fc.matrix_logarithms(spd_stack(self.rng, n=8, n_roi=5))
        rows, cols = np.triu_indices(5, k=1)
        self.edges = self.logs[:, rows, cols]

    def test_reference_ignores_heldout_rows(self) -> None:
        """The leakage guarantee: held-out rows must not move the fitted reference."""
        train = self.edges[:5]
        fitted = fc.TangentCentering().fit(train)
        transformed = fitted.transform(self.edges)

        extreme = self.edges.copy()
        extreme[5:] *= 1_000.0
        refitted = fc.TangentCentering().fit(train).transform(extreme)

        np.testing.assert_array_equal(refitted[:5], transformed[:5])

    def test_centering_matches_explicit_formula(self) -> None:
        train = np.arange(5)
        expected = (self.edges - self.edges[train].mean(axis=0)) * fc.TANGENT_SCALING

        actual = fc.TangentCentering().fit(self.edges[train]).transform(self.edges)

        np.testing.assert_array_equal(actual, expected)

    def test_paired_transform_returns_high_minus_low(self) -> None:
        low, high = self.edges, self.edges[::-1]
        stacked = np.hstack([low, high])
        train = np.arange(5)
        expected = ((high - high[train].mean(axis=0)) * fc.TANGENT_SCALING
                    - (low - low[train].mean(axis=0)) * fc.TANGENT_SCALING)

        actual = fc.TangentCentering(paired=True).fit(stacked[train]).transform(stacked)

        np.testing.assert_allclose(actual, expected, rtol=0, atol=1e-15)

    def test_log_triangles_survive_chunk_boundaries(self) -> None:
        covariances = spd_stack(self.rng, n=7, n_roi=6)
        packed = fc.pack_triangle(covariances)
        rows, cols = np.triu_indices(6, k=1)
        expected = fc.matrix_logarithms(covariances)[:, rows, cols]

        for chunk in (1, 3, 7, 50):  # below, across and beyond the row count
            with self.subTest(chunk=chunk):
                np.testing.assert_allclose(
                    fc.log_triangles(packed, n_roi=6, chunk=chunk), expected)

    def test_covariances_are_positive_definite_with_fewer_frames_than_rois(self) -> None:
        covariances = fc.subject_covariances([self.rng.normal(size=(8, 5))])

        self.assertGreater(np.linalg.eigvalsh(covariances[0]).min(), 0.0)


class FingerprintTests(unittest.TestCase):

    def test_twelve_networks_give_78_features_excluding_self_correlations(self) -> None:
        labels = np.repeat(np.arange(12), 3)
        correlation = np.full((36, 36), 0.5)
        np.fill_diagonal(correlation, 1.0)

        features = fc.network_fingerprint(correlation, labels)

        self.assertEqual(features.shape, (78,))
        np.testing.assert_allclose(features, 0.5)  # diagonal excluded within-network


class DelayedSegmentationTests(unittest.TestCase):
    """The 4 s HRF shift must move frames by exactly ``floor(delay / TR)``."""

    def _spec_with_ev(self, directory: Path, onset: float) -> ds.DatasetSpec:
        ev_dir = directory / "subjects" / "sub01" / "EVs" / "tfMRI_WM_RL"
        ev_dir.mkdir(parents=True)
        for condition in ds.COND_0BACK:
            (ev_dir / f"{condition}.txt").write_text(f"{onset} {ds.TR * 4} 1\n")
        return ds.DatasetSpec(kind="B", name="test", loader="test", task_dir=directory,
                              behaviour=directory / "wm.csv", rest_dir=None, atlas=None,
                              n_expected=1)

    def test_delay_shifts_frames_by_whole_repetition_times(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            spec = self._spec_with_ev(Path(tmp), onset=10.0)

            undelayed = pp.condition_frames(spec, "sub01", run=0, level="0back")
            delayed = pp.condition_frames(spec, "sub01", run=0, level="0back", delay=4.0)

            self.assertEqual(undelayed.tolist(), [13, 14, 15, 16])  # floor(10 / 0.72)
            self.assertEqual(delayed.tolist(), [19, 20, 21, 22])  # floor(14 / 0.72)


if __name__ == "__main__":
    unittest.main()
