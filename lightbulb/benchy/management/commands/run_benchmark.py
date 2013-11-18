import os

#from pusher import Pusher
from time import time, sleep
from humanize import filesize
from optparse import make_option

from django.db import models
from django import get_version
from django.db import connection
from django.db.models import get_app
from django.db.utils import DatabaseError
from django.core.management.base import LabelCommand, CommandError

from lightbulb.benchy import runners
from lightbulb.benchy.models import BenchmarkResult


BASEDIR = os.path.join(os.getcwd(), "results")
DJANGO_VERSION = get_version()

RUNNERS = {
    'mysql': runners.MysqlRunner,
    'postgresql': runners.PostgresqlRunner,
}


class Command(LabelCommand):
    num_queries = 100
    option_list = LabelCommand.option_list + (
        make_option(
            '-b', '--num-models',
            dest='num_models',
            type=int,
            default=200,
            help="Upper boundary for block models to test against"
        ),
        make_option(
            '-s', '--step-size',
            dest='step_size',
            type=int,
            default=5,
            help="Size in which to step through the number of block interval"
        ),
    )

    def handle(self, *labels, **options):
        self.num_models = options.get('num_models')
        self.step_size = options.get('step_size')
        if not labels:
            labels = ('model_utils_test', 'generic_m2m', 'polymorphic_test')
        super(Command, self).handle(*labels, **options)

    def handle_label(self, app_label, **options):
        runner_class = RUNNERS.get(connection.vendor)
        if not runner_class:
            raise CommandError(
                "No runner for {} available".format(connection.vendor))

        self.runner = runner_class(app_label)

        if not os.path.exists(BASEDIR):
            os.makedirs(BASEDIR)

        filename = '{}_{}_Django-{}_benchmark_results.csv'.format(
            app_label, connection.vendor, DJANGO_VERSION)

        print '-' * 80
        print 'App:', app_label
        print 'Django version:', DJANGO_VERSION
        print 'Database engine:', connection.vendor

        with open(os.path.join(BASEDIR, filename), 'w') as json_fh:
            self.json_fh = json_fh
            try:
                self.run_benchmark(app_label)
            except DatabaseError as exc:
                print 'Database error', exc.args[1]
                self.json_fh.write(
                    "{{'error': 'Database failed with error: {}'}}".format(
                        exc.args[1]))
        print '-' * 80

    def run_benchmark(self, app_label):
        # run from 1 to 500 sample block classes
        for num_models in xrange(0, self.num_models + 1, self.step_size):
            # starting at zero makes no sense at all but we want to have
            # the steps counted in an intuitive manner, so start with 1 here
            if num_models == 0:
                num_models = 1

            self.runner.generate_models(num_models)
            self.runner.syncdb()

            bm_result = BenchmarkResult(
                uuid=self.runner.uuid, name=app_label, num_models=num_models)
            bm_result.start = time()

            start = time()
            container = self.runner.query_wrapper.create_query(
                app_label, num_models)

            bm_result.create_time_complete = time() - start

            bm_result.create_time_sql = sum(
                [float(q.get('time', 0)) for q in connection.queries]
            )

            query_times = []
            processing_times = []
            memory_rss = []
            memory_vrt = []
            for it in xrange(0, self.num_queries):
                # clear previously logged queries
                connection.queries = []

                # reset the value for monitored memory usage
                self.runner.monitor.reset_values()

                start = time()
                self.runner.query_wrapper.select_query(container.id)

                processing_times.append((time() - start))

                rss, vrt = self.runner.monitor.get_memory_values()
                memory_rss.append(rss)
                memory_vrt.append(vrt)

                query_time_sql = sum(
                    [float(q.get('time', 0)) for q in connection.queries]
                )
                query_times.append(query_time_sql)

            bm_result.end = time()

            num_queries = len(query_times)
            bm_result.query_time_sql = sum(query_times) / num_queries
            bm_result.query_time_complete = sum(processing_times) / num_queries

            bm_result.db_rss = sum(memory_rss) / len(memory_rss)
            bm_result.db_vrt = sum(memory_vrt) / len(memory_vrt)

            self.json_fh.write("{}\n".format(bm_result.to_json()))
            self.json_fh.flush()

            print ("{num_models}, {test_duration:.4f} s, "
                   "{create_time_sql:.4f} s, {create_time_complete:.4f} s, "
                   "{query_time_sql:.4f} s, {query_time_complete:.4f} s, "
                   "{db_rss}, {db_vrt}").format(
                num_models=num_models,
                test_duration=bm_result.end - bm_result.start,
                create_time_sql=bm_result.create_time_sql,
                create_time_complete=bm_result.create_time_complete,
                query_time_sql=bm_result.query_time_sql,
                query_time_complete=bm_result.query_time_complete,
                db_rss=filesize.naturalsize(bm_result.db_rss),
                db_vrt=filesize.naturalsize(bm_result.db_vrt),
            )
            self.runner.drop_all_tables()
