import os
from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'agenciaego_django',
        'USER': 'wagtail',
        'PASSWORD': 'Wagtail123!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

MEDIA_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '../media/').replace('\\','/'))
STATIC_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '../static/').replace('\\','/'))

BASE_URL = 'http://wagtail.egoagencydev.com'

try:
    from .local import *
except ImportError:
    pass
