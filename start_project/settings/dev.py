from .base import *

SECRET_KEY = "django-insecure-byz$u!^eg4*7dwjf2rz1#&7-a(8hau@n0qu&+x$v^s1a_b2o52"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  #Temporary setting this to False for dev it should be true.

ALLOWED_HOSTS = ['*']

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'