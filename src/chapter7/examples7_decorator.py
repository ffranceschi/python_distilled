_registry = { }
def register_decoder(cls):
    for mt in cls.mimetypes:
        _registry[mt.mimetype] = cls
        return cls

def create_decoder(mimetype):
    return _registry[mimetype]()


@register_decoder
class TextDecoder:
    mimetypes = [ 'text/plain' ]

decoder = create_decoder('image/jpg')





