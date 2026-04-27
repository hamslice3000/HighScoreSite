import os
import sys


sys.path.insert(0, os.path.dirname(__file__))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

#wsgi = imp.load_source('wsgi', 'passenger_wsgi.py')
#application = wsgi.application
