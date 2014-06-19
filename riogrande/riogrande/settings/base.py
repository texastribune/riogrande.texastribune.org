# Base settings, and such.

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
DJANGO_ROOT = os.path.dirname(os.path.dirname(__file__))
SITE_ROOT = os.path.dirname(DJANGO_ROOT)

DEBUG = False

TEMPLATE_DEBUG = False

# Application definitions

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.gis',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # helpers
    'djgeojson',
    'sortedm2m',
    'storages',

    # apps
    'days',
    'measurements',
    'photos',
    'pings',
    'posts',
    'stories',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'riogrande.urls'

WSGI_APPLICATION = 'riogrande.wsgi.application'

# Databases

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# General configuration

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Templates

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
)

# Media files

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')

# Static files

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'static'),
)

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(SITE_ROOT, 'assets')

# WhiteNoise configuration

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Secret configuration
# Note: Only use for development and testing!

SECRET_KEY = 'this_is_my_development_key'

# South configuration

INSTALLED_APPS += (
    # Database migration helpers:
    'south',
)
