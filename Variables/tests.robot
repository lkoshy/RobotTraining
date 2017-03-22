*** Settings ***
Variables   dynamicvariablefile.py      John

*** Variables ***
${SCALAR}                The value
# Create list varibles in the variable table
@{LIST}     first item  second item     third item
@{LONG LIST}     1  2   3   4   5   6
...              11     12  13    # a long list can be continued to the second line using three dots
${LONG STRING}  This is so long string
...             that I split this to two lines.
${SEPARATOR}    SEPARATOR=\n  # SEPARATOR is not part of the final value.
...             This example illustrates using a
...             custom separator. Now we
...             have a multiline string
...             This is the third row.

#Dict variables
&{DICT}     key=value   foo=bar     list=${LIST}

*** Test Cases ***
Scalar variables
    Should be equal   ${SCALAR}  The value
    Should be equal   ==${SCALAR}==  ==The value==
    ${integer}=   Convert to integer   42
    Should not be equal    ${integer}  42
    Should be equal as integers   ${integer}  42
    Should be equal    **${integer}**  **42**

List variables
    Length should be   ${LIST}    3
    Length should be   ${LONG LIST}    9
    Log many           @{LIST}   # '@' refering to the whole list and the list is expanded. called with those 3 list item as arguments
    Log many           first item  second item  third item
    ${list1}=    Create list    a   b   c
    @{list2}=    Create list    a   b   c
    Should be equal     ${list1}    ${list2}
    Log many        @{list1}    @{list2}

Strings in multiple line
    Log many    ${LONG STRING}  ${SEPARATOR}

Dictionary variables
    Length should be    ${DICT}     3
    Log many            &{DICT}

Accessing list and dict items
    Should be equal     @{LIST}[0]      first item
    Should be equal     @{LIST}[1]      second item
    Should be equal     &{DICT}[key]    value
    Should be equal     &{DICT}[list]   ${LIST}

Built-in variables
    Should be empty     ${EMPTY}
    Length should be    ${SPACE}     1
    Log many            ${TEMPDIR}  ${EXECDIR}  ${CURDIR}

Numbers, Boolean and None
    ${integer}=         Convert to integer      42
    Should be equal     ${integer}      ${42}    # robot converts to integer 42
    Should be equal as numbers      ${3.14}     3.14
    Should be equal                 ${1e6}      ${1000 000}

Automatic variables
    [Documentation]     Robot documentation
    [Tags]      example     tags
    Log many    @{TEST TAGS}
    [Teardown]  Log many    ${TEST STATUS}      ${TEST MESSAGE}

Variable scopes 1
    Should be equal     ${SCALAR}   The value
    ${scalar} =       Set variable    new value
    Should be equal     ${SCALAR}       new value
    scalar variable value should be     The value   # user defined keyword
    set test variable   ${SCALAR}   # built in keyword
    Set suite variable      ${NEW VARIABLE}     New variable in suite scope
    Set global variable      ${GLOBAL}           Global variable are also seen by other suites

Variable scopes 2
    Should be equal     ${SCALAR}   The value
    Should be equal     ${NEW VARIABLE}     New variable in suite scope   # available in all scopes
    Should be equal     ${GLOBAL}           Global variable are also seen by other suites

Extended variable syntax
    Should be equal     ${OBJECT.name}  John
    Length should be    ${OBJECT.num}   4
    Should be equal     ${OBJECT.greet('Lisa')}  John says hello to Lisa.


Accessing dict values using extended variable syntax
    Should be equal     ${DICT.key}   &{DICT}[key]
    Should be equal     ${DICT.list}  &{DICT}[list]
    Log many            @{DICT.list}



*** Keywords ***
scalar variable value should be
    [Arguments]     ${expected}
    Should be equal     ${SCALAR}   ${expected}

