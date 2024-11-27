{%- set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

{% if is_open_source -%}
[![Build][github-ci-image]][github-ci-link]
[![Coverage Status][codecov-image]][codecov-link]
[![PyPI Version][pypi-image]][pypi-link]
[![PyPI - Python Version][python-image]][pypi-link]
![License][license-image]
{%- endif %}

# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

<p align="center">
  <img src="media/package_illustration.png" alt="Illustration">
</p>

## Contents <!-- omit from toc -->

- [⬇️ Installation](#️-installation)
- [🏃 Getting Started](#-getting-started)
- [🧾 License](#-license)

## ⬇️ Installation

You can install **{ cookiecutter.project_slug }}** via pip:

```bash
pip install { cookiecutter.project_slug | replace("_", "-") }}
```

<!-- ### Requirements -->

## 🏃 Getting Started

[Documentation](https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io)

<!-- ## 📔 Citation -->

{% if is_open_source -%}

## 🧾 License

[{{cookiecutter.open_source_license}}](LICENSE)

{% endif -%}

<!-- ## 🤝 Contributing -->

## Credits <!-- omit from toc -->

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [Kajiih/cookiecutter-pypackage-kj](https://github.com/Kajiih/cookiecutter-pypackage-kj) project template based on  [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).

{% if is_open_source -%}
<!-- Links -->
[github-ci-image]: https://github.com/{{ __gh_slug }}/actions/workflows/build.yml/badge.svg?branch=main
[github-ci-link]: https://github.com/{{__gh_slug }}/actions?query=workflow%3Abuild+branch%3Amain

[codecov-image]: https://img.shields.io/codecov/c/github/{{ __gh_slug }}/main.svg?logo=codecov&logoColor=aaaaaa&labelColor=333333
[codecov-link]: https://codecov.io/github/{{__gh_slug }}

[pypi-image]: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug | replace("_", "-") }}.svg?logo=pypi&logoColor=aaaaaa&labelColor=333333
[pypi-link]: https://pypi.python.org/pypi/{{ cookiecutter.project_slug | replace("_", "-") }}

[python-image]: https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug | replace("_", "-") }}?logo=python&logoColor=aaaaaa&labelColor=333333
[license-image]: https://img.shields.io/badge/license-{{ cookiecutter.open_source_license | replace(" ", "_") }}-blue.svg?labelColor=333333
{%- endif %}
