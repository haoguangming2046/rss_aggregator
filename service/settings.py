# Bare implementation of Django Settings file to use Django ORM as a standalone

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY = 'e7pok(8kajvnxcyr*-%d8y_=0**-@ayxvhff$lgm50y*nac@qy'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

INSTALLED_APPS = (
    'db',
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
