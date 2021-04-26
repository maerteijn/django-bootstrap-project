from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("app/", include("django_bootstrap_app.urls")),
]
