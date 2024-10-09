# shellcheck disable=SC1083
cd {{ cookiecutter.project_slug }} || exit

# GitHub repo
git init
git remote add origin https://github.com/{{cookiecutter.__gh_slug}}
git add -A
git commit -m "🎉 First commit"
git push origin main

# Conda virtual environment
conda create -n {{cookiecutter.virtual_env_name}} python={{cookiecutter.minimal_python_version}}
conda activate {{cookiecutter.virtual_env_name}}

# Install dependencies
pip install -r requirements/base.txt
pip install -r requirements/dev.txt
