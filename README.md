# py-template
Python project template using cookiecutter 🍪

[![Test Project Template](https://github.com/iplitharas/project-template/actions/workflows/test.yaml/badge.svg)](https://github.com/iplitharas/project-template/actions/workflows/test.yaml)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code Style](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)




## Features
A Python project template using [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/README.html) 🍪 
with the following features:
- [pyenv](https://github.com/pyenv/pyenv) for managing Python versions
- [poetry](https://python-poetry.org/) for dependency management
- [ruff](https://github.com/astral-sh/ruff) for code style and linter enforcement
- [mypy](https://mypy.readthedocs.io/en/stable/) for static type checking
- [pre-commit](https://pre-commit.com/) hooks for code linting and formatting
- [pytest](https://docs.pytest.org/en/6.2.x/) for testing
- [make](https://www.gnu.org/software/make/) for running common tasks
- [basic multi stage docker file](https://github.com/iplitharas/project-template/blob/main/%7B%7Bcookiecutter.__project_slug%7D%7D/Dockerfile) for building and running the project.
- [GitHub Actions](https://docs.github.com/en/actions) for CI/CD


## Usage
Create a new project using the template by running the following command:
```bash
cookiecutter git@github.com:iplitharas/project-template.git
```
Go to the project directory and build it:
```bash
cd <project-name>
make setup-local-env
```

![create.gif](data/create.gif)
