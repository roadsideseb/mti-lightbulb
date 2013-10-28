from django.db import models
from django.template.defaultfilters import slugify

from model_utils.managers import InheritanceManager


class Container(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Container, self).save(*args, **kwargs)

    def __unicode__(self):
        return "Container {}".format(self.name)


class ContentBlock(models.Model):
    container = models.ForeignKey('Container', related_name="blocks")
    display_order = models.PositiveIntegerField()

    objects = InheritanceManager()

    def save(self, *args, **kwargs):
        if self.display_order is None:
            self.display_order = self.container.blocks.count()
        super(ContentBlock, self).save(*args, **kwargs)

    def __unicode__(self):
        return "Content block {} in {}".format(
            self.display_order,
            self.container.name
        )


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
