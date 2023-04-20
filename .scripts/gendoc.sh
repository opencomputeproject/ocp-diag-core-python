#!/bin/bash
set -eo pipefail

cd docs/src
sphinx-build -M markdown . _build
mv _build/markdown/*.md ..
