# Base settings, and such.

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

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

    # apps
    'measurements',
    'pings',

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

# Media files

MEDIA_URL = '/media/'

# Static files

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

STATIC_URL = '/static/'

# Secret configuration
# Note: Only use for development and testing!

SECRET_KEY = 'this_is_my_development_key'

# South configuration

INSTALLED_APPS += (
    # Database migration helpers:
    'south',
)
