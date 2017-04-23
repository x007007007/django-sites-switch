from .middleware import get_request
from django.contrib.sites.models import SiteManager as _SiteManager
from django.contrib.sites.models import Site as _Site
from django.contrib.sites.models import ImproperlyConfigured
from django.contrib.sites import models as _models


class SiteManager(_SiteManager):
    def get_current(self, request=None):
        """
        Returns the current Site based on the SITE_ID in the project's settings.
        If SITE_ID isn't defined, it returns the site with domain matching
        request.get_host(). The ``Site`` object is cached the first time it's
        retrieved from the database.
        """
        if request is None:
            request = get_request()
        if request is not None:
            try:
                return self._get_site_by_request(request)
            except _Site.DoesNotExist:
                pass
        from django.conf import settings
        site_id = getattr(settings, 'SITE_ID', '')
        if site_id:
            try:
                return self._get_site_by_id(site_id)
            except _Site.DoesNotExist:
                pass
        raise ImproperlyConfigured(
            "You're using the Django \"sites framework\" Monkey Patched "
            "`django-sites-switch` without having "
            "set the SITE_ID setting. Create a site in your database and "
            "set the SITE_ID setting or pass a request to "
            "Site.objects.get_current() "
            "or set middleware to fix this error."
        )


_models.SiteManager.get_current = SiteManager.get_current
