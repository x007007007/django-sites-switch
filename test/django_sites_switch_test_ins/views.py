from django.contrib.sites.models import Site
from django.http.request import HttpRequest
from django.shortcuts import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.



def havent_request(request):
    return HttpResponse(Site.objects.get_current().domain)

def have_request(request):
    return HttpResponse(Site.objects.get_current(request).domain)

def shortcut(request):
    return HttpResponse(get_current_site(request).domain)