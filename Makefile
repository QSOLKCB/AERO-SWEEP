GPRBUILD ?= gprbuild
GNATPROVE ?= gnatprove
PYTHON ?= python3

.PHONY: all build prove test test-oracle test-differential clean

all: test

build:
	$(GPRBUILD) -p -P tests/det2_cli.gpr

prove:
	$(GNATPROVE) -P kernel/aero_sweep.gpr --level=2

test-oracle:
	$(PYTHON) -B -m unittest tests.test_oracle -v

test-differential: build
	$(PYTHON) -B -m unittest tests.test_differential -v

test: build test-oracle test-differential

clean:
	gprclean -r -P tests/det2_cli.gpr
