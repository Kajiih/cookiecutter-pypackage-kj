#!/usr/bin/env python
"""Post cookiecutter project generation hook."""

import pathlib

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"

if __name__ == "__main__":
    if "Not open source" == "{{ cookiecutter.open_source_license }}":  # noqa: PLR0133
        pathlib.Path("LICENSE").unlink()


print("\n" + "=" * 80)
print(f"{BOLD}{GREEN}🎉 PROJECT BUILT SUCCESSFULLY 🎉{RESET}")
print(f"\n{CYAN}To set up the project for development, follow these steps:{RESET}\n")
print(f"{YELLOW}1.{RESET} Navigate to the project directory: `cd {{ cookiecutter.project_slug }}`")
print(f"{YELLOW}2.{RESET} Run the setup script: `bash setup_project.sh`\n")
print("=" * 80 + "\n")
