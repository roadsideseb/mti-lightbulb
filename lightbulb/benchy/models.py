from django import get_version
from django.db import connection

from marshmallow.serializer import fields, Serializer

DJANGO_VERSION = get_version()


class BenchmarkResultSerializer(Serializer):
    django_version = fields.String()
    database_vendor = fields.String()
    database_name = fields.String()

    class Meta:
        fields = ('uuid', 'name', 'num_models', 'django_version',
                  'database_vendor', 'database_name', 'start', 'end',
                  'create_time_sql', 'create_time_complete', 'query_time_sql',
                  'query_time_complete', 'db_rss', 'db_vrt')


class BenchmarkResult(object):
    django_version = DJANGO_VERSION
    serializer = BenchmarkResultSerializer

    def __init__(self, uuid, name, num_models):
        self.database_vendor = connection.vendor
        self.uuid = uuid
        self.name = name
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
        return self.serializer(self).data
