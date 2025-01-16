#!/bin/bash
read -p 'Enter the package name: ' package
source .virtual-environment/bin/activate
pip install $package
pip freeze > dependencies.txt
echo "package installed and dependencies updated"