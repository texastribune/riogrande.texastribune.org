# Local development settings.

import os

from .base import *


DEBUG = True

TEMPLATE_DEBUG = DEBUG

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'local.db'),
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
    'debug_toolbar.apps.DebugToolbarConfig',
)
