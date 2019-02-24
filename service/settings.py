# Bare implementation of Django Settings file to use Django ORM as a standalone

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY = 'e7pok(8kajvnxcyr*-%d8y_=0**-@ayxvhff$lgm50y*nac@qy'

INSTALLED_APPS = (
    'db',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rss_service',
        'USER': os.environ.get("DB_USER", "root"),
        'PASSWORD': os.environ.get("DB_PASSWORD", ""),
        'HOST': os.environ.get("DB_HOST", "localhost"),
        'PORT': os.environ.get("DB_PORT", "3306"),
    }
}
