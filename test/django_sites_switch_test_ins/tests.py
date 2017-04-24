from django.test import TestCase
from django.test import Client
from django.http.response import HttpResponse
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
# Create your tests here.

class DjangoSitesSwitchTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_record_and_rid_auto_switch(self):
        with self.settings(
            INSTALLED_APPS=settings.INSTALLED_APPS + [
                'django_sites_switch',
            ],
            MIDDLEWARE=settings.MIDDLEWARE + [
                'django_sites_switch.middleware.RecordAndRidRequestMiddleware',
            ]
        ):
            from django.contrib.sites.models import Site
            Site.objects.create(domain="domain-a.loc", name="domain-a.loc")
            Site.objects.create(domain="domain-b.loc", name="domain-b.loc")

            resp = self.c.get("/test/get_request/no_req/", SERVER_NAME="domain-a.loc")  # type:HttpResponse
            self.assertEqual(resp.content.decode(), "domain-a.loc")

            resp = self.c.get("/test/get_request/no_req/", SERVER_NAME="domain-b.loc")  # type:HttpResponse
            self.assertEqual(resp.content.decode(), "domain-b.loc")

            try:
                resp = self.c.get("/test/get_request/no_req/")  # type:HttpResponse
            except Exception as e:
                self.assertIsInstance(e, ImproperlyConfigured)

            resp = self.c.get("/test/get_request/req/", SERVER_NAME="domain-a.loc")  # type:HttpResponse
            self.assertEqual(resp.content.decode(), "domain-a.loc")

            resp = self.c.get("/test/get_request/req/", SERVER_NAME="domain-b.loc")  # type:HttpResponse
            self.assertEqual(resp.content.decode(), "domain-b.loc")

            try:
                resp = self.c.get("/test/get_request/req/")  # type:HttpResponse
            except Exception as e:
                self.assertIsInstance(e, ImproperlyConfigured)

    def test_record_and_rid_auto_switch_have_site_id(self):
        with self.settings(
            SITE_ID=1,
            INSTALLED_APPS=settings.INSTALLED_APPS + [
                'django_sites_switch',
            ],
            MIDDLEWARE=settings.MIDDLEWARE + [
                'django_sites_switch.middleware.RecordAndRidRequestMiddleware',
            ]
        ):
            from django.contrib.sites.models import Site
            Site.objects.create(domain="domain-a.loc", name="domain-a.loc")
            Site.objects.create(domain="domain-b.loc", name="domain-b.loc")

            resp = self.c.get("/test/get_request/no_req/", SERVER_NAME="domain-a.loc")  # type:HttpResponse
            self.assertEqual(resp.content.decode(), "domain-a.loc")

            resp = self.c.get("/test/get_request/no_req/", SERVER_NAME="domain-b.loc")  # type:HttpResponse
            self.assertEqual(resp.content.decode(), "domain-b.loc")

            resp = self.c.get("/test/get_request/req/")  # type:HttpResponse
            self.assertEqual(resp.content.decode(), "example.com")

            resp = self.c.get("/test/get_request/req/", SERVER_NAME="domain-a.loc")  # type:HttpResponse
            self.assertEqual(resp.content.decode(), "domain-a.loc")

            resp = self.c.get("/test/get_request/req/", SERVER_NAME="domain-b.loc")  # type:HttpResponse
            self.assertEqual(resp.content.decode(), "domain-b.loc")

            resp = self.c.get("/test/get_request/req/")  # type:HttpResponse
            self.assertEqual(resp.content.decode(), "example.com")