from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class DjangoBootstrapAdminConfig(AdminConfig):
    default_site = 'django_bootstrap.admin.DjangoBootstrapAdminSite'


class DjangoBootstrapConfig(AppConfig):
    name = "django_bootstrap"