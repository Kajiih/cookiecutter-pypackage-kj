#!/bin/bash
# shellcheck disable=SC1083
# shellcheck source=/dev/null
cd {{ cookiecutter.project_slug }} || exit

# Virtual environment
uv venv --python {{cookiecutter.minimal_python_version}}
source .venv/bin/activate
# .venv\Scripts\activate # Windows
uv sync

# GitHub repo
git init
git remote add origin https://github.com/{{cookiecutter.__gh_slug}}
# Delete this script
rm "$(basename "$0")"
# 1st commit
git add -A
git commit -m "🎉 Project setup"
git push origin main
