import logging
import itertools

from optparse import make_option

from django.db.backends import util
from django.db.models import get_model
from django.core.management import call_command
from django.core.management.base import NoArgsCommand

from devserver.logger import GenericLogger
from devserver.modules.sql import DatabaseStatTracker

from cpoc.multi_table import factories as mt_factories

logger = logging.getLogger('benchy')


class Command(NoArgsCommand):
    option_list = NoArgsCommand.option_list + (
        make_option(
            '-b', '--num-blocks',
            dest='num_blocks',
            type=int,
            default=500,
        ),
    )

    def handle_noargs(self, **options):
        print "Clearing data from database"
        call_command('flush', interactive=False)

        block_factories = itertools.cycle([
            mt_factories.TextBlockFactory,
            mt_factories.ImageBlockFactory,
        ])

        container = mt_factories.ContainerFactory()
        for idx in xrange(0, options.get('num_blocks')):
            block_factories.next().create(container=container)

        DatabaseStatTracker.logger_name = 'benchy'
        util.CursorDebugWrapper = DatabaseStatTracker
        DatabaseStatTracker.logger = GenericLogger(DatabaseStatTracker)

        container = get_model('multi_table', 'Container').objects.get(id=container.id)
        list(container.blocks.select_subclasses().order_by('display_order'))
