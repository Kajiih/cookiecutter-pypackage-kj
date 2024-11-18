#!/usr/bin/env python
"""Post cookiecutter project generation hook."""

import pathlib
import shutil

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"


def get_python_command() -> str:
    """Determine whether 'python3' or 'python' should be used."""
    if shutil.which("python3"):
        return "python3"
    return "python"  # Default to 'python' if neither is found


if __name__ == "__main__":
    if "Not open source" == "{{ cookiecutter.open_source_license }}":  # noqa: PLR0133
        pathlib.Path("LICENSE").unlink()

    python_cmd = get_python_command()

    print("\n" + "=" * 80)
    print(f"{BOLD}{GREEN}🎉 PROJECT BUILT SUCCESSFULLY 🎉{RESET}")
    print(f"\nTo set up the project for development, follow these steps:\n")
    print(
        f"{YELLOW}1.{RESET} Navigate to the project directory: {GREEN}cd {{ cookiecutter.project_slug }}{RESET}"
    )
    print(f"{YELLOW}2.{RESET} Run the setup script: {GREEN}{python_cmd} setup_project.py{RESET}\n")
    print("=" * 80 + "\n")
