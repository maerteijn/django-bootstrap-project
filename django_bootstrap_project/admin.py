from django.contrib import admin


class DjangoBootstrapProjectAdminSite(admin.AdminSite):
    index_template = "admin/django-bootstrap-project-admin-index.html"
