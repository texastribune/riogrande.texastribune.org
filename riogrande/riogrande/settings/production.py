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

ALLOWED_HOSTS = ['*']

# Database

DATABASES = {}

# Secret configuration

SECRET_KEY = get_env_setting('SECRET_KEY')

# django-storage configuration
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# AWS settings
AWS_ACCESS_KEY_ID = get_env_setting('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_env_setting('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = get_env_setting('AWS_STORAGE_BUCKET_NAME')
