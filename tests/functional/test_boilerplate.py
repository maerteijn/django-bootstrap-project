import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


def test_django_bootstrap_project_installed(settings):
    assert hasattr(settings, "DEBUG")


@pytest.mark.django_db
def test_create_user():
    User.objects.create_user(username="test")


@pytest.mark.django_db
def test_login_django_admin(admin_client):
    response = admin_client.get(reverse("admin:index"))
    assert response.status_code == 200
