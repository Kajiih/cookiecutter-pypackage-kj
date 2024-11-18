{%- set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

<p align="center">
  <img src="media/package_illustration.png" alt="Illustration">
</p>

{% if is_open_source -%}
<div align="center">
    <a href="https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}">
        <img src="https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg" alt="PyPI version">
    </a>
    <a href="https://{{ cookiecutter.project_slug | replace('_', '-') }}.readthedocs.io/en/latest/?version=latest">
        <img src="https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace('_', '-') }}/badge/?version=latest" alt="Documentation Status">
    </a>
</div>
{%- endif %}

## Contents <!-- omit from toc -->

- [💻 Installation](#-installation)
- [🏃 Getting Started](#-getting-started)
- [🧾 License](#-license)

## 💻 Installation

1. **Create virtual environment**

    TO UPDATE

2. **Install the package and its dependencies**

    TO UPDATE

<!-- ### Requirements -->

## 🏃 Getting Started

[Documentation](https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io)

<!-- ## 📔 Citation -->

{% if is_open_source -%}

## 🧾 License

| Component            | License                                                                  |
| -------------------- | -------------------------------------------------------------------------|
| Codebase (this repo) | [{{cookiecutter.open_source_license}}](LICENSE)|

{% endif -%}

<!-- ## 🤝 Contributing -->

## Credits <!-- omit from toc -->

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [Kajiih/cookiecutter-pypackage-kj](https://github.com/Kajiih/cookiecutter-pypackage-kj) project template based on  [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
