"""
Script to set up the python project.

- Create a virtual environment with uv
- Initializes git and a dedicated github repository

"""

import os
import subprocess
import sys
from pathlib import Path

# Variables
REPO_NAME = "{{ cookiecutter.__gh_slug }}"
REPO_DESCRIPTION = "{{ cookiecutter.project_short_description }}"
PRIVATE = False  # Set to True if the repository should be private
PY_VERSION = "{{ cookiecutter.minimal_python_version }}"


def run_command(command, check=True):
    """Run a shell command and optionally raise an error if it fails."""
    try:
        subprocess.run(command, shell=True, check=check)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        sys.exit(1)


def check_command_exists(command_name):
    """Check if a command exists in the system."""
    if not shutil.which(command_name):
        print(f"{command_name} is not installed. Aborting.")
        sys.exit(1)


def main():
    # Check for required commands
    required_commands = ["uv", "git", "gh"]
    for cmd in required_commands:
        check_command_exists(cmd)

    # Virtual environment
    print("Creating virtual environment...")
    run_command(f"uv venv --python {PY_VERSION}")

    if os.name == "nt":  # Windows
        activate_command = ".venv\\Scripts\\activate"
    else:  # MacOS/Linux
        activate_command = "source .venv/bin/activate"

    run_command(activate_command)
    run_command("uv sync")

    # Initialize Git repository
    print("Initializing Git repository...")
    run_command("git init")
    run_command("git branch -M main")

    # GitHub repo creation
    visibility = "--public" if not PRIVATE else "--private"
    print("Creating GitHub repository...")
    try:
        run_command(
            f'gh repo create "{REPO_NAME}" {visibility} --description "{REPO_DESCRIPTION}" --source . --remote origin'
        )
    except subprocess.CalledProcessError:
        print("Failed to create GitHub repository. Aborting.")
        sys.exit(1)

    # Delete this script (optional)
    script_path = Path(__file__).resolve()
    print(f"Deleting setup script {script_path}...")
    script_path.unlink()

    # Initial commit and push
    print("Setting up initial commit and pushing to GitHub...")
    run_command("git add -A")
    run_command('git commit -m "🎉 Project setup"')
    run_command("git push origin main")

    # Success message
    print("\n===========================================================")
    print("🎉 Project setup successfully completed!")
    print("Git repository initialized and pushed to GitHub.")
    print("Virtual environment created and dependencies installed.")
    print("You're ready to start coding!")
    print("===========================================================\n")


if __name__ == "__main__":
    import shutil

    main()
