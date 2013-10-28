
_library = {}


def register_block(klass):
    global _library
    _library[klass.__name__.lower()] = klass
    return klass


def get_blocks():
    return _library


def get_block_class(name):
    return _library.get(name)


class BaseContentBlock(object):
    template_name = None
    name = None


class TextBlock(BaseContentBlock):
    text = unicode
