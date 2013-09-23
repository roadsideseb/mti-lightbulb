import csv

from time import time
from optparse import make_option

from django.db import models
from django.db import connection
from django.utils import timezone
from django.db.models import get_app
from django.db.models import get_model
from django.core.management import call_command
from django.db.models.related import RelatedObject
from django.core.management.base import LabelCommand, CommandError


class Command(LabelCommand):
    num_queries = 100
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
            labels = ('multi_table', 'generic_m2m')  # 'json_data')
        super(Command, self).handle(*labels, **options)

    def handle_label(self, app_label, **options):
        self.num_blocks = options.get('num_blocks')
        self.step_size = options.get('step_size')

        self.csv_fh = open(
            '{}_{}_{}_benchmark_results.csv'.format(
                timezone.now(),
                app_label,
                connection.vendor
            ),
            'w'
        )

        self.csv_writer = csv.writer(self.csv_fh)
        header = [
            "blocks",
            "create time (SQL)",
            "create time (complete)",
            "query time (SQL)",
            "query time (complete)"
        ]
        self.csv_writer.writerow(header)
        print ', '.join(header)

        self.run_benchmark(app_label)
        self.csv_fh.close()

    def run_benchmark(self, app_label):
        # run from 1 to 500 sample block classes
        for num_blocks in xrange(1, self.num_blocks + 1, self.step_size):
            # create all the block models on the models module
            for ib in xrange(num_blocks):
                self._inject_block_model(app_label, ib)

            call_command('syncdb', interactive=False, verbosity=0)

            connection.queries = []

            start = time()
            container = self._create_container_and_blocks(
                app_label,
                num_blocks
            )
            create_duration = time() - start

            sql_time = sum(
                [float(q.get('time', 0)) for q in connection.queries]
            )

            query_times = []
            processing_times = []
            for it in xrange(0, self.num_queries):
                # clear previously logged queries
                connection.queries = []

                start = time()
                getattr(self, "run_{}_query".format(app_label))(container.id)
                processing_times.append((time() - start))

                sql_time = sum(
                    [float(q.get('time', 0)) for q in connection.queries]
                )
                query_times.append(sql_time)

            self.csv_writer.writerow([
                num_blocks,
                sql_time,
                create_duration,
                sum(query_times) / len(query_times),
                sum(processing_times) / len(processing_times),
            ])
            self.csv_fh.flush()
            print ("{num_blocks}, {create_time_sql}, "
                   "{create_time_processing}, {query_time_sql}, "
                   "{query_time_processing}").format(
                num_blocks=num_blocks,
                create_time_sql=sql_time,
                create_time_processing=create_duration,
                query_time_sql=sum(query_times) / len(query_times),
                query_time_processing=sum(processing_times) / len(processing_times),
            )
            self._drop_all_tables()

    def run_multi_table_query(self, container_id):
        container = get_model('multi_table', 'Container').objects.get(
            id=container_id
        )
        # generate a list here to make sure that the queryset is not
        # just assembled but also executed!!
        list(container.blocks.select_subclasses().order_by('display_order'))

    def run_generic_m2m_query(self, container_id):
        container = get_model('generic_m2m', 'Container').objects.get(
            id=container_id
        )
        list(container.blocks.all().generic_objects())

    def _inject_block_model(self, label, model_number):
        app_models = get_app(label)

        class Meta:
            app_label = label

        attrs = {
            'text': models.TextField(),
            '__module__': 'cpoc.{}.models'.format(label),
            'Meta': Meta,
        }
        class_name = "Text{}Block".format(model_number)
        setattr(
            app_models,
            class_name,
            type(class_name, (app_models.ContentBlock,), attrs)
        )
        model_class = getattr(app_models, class_name)

        if not label == 'multi_table':
            return

        text_field = None
        for field in model_class._meta.fields:
            if field.name == 'contentblock_ptr':
                text_field = field
                break

        if text_field is None:
            raise CommandError("cannot find text field on model")

        # this needs to be fixed up so that the generated classes show up
        # during retrieval of subclasses
        related = RelatedObject(
            app_models.ContentBlock,
            model_class,
            text_field
        )
        app_models.ContentBlock._meta._related_objects_cache[related] = None

    def _drop_all_tables(self):
        for table_name in connection.introspection.table_names():
            cursor = connection.cursor()
            cursor.execute(
                "DROP TABLE {} CASCADE;".format(
                    connection.ops.quote_name(table_name)
                )
            )

    def _create_container_and_blocks(self, app_label, num_blocks):
        container = get_model(app_label, 'Container').objects.create(
            name='Dummy Container',
        )
        for idx in xrange(1, num_blocks):
            klass = getattr(get_app(app_label), "Text{}Block".format(idx))
            getattr(
                self,
                '_create_{}_block'.format(app_label)
            )(klass, container, idx)
        return container

    def _create_multi_table_block(self, klass, container, index):
        klass.objects.create(
            text="The text of block #{}".format(index),
            container=container
        )

    def _create_generic_m2m_block(self, klass, container, index):
        block = klass.objects.create(text="Text of block #{}".format(index))
        container.blocks.connect(block)
