import imp
import os
import sys


sys.path.insert(0, os.path.dirname(__file__))

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
# Set the application
import django.core.handlers.wsgi
from paste.exceptions.errormiddleware import ErrorMiddleware
application = django.core.handlers.wsgi.WSGIHandler()
# Use paste to display errors
application = ErrorMiddleware(application, debug=True)

#wsgi = imp.load_source('wsgi', 'passenger_wsgi.py')
#application = wsgi.application
