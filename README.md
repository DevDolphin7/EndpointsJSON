# EndpointsJSON

This app is designed to help you maintain an `endpoints.json` file while developing an API.

_Manually formatting the file can be a pain_, this app allows you to _concentrate on the contents_ of the file and deals with the formatting for you. **It manages formatting for**:

-   The HTML method 🗳️
-   The endpoint path 👣
-   The detailed information for each endpoint ℹ️
-   The order of the endpoints 🔀
-   Removing an endpoint ❌
-   Adding a new endpoint with detailed information ➕

# Images

![The home screen in light mode showing the logo, breif project description and an open file button](Screenshots/Home-light.png)

![The main screen in light mode showing the editing options available](Screenshots/Main-light.png)

**_Dark theme is also available:_**  
![The home screen in dark mode showing the logo, breif project description and an open file button](Screenshots/Home-dark.png)

![The main screen in light mode showing the editing options available](Screenshots/Main-dark.png)

# Getting Started

## For Windows Users

On windows:

-   Navigate to the [latest release](https://github.com/DevDolphin7/EndpointsJSON/releases)
-   Click to download `EndpointsJSON.zip`
-   Extract all the contents to your desired installation folder
-   Open the `EndpointsJSON` folder
-   Double click the `EndpointsJSON.exe` file

## For Linux / macOS Docker Users

Navigate to the [devdolphin7/endpoints-json](https://hub.docker.com/r/devdolphin7/endpoints-json) docker repo and follow the README.

## For Developers

> 💡 Commands below assume the [software dependencies](#software) are already installed on the operating system.

_Navigate to the directory where you'd like to install it_ and run:

| Linux / Mac / WSL                                            | Windows                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `git clone https://github.com/DevDolphin7/EndpointsJSON.git` | `git clone https://github.com/DevDolphin7/EndpointsJSON.git` |
| `cd ./EndpointsJSON`                                         | `cd .\EndpointsJSON`                                         |
| `./install.sh`                                               | `.\install.bat`                                              |
| `source .virtual-environment/bin/activate`                   | `.\.virtual-environment\Scripts\activate`                    |
| `python3 src/app.py`                                         | `py src\app.py`                                              |

> 💡The install script creates a local virtual environment to install the dependencies and locally installs the src module for sibling imports.

You may wish to consider adding the virtual environment to the path of your development environment so the dependencies can be found. [To do this in VS Code](https://code.visualstudio.com/docs/python/environments):

-   Open the Command Palette 🎨
-   Look for "Python: Select Interpreter" 🐍
-   Select the one that contains ".virtual-environment"

# Dependencies

If you modify the code, to keep the list of dependencies up to date it's recommended adding and removing pip packages through the `add-package` and `remove-package` scripts 🚀

## Operating System

Tested on:

-   Windows 11 (.exe and developer setup)
-   Ubuntu 24.01 (docker and developer setup)

## Software

-   [Python 3](https://www.python.org/downloads/)
-   [pip](https://packaging.python.org/en/latest/overview/)

## Packages

Pip package dependencies are listed in dependencies.txt:

-   customtkinter==5.2.2
-   darkdetect==0.8.0
-   distro==1.9.0
-   fonttools==4.55.4
-   packaging==24.2
-   pillow==11.1.0
-   setuptools==75.8.0
-   wheel==0.45.1
-   The install script will install a local copy of the `src` directory as a module, run `pip freeze` to see it.

# Support

Feel free to drop me an email on [DevDolphin7@outlook.com](mailto:devdolphin7@outlook.com) or [raise a GitHub issue](https://github.com/DevDolphin7/EndpointsJSON/issues).

Check out the [docker site](https://hub.docker.com/r/devdolphin7/endpoints-json).

This repo is not actively maintained.
