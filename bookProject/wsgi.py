"""
WSGI config for bookProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookProject.settings')

    application = get_wsgi_application()
except Exception as e:
    print(f"WSGI application failed to load: {e}")
