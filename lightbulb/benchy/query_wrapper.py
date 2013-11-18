from django.db.models import get_app
from django.db.models import get_model


class BaseQueryWrapper(object):

    def create_query(self, app_label, num_models):
        raise NotImplementedError()

    def select_query(self, model_id):
        raise NotImplementedError()


class ContainerBlockQueryWrapper(BaseQueryWrapper):

    def create_query(self, app_label, num_models):
        container = get_model(app_label, 'Container').objects.create(
            name='Dummy Container')
        for idx in xrange(1, num_models):
            klass = getattr(get_app(app_label), "Text{}Block".format(idx))
            for iddx in xrange(0, 20):
                self.create_block_query(klass, container, idx)
        return container
