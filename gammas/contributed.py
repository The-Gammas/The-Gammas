"""Analysis methods contributed by teammates, kept under their authorship.

**These implementations are not refactored, renamed or "improved" here.** They are the author's
method, and the numbers the project reports are attributed to them: a well-meaning edit to
``measure_system_segregation`` would change the ΔSegregation = −0.0236 that
``docs/final-report.md`` credits to Goutham Arcod. If one looks wrong, that is a conversation
with its author, not a commit here.

``network_fingerprint`` is also his method but lives in :mod:`gammas.connectivity`, where its
eight call sites import it from. Roles and evidence: ``AUTHORS.md``.
"""

from __future__ import annotations

import numpy as np


def measure_system_segregation(fc_matrix: np.ndarray, network_names: np.ndarray,
                               societies) -> float:
    """Chan-style system segregation, ``(W - B) / W``. **Goutham Arcod's method, verbatim.**

    Origin: ``measure_system_segregation`` in `sandbox/goutham/FCM_entropy.ipynb`
    (commit ``f886169``). Moved here unchanged so the group-level direction this project
    reports is his method and not a re-derivation of it. Chan et al. 2014, PNAS.

    Within-network means take the strict upper triangle, so the diagonal never inflates ``W``,
    and a network contributes to ``W`` only when its within-network mean is positive.

    Args:
        fc_matrix: ``(n_roi, n_roi)`` functional-connectivity matrix for one condition.
        network_names: ``(n_roi,)`` network label per ROI.
        societies: the network labels to iterate over.

    Returns:
        Segregation index, or ``0.0`` when no network has a positive within-network mean.
    """
    within_vals, between_vals = [], []
    for netA in societies:
        idxA = np.where(network_names == netA)[0]
        idx_other = np.where(network_names != netA)[0]
        sub = fc_matrix[np.ix_(idxA, idxA)]
        n = len(idxA)
        if n > 1:
            w_in = sub[np.triu_indices(n, k=1)].mean()
            if w_in > 0:
                within_vals.append(w_in)
        between_vals.append(fc_matrix[np.ix_(idxA, idx_other)].mean())
    mean_within = np.mean(within_vals) if within_vals else 0.0
    mean_between = np.mean(between_vals) if between_vals else 0.0
    return (mean_within - mean_between) / mean_within if mean_within > 0 else 0.0
