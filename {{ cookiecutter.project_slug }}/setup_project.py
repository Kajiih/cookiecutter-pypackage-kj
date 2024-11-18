"""
Script to set up the python project.

- Create a virtual environment with uv
- Initializes git and a dedicated github repository

"""

import os
import shutil
import subprocess  # noqa: S404
import sys
from pathlib import Path

# Variables
REPO_NAME: str = "{{ cookiecutter.__gh_slug }}"
REPO_DESCRIPTION: str = "{{ cookiecutter.project_short_description }}"
PRIVATE: bool = False  # Set to True if the repository should be private
PY_VERSION: str = "{{ cookiecutter.minimal_python_version }}"


def run_command(command: list[str], check: bool = True) -> None:
    """Run a shell command and optionally raise an error if it fails."""
    try:
        subprocess.run(command, check=check)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        sys.exit(1)


def check_command_exists(command_name: str) -> None:
    """Check if a command exists in the system."""
    if shutil.which(command_name) is None:
        print(f"{command_name} is not installed. Aborting.")
        sys.exit(1)


def check_required_commands() -> None:
    """Check for required commands."""
    required_commands: list[str] = ["uv", "git", "gh"]
    for cmd in required_commands:
        check_command_exists(cmd)


def create_virtualenv() -> None:
    """Create a virtual environment using uv."""
    proceed = input("Do you want to create a virtual environment? (y/n): ").strip().lower()
    if proceed == "y":
        print("Creating virtual environment...")
        run_command(["uv", "venv", "--python", PY_VERSION])
        # Install dependencies
        run_command(["uv", "sync"])
    else:
        print("Skipping virtual environment creation.")


def initialize_git_repo() -> None:
    """Initialize a Git repository."""
    proceed = input("Do you want to initialize a Git repository? (y/n): ").strip().lower()
    if proceed == "y":
        print("Initializing Git repository...")
        run_command(["git", "init"])
        run_command(["git", "branch", "-M", "main"])
    else:
        print("Skipping Git repository initialization.")


def create_github_repo() -> None:
    """Create a GitHub repository."""
    proceed = input("Do you want to create a GitHub repository? (y/n): ").strip().lower()
    if proceed == "y":
        visibility: str = "--public" if not PRIVATE else "--private"
        print("Creating GitHub repository...")
        try:
            run_command([
                "gh",
                "repo",
                "create",
                REPO_NAME,
                visibility,
                "--description",
                REPO_DESCRIPTION,
                "--source",
                ".",
                "--remote",
                "origin",
            ])
        except subprocess.CalledProcessError:
            print("Failed to create GitHub repository. Aborting.")
            sys.exit(1)
    else:
        print("Skipping GitHub repository creation.")


def delete_setup_script() -> None:
    """Delete the setup script."""
    proceed = input("Do you want to delete the setup script? (y/n): ").strip().lower()
    if proceed == "y":
        script_path: Path = Path(__file__).resolve()
        print(f"Deleting setup script {script_path}...")
        script_path.unlink()
    else:
        print("Skipping deletion of setup script.")


def initial_commit_and_push() -> None:
    """Make initial commit and push to GitHub."""
    proceed = (
        input("Do you want to make the initial commit and push to GitHub? (y/n): ").strip().lower()
    )
    if proceed == "y":
        print("Setting up initial commit and pushing to GitHub...")
        run_command(["git", "add", "-A"])
        run_command(["git", "commit", "-m", "🎉 Project setup"])
        run_command(["git", "push", "origin", "main"])
    else:
        print("Skipping initial commit and push.")


def display_success_message() -> None:
    """Display the success message and instructions."""
    print("\n" + "=" * 59)
    print("🎉 Project setup successfully completed!")
    print("Virtual environment created and dependencies installed.")
    print("Git repository initialized and pushed to GitHub.")
    print("You're ready to start coding!")
    print("=" * 59 + "\n")
    # Instructions to activate virtual environment
    print("To activate the virtual environment, run:")
    if os.name == "nt":
        print(".venv\\Scripts\\activate")
    else:
        print("source .venv/bin/activate")


def main() -> None:
    check_required_commands()
    create_virtualenv()
    initialize_git_repo()
    create_github_repo()
    delete_setup_script()
    initial_commit_and_push()
    display_success_message()


if __name__ == "__main__":
    main()
