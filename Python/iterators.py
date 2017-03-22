class Iterable:
    def __init__(self, limit):
        self.limit = limit

    # __iter__ makes a class iterable. iter returns an iterator
    def __iter__(self):
        return Iterator(self.limit)


class Iterator:
    def __init__(self, limit):
        self.limit = limit
        self.index = -1

    def __next__(self):
        self.index += 1
        if self.index >= self.limit:
            raise StopIteration
        return self.index

    def __iter__(self):
        return self


def generator_function(limit):
    index = 0
    while index < limit:
        yield index
        index += 1
