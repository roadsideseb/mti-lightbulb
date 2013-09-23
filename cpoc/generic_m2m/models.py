from django.db import models
from django.template.defaultfilters import slugify

from genericm2m.models import RelatedObjectsDescriptor


class Container(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    blocks = RelatedObjectsDescriptor()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Container, self).save(*args, **kwargs)

    def __unicode__(self):
        return "Container {}".format(self.name)


class ContentBlock(models.Model):
    display_order = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if self.display_order is None:
            self.display_order = 0
        super(ContentBlock, self).save(*args, **kwargs)

    def __unicode__(self):
        return "Content block {}".format(self.display_order)

    class Meta:
        abstract = True


class TextBlock(ContentBlock):
    text = models.TextField()

    def __unicode__(self):
        return "Textblock '{}'".format(self.text[:20])


class ImageBlock(ContentBlock):
    image = models.ImageField(upload_to="images")

    def __unicode__(self):
        return "Image block '{}'".format(self.image.path)


class UserBlock(ContentBlock):
    user = models.ForeignKey('auth.User', related_name="+")

    def __unicode__(self):
        return "User block for {}".format(self.user.username)
