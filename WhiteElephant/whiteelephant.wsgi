"""
WSGI config for game project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys 

sys.path.append('/opt/WhiteElephant/WhiteElephant')
#sys.path.append('/opt/WhiteElephant/WhiteElephant/WhiteElephant')
os.environ['DJANGO_SETTINGS_MODULE'] = 'WhiteElephant.settings'

from django.core.wsgi import get_wsgi_application
#print(application)
application = get_wsgi_application()
