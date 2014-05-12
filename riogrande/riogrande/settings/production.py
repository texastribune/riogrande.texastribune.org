# Settings for production.

from os import environ
from django.core.exceptions import ImproperlyConfigured

from .base import *


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)


# Host configuration
ALLOWED_HOSTS = []

# Database
DATABASES = {}

# Cache
CACHES = {}

# Secret configuration
SECRET_KEY = get_env_setting('SECRET_KEY')
