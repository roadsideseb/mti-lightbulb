import shortuuid

from django.db import models
from django import get_version
from django.db import connection
from django.db.models import get_app
from django.core.management import call_command
from django.db.models.related import RelatedObject
from lightbulb.benchy.models import BenchmarkResult, Failure

from .monitors import MemoryMonitor
from ..generic_m2m import query_wrapper as generic_m2m_qw
from ..model_utils_test import query_wrapper as model_utils_test_qw
from ..polymorphic_test import query_wrapper as polymorphic_test_qw

WRAPPERS = {
    'generic_m2m': generic_m2m_qw.QueryWrapper,
    'polymorphic_test': polymorphic_test_qw.QueryWrapper,
    'model_utils_test': model_utils_test_qw.QueryWrapper,
}


class AbstractBenchmarkRunner(object):
    PROCESS_FILTER = None
    DROP_TABLE_SQL = None

    def __init__(self, app_label):
        self.django_version = get_version()
        self.test_id = shortuuid.uuid()
        self.test_name = '{}_{}_{}'.format(
            app_label, self.django_version, connection.vendor)
        self.app_label = app_label

        query_wrapper = WRAPPERS.get(app_label)
        if not query_wrapper:
            raise TypeError("Couldn't find suitable query wrapper")
        self.query_wrapper = query_wrapper()

        self.monitor = MemoryMonitor(
            self.get_process_filter(connection.settings_dict))
        self.monitor.start()

    def create_result(self, num_models):
        return BenchmarkResult(
            self.test_id, test_name=self.test_name, app_label=self.app_label,
            num_models=num_models)

    def create_failure(self, exc):
        return Failure(
            self.test_id, test_name=self.test_name, app_label=self.app_label,
            exc=exc)

    def get_process_filter(self, dbsettings):
        return self.PROCESS_FILTER

    def drop_all_tables(self):
        for table_name in connection.introspection.table_names():
            cursor = connection.cursor()
            cursor.execute(
                self.DROP_TABLE_SQL.format(
                    connection.ops.quote_name(table_name)))
            cursor.close()

    def generate_models(self, num_models):
        models_module = get_app(self.app_label)
        post_hook_method = getattr(
            self, 'post_generation_{}'.format(self.app_label), None)

        for idx in xrange(num_models):
            class Meta:
                app_label = self.app_label
            attrs = {
                'text': models.TextField(),
                '__module__': 'lightbulb.{}.models'.format(self.app_label),
                'Meta': Meta}
            class_name = "Text{}Block".format(idx)
            setattr(models_module,class_name,
                    type(class_name, (models_module.ContentBlock,), attrs))

            if post_hook_method is not None:
                post_hook_method(models_module, class_name)

        models_module.ContentBlock._meta.init_name_map()

    def post_generation_model_utils_test(self, models_module, class_name):
        model_class = getattr(models_module, class_name)

        text_field = None
        for field in model_class._meta.fields:
            if field.name == 'contentblock_ptr':
                text_field = field
                break

        if text_field is None:
            raise AttributeError("cannot find text field on model")

        # this needs to be fixed up so that the generated classes show up
        # during retrieval of subclasses
        related = RelatedObject(
            models_module.ContentBlock, model_class, text_field)

        meta = models_module.ContentBlock._meta
        meta._related_objects_cache[related] = None
        meta._related_objects_proxy_cache[related] = None

    def syncdb(self):
        call_command('syncdb', interactive=False, verbosity=0)
        connection.queries = []

    def __del__(self):
        self.monitor.terminate()
        self.monitor.join()


class PostgresqlRunner(AbstractBenchmarkRunner):
    PROCESS_FILTER = 'postgres: {db_user}'
    DROP_TABLE_SQL = "DROP TABLE {} CASCADE;"

    def get_process_filter(self, dbsettings):
        return self.PROCESS_FILTER.format(db_user=dbsettings.get("USER"))


class MysqlRunner(AbstractBenchmarkRunner):
    PROCESS_FILTER = 'mysqld'
    DROP_TABLE_SQL = ("SET FOREIGN_KEY_CHECKS=0; DROP TABLE {} CASCADE; "
                      "SET FOREIGN_KEY_CHECKS=1;")
