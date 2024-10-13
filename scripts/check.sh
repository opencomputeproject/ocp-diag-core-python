#!/bin/bash
set -eo pipefail

# run all the CI checks, for local evaluation

# linter
black . --check --diff

# typings
mypy . --check-untyped-defs

# tests
pytest -v --cov-fail-under=100
