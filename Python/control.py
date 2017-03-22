def is_positive(number):
    if number > 0:
        template = '{} is positive'
    elif number < 0:
        template = '{} is negative'
    else:
        template = '{} is zero'
    return template.format(number)


# Regular for loop
def select_positive(numbers):
    positive = []
    for num in numbers:
        if num > 0:
            positive.append(num)
    return positive


# Alternatively using list comprehension
# (this version overrides the one above)
def select_positive(numbers):
    return [num for num in numbers if num > 0]


def should_be_positive(number):
    if float(number) <= 0:
        raise AssertionError('{} is not positive'.format(number))
    print '{} is positive'.format(number)
