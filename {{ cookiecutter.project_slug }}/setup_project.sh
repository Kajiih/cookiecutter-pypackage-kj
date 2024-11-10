#!/bin/bash
# shellcheck disable=SC1083
# shellcheck source=/dev/null

# Variables
PROJECT_SLUG="{{ cookiecutter.project_slug }}"
REPO_NAME="{{ cookiecutter.__gh_slug }}"
REPO_DESCRIPTION="{{ cookiecutter.project_short_description }}"
PRIVATE=false # Set to true if the repository should be private
PY_VERSION="{{ cookiecutter.minimal_python_version }}"

# Check for required commands
command -v uv >/dev/null 2>&1 || {
    echo >&2 "uv is not installed. Aborting."
    exit 1
}
command -v git >/dev/null 2>&1 || {
    echo >&2 "git is not installed. Aborting."
    exit 1
}
command -v gh >/dev/null 2>&1 || {
    echo >&2 "gh (GitHub CLI) is not installed. Aborting."
    exit 1
}

# Navigate to the project directory
cd "$PROJECT_SLUG" || exit

# Virtual environment
uv venv --python "$PY_VERSION"
source .venv/bin/activate
# .venv\Scripts\activate # Windows
uv sync

# GitHub repo creation
VISIBILITY="--public"
if [ "$PRIVATE" = true ]; then
    VISIBILITY="--private"
fi

if ! gh repo create "$REPO_NAME" "$VISIBILITY" --description "$REPO_DESCRIPTION" --source . --remote origin; then
    echo "Failed to create GitHub repository. Aborting."
    exit 1
fi

# Delete this script (optional, comment out if not desired)
rm "$(basename "$0")"

# Initial commit and push
git branch -M main # Ensure the branch name is 'main'
git add -A
git commit -m "🎉 Project setup"
git push origin main
