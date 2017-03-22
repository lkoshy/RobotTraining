from functools import wraps


def div(func):
    @wraps(func) # decorate using the built in wrap function
                #which will automatically preserve the signature of the function passed.
    def wrapper(*args, **kwargs):
        return '<div>{}</div>'.format(func(*args, **kwargs))
    return wrapper


def p(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return '<p>{}</p>'.format(func(*args, **kwargs))
    return wrapper


# this method returns a tag
def tag(name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return '<{tag}>{text}</{tag}>'.format(text=func(*args, **kwargs),
                                                  tag=name)
        return wrapper
    return decorator


class Person(object):
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    # syntax related to property
    @full_name.setter
    def full_name(self, name):
        self.first_name, self.last_name = name.split(' ', 1)
