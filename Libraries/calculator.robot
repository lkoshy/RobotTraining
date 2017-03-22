*** Settings ***
Library            CalculatorLibrary.py
Library  CalculatorLibrary.py
Library  CalculatorLibraryEmbedded.py

*** Test Cases ***
Push buttons
    Push Button    1
    Push Button    2
    Result Should Be    12

Calculation
    Push Button    1
    Push Button    +
    Push Button    2
    Push Button    =
    Result Should Be    3

Clear
    Push Button    1
    Push Button    C
    Result Should Be    ${EMPTY}

Longer calculation
    Push Buttons    1 + 2 + 3 + 4 - 10 =
    Result Should Be    0

Validating calculation
    [Template]    Calculation Result Should Be
    12                    12
    1 + 2                 3
    1 + 2 + 3 + 4 - 10    0

Invalid expression
    [Template]    Calculation Should Fail
    invalid    Invalid button 'i'.
    1 + * 2    Invalid expression '1+*2'.
    1 / 0      Division by zero.

Embedded arguments
    Given calculator is cleared
    When calculation "1 + 3" is evaluated
    Then result should be "4"
