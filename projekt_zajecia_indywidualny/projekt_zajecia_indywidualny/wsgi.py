"""
WSGI config for projekt_zajecia_indywidualny project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projekt_zajecia_indywidualny.settings')

application = get_wsgi_application()
