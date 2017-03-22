# Implement imported decorators.

import inspect
import pytest

from decorators import (
   div,
   p,
   tag,
   Person
)


def test_decorator_without_special_syntax():
    def greet():
        return 'Hello, world!'
    div_greet = div(greet)
    assert div_greet() == '<div>Hello, world!</div>'


def test_decorator_syntax():
    @div
    def greet():
        return 'Hello, world!'
    assert greet() == '<div>Hello, world!</div>'


def test_forward_arguments():
    @div
    def greet(name='world'):
        return 'Hello, {}!'.format(name)
    assert greet() == '<div>Hello, world!</div>'
    assert greet('Robot') == '<div>Hello, Robot!</div>'


def test_func_info():
    @div
    def greet(name):
        """Example docstring."""
        return 'Hello, {}!'.format(name)
    assert greet.__name__ == 'greet'
    assert greet.__doc__ == 'Example docstring.'
    # Unfortunately `functools.wraps` doesn't preserve function signature.
    # External `decorator` module can be used if that is needed.
    spec = inspect.getargspec(greet)
    assert spec.args == []
    assert spec.varargs == 'args'
    assert spec.keywords == 'kwargs'


def test_stacked():
    @div
    @p
    def greet(name):
        return 'Hello, {}!'.format(name)
    assert greet('Robot') == '<div><p>Hello, Robot!</p></div>'


def test_decorator_arguments():
    @tag('div')
    def greet(name):
        return 'Hello, {}!'.format(name)
    assert greet('Robot') == '<div>Hello, Robot!</div>'

    @tag('div')
    @tag('p')
    def greet(name):
        return 'Hello, {}!'.format(name)
    assert greet('Robot') == '<div><p>Hello, Robot!</p></div>'
    assert greet.__name__ == 'greet'


def test_property():
    person = Person('John', 'Doe')
    assert person.first_name == 'John'
    assert person.last_name == 'Doe'
    assert person.full_name == 'John Doe'
    person.first_name = 'Jane'
    assert person.full_name == 'Jane Doe'


def test_property_setter():
    person = Person('John', 'Doe')
    person.full_name = 'Jane Smith'
    assert person.first_name == 'Jane'
    assert person.last_name == 'Smith'
    person.full_name = 'Guido van Rossum'
    assert person.first_name == 'Guido'
    assert person.last_name == 'van Rossum'
