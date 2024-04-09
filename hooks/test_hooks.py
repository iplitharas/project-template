"""
Test cases for cookie cutter hooks.
"""

from .post_gen_project import (
    git_init,
    check_git_env,
    check_python,
    check_make,
    check_docker,
    check_poetry,
    main,
)
from unittest.mock import patch, MagicMock


MODULE = "hooks.post_gen_project"


@patch(f"{MODULE}.subprocess.run")
def test_git_init_success(mocked_subprocess_run, capsys):
    """
    Given a mocked `subprocess.run`.
    When I call the `git_init` function.
    Then I'm expecting the `subprocess.run` to be called with the correct arguments.
    and the right output to be printed to the console.
    """
    # Given/When
    result = git_init()

    # Then
    assert result is True
    mocked_subprocess_run.assert_called_once_with(
        ["git", "init"], capture_output=True, check=True
    )
    captured = capsys.readouterr()
    assert "Initialize git" in captured.out
    assert result is True


@patch(f"{MODULE}.subprocess.run")
def test_git_init_failure(mocked_subprocess_run, capsys):
    """
    Given a mocked `subprocess.run` where it raises an exception
    When I call the `git_init` function
    Then I'm expecting the `subprocess.run` to be called with the correct arguments.
    and the right output to be printed to the console.
    """
    # Given
    mocked_subprocess_run.side_effect = Exception("Git is not installed")

    # When
    result = git_init()
    # Then
    assert result is False
    mocked_subprocess_run.assert_called_once_with(
        ["git", "init"], capture_output=True, check=True
    )
    captured = capsys.readouterr()
    assert "Initialize git" in captured.out
    assert "Git is not installed" in captured.out


@patch(f"{MODULE}.subprocess.run")
def test_check_git_env_success(mocked_subprocess_run, capsys):
    """
    Given a mocked `subprocess.run`.
    When I call the `check_git_env` function.
    Then I'm expecting the `subprocess.run` to be called with the correct arguments.
    """
    # Given/When
    result = check_git_env()

    # Then
    assert result is True
    mocked_subprocess_run.assert_called_once_with(
        ["git", "rev-parse", "--is-inside-work-tree"], capture_output=True, check=True
    )
    captured = capsys.readouterr()
    assert "Checking if git environment exists" in captured.out
    assert result is True


@patch(f"{MODULE}.subprocess.run")
def test_check_git_env_failure(mocked_subprocess_run, capsys):
    """
    Given a mocked `subprocess.run` where it raises an exception
    When I call the `check_git_env` function.
    Then I'm expecting the `subprocess.run` to be called with the correct arguments.
    """
    # Given
    mocked_subprocess_run.side_effect = Exception("No git repo found")
    # When
    result = check_git_env()

    # Then
    mocked_subprocess_run.assert_called_once_with(
        ["git", "rev-parse", "--is-inside-work-tree"], capture_output=True, check=True
    )
    captured = capsys.readouterr()
    assert "Checking if git environment exists" in captured.out
    assert "No git repo found" in captured.out
    assert result is False


@patch(f"{MODULE}.subprocess.run")
@patch(f"{MODULE}.REQUESTED_PYTHON_VERSION", "3.8.0")
def test_check_python_success(mocked_subprocess_run, capsys):
    """
    Given a mocked `subprocess.run`.
    When I call the `check_python` function.
    Then I'm expecting the `subprocess.run` to be called with the correct arguments.
    """
    # Given/When
    result = check_python()
    # Then
    assert result is True
    mocked_subprocess_run.assert_called_once_with(
        ["pyenv", "local", "3.8.0"], capture_output=True, check=True
    )
    captured = capsys.readouterr()
    assert "Checking if `python` using pyenv is installed" in captured.out
    assert "Found" in captured.out
    assert result is True


@patch(f"{MODULE}.subprocess.run")
@patch(f"{MODULE}.REQUESTED_PYTHON_VERSION", "3.8.0")
def test_check_python_failure(mocked_subprocess_run, capsys):
    """
    Given a mocked `subprocess.run` where it raises an exception
    When I call the `check_python` function.
    Then I'm expecting the `subprocess.run` to be called with the correct arguments.
    """
    # Given
    mocked_subprocess_run.side_effect = Exception("Python is not installed")
    # When
    result = check_python()
    # Then
    assert result is False
    mocked_subprocess_run.assert_called_once_with(
        ["pyenv", "local", "3.8.0"], capture_output=True, check=True
    )
    captured = capsys.readouterr()
    assert "Checking if `python` using pyenv is installed" in captured.out
    assert "Python is not installed" in captured.out


@patch(f"{MODULE}.subprocess.run")
def test_check_make_success(mocked_subprocess_run, capsys):
    """
    Given a mocked `subprocess.run`.
    When I call the `check_make` function.
    Then I'm expecting the `subprocess.run` to be called with the correct arguments.
    """
    # Given/When
    result = check_make()
    # Then
    assert result is True
    mocked_subprocess_run.assert_called_once_with(
        ["make", "--version"], capture_output=True, check=True
    )
    captured = capsys.readouterr()
    assert "Checking if make is installed" in captured.out
    assert "Found" in captured.out
    assert result is True


@patch(f"{MODULE}.subprocess.run")
def test_check_make_failure(mocked_subprocess_run, capsys):
    """
    Given a mocked `subprocess.run` where it raises an exception
    When I call the `check_make` function.
    Then I'm expecting the `subprocess.run` to be called with the correct arguments.
    """
    # Given
    mocked_subprocess_run.side_effect = Exception("Make is not installed")
    # When
    result = check_make()
    # Then
    assert result is False
    mocked_subprocess_run.assert_called_once_with(
        ["make", "--version"], capture_output=True, check=True
    )
    captured = capsys.readouterr()
    assert "Checking if make is installed" in captured.out
    assert "make is not installed" in captured.out


@patch(f"{MODULE}.subprocess.run")
def test_check_docker_success(mocked_subprocess_run, capsys):
    """
    Given a mocked `subprocess.run`.
    When I call the `check_docker` function.
    Then I'm expecting the `subprocess.run` to be called with the correct arguments.
    """
    # Given/When
    result = check_docker()
    # Then
    assert result is True
    mocked_subprocess_run.assert_called_once_with(
        ["docker", "--version"], capture_output=True, check=True
    )
    captured = capsys.readouterr()
    assert "Checking if docker is installed" in captured.out
    assert "Found" in captured.out
    assert result is True


@patch(f"{MODULE}.subprocess.run")
def test_check_docker_failure(mocked_subprocess_run, capsys):
    """
    Given a mocked `subprocess.run` where it raises an exception
    When I call the `check_docker` function.
    Then I'm expecting the `subprocess.run` to be called with the correct arguments.
    """
    # Given
    mocked_subprocess_run.side_effect = Exception("Docker is not installed")
    # When
    result = check_docker()
    # Then
    assert result is False
    mocked_subprocess_run.assert_called_once_with(
        ["docker", "--version"], capture_output=True, check=True
    )
    captured = capsys.readouterr()
    assert "Checking if docker is installed" in captured.out
    assert "Docker is not installed" in captured.out


@patch(f"{MODULE}.subprocess.run")
@patch(f"{MODULE}.REQUESTED_POETRY_VERSION", "9.9.9")
def test_check_poetry_success(mocked_subprocess_run, capsys):
    """
    Given a mocked `subprocess.run`.
    When I call the `check_poetry` function.
    Then I'm expecting the `subprocess.run` to be called with the correct arguments.
    """
    # Given
    mocked_subprocess_run.return_value = MagicMock(stdout=b"Poetry version 9.9.9")
    # When
    result = check_poetry()

    # Then
    assert result is True
    mocked_subprocess_run.assert_called_once_with(
        ["poetry", "--version"], capture_output=True, check=True
    )
    captured = capsys.readouterr()
    assert "Checking if `poetry` is installed" in captured.out
    assert "Found" in captured.out
    assert result is True


@patch(f"{MODULE}.subprocess.run")
@patch(f"{MODULE}.REQUESTED_POETRY_VERSION", "9.9.9")
def test_check_poetry_fails_due_to_wrong_version(mocked_subprocess_run, capsys):
    """
    Given a mocked `subprocess.run`.
    When I call the `check_poetry` function where the installed poetry version
    is different that the requested version.
    Then I'm expecting the `subprocess.run` to be called with the correct arguments.
    """
    # Given
    mocked_subprocess_run.return_value = MagicMock(stdout=b"Poetry version 1.0.0")
    # When
    result = check_poetry()
    # Then
    assert result is False
    mocked_subprocess_run.assert_called_once_with(
        ["poetry", "--version"], capture_output=True, check=True
    )
    captured = capsys.readouterr()
    assert "Checking if `poetry` is installed" in captured.out
    assert "Poetry version: `9.9.9` is not installed. Found: `1.0.0`" in captured.out


@patch(f"{MODULE}.subprocess.run")
def test_check_poetry_fails_due_to_missing_poetry_installation(
    mocked_subprocess_run, capsys
):
    """
    Given a mocked `subprocess.run`.
    When I call the `check_poetry` function and the `poetry` is not installed
    Then I'm expecting the `subprocess.run` to be called with the correct arguments.
    """
    # Given
    mocked_subprocess_run.side_effect = Exception("Poetry is not installed")
    # When
    result = check_poetry()
    # Then
    assert result is False
    mocked_subprocess_run.assert_called_once_with(
        ["poetry", "--version"], capture_output=True, check=True
    )
    captured = capsys.readouterr()
    assert "Checking if `poetry` is installed" in captured.out
    assert "poetry is not installed" in captured.out


@patch(f"{MODULE}.check_docker")
@patch(f"{MODULE}.check_make")
@patch(f"{MODULE}.check_poetry")
@patch(f"{MODULE}.check_python")
def test_main_runs_the_right_checks_and_create_project(
    mocked_check_python,
    mocked_check_poetry,
    mocked_check_make,
    mocked_check_docker,
    capsys,
):
    """
    Given `mocked functions` where all of them return `True`.
    When I call the `main` function
    Then I'm expecting the right functions to be called.
    and the project to be created successfully.
    """
    # Given
    mocked_check_python.return_value = True
    mocked_check_poetry.return_value = True
    mocked_check_make.return_value = True
    mocked_check_docker.return_value = True
    # When
    result = main()
    # Then
    assert result is None
    mocked_check_python.assert_called_once()
    mocked_check_poetry.assert_called_once()
    mocked_check_make.assert_called_once()
    mocked_check_docker.assert_called_once()
    captured = capsys.readouterr()
    assert "Project created successfully" in captured.out
