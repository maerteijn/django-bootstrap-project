# django-bootstrap-project
[![Django CI](https://github.com/maerteijn/django-bootstrap-project/actions/workflows/ci.yml/badge.svg)](https://github.com/maerteijn/django-bootstrap-project/actions/workflows/ci.yml)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

A clean Poetry based Django project which includes CI

## Install with pdm
```bash
git clone https://github.com/maerteijn/django-bootstrap-project
pip install pdm
pdm install
```

## Linting
`flake8-black` and `flake8-isort` are installed too. The flake8-pylint pluging is still
in early development, so we need to call pylint manually
```bash
pdm run flake8
pdm run pylint
```

## Black
```bash
pdm run black
```

## Isort
```bash
pdm run isort
```

## Test
Pytest with coverage is default enabled
```bash
pdm run pytest
```

## Run development server
```bash
pdm run manage.py migrate
pdm run manage.py createsuperuser
pdm run manage.py runserver
```

