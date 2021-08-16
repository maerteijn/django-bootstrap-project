# django-bootstrap-project
[![Django CI](https://github.com/maerteijn/django-bootstrap-project/actions/workflows/ci.yml/badge.svg)](https://github.com/maerteijn/django-bootstrap-project/actions/workflows/ci.yml)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

A clean Poetry based Django project which includes CI

## Install with poetry
```bash
git clone https://github.com/maerteijn/django-bootstrap-project
pip install poetry

# This will also create a virtualenv when not activated
poetry install
source $(poetry env info --path)/bin/activate
```

## Linting
`flake8-black` and `flake8-isort` are installed too. The flake8-pylint pluging is still
in early development, so we need to call pylint manually
```bash
flake8
pylint src/
```

## Black
```bash
black src/
```

## Isort
```bash
isort .
```

## Test
Pytest with coverage is default enabled
```bash
pytest
```

## Run
When you used a virtualenv yourself (mkvirtualenv or pyenv), you can just run the scripts below.

If not, activate the venv created with poetry:
```bash
source $(poetry env info --path)/bin/activate
```

Now you can acces `manage.py` from anywhere as it is an installed script
```bash
manage.py migrate
manage.py createsuperuser
manage.py runserver
```

