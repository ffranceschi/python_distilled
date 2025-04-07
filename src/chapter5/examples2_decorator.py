def trace(func):
    def call(*args, **kwargs):
        print('Calling', func.__name__)
        print(f'args: {args}, kwargs: {kwargs}')
        return func(*args, **kwargs)
    return call

@trace
def square(x):
    return x * x

print(square(3))

# ----
_event_handlers = { }
def eventhandler(event):
    def register_function(func):
        _event_handlers[event] = func
        print(f'Evento: {event}, _event_handlers = {_event_handlers}')
        return func
    return register_function

@eventhandler('BUTTON')
def handle_button(msg):
    pass

handle_button('BUTTON1')