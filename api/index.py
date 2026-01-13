import os
import sys
import django
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from vercel_wsgi import handler

# Add the project directory to the path
sys.path.insert(0, os.path.dirname(__file__))

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

# Setup Django
django.setup()

# Get the WSGI application
app = get_wsgi_application()