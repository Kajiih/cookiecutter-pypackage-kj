import os
import subprocess
import sys

# Define the cookiecutter variables
project_slug = "{{ cookiecutter.project_slug }}"
gh_repo_slug = "{{ cookiecutter.__gh_slug }}"
virtual_env_name = "{{ cookiecutter.virtual_env_name }}"
minimal_python_version = "{{ cookiecutter.minimal_python_version }}"

# Change directory to the project folder
os.chdir(project_slug)

# Initialize Git repository and make the first commit
try:
    subprocess.run(["git", "init"], check=True)
    subprocess.run(
        ["git", "remote", "add", "origin", f"https://github.com/{gh_repo_slug}"], check=True
    )
    subprocess.run(["git", "add", "-A"], check=True)
    subprocess.run(["git", "commit", "-m", "🎉 First commit"], check=True)
    subprocess.run(["git", "branch", "-M", "main"], check=True)
    subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
    print("✅ Git repository initialized and first commit pushed.")
except subprocess.CalledProcessError as e:
    print(f"❌ Error in Git operations: {e}")
    sys.exit(1)

# Create and activate Conda environment
try:
    subprocess.run(
        ["conda", "create", "-n", virtual_env_name, f"python={minimal_python_version}", "-y"],
        check=True,
    )
    print(f"✅ Conda environment '{virtual_env_name}' created.")

    # Conda environment activation is only fully possible in a subprocess.
    # If running this script manually, activate the environment with `conda activate <env>`
except subprocess.CalledProcessError as e:
    print(f"❌ Error in creating Conda environment: {e}")
    sys.exit(1)

# Install dependencies
try:
    subprocess.run(
        ["conda", "run", "-n", virtual_env_name, "pip", "install", "-r", "requirements/base.txt"],
        check=True,
    )
    subprocess.run(
        ["conda", "run", "-n", virtual_env_name, "pip", "install", "-r", "requirements/dev.txt"],
        check=True,
    )
    print("✅ Dependencies installed.")
except subprocess.CalledProcessError as e:
    print(f"❌ Error in installing dependencies: {e}")
    sys.exit(1)
