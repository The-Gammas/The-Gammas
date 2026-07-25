"""Shared A/B data layer for The Gammas — HCP N-back working-memory project.

Both cohorts sit behind one interface, so downstream code never branches on the dataset:
``ds.spec_a(DATA)`` and ``ds.spec_b(DATA)`` return the same shaped object.

Reproduction note: ``preprocessing.condition_frames`` and ``condition_timeseries`` default to
``delay=HRF_DELAY`` (4.0 s haemodynamic shift). That default is load-bearing — with ``delay=0.0``
the canonical prediction drops from r = 0.366 to r = 0.152.

Submodules are imported on demand, so ``from gammas import datasets`` does not pull in
scikit-learn or pandas for callers that only need the loaders.
"""
