# Implement imported functions in a separate module.

from functions import (
    simple,
    one_argument,
    two_arguments,
    defaults,
    varargs,
    kwargs,
    caller
)


def test_simple():
    simple()
    greeting = simple()
    assert greeting == 'Hello, world!'
    assert simple.__name__ == 'simple'


def test_function_is_assignable():
    my_simple = simple
    assert my_simple() == 'Hello, world!'
    assert my_simple.__name__ == 'simple'


def test_arguments():
    assert one_argument('world') == 'Hello, world!'
    assert one_argument('tellus') == 'Hello, tellus!'
    assert one_argument(99) == 'Hello, 99!'
    assert two_arguments(1, 2) == 3
    assert two_arguments('1', '2') == 3


def test_arguments_with_default_values():
    assert defaults('world') == 'Hello, world!'
    assert defaults('tellus', '!!?!?') == 'Hello, tellus!!?!?'
    assert defaults('tellus', ending='!!?!?') == 'Hello, tellus!!?!?'
    assert defaults(ending='!!?!?', name='tellus') == 'Hello, tellus!!?!?'
    assert defaults('Kitty', separator=' ') == 'Hello Kitty!'
    assert defaults('again', separator=' ', ending='...') == 'Hello again...'
    assert defaults('again', '...', ' ') == 'Hello again...'


# Topics below are somewhat more advanced. They can be gone through later or
# skipped altogether.

def test_variable_number_of_arguments():
    assert varargs() == 0
    assert varargs(1) == 1
    assert varargs(1, 2) == 3
    assert varargs(1, 2, 3, 4, 5) == 15


def test_argument_unpacking():
    args = [1, 2]
    assert varargs(*args) == 3    # equivalent to `varargs(1, 2)`
    assert defaults(*args) == 'Hello, 12'
    assert varargs(*range(100)) == 4950


def test_keyword_arguments():
    assert kwargs() == ''
    assert kwargs(a=1) == 'a: 1'
    assert kwargs(x=1, z=3, y=2) == 'x: 1, y: 2, z: 3'


def test_caller():
    assert caller(simple) == 'Hello, world!'
    assert caller(one_argument, 'called') == 'Hello, called!'
    assert caller(varargs, 1, 2) == 3
    assert caller(defaults, 'tellus', ending='!!?!?') == 'Hello, tellus!!?!?'
    assert caller(kwargs, foo=1, bar=2) == 'bar: 2, foo: 1'
