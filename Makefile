# The Gammas — the two commands worth not remembering.
#
# Override the interpreter if yours is not on PATH:  make test PYTHON=/path/to/python

PYTHON ?= python

.PHONY: test reproduce

test:
	"$(PYTHON)" -m unittest discover -s tests

reproduce:   # re-run the analysis end to end (needs data/, ~8 min)
	@test -d data/B_load_hcp || { echo "data/B_load_hcp missing — see data/README.md"; exit 1; }
	"$(PYTHON)" -m nbconvert --to notebook --execute --inplace \
		--ExecutePreprocessor.timeout=2400 \
		pipeline/01_explore_dataset_b.ipynb pipeline/02_canonical_analysis_and_slides.ipynb
	@echo "Done. pipeline/02 cell 10 must report pass = True."
