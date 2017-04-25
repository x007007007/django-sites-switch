# django-sites-switch
[![Build Status](https://travis-ci.org/x007007007/django-sites-switch.svg?branch=master)](https://travis-ci.org/x007007007/django-sites-switch)
[![codecov](https://codecov.io/gh/x007007007/django-sites-switch/branch/master/graph/badge.svg)](https://codecov.io/gh/x007007007/django-sites-switch)


monkey patch django.contrib.site,
let site object automatically switch by http request


## install
git+ssh://git@github.com/x007007007/django-sites-switch.git#egg=django-sites-switch

## usage

add `django_sites_switch` in INSTALLED_APPS, like

```
INSTALLED_APPS = [
        # ...
    'django.contrib.sites',
        # ...
    'django_sites_switch',
        # ...
]
```

add middleware at tail of `MIDDLEWARE` in django setting ,like
```
MIDDLEWARE = [

       # ...
    'django_sites_switch.middleware.RecordAndRidRequestMiddleware',
]
```
or like
MIDDLEWARE = [

       # ...
    'django_sites_switch.middleware.RidRecordRequestMiddleware',
       # ...
    'django_sites_switch.middleware.RecordRequestMiddleware'
]
if http request do not in your sites database,
while use setting.SITE_ID as default site, make sure you have config



