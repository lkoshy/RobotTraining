import random as _random
# avoid exposing 'random' as a variable. in the local namespace it is referenced as _random
# alternative is using '__all__' in the module level or switching to dynamic variable files

SCALAR = 'The value'
INTEGER = 42
LIST = ['first', 'second', 'third']
DICT = {
    'key': 'value',
    'foo': 'bar',
    'list': LIST
}
RANDOM_INTEGER = _random.randint(0, 10)  # you can also create a kw to generate a random variable
