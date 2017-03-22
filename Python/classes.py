class Simple(object):
    attribute = 'Hello, world!'
    _private_by_convention = 123
    __a_bit_more_private = 456


class Person(object):

    def __init__(self, name, email=None):
        self.name = name
        self.email = email

    def greet(self, name, greeting='hello'):
        return '{} says {} to {}'.format(self.name, greeting, name)

    def __str__(self):
        if not self.email:
            return self.name
        return '{} <{}>'.format(self.name, self.email)

        # Alternatively using ternary if/else (bit long in this case)
        return '{} <{}>'.format(self.name, self.email) if self.email else self.name

    def __eq__(self, other):
        return (isinstance(other, Person) and
                self.name == other.name and
                self.email == other.email)

    def __ne__(self, other):
        return not self == other


# Keywords for Robot

def create_person(name, email=None):
    return Person(name, email)


def greet_person(person1, person2, greeting='hello'):
    print person1.greet(person2.name, greeting)
