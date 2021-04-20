def test_django_bootstrap_project_installed(settings):
    assert hasattr(settings, "DEBUG")
