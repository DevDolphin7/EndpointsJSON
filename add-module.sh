#!/bin/bash
read -p 'Enter the module name: ' module
source .virtual-environment/bin/activate
pip install $module
pip freeze > dependencies.txt