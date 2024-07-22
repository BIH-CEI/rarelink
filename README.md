# PythonTemplate
This repository contains a simple template for Python repositories, including actions and a `.gitignore` file. The actions include organizing imports with `isort`, linting using `ruff`, automatic test execution using `pytest`, as well as a small coverage report with `coverage` on merging to the main branch.

## Get started

First, clone the repository.

Create the `main`, `develop` and, `gh-pages` branches.

Whenever you want to change something, create a new branch. If it is done, create a pull request to the `develop` branch.

Only pull from `develop` to `main` with fully functional, tested and documented new versions.

### Repository Settings
**Branch Protection Rules**
1. Go to the repository settings
2. Open `Branches` in the left sidebar
3. Click `Add branch ruleset`
4. Choose an appropriate ruleset name, such as `Branch protection rules for main and develop`
5. Under `target branches`, enter `main` and `develop`
6. Under `Rules` select at least:
    - `Restricht deletions`
    - `Require linear history`
    - `Require a pull request before merging`
      - Select an appropriate number of reviewers
      - 
    - `Block force pushes`
7. Click `Create` to finish. you can now find the ruleset under `Rules`>`Rulesets`

**Actions Permissions**
1. Go to the repository settings
2. Open `Actions` > `General` in the left sidebar
3. Under `Workflow permissions`, select
   - `Read and write permissions`
   - `Allow GitHub Actions to create and approve pull requests`

### Set Up Project
1. [Optional] Create a new virtual environment
2. Run `pip install -e .[test,docs]`

**Documentation Setup**
1. Create a `docs` folder in the root of the project and open it (`mkdir docs && cd docs`)
2. Run `spinx-quickstart` to create a new documentation (On Windows, run `sphinx-quickstart.exe`). Fill out all relevant information.
    - Select no `[n]` when asked `Separate source and build directories (y/n) [n]`
3. [Optionally] Run `make html` to build the documentation (On Windows, might have to write full path to `make.bat`).
4. Copy `docs/conf.py` into your own docs folder, replacing the existing one.
5. Change all relevant fields in the `pyproject.toml` and `docs/conf.py` files. (Don't forget the intersphinx setup)

If you want to run sphinx locally: 
- `sphinx-apidoc --separate --module-first -d 2 -H "API reference" --follow-links -o apidocs ../src/template_for_python_projects`
- `make.bat` html
- Open `docs/_build/html/index.html` in your browser



You can also add a badge like this one to your README.md file:
[![Build status](https://github.com/frehburg/TemplateForPythonProjects/workflows/CI/badge.svg)](https://github.com/frehburg/TemplateForPythonProjects/actions/workflows/python_ci.yml)  
[Stable Documentation](https://frehburg.github.io/TemplateForPythonProjects/stable/)  
[Latest Documentation](https://frehburg.github.io/TemplateForPythonProjects/latest/)  

See here a template for your README

# Project Name

Brief description of your project.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Description

A brief overview of your project and its purpose.

## Features

List the key features of your project.

## Getting Started

Instructions on how to set up and run your project locally.

### Prerequisites

List any software, libraries, or dependencies that need to be installed before setting up the project.

### Installation

Step-by-step instructions on how to install and set up your project.

To install your own code run `pip install -e .` in a terminal

## Features

Provide examples and explanations of how your project can be used. Include code snippets or screenshots if necessary.

## Contributing

Guidelines for contributing to your project. Include information about how others can contribute, submit issues, and create pull requests.

## License

Specify the license under which your project is distributed.

## Acknowledgements