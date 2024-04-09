"""
Post generation hooks:
https://cookiecutter.readthedocs.io/en/1.7.2/advanced/hooks.html
"""

import sys
import re
import subprocess
from dataclasses import dataclass


REQUESTED_PYTHON_VERSION = "{{ cookiecutter.python_version }}"
REQUESTED_POETRY_VERSION = "{{ cookiecutter.poetry_version }}"
PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_SLUG = "{{ cookiecutter.__project_slug }}"
SETUP_GIT = "{{ cookiecutter.init_git }}"


@dataclass(frozen=True)
class Colors:
    """
    Colors
    """

    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def git_init() -> bool:
    """
    Initialize git
    """
    try:
        print(f"{Colors.HEADER}Initialize git...{Colors.RESET}")
        subprocess.run(["git", "init"], capture_output=True, check=True)
        return True
    except Exception as error:
        print(f"{Colors.FAIL}Git is not installed: {error}{Colors.RESET}")
        return False


def check_git_env() -> bool:
    """
    Check if git environment exists
    """
    try:
        print(f"{Colors.HEADER}Checking if git environment exists...{Colors.RESET}")
        subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            capture_output=True,
            check=True,
        )
        print("Found 👾: git repo initialized")
        return True
    except Exception:
        print(
            f"{Colors.FAIL}🚨🚨 No git repo found: either run this inside "
            f"a git repo or select git init (y) 🚨🚨{Colors.RESET}"
        )
        return False


def check_python() -> bool:
    """
    Check if python is installed
    """
    try:
        print(
            f"{Colors.HEADER}Checking if `python` using pyenv is installed...{Colors.RESET}"
        )

        subprocess.run(
            ["pyenv", "local", REQUESTED_PYTHON_VERSION],
            capture_output=True,
            check=True,
        )
        print("Found 🐍: ", REQUESTED_PYTHON_VERSION)
        return True
    except Exception:
        print(f"{Colors.FAIL}🐛 Python is not installed{Colors.RESET}")
        print(
            f"{Colors.GREEN}Please install python using pyenv: `pyenv download"
            f" {REQUESTED_PYTHON_VERSION}`{Colors.RESET} "
        )
        return False


def check_make() -> bool:
    """
    Check if make is installed
    """
    try:
        print(f"{Colors.HEADER}Checking if make is installed...{Colors.RESET}")
        result = subprocess.run(["make", "--version"], capture_output=True, check=True)
        version = result.stdout.decode("utf-8").strip()
        print("Found 🛠️: ", version)
        return True
    except Exception:
        print("🚨🚨 make is not installed 🚨🚨")
        return False


def check_poetry() -> bool:
    """
    Check if poetry is installed
    """
    try:
        print(f"{Colors.HEADER}Checking if `poetry` is installed...{Colors.RESET}")
        result = subprocess.run(
            ["poetry", "--version"], capture_output=True, check=True
        )
        version = result.stdout.decode("utf-8").strip()
        match = re.search(r"(\d+\.\d+\.\d+)", version)

        if match:
            poetry_version = match.group(1)
            if poetry_version != REQUESTED_POETRY_VERSION:
                print(
                    f"{Colors.FAIL}Poetry version:"
                    f" `{REQUESTED_POETRY_VERSION}` is not installed. "
                    f"Found: `{poetry_version}` "
                    f"{Colors.RESET}"
                )
                return False

        print("Found 🐍: ", version)
        return True
    except Exception:
        print(f"{Colors.FAIL}poetry is not installed{Colors.FAIL}")
        return False


def check_docker() -> bool:
    """
    Check if docker is installed
    """
    try:
        print(f"{Colors.HEADER}Checking if docker is installed...{Colors.RESET}")
        result = subprocess.run(
            ["docker", "--version"], capture_output=True, check=True
        )
        version = result.stdout.decode("utf-8").strip()
        print("Found 🐳: ", version)
        return True
    except Exception:
        print(f"{Colors.FAIL}Docker is not installed{Colors.RESET}")
        return False


def main():
    mandatory_checks = [
        check_python,
        check_poetry,
    ]

    optional_checks = [
        check_make,
        check_docker,
    ]

    print("⌛ Checking dependencies...")
    for check in mandatory_checks:
        if not check():
            sys.exit(1)
    for check in optional_checks:
        check()

    if SETUP_GIT == "True":
        if not git_init():
            sys.exit(1)
    elif SETUP_GIT == "False":
        if not check_git_env():
            sys.exit(1)

    print("🚀🚀 Project created successfully 🚀🚀")


if __name__ == "__main__":
    sys.exit(main())
