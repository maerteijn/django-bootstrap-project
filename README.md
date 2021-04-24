# django-bootstrap-project
[![Django CI](https://github.com/maerteijn/django-bootstrap-project/actions/workflows/ci.yml/badge.svg)](https://github.com/maerteijn/django-bootstrap-project/actions/workflows/ci.yml)

A clean Poetry based Django project which includes CI

## Install with poetry
```bash
git clone https://github.com/maerteijn/django-bootstrap-project
pip install poetry

# This will also create a virtualenv when not activated
poetry install
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
`manage.py` is installed as a script so you can run it from anywhere
```bash
manage.py migrate
manage.py createsuperuser
manage.py runserver
```

