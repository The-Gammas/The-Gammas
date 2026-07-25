"""Analysis methods contributed by teammates, kept under their authorship.

**Why this module exists.** Some of the methods this project rests on were designed by other
members of the team, not by whoever moved them into the shared layer. Burying them among our
own functions would erase that, and copying them into every notebook that needs them makes the
same logic drift in several places at once. This module is the single home for that code, with
the author, the origin file and the commit stated next to each function.

**The rule, and it matters.** These implementations are *not* refactored, renamed or "improved".
They are the author's method. If one of them looks wrong, that is a conversation to have with
its author and a change to make together — not a silent edit here. Only the docstring and the
type hints are ours.

**Their own notebooks keep their own copies, on purpose.** Nothing here asks a contributor to
import from us. `sandbox/goutham/FCM_entropy.ipynb` and `pipeline/04_goutham_pipeline_
reconciliation.ipynb` both keep an inline definition, and that is deliberate: the sandbox is
where the author reads and reasons about his own logic, and `pipeline/04` is a dated record of
the reconciliation exactly as it ran. This module gives *us* one mapped, tested copy for shared
analyses; it does not take theirs away.

Map of contributed methods across the repo:

| Method | Author | Lives in | Origin |
|---|---|---|---|
| `measure_system_segregation` | Goutham Arcod | here | `sandbox/goutham/FCM_entropy.ipynb` (`f886169`) |
| `network_fingerprint` | Goutham Arcod (as `get_brain_profile`) | :mod:`gammas.connectivity` | `sandbox/goutham/per_analysis.ipynb` (`5071ccd`) |

`network_fingerprint` stays in :mod:`gammas.connectivity` because eight call sites across two
pipeline notebooks import it from there; its attribution lives in its own docstring. This table
is the complete map, so the split does not hide anything.

See `AUTHORS.md` for CRediT roles and `docs/final-report.md` §12 for the narrative.
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
