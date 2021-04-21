from django.contrib import admin
from pkg_resources import get_distribution


class DjangoBootstrapProjectAdminSite(admin.AdminSite):
    site_header = "My Django Bootstrap Project Admin Site"

    def each_context(self, request):
        ctx = super().each_context(request)
        return {**ctx, "version": get_distribution("django-bootstrap-project").version}
