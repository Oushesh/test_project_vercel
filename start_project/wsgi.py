"""
WSGI config for start_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "start_project.settings.dev")

application = get_wsgi_application()

app = application #For vercel https://www.youtube.com/watch?v=ZjVzHcXCeMU