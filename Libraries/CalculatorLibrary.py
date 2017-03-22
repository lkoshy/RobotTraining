from calculator import Calculator, CalculationError
from robot.api import logger


class CalculatorLibrary:
    """Library for testing *Calculator*

    Uses push() method for interaction
    """

    def __init__(self):
        self.calc = Calculator()
        self.result = ''

    # signature of the key word
    # kw can also return a value
    def push_button(self, button):
        """ Pushes the specified ``button``

        """
        logger.info('Pushing button {}'.format(button))
        self.result = self.calc.push(button)
        return self.result

    def result_should_be(self, expected):
        if self.result != expected:
            raise AssertionError('Expected result '
                                 'should be {} but was {}'.format(expected, self.result))

    def push_buttons(self, expression):
        for button in expression.replace(' ', ''):
            self.push_button(button)

    def calculation_result_should_be(self, expression, expected):
        self.push_buttons('C' + expression + '=')
        self.result_should_be(expected)

    def calculation_should_fail(self, expression, expected_error):
        try:
            self.push_buttons('C' + expression + '=')
        except CalculationError as error:
            if str(error) != expected_error:
                raise AssertionError('Expected error '
                                     '{} but was {}'.format(expected_error, self.result))
        else:
            raise AssertionError('Expected error "{}"did not occur'.format(expected_error))
