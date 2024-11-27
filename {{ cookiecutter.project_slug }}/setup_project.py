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

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
RED = "\033[31m"

# Variables
REPO_NAME: str = "{{ cookiecutter.__gh_slug }}"
REPO_DESCRIPTION: str = "{{ cookiecutter.project_short_description }}"
PRIVATE: bool = False  # Set to True if the repository should be private
PY_VERSION: str = "{{ cookiecutter.minimal_python_version }}"


def run_command(command: list[str], check: bool = True) -> None:
    """Run a shell command and optionally raise an error if it fails."""
    try:
        subprocess.run(command, check=check)  # noqa: S603
    except subprocess.CalledProcessError as e:
        print(f"{RED}Command failed: {e}{RESET}")
        sys.exit(1)


def check_command_exists(command_name: str) -> None:
    """Check if a command exists in the system."""
    if shutil.which(command_name) is None:
        print(f"{RED}{command_name} is not installed. Aborting.{RESET}")
        sys.exit(1)


def check_required_commands() -> None:
    """Check for required commands."""
    required_commands: list[str] = ["uv", "git", "gh"]
    for cmd in required_commands:
        check_command_exists(cmd)


def create_virtualenv() -> None:
    """Create a virtual environment using uv."""
    proceed = input("\nDo you want to create a virtual environment? (Y/n): ").strip().lower()
    if proceed != "n":
        print(f"{GREEN}Creating virtual environment...{RESET}")
        run_command(["uv", "venv", "--python", PY_VERSION])
        # Install dependencies
        print(f"{GREEN}Installing dependencies...{RESET}")
        run_command(["uv", "sync"])
    else:
        print(f"{YELLOW}Skipping virtual environment creation.{RESET}")


def initialize_git_repo() -> None:
    """Initialize a Git repository."""
    proceed = input("\nDo you want to initialize a Git repository? (Y/n): ").strip().lower()
    if proceed != "n":
        print(f"{GREEN}Initializing Git repository...{RESET}")
        run_command(["git", "init"])
        run_command(["git", "branch", "-M", "main"])
    else:
        print(f"{YELLOW}Skipping Git repository initialization.{RESET}")


def create_github_repo() -> None:
    """Create a GitHub repository."""
    proceed = input("\nDo you want to create a GitHub repository? (Y/n): ").strip().lower()
    if proceed != "n":
        visibility: str = "--public" if not PRIVATE else "--private"
        print(f"{GREEN}Creating GitHub repository...{RESET}")
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
            print(f"{RED}Failed to create GitHub repository. Aborting.{RESET}")
            sys.exit(1)
    else:
        print(f"{YELLOW}Skipping GitHub repository creation.{RESET}")


def delete_setup_script() -> None:
    """Delete the setup script."""
    proceed = input("\nDo you want to delete the setup script? (Y/n): ").strip().lower()
    if proceed != "n":
        script_path: Path = Path(__file__).resolve()
        print(f"{GREEN}Deleting setup script {script_path}...{RESET}")
        script_path.unlink()
    else:
        print(f"{YELLOW}Skipping deletion of setup script.{RESET}")


def initial_commit_and_push() -> None:
    """Make initial commit and push to GitHub."""
    proceed = (
        input("\nDo you want to make the initial commit and push to GitHub? (Y/n): ")
        .strip()
        .lower()
    )
    if proceed != "n":
        print(f"{GREEN}Setting up initial commit and pushing to GitHub...{RESET}")
        run_command(["git", "add", "-A"])
        run_command(["git", "commit", "-m", "🎉 Project setup"])
        run_command(["git", "push", "origin", "main"])
    else:
        print(f"{YELLOW}Skipping initial commit and push.{RESET}")


def display_success_message() -> None:
    """Display the success message and instructions."""
    print("\n" + "=" * 59)
    print(f"{BOLD}{GREEN}🎉 Project setup successfully completed!{RESET}")
    print("\nYou're ready to start coding!\n")

    # Instructions to activate virtual environment
    if os.name == "nt":
        activate_command = f"{GREEN}.venv\\Scripts\\activate{RESET}"
    else:
        activate_command = f"{GREEN}source .venv/bin/activate{RESET}"
    print(f"To activate the virtual environment, run: {activate_command}")
    print("=" * 59 + "\n")


def main() -> None:
    """Run all setup commands."""
    check_required_commands()
    create_virtualenv()
    initialize_git_repo()
    create_github_repo()
    delete_setup_script()
    initial_commit_and_push()
    display_success_message()


if __name__ == "__main__":
    main()
