python3 -m venv .virtual-environment
echo "Local virtual environment created"
source .virtual-environment/bin/activate
echo "Local virtual environment activated, installing dependencies:"
python3 -m pip install -r dependencies.txt