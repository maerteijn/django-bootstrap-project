from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class DjangoBootstrapProjectAdminConfig(AdminConfig):
    default_site = "django_bootstrap_project.admin.DjangoBootstrapProjectAdminSite"


class DjangoBootstrapProjectConfig(AppConfig):
    name = "django_bootstrap_project"
