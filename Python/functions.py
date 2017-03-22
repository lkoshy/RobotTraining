def simple():
    print 'Hi there!'
    return 'Hello, world!'


def one_argument(name):
    # Old, C-like string formatting:
    return "Hello, %s!" % name
    # New style string formatting:
    return "Hello, {}!".format(name)
    # Concatenate using '+':
    return "Hello, " + str(name) + "!"


def two_arguments(num1, num2):
    return float(num1) + float(num2)


def defaults(name, ending='!', separator=', '):
    # Old style:
    return 'Hello%s%s%s' % (separator, name, ending)
    # New style:
    return 'Hello{}{}{}'.format(separator, name, ending)
    # With explicit indices:
    return 'Hello{0}{1}{2}'.format(separator, name, ending)
    # With indices in different order:
    return 'Hello{2}{0}{1}'.format(name, ending, separator)
    # Named placeholders:
    return 'Hello{sep}{name}{end}'.format(sep=separator, name=name, end=ending)


# Regular for loop
def varargs(*numbers):
    result = 0
    for num in numbers:
        result += int(num)
    return result


# Alternatively using built-in function `sum` and a generator expression
def varargs(*numbers):
    return sum(int(n) for n in numbers)


def kwargs(**args):
    result = []
    for key in sorted(args):
        result.append('{}: {}'.format(key, args[key]))
    return ', '.join(result)


# Alternatively iterating items
def kwargs(**args):
    result = []
    for key, value in sorted(args.items()):
        result.append('{}: {}'.format(key, value))
    return ', '.join(result)


# Alternatively using generator expression
def kwargs(**args):
    return ', '.join('{}: {}'.format(key, args[key]) for key in sorted(args))


def caller(func, *args, **kws):
    return func(*args, **kws)
