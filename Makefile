# The Gammas — one command per thing you might want to do.
#
# Deliberately four targets. This is a live project, not a finished artifact: add a target when
# a command is worth not remembering, not to look complete.
#
# Override the interpreter if yours is not on PATH:
#   make test PYTHON=/path/to/python

PYTHON ?= python
NOTEBOOKS := pipeline/01_explore_dataset_b.ipynb pipeline/02_canonical_analysis_and_slides.ipynb

.PHONY: help test reproduce check

help:  ## Show the available targets
	@grep -E '^[a-z-]+:.*?## ' $(MAKEFILE_LIST) | awk -F':.*?## ' '{printf "  %-12s %s\n", $$1, $$2}'

test:  ## Run the unit tests (seconds, no project data needed)
	"$(PYTHON)" -m unittest discover -s tests

reproduce:  ## Re-run the analysis end to end: pipeline/01 -> 02 (needs data/, ~8 min)
	@test -d data/B_load_hcp || { echo "data/B_load_hcp missing — see data/README.md"; exit 1; }
	"$(PYTHON)" -m nbconvert --to notebook --execute --inplace \
		--ExecutePreprocessor.timeout=2400 $(NOTEBOOKS)
	@echo "Done. Check the reproduction gate in pipeline/02 cell 10: it must report pass = True."

check:  ## Tests + every notebook parses as valid nbformat
	$(MAKE) test PYTHON="$(PYTHON)"
	@"$(PYTHON)" -c "import glob, nbformat; \
		[nbformat.validate(nbformat.read(f, as_version=4)) for f in glob.glob('*/*.ipynb') + glob.glob('*/*/*.ipynb')]; \
		print('notebooks OK')"
