import os
import sys
import django
from django.conf import settings
from django.core.wsgi import get_wsgi_application

# Add the project directory to the path
sys.path.insert(0, os.path.dirname(__file__))

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

# Setup Django
django.setup()

# Get the WSGI application
app = get_wsgi_application()

# Vercel handler for WSGI
def handler(request, response):
    # This is a basic handler - Vercel may need ASGI for full support
    # For now, this should work for basic requests
    return app