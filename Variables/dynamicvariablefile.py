#  dy files shd implement this fn.
def get_variables(name):
    return {'dynamic': 'Variable from dynamic variable file',
            'name': name,
            'object': Object(name)
            }


class Object:
    def __init__(self, name):
        self.name = name
        self.num = [1,2,3,4]

    def greet(self, name):
        return '{} says hello to {}.'.format(self.name, name)

    def __str__(self):
        return self.name


