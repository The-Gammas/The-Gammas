"""Shared A/B data layer for The Gammas — HCP N-back working-memory project.

Both HCP cohorts sit behind one interface, so downstream code never branches on the
dataset: ``ds.spec_a(DATA)`` and ``ds.spec_b(DATA)`` return the same shaped object.

Layering, bottom-up — each module may import the ones above it, never the reverse:

    datasets       config + raw reads from disk (subject lists, parcellated BOLD)
    preprocessing  condition segmentation (0-back / 2-back), behaviour tables
    connectivity   functional-connectivity transformers (Pearson, tangent space)
    evaluation     cross-validation, permutation nulls, leakage-safe splits

Usage from a notebook at any depth in the repo::

    sys.path.insert(0, str(ROOT))
    from gammas import datasets as ds, preprocessing as pp, evaluation as ev

Reproduction note: ``preprocessing.condition_frames`` and ``condition_timeseries``
default to ``delay=4.0`` seconds (haemodynamic shift). That default is load-bearing —
with ``delay=0.0`` the canonical prediction drops from r = 0.366 to r = 0.152. See
``docs/final-report.md`` and ``docs/data-dictionary.md``.
"""

from . import connectivity, datasets, evaluation, preprocessing

__all__ = ["datasets", "preprocessing", "connectivity", "evaluation"]
