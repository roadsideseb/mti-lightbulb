import json

from socket import gethostname

from django import get_version
from django.db import connection

from marshmallow.serializer import fields, Serializer

DJANGO_VERSION = get_version()


class BenchmarkResultSerializer(Serializer):
    django_version = fields.String()
    database_vendor = fields.String()
    database_name = fields.String()
    database_host = fields.String()
    hostname = fields.String()

    class Meta:
        fields = ('test_id', 'test_name', 'app_label', 'num_models',
                  'django_version', 'database_vendor', 'database_name',
                  'database_host', 'hostname', 'start', 'end',
                  'create_time_sql', 'create_time_complete', 'query_time_sql',
                  'query_time_complete', 'db_rss', 'db_vrt')


class BenchmarkResult(object):
    django_version = DJANGO_VERSION
    serializer = BenchmarkResultSerializer

    def __init__(self, test_id, test_name, app_label, num_models):
        self.database_vendor = connection.vendor
        self.database_host = connection.settings_dict.get('NAME')
        self.database_host = connection.settings_dict.get('HOST')
        self.hostname = gethostname()
        self.test_id = test_id
        self.test_name = test_name
        self.app_label = app_label
        self.num_models = num_models

        self.start = None
        self.end = None
        self.create_time_sql = None
        self.create_time_complete = None
        self.query_time_sql = None
        self.query_time_complete = None

        self.db_rss = None
        self.db_vrt = None

    def to_json(self):
        return json.dumps(self.serializer(self).data)
