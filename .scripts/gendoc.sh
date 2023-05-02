#!/bin/bash
set -eo pipefail

# this script will build the markdown api reference docs
# make sure that requirements.txt have been installed

cd docs/src
sphinx-build -M markdown . _build
mv _build/markdown/*.md ..
