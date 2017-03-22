*** Variables ***
@{animals}  cat  dog    cow     horse

*** Test Cases ***
Normal for loop
# for loop syntax in robot.
#
    :FOR    ${animal}   IN  @{animals}
    \   Log   ${animal}
    \   Log     Another keyword inside the loop
    Log     Outside the for loop

# not commonly used
Multiple loop variables
    :FOR    ${char}     ${num}  IN  a   1   c   2   e   3
    \   Log     ${char}: ${num}

For in range
    :FOR       ${index}     IN RANGE    10
    \   Log     ${index}

# nested for loops not possible but something similar is possible
# call a kw from another loop
Nested for loop
    :FOR    ${animal} IN    ${ANIMALS}
    \   keyword with loop   ${animal}

*** Keywords ***
keyword with loop
    [Arguments]     ${arg}
    :FOR ${item}  IN     ${arg}     some    value  here
    \

