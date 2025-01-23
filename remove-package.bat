@ECHO off
set /p "package=Enter the package name to be removed: "
ECHO "Installing package and dependencies..."
pip uninstall %package%
ECHO "Updating dependencies..."
powershell -Command (pip freeze) -replace '.*=src','' > dependencies.txt
ECHO "Package removed and dependencies updated"