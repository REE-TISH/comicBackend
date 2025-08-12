import os
import django
from channels.routing import get_default_application
from Messages.routing import application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'comicBackend.settings')

django.setup()
application = get_default_application()
