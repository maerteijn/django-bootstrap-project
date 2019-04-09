from django.contrib import admin


class DjangoBootstrapAdminSite(admin.AdminSite):
    index_template = "admin/django-bootstrap-admin-index.html"
