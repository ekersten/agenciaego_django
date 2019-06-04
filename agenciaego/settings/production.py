import os
from .base import *

DEBUG = True

SECRET_KEY='fwm$qp4075yza9_(i876v(rcvqt@6uf$^ckg^zf6w)q-rm=oe2`'

ALLOWED_HOSTS = ['wagtail.egoagencydev.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'watail',
        'USER': 'wagtail',
        'PASSWORD': 'Wagtail123!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'sql_mode': 'STRICT_TRANS_TABLES',
    }
}



MEDIA_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '../media/').replace('\\','/'))
STATIC_ROOT = '/home/egoagency/webapps/wagtail_static'

BASE_URL = 'http://wagtail.egoagencydev.com'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/egoagency/logs/user/django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


try:
    from .local import *
except ImportError:
    pass
