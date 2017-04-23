from django.test import TestCase
from .middleware import RecordRequestMiddleware
from .middleware import get_request
from django.http.request import HttpRequest
# Create your tests here.

class DjangoSitesSwitchTestCase(TestCase):
    def test_middleware(self):
        RecordRequestMiddleware.process_request