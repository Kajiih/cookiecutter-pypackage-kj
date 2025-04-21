
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

- [📋 Requirements](#-requirements)
- [🚀 Quickstart](#-quickstart)
- [✨ Features](#-features)

## 📋 Requirements

Unsure the following dependencies are installed:

- Python>=3.12
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html)
- [Git](https://git-scm.com/downloads)
- [GitHub CLI (gh)](https://cli.github.com/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## 🚀 Quickstart

1. **Install the [requirement](#-requirements)**

    You can verify all required tools are correctly installed by running:

    ```bash
    cookiecutter --version
    git --version
    gh --version
    uv --version
    ```

2. **Generate the Python package project:**

    ```bash
    cookiecutter https://github.com/Kajiih/cookiecutter-pypackage-kj.git
    ```

3. **Setup the project**

    Follow the instructions displayed at the end of the generation process to initialize Git, create the GitHub repository, and set up the virtual environment

4. **Start coding your awesome package!**

## ✨ Features

- Automatically setups GitHub repository and virtual environment with `uv`
- Configurations for `Ruff`, `Pytest`, `pytest-coverage`
- Dynamic project metadata with `hatch`
