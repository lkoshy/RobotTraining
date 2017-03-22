*** Settings ***
Variables   variablefile.py
Variables   dynamicvariablefile.py  John
Variables   variables.yaml

*** Testcases ***
Variable file
    Should be equal     ${SCALAR}    The value
    Should be equal     ${INTEGER}   ${42}
    Log many            @{LIST}      &{DICT}
    Log                 ${RANDOM INTEGER}

Dynamic variable file
    Should be equal     ${DYNAMIC}    Variable from dynamic variable file
    Should be equal     ${NAME}       John
    Log     ${OBJECT}

YAML variable file
    Should be equal   ${YAML}   is cool!
    Should be equal   ${YAML INTEGER}   ${42}
    Log many          @{YAML LIST}
