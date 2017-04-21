# django-sites-switch
monkey patch django.contrib.site,
let site object automatically switch by http request

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
    'django_sites_switch.middleware.RecordRequestMiddleware',
]
```

if http request do not in your sites database,
while use setting.SITE_ID as default site, make sure you have config