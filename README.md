# PhysiScript
![GitHub](https://img.shields.io/github/license/shaiavr/physiscript?style=flat-square)

***
## Getting Started

### Prerequisites

Python 3.10 or higher is required. In additional, [poetry](https://python-poetry.org/) is required to setup a virtual environment and install dependencies.

### Installing Poetry

Open a terminal (or PowerShell on Windows) and run the following command:

* For Mac/Linux: `curl -sSL https://install.python-poetry.org | python -`
* For Windows (Using PowerShell): `(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -`

Run `poetry --version` to verify the installation succeeded.

### Setting up the project

1. Clone the repo: `git clone https://github.com/ShaiAvr/PhysiScript.git`
2. Setup environment and install dependencies: `poetry install`
3. Activate the virtual environment using `poetry shell` (or run commands using `poetry run`)
4. Install [pre-commit](https://pre-commit.com/) hooks: `pre-commit install`

### Optional steps

The project uses [flakeheaven](https://flakeheaven.readthedocs.io/en/latest/) to for linting. If your IDE supports setting `flake8` path, set it to `[VIRTUAL-ENV-PATH]/bin/flake8heavened` or `[VIRTUAL-ENV-PATH]/bin/flake8heavened.exe` on Windows where `VIRTUAL-ENV-PATH` is the path to the virtual environment created by poetry (you can run `poetry env info` to find the location of the virtual environment).
