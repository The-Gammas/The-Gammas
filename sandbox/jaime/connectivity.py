"""Functional-connectivity representations (Jaime's sandbox).

**Category: FC representations.** Turns condition-restricted BOLD into the two feature
sets notebook ``06`` compares: the team's 78-dim within/between-network fingerprint and
off-diagonal log-Euclidean tangent edges. Downstream of :mod:`preprocessing`, consumed by
the modelling notebooks alongside :mod:`evaluation`.

Tangent geometry here is **log-Euclidean**: the reference is the arithmetic mean of the
training matrix logarithms. ``nilearn.connectome.ConnectivityMeasure(kind="tangent")``
is *not* a drop-in — it uses the affine-invariant geometric mean and yields different
numbers, so swapping it in would silently move every benchmark value.
"""

from __future__ import annotations

import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.covariance import LedoitWolf

EIGENVALUE_FLOOR = 1e-10
TANGENT_SCALING = np.sqrt(2.0)


def _spectral_map(matrices: np.ndarray, transform) -> np.ndarray:
    """Apply a function to the eigenvalues of a symmetric stack, batched.

    Ours — ``np.linalg.eigh`` is already batched, so no per-subject loop is needed. The
    final symmetrisation removes the ~1e-16 asymmetry the reconstruction introduces.
    """
    values, vectors = np.linalg.eigh(matrices)
    mapped = transform(np.clip(values, EIGENVALUE_FLOOR, None))
    result = (vectors * mapped[..., None, :]) @ np.swapaxes(vectors, -1, -2)
    return (result + np.swapaxes(result, -1, -2)) / 2.0


def subject_covariances(timeseries: list[np.ndarray]) -> np.ndarray:
    """Positive-definite Ledoit-Wolf covariance per entry, ``(n, n_roi, n_roi)``.

    Shrinkage is required because each condition has fewer frames (312) than ROIs (360),
    so the sample covariance is singular. Inputs follow the project's ``(n_roi, n_frames)``
    convention; eigenvalues are floored so the matrix logarithm stays defined.
    """
    covariances = np.stack([
        LedoitWolf(assume_centered=False).fit(np.asarray(x, dtype=float).T).covariance_
        for x in timeseries
    ])
    return _spectral_map(covariances, lambda v: v)


def matrix_logarithms(covariances: np.ndarray) -> np.ndarray:
    """Symmetric matrix logarithm of an SPD stack, ``(n, n_roi, n_roi)``.

    Subject-local, so it may be computed once and reused across folds — only the tangent
    *reference* is fold-dependent.
    """
    return _spectral_map(np.asarray(covariances, dtype=float), np.log)


def pack_triangle(matrices: np.ndarray) -> np.ndarray:
    """Flatten each symmetric matrix to its upper triangle, diagonal included.

    Ours — halves the cache footprint; the diagonal is kept so unpacking is lossless.
    """
    upper = np.triu_indices(matrices.shape[-1])
    return matrices[:, upper[0], upper[1]]


def log_triangles(packed: np.ndarray, n_roi: int, chunk: int = 64) -> np.ndarray:
    """Packed covariance rows -> off-diagonal log-edge rows, ``(n, n_roi(n_roi-1)/2)``.

    Ours — the cache stores packed covariances but every downstream step reads only the
    off-diagonal triangle, so this is the single hop from disk to features. Chunked because
    a 336x360x360 float64 eigendecomposition holds ~1 GB of intermediates at once.
    """
    full, offdiag = np.triu_indices(n_roi), np.triu_indices(n_roi, k=1)
    rows = np.empty((len(packed), offdiag[0].size), dtype=float)
    for start in range(0, len(packed), chunk):
        block = packed[start:start + chunk]
        matrices = np.zeros((len(block), n_roi, n_roi))
        matrices[:, full[0], full[1]] = block
        matrices[:, full[1], full[0]] = block
        rows[start:start + chunk] = matrix_logarithms(matrices)[:, offdiag[0], offdiag[1]]
    return rows


class TangentCentering(BaseEstimator, TransformerMixin):
    """Centre log-edge rows on the training-set mean — the leakage-critical step.

    The reference is fitted from training rows only, so inside a scikit-learn ``Pipeline``
    the fold's held-out subjects never influence their own features. Reimplements the
    audited benchmark's log-Euclidean tangent projection.

    Args:
        paired: if ``True``, ``X`` is ``[low | high]`` column-stacked and the output is the
            2-back-minus-0-back reconfiguration; if ``False``, ``X`` is a single condition.
    """

    def __init__(self, paired: bool = False) -> None:
        self.paired = paired

    def fit(self, X: np.ndarray, y: np.ndarray | None = None) -> "TangentCentering":
        self.reference_ = np.asarray(X, dtype=float).mean(axis=0)
        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        centered = (np.asarray(X, dtype=float) - self.reference_) * TANGENT_SCALING
        if not self.paired:
            return centered
        low, high = np.hsplit(centered, 2)
        return high - low


def network_fingerprint(correlation: np.ndarray, network_labels: np.ndarray) -> np.ndarray:
    """Within/between-network correlation means, ``(78,)`` for 12 networks.

    Reimplements the audited baseline's ``get_brain_profile``: within-network means exclude
    the diagonal, network pairs follow the upper triangle of the 12x12 network grid.
    """
    _, membership = np.unique(network_labels, return_inverse=True)
    n_networks = membership.max() + 1
    features = []
    for first in range(n_networks):
        rows = np.flatnonzero(membership == first)
        for second in range(first, n_networks):
            block = correlation[np.ix_(rows, np.flatnonzero(membership == second))]
            if first == second:
                block = block[np.triu_indices(rows.size, k=1)]
            features.append(block.mean())
    return np.asarray(features, dtype=float)
