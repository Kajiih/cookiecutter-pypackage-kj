
# Kajih's Cookiecutter Python Package Template

<div align="center">
<a href="https://gitmoji.dev">
  <img
    src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg"
    alt="Gitmoji"
  />
</a>
</div>

## Contents <!-- omit from toc -->

- [💻 Quickstart](#-quickstart)
- [✨ Features](#-features)

## 💻 Quickstart

1. **Install the latest Cookiecutter** if you haven't installed it yet:

    ```bash
    pip install -U cookiecutter
    ```

2. **Generate the Python package project:**

    ```bash
    cookiecutter https://github.com/Kajiih/cookiecutter-pypackage-kj.git
    ```

3. **Create a GitHub repository with the according name**

    See the name printed in the consol of the end of the project generation.

4. Execute the [bash script]({{%20cookiecutter.project_slug%20}}/setup_project.bash) to initialize git, pushing the first commit to your GitHub repository, creating a conda environment and installing dependencies

    ```bash
    bash {{ cookiecutter.project_slug }}/setup_project.sh
    ```

    If there is any error, execute the commands manually one by one.

5. Start coding your awesome package!

## ✨ Features

- Configurations for `Ruff`, `Pytest`, `pytest-coverage`
- Dynamic versioning and dependencies with `hatch`
- TODOs management with [todo+](https://github.com/fabiospampinato/vscode-todo-plus#demo)

## Note <!-- omit from toc -->

- Run command `Create Table of Contents` (in the VS Code Command Palette) to insert a new table of contents.
