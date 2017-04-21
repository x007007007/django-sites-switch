from .middleware import get_request
from django.contrib.sites.models import SiteManager as _SiteManager
from django.contrib.sites.models import Site as _Site
from django.contrib.sites import models as _models

class SiteManager(_SiteManager):
    def _get_site_by_id(self, site_id):
        try:
            super(SiteManager, self)._get_site_by_id(site_id=site_id)
        except _Site.DoesNotExist:
            raise ImproperlyConfigured(
                "You're using the Django \"sites framework\" without having "
                "set the SITE_ID setting. Create a site in your database and "
                "set the SITE_ID setting or pass a request to "
                "Site.objects.get_current() to fix this error."
            )

    def get_current(self, request=None):
        """
        Returns the current Site based on the SITE_ID in the project's settings.
        If SITE_ID isn't defined, it returns the site with domain matching
        request.get_host(). The ``Site`` object is cached the first time it's
        retrieved from the database.
        """
        if not request:
            request = get_request()
        try:
            return self._get_site_by_request(request)
        except _Site.DoesNotExist:
            from django.conf import settings
            if getattr(settings, 'SITE_ID', ''):
                site_id = settings.SITE_ID
                return self._get_site_by_id(site_id)

_models.SiteManager = SiteManager