#!/bin/bash
read -p 'Enter the module name to be removed: ' module
source .virtual-environment/bin/activate
pip uninstall $module
pip freeze > dependencies.txt