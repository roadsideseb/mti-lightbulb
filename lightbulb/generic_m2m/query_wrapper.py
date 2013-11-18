from django.db.models import get_model

from ..benchy.query_wrapper import ContainerBlockQueryWrapper


class QueryWrapper(ContainerBlockQueryWrapper):

    def select_query(self, model_id):
        container = get_model('generic_m2m', 'Container').objects.get(
            id=model_id)
        list(container.blocks.all().generic_objects())

    def create_block_query(self, klass, container, index):
        block = klass.objects.create(text="Text of block #{}".format(index))
        container.blocks.connect(block)
