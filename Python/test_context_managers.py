# Implement imported context managers.

import pytest

from contextmanagers import ErrorHandler, error_handler



def test_handle_exceptions():
    with ErrorHandler():  # with is context manager
        pass
    with ErrorHandler():
        raise Exception('This ought to be handled!')


def test_access_manager():
    with ErrorHandler() as handler:
        pass
    assert handler.error is None
    with ErrorHandler() as handler:
        raise Exception('This ought to be handled!')
    assert handler.error == 'This ought to be handled!'


def test_dont_catch_system_exiting():
    with pytest.raises(KeyboardInterrupt):
        with ErrorHandler():
            raise KeyboardInterrupt('This should not be caught!')


def test_implemented_using_contextmanager_decorator():
    with error_handler():
        pass
    with error_handler():
        raise Exception('This ought to be handled!')
    with pytest.raises(KeyboardInterrupt):
        with error_handler():
            raise KeyboardInterrupt('This should not be caught!')
