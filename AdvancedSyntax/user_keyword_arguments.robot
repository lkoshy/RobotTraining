*** Test Cases ***
Positional arguments
    No arguments
    One argument    xxx
    Three arguments     a   b   c

Embedded arguments
    This is a "good" example
    This is a "bad" example

Default values
    Default values      foo
    Default values      foo     bar
    Default values      foo     bar     zip

*** Keywords ***
No arguments
    No operation

One argument
    [Arguments]  ${arg}
    Log         ${arg}

Three arguments
    [Arguments]  ${arg1}    ${arg2}     ${arg3}
    Log many     ${arg1}    ${arg2}     ${arg3}

This is a "${type}" example
    Log     ${type}

Default values
    [Arguments]     ${mandatory}    ${opt1}=xxx     ${opt2}=${42}
    Log many     ${mandatory}  ${opt1}   ${opt2}


