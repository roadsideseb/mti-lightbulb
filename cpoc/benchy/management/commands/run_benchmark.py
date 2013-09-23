import csv
import itertools

from time import time
from optparse import make_option

from django.db import connection
from django.db.models import get_model
from django.core.management import call_command
from django.db.models.related import RelatedObject
from django.core.management.base import LabelCommand, CommandError

from cpoc.multi_table import models as mt_models


class Command(LabelCommand):
    option_list = LabelCommand.option_list + (
        make_option(
            '-b', '--num-blocks',
            dest='num_blocks',
            type=int,
            default=500,
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
        if not labels:
            labels = ('multi_table', 'generic_m2m', 'json_data')
        super(Command, self).handle(*labels, **options)

    def handle_label(self, app, **options):
        self.num_blocks = options.get('num_blocks')
        self.step_size = options.get('step_size')

        print "Clearing data from database"

        bench_method = getattr(self, "run_{}_benchmark".format(app))
        if not bench_method:
            raise CommandError(
                "no benchmark can be run for app '{}'".format(app)
            )
        bench_method()

    def run_multi_table_benchmark(self):
        from cpoc.multi_table import factories

        csv_fh = open('multi_table_benchmark_results.csv', 'w')
        csv_writer = csv.writer(csv_fh)

        header = [
            "blocks",
            "create time (SQL)",
            "create time (complete)",
            "query time (SQL)",
            "query time (complete)"
        ]
        csv_writer.writerow(header)
        print ', '.join(header)

        # run from 1 to 500 sample block classes
        for num_blocks in xrange(1, self.num_blocks + 1, self.step_size):
            # create all the block models on the models module
            [self._inject_block_model(i) for i in xrange(num_blocks)]

            cursor = connection.cursor()
            call_command('syncdb', interactive=False, verbosity=0)

            connection.queries = []

            start = time()
            container = factories.ContainerFactory()

            for idx in xrange(1, num_blocks):
                block_class = getattr(mt_models, "Text{}Block".format(idx))
                block_class.objects.create(
                    text="The text of block #{}".format(idx),
                    container=container
                )

            create_duration = time() - start

            sql_time = sum(
                [float(q.get('time', 0)) for q in connection.queries]
            )

            query_times = []
            processing_times = []
            for it in xrange(0, 500):
                # clear previously logged queries
                connection.queries = []

                start = time()
                container = get_model('multi_table', 'Container').objects.get(
                    id=container.id
                )
                # generate a list here to make sure that the queryset is not
                # just assembled but also executed!!
                list(
                    container.blocks.select_subclasses().order_by(
                        'display_order'
                    )
                )
                processing_times.append((time() - start))

                sql_time = sum(
                    [float(q.get('time', 0)) for q in connection.queries]
                )
                query_times.append(sql_time)

            csv_writer.writerow([
                num_blocks,
                sql_time,
                create_duration,
                sum(query_times) / len(query_times),
                sum(processing_times) / len(processing_times),
            ])
            csv_fh.flush()
            print ("{num_blocks}, {create_time_sql}, "
                   "{create_time_processing}, {query_time_sql}, "
                   "{query_time_processing}").format(
                num_blocks=num_blocks,
                create_time_sql=sql_time,
                create_time_processing=create_duration,
                query_time_sql=sum(query_times) / len(query_times),
                query_time_processing=sum(processing_times) / len(processing_times),
            )

            # clean up after myself
            for table_name in connection.introspection.table_names():
                cursor = connection.cursor()
                cursor.execute(
                    "DROP TABLE {} CASCADE;".format(
                        connection.ops.quote_name(table_name)
                    )
                )
        csv_fh.close()

    def _inject_block_model(self, model_number):
        from django.db import models

        class Meta:
            app_label = 'multi_table'

        attrs = {
            'text': models.TextField(),
            '__module__': 'cpoc.multi_table.models',
            'Meta': Meta,
        }
        class_name = "Text{}Block".format(model_number)
        setattr(
            mt_models,
            class_name,
            type(class_name, (mt_models.ContentBlock,), attrs)
        )

        model_class = getattr(mt_models, class_name)

        # this needs to be fixed up so that the generated classes show up
        # during retrieval of subclasses
        related = RelatedObject(
            mt_models.ContentBlock,
            model_class,
            model_class._meta.fields[3]
        )
        mt_models.ContentBlock._meta._related_objects_cache[related] = None

    #def run_json_data_bench(self):
    #    #from cpoc.json_data import factories

    #    block_factories = itertools.cycle([
    #        factories.TextBlockFactory,
    #        factories.ImageBlockFactory,
    #    ])

    #    container = factories.ContainerFactory()
    #    for idx in xrange(0, self.num_blocks):
    #        block_factories.next().create(container=container)

    #    # clear previously logged queries
    #    connection.queries = []
    #    container = get_model('multi_table', 'Container').objects.get(
    #        id=container.id
    #    )
    #    list(container.blocks.select_subclasses().order_by('display_order'))

    #    for idx, query_dct in enumerate(connection.queries):
    #        print "Query {}: {}".format(idx, query_dct.get('time', 'N/A'))

    def run_generic_m2m_bench(self):
        from cpoc.generic_m2m import factories

        block_factories = itertools.cycle([
            factories.TextBlockFactory,
            factories.ImageBlockFactory,
        ])

        # clear previously logged queries
        connection.queries = []

        start = time()
        container = factories.ContainerFactory()
        for idx in xrange(0, self.num_blocks):
            container.blocks.connect(block_factories.next().create())
        create_duration = time() - start

        sql_time = sum([float(q.get('time', 0)) for q in connection.queries])

        print "Create time: SQL {} | all {}".format(sql_time, create_duration)

        query_times = []
        processing_times = []
        for idx in xrange(0, 1):
            # clear previously logged queries
            connection.queries = []

            start = time()
            container = get_model('generic_m2m', 'Container').objects.get(
                id=container.id
            )

            list(container.blocks.all().generic_objects())
            processing_times.append(time() - start)

            sql_time = sum(
                [float(q.get('time', 0)) for q in connection.queries]
            )
            query_times.append(sql_time)

        print "Average query time (SQL): {} in {:.4f}s".format(
            len(connection.queries),
            sum(query_times) / len(query_times)
        )
        print "Average processing time: {:.4f}s".format(
            sum(processing_times) / len(processing_times)
        )
