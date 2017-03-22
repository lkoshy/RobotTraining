# Implement imported iterators/generators.
import pytest


from iterators import Iterable, Iterator, generator_function


def test_iterator():
    iterable = Iterable(3)
    assert [item for item in iterable] == [0, 1, 2]
    assert tuple(iterable) == (0, 1, 2)


def test_iterator_protocol():
    it = iter(Iterable(3))
    assert isinstance(it, Iterator)
    assert next(it) == 0
    assert next(it) == 1
    assert next(it) == 2
    with pytest.raises(StopIteration):
        next(it)


def test_generator():
    generator = generator_function(3)
    assert list(generator) == [0, 1, 2]
    # Once consumed, the generator is empty
    assert list(generator) == []
    assert list(generator_function(3)) == [0, 1, 2]
