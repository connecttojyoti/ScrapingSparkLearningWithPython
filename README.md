# Holiday extraction from web page with Python
This is a extraction and storing in in-memory sqlite database of holidays from a web page

# Pre-requisites 
Please make sure you have the following installed
and can run them

1. Python (3.8 or later), you can use for example pyenv to manage your python versions locally
2. Poetry

# Virtual Environment setup 
## Getting Pyenv
### Homebrew in macOS
Consider installing with [Homebrew](https://brew.sh/)

brew update
brew install pyenv
brew install python@3.8

If you want to install (and update to) the latest development head of Pyenv rather than the latest release, instead run:

brew install pyenv --head

### Virtual Environment creation through Pycharm IDE
use [Virtual Environment](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)

### Virtual Environment creation through system terminal
1. Navigate to your project directory
2. Creation of virtual environment according to the directory <br>
    a. for current directory - python3.8 -m venv .venv   <br>
    b. for some other directory - python3.8 -m venv /path/to/new/virtual/environment
3. Open the project into IDE
4. Activate the virtual environment
   source .venv/bin/activate

# Install all dependencies 
Poetry install

# Setup
Run unit tests
poetry run pytest tests/unit
