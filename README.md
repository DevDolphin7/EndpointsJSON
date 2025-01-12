# Getting Started

## For Linux / Mac / WSL developers
- `git clone https://github.com/DevDolphin7/EndpointsJSON.git`
- `cd ./EndpointsJSON`
- `./install.sh` <- this script creates a local virtual environment to install the dependencies
- `source .virtual-environment/bin/activate`
- `python app.py`

You may wish to consider adding the virtual environment to the path of your development environment so the dependencies can be found. [To do this in VS Code](https://code.visualstudio.com/docs/python/environments):
- Open the Command Palette
- Look for "Python: Select Interpreter"
- Select the one that contains ".virtual-environment"

To update the list of dependencies, run `pip freeze > dependencies.txt`