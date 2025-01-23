@ECHO off
set /p "package=Enter the package name: "
ECHO "Installing package and dependencies..."
pip install %package%
ECHO "Updating dependencies..."
powershell -Command (pip freeze) -replace '.*=src','' > dependencies.txt
ECHO "Package installed and dependencies updated"