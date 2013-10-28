from django.db import models
from django.utils.datastructures import SortedDict
from django.template.defaultfilters import slugify

from jsonfield import JSONField


class Container(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    blocks = JSONField(load_kwargs={'object_pairs_hook': SortedDict})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.blocks is None:
            self.blocks = []
        super(Container, self).save(*args, **kwargs)

    def __unicode__(self):
        return "Container {}".format(self.name)
