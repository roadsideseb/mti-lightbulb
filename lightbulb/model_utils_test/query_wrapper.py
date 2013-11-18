from django.db.models import get_model

from ..benchy.query_wrapper import ContainerBlockQueryWrapper


class QueryWrapper(ContainerBlockQueryWrapper):

    def select_query(self, model_id):
        container = get_model('model_utils_test', 'Container').objects.get(
            id=model_id)
        # generate a list here to make sure that the queryset is not
        # just assembled but also executed!!
        list(container.blocks.select_subclasses().order_by('display_order'))

    def create_block_query(self, klass, container, index):
        klass.objects.create(
            text="The text of block #{}".format(index), container=container)
