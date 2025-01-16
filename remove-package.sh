#!/bin/bash
read -p 'Enter the package name to be removed: ' package
source .virtual-environment/bin/activate
pip uninstall $package
pip freeze > dependencies.txt
echo "package uninstalled and dependencies updated"