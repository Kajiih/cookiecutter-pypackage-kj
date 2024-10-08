#!/usr/bin/env python
"""Post cookiecutter project generation hook."""

import pathlib

if __name__ == "__main__":
    if "Not open source" == "{{ cookiecutter.open_source_license }}":  # noqa: PLR0133
        pathlib.Path("LICENSE").unlink()
