*** Test Cases ***
Run keyword if
    Run keyword if      7 > 5   Log     the expression was true!
    Run keyword if      7 < 5   Fail     the expression was true!

Run keyword if/unless
    Run keyword if      7 > 5   Log     the expression was true!
    Run keyword unless  7 > 5   Log     the expression was not true!


#more commonly done the following way these days
Run keyword If with ELSE
    Run keyword if      7 > 5
    ...     Log     The exp was true!
    ...     ELSE
    ...     Log     The exp ws not true!

