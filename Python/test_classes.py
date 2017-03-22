# Implement imported classes in a separate module.

from classes import (
    Simple,
    Person
)


def test_instantiation():
    s = Simple()
    t = Simple()
    assert isinstance(s, Simple)
    assert isinstance(t, Simple)
    assert s is not t
    assert s != t


def test_class_and_instance_attributes():
    assert Simple.attribute == 'Hello, world!'
    instance = Simple()
    assert instance.attribute == 'Hello, world!'
    instance.attribute = 42
    assert instance.attribute == 42
    assert Simple.attribute == 'Hello, world!'


def test_no_privacy():
    assert Simple._private_by_convention == 123
    assert not hasattr(Simple, '__a_bit_more_private')
    assert Simple._Simple__a_bit_more_private == 456


def test_instantiation_with_arguments():
    jane = Person('Jane')
    assert jane.name == 'Jane'
    assert jane.email is None
    assert not hasattr(Person, 'name')
    john = Person('John', 'john@example.com')
    assert john.name == 'John'
    assert john.email == 'john@example.com'


def test_methods():
    jane = Person('Jane')
    assert jane.greet('John') == 'Jane says hello to John'
    jane.name = 'Janet'
    assert jane.greet('Johnny') == 'Janet says hello to Johnny'
    assert Person('John').greet('Jane', greeting='hi') == 'John says hi to Jane'


def test_string_representation():
    jane = Person('Jane')
    assert str(jane) == 'Jane'
    jane = Person('Jane', 'j@a.ne')
    assert str(jane) == 'Jane <j@a.ne>'
    assert 'To: %s' % jane == 'To: Jane <j@a.ne>'
    assert 'To: {}'.format(jane) == 'To: Jane <j@a.ne>'


def test_equality():
    jane1 = Person('Jane')
    jane2 = Person('Jane')
    assert jane1 is jane1
    assert jane1 is not jane2
    assert jane1 == jane1
    assert jane1 == jane2
    assert not jane1 == 'Jane'
    assert not jane1 != jane2
    assert jane1 != 'Jane'
    john1 = Person('John', 'john@1.email')
    john2 = Person('John', 'john@2.email')
    assert not john1 == john2
    assert john1 != john2
