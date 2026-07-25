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
import unittest.mock
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gammas import connectivity as fc  # noqa: E402
from gammas import contributed as contrib  # noqa: E402
from gammas import datasets as ds  # noqa: E402
from gammas import evaluation as ev  # noqa: E402
from gammas import preprocessing as pp  # noqa: E402


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


    def test_centering_matches_explicit_formula(self) -> None:
        """Also the leakage guarantee: if the transform is exactly this formula, held-out rows
        cannot move the fitted reference, because the reference only ever sees train."""
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
                              behaviour=directory / "wm.csv", rest_dir=None, atlas=None)

    def test_delay_shifts_frames_by_whole_repetition_times(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            spec = self._spec_with_ev(Path(tmp), onset=10.0)

            undelayed = pp.condition_frames(spec, "sub01", run=0, level="0back", delay=0.0)
            delayed = pp.condition_frames(spec, "sub01", run=0, level="0back", delay=4.0)

            self.assertEqual(undelayed.tolist(), [13, 14, 15, 16])  # floor(10 / 0.72)
            self.assertEqual(delayed.tolist(), [19, 20, 21, 22])  # floor(14 / 0.72)

    def test_default_delay_is_the_canonical_shift(self) -> None:
        """Regression guard for the bug this suite used to miss.

        The delay was a parameter nobody had to pass, so every caller that omitted it
        silently reproduced r = 0.152 instead of the canonical r = 0.366. The old suite
        stayed green because it only checked that the parameter *worked*, never that the
        default was right. Callers that omit ``delay`` must now get the 4 s shift.
        """
        self.assertEqual(pp.HRF_DELAY, 4.0)
        with tempfile.TemporaryDirectory() as tmp:
            spec = self._spec_with_ev(Path(tmp), onset=10.0)

            default = pp.condition_frames(spec, "sub01", run=0, level="0back")
            explicit = pp.condition_frames(spec, "sub01", run=0, level="0back", delay=4.0)

            np.testing.assert_array_equal(default, explicit)


class SplitLeakageTests(unittest.TestCase):
    """The leakage guarantee. If this breaks, every reported r inflates and nothing warns.

    ``make_split`` is the only thing standing between us and a subject appearing in both train
    and test. It reads the cohort from disk, so the subject list is stubbed: the split logic is
    what is under test, not the loader.
    """

    COHORT = [f"{i:03d}" for i in range(50)]

    def _split(self, **kwargs) -> dict:
        with unittest.mock.patch.object(ev.ds, "load_subjects", return_value=list(self.COHORT)):
            return ev.make_split(spec=None, **kwargs)

    def test_returned_splits_are_leakage_free_by_construction(self) -> None:
        """``make_split`` runs ``_validate_split`` before returning (evaluation.py), so any split
        it hands back already satisfies disjointness, coverage and fold partitioning. What that
        does not cover is the fold count."""
        split = self._split(cv_folds=5)

        self.assertEqual(len(split["cv"]), 5)
        self.assertEqual(sorted(split["train"] + split["test"]), sorted(self.COHORT))

    def test_same_seed_reproduces_the_same_split(self) -> None:
        self.assertEqual(self._split(seed=7), self._split(seed=7))
        self.assertNotEqual(self._split(seed=7)["test"], self._split(seed=8)["test"])

    def test_validate_split_rejects_a_leaked_split(self) -> None:
        leaked = {"train": ["a", "b"], "test": ["b"], "n_total": 3,
                  "cv": [{"fold": 0, "val": ["a", "b"]}]}

        with self.assertRaisesRegex(ValueError, "leak"):
            ev._validate_split(leaked)

    def test_validate_split_rejects_folds_that_do_not_cover_train(self) -> None:
        dropped = {"train": ["a", "b"], "test": ["c"], "n_total": 3,
                   "cv": [{"fold": 0, "val": ["a"]}]}

        with self.assertRaisesRegex(ValueError, "partition"):
            ev._validate_split(dropped)


class StatisticsTests(unittest.TestCase):
    """The three statistics the conclusions rest on, against outcomes we can predict."""

    def setUp(self) -> None:
        rng = np.random.default_rng(11)
        self.control = rng.normal(size=400)
        # both vectors are the control plus independent noise: raw correlation is driven by the
        # shared control, so partialling it out must collapse the association to ~0
        self.prediction = self.control + rng.normal(scale=0.5, size=400)
        self.target = self.control + rng.normal(scale=0.5, size=400)

    def test_partial_correlation_removes_a_shared_driver(self) -> None:
        raw = ev.correlation(self.prediction, self.target)
        partial = ev.partial_correlation(self.prediction, self.target, self.control)

        self.assertGreater(raw, 0.6)          # looks like a strong effect
        self.assertLess(abs(partial), 0.15)   # and is almost entirely the control

    def test_partial_correlation_leaves_an_unrelated_control_alone(self) -> None:
        unrelated = np.random.default_rng(12).normal(size=400)

        raw = ev.correlation(self.prediction, self.target)
        partial = ev.partial_correlation(self.prediction, self.target, unrelated)

        self.assertAlmostEqual(raw, partial, delta=0.05)

    def test_permutation_p_separates_real_association_from_none(self) -> None:
        signal = np.arange(60.0)
        noise = np.random.default_rng(13).normal(size=60)

        self.assertLess(ev.permutation_p(signal, signal, n_perm=999), 0.01)
        self.assertGreater(ev.permutation_p(noise, signal, n_perm=999), 0.05)



class ContributedAttributionTests(unittest.TestCase):
    """Contributed methods must stay attributed and behave as their author defined them."""

    def test_segregation_is_within_minus_between_over_within(self) -> None:
        labels = np.repeat(["net1", "net2"], 3)
        fc = np.full((6, 6), 0.2)                       # between-network baseline
        fc[:3, :3] = fc[3:, 3:] = 0.8                   # stronger within-network
        np.fill_diagonal(fc, 1.0)                       # must be excluded from W

        segregation = contrib.measure_system_segregation(fc, labels, ["net1", "net2"])

        self.assertAlmostEqual(segregation, (0.8 - 0.2) / 0.8, places=12)

    def test_segregation_returns_zero_when_no_within_network_signal(self) -> None:
        labels = np.repeat(["net1", "net2"], 3)
        fc = np.zeros((6, 6))

        self.assertEqual(contrib.measure_system_segregation(fc, labels, ["net1", "net2"]), 0.0)



if __name__ == "__main__":
    unittest.main()
