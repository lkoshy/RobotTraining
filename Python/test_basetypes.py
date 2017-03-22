# Create needed variables here.

string = 'Hello, world!'
multiline_string = '''first line
second line
last line
'''
unicode_string = u'Hyv\xe4'
raw_string = r'c:\temp'
number = 3.14
integer = 42
boolean = True


def test_string():
    assert string == 'Hello, world!'
    assert string == "Hello, world!"


def test_multiline_string():
    assert multiline_string == 'first line\nsecond line\nlast line\n'
    assert multiline_string == '''first line
second line
last line
'''


def test_unicode_string():
    assert unicode_string == u'Hyv\xe4'


def test_raw_string():
    assert raw_string == r'c:\temp'
    assert raw_string == 'c:\\temp'


def test_string_methods():
    assert string.startswith('Hello')
    assert 'world' in string
    assert string.lower() == 'hello, world!'
    assert unicode_string.upper() == u'HYV\xc4'
    assert string + '!!?!?!' == 'Hello, world!!!?!?!'
    assert string * 2 == 'Hello, world!Hello, world!'


def test_numbers():
    assert number == 3.14
    assert number != '3.14'
    assert number == float('3.14')
    assert integer == 42
    assert integer == 42.0
    assert integer != 42.00000000000001
    assert integer == int('42')
    assert integer == int(42.9)
    assert integer == round(41.9)
    assert integer * 2 == 84
    assert number + integer == 45.14
    assert 5 / 2 == 2    # With Python 3 you would get 2.5!
                         # Can be changed in Python 2 with
                         # from __future__ import division
    assert 5 // 2 == 2   # Same result regardless Python version.


def test_boolean():
    assert boolean is True
    assert boolean == True    # Not recommended
    assert boolean is not False
    assert boolean
