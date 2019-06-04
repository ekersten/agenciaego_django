"""
WSGI config for agenciaego project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
# import sys
# import site


# def execfile(filepath, globals=None, locals=None):
#     if globals is None:
#         globals = {}
#     globals.update({
#         "__file__": filepath,
#         "__name__": "__main__",
#     })
#     with open(filepath, 'rb') as file:
#         exec(compile(file.read(), filepath, 'exec'), globals, locals)


# site.addsitedir('/home/egoagency/webapps/wagtail/.virtualenv/lib/python3.7/site-packages')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'agenciaego.settings.production'
# activate_this = os.path.expanduser('/home/egoagency/webapps/wagtail/.virtualenv/bin/activate_this.py')
# execfile(activate_this, dict(__file__=activate_this))

# project = '/home/egoagency/webapps/wagtail/site'
# workspace = os.path.dirname(project)
# sys.path.append(workspace)

# sys.path = ['/home/egoagency/webapps/wagtail/site',
#             '/home/egoagency/webapps/wagtail/'] + sys.path



from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agenciaego.settings.production")

application = get_wsgi_application()
