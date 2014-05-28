# Local development settings.

import os

from .base import *


DEBUG = True

TEMPLATE_DEBUG = DEBUG

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': os.path.join(SITE_ROOT, 'local.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Cache

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Django debug toolbar

INSTALLED_APPS += (
    'debug_toolbar',
)
