# Implement imported functions in a separate module.

from control import (
    is_positive,
    select_positive,
    should_be_positive
)


def test_if_else():
    assert is_positive(1) == '1 is positive'
    assert is_positive(-1.5) == '-1.5 is negative'
    assert is_positive(0) == '0 is zero'


def test_looping():
    assert select_positive([]) == []
    assert select_positive([1, 2]) == [1, 2]
    assert select_positive((0, -1)) == []
    assert select_positive([1, -2, 0, -1.5, 7, 1.1]) == [1, 7, 1.1]
    assert select_positive((1, 2, -3)) == [1, 2]


def test_exceptions():
    should_be_positive(1)
    try:
        should_be_positive(-1)
    except AssertionError as err:
        assert str(err) == '-1 is not positive'
    except ValueError:
        raise AssertionError('This should never happen!!')
    else:
        raise AssertionError('Expected AssertionError')


def test_errors():
    should_be_positive('1')
    try:
        should_be_positive('xxx')
    except ValueError:
        pass
    else:
        raise AssertionError('Expected ValueError')
    finally:
        pass  # finally block executed always
