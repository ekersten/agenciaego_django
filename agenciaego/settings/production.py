import os
from .base import *

DEBUG = False

MEDIA_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '../media/').replace('\\','/'))
STATIC_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '../static/').replace('\\','/'))

BASE_URL = 'http://wagtail.egoagencydev.com'

try:
    from .local import *
except ImportError:
    pass
