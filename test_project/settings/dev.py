from .base import *

SECRET_KEY = 'django-insecure-&yaow(u@rkj5&xq7=c2c#s_!m)td058vpq3zemi8xbla1!q+&1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  #Temporary setting this to False for dev it should be true.

ALLOWED_HOSTS = ['*']

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'
