import os

from .base import *

DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
DATABASES['default']['PORT'] = os.getenv('DB_PORT', 9932)
DATABASES['default']['OPTIONS'] = {'autocommit': True}
