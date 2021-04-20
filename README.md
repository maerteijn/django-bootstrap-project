# django-bootstrap-project

A clean Poetry based Django project which includes CI

## Install with poetry
```bash
git clone https://github.com/maerteijn/django-bootstrap-project
pip install poetry

# This will also create a virtualenv when not activated
poetry install
```

## Linting
`flake8-black` and `flake8-isort` are installed too:
```bash
flake8
```

## Black
```bash
black django_bootstrap_project
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

