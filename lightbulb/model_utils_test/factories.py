import factory
import humanize

from django.db.models import get_model


class ContainerFactory(factory.DjangoModelFactory):
    FACTORY_FOR = get_model("model_utils_test", "Container")

    name = factory.Sequence(lambda n: "Container {}".format(n))


class TextBlockFactory(factory.DjangoModelFactory):
    FACTORY_FOR = get_model("model_utils_test", "TextBlock")

    text = factory.Sequence(
        lambda n: "Sample text {}".format(humanize.apnumber(n))
    )


class ImageBlockFactory(factory.DjangoModelFactory):
    FACTORY_FOR = get_model("model_utils_test", "ImageBlock")

    image = factory.django.ImageField(color='red')
