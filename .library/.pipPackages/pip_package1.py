#A package is a collection of modules that are organized in a directory hierarchy. A module is a single file that contains Python code, while a package is a directory that contains multiple modules and an __init__.py file.
#Pip allows you to install packages from the Python Package Index (PyPI) and other repositories. It is a command-line tool that you can use to manage your Python packages, including installing, upgrading, and uninstalling them.

# To create a pip package, you need to use this command. pip install packagename


import cowsay, sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[2] + "!")
else:
    cowsay.cow("Hello, World!")

