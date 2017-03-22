from contextlib import contextmanager

# create an obj of class EH and use it as context manager

class ErrorHandler:

    def __init__(self):
        self.error = None

    def __enter__(self):  # is called when the context is called.
        return self

    # is called when context is consumed.
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.error = str(exc_val)
            return isinstance(exc_val, Exception)
        return False


@contextmanager
def error_handler():
    try:
        yield  # yield will return a generator
    except Exception:
        pass
