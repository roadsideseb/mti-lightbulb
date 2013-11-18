import os

from .base import *

DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
DATABASES['default']['PORT'] = os.getenv('DB_PORT', 9906)
DATABASES['default']['OPTIONS'] = {'init_command': 'SET autocommit=1'}
