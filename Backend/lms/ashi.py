import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'lms' project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lms.settings')

# Get the WSGI application for use with any WSGI-compatible web server.
application = get_wsgi_application()
