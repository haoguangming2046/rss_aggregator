"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

ENVIRONMENT = os.environ.get('environment', 'development')

SETTINGS_MAP = {
    'development': 'server.settings.development',
}

os.environ.setdefault('DJANGO_SETTINGS_MODULE', SETTINGS_MAP.get(
    ENVIRONMENT, 'server.settings.development'))

application = get_wsgi_application()
