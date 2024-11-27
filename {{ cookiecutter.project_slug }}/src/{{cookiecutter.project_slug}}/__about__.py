"""About {{ cookiecutter.project_name }}."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

__app_name__ = "{{ cookiecutter.project_slug }}"
__version__ = "{{ cookiecutter.version }}"
__authors__ = ["{{ cookiecutter.full_name }}"]
__author_emails__ = ["{{ cookiecutter.email }}"]
__repo_url__ = "https://github.com/{{ cookiecutter.__gh_slug }}"
__issues_url__ = f"{__repo_url__}/issues"
__documentation__ = "https://{{ cookiecutter.project_slug | replace('_', '-') }}.readthedocs.io"
