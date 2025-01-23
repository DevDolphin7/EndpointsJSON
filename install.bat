py -m venv .virtual-environment
ECHO "Local virtual environment created"
powershell -Command .\.virtual-environment\Scripts\activate
ECHO "Local virtual environment activated, installing dependencies:"
py -m pip install -r dependencies.txt
ECHO "dependencies installed, installing this module in an editable state for sibling imports, see https://stackoverflow.com/questions/6323860/sibling-package-imports"
py -m pip install -e .