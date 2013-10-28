import factory
import humanize

from django.db.models import get_model


class ContainerFactory(factory.DjangoModelFactory):
    FACTORY_FOR = get_model("generic_m2m", "Container")

    name = factory.Sequence(lambda n: "Container {}".format(n))


class TextBlockFactory(factory.DjangoModelFactory):
    FACTORY_FOR = get_model("generic_m2m", "TextBlock")

    text = factory.Sequence(
        lambda n: "Sample text {}".format(humanize.apnumber(n))
    )


class ImageBlockFactory(factory.DjangoModelFactory):
    FACTORY_FOR = get_model("generic_m2m", "ImageBlock")

    image = factory.django.ImageField(color='red')
