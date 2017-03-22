# extend the existing libr
# 1.simply inherit and add new functionality
# 2. use existing libr as a tool internally


# Notes: keywords can have tags
# Hybrid and dynamic APIs
# Dynamic APi - 1. libr can scan what scripts are in the file sys and can expose
#   the scripts as keywords
#   2. when libr grow larger,

from robot.api.deco import keyword
from CalculatorLibrary import CalculatorLibrary


class CalculatorLibraryEmbedded:
    def __init__(self):
        self.lib = CalculatorLibrary()

    @keyword
    def calculator_is_cleared(self):
        self.lib.push_button('C')

    # giving custom name to keywords
    @keyword('Calculation "${expression}" is evaluated')
    def calculation_is_evaluated(self, expression):
        self.lib.push_buttons(expression + '=')

    @keyword('Result should be "${expected}"', tags=['keyword', 'tags', 'here'])
    def result_should_be(self, expected):
        self.lib.result_should_be(expected)