#!/bin/bash
python3 -m venv .virtual-environment
echo "Local virtual environment created"
source .virtual-environment/bin/activate
echo "Local virtual environment activated, installing dependencies:"
python3 -m pip install -r dependencies.txt
echo "dependencies installed, installing this module in an editable state for sibling imports, see https://stackoverflow.com/questions/6323860/sibling-package-imports"
python3 -m pip install -e .