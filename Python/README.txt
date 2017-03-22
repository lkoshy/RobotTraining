This directory contains Python training material.

Files starting with `test_` contain exercises. They can be executed with
`py.test` tool that can be installed with `pip install pytest` and used like:

    py.test test_basetypes.py       # run all tests in test_basetypes.py
    py.test test_basetypes.py -x    # same but stop on the first failure
    py.test .                       # run all tests in the current directory

Additional Python files need to be created to make tests pass. See test files
themselves for more details. The recommended order to go through the exercises
is:

    # Basic course
    test_basetypes.py
    test_containers.py
    test_modules.py
    test_functions.py
    test_control.py
    test_classes.py
    # Advanced course
    test_files.py
    test_decorators.py
    test_iterators.py
    test_context_managers.py

There is a lot of Python related training material freely available in the
Internet. You can start from the official Python Tutorial
<http://docs.python.org/2/tutorial/> or look at what other resources are
available at https://www.python.org/about/gettingstarted/.

For Python style guide see PEP-8: https://www.python.org/dev/peps/pep-0008/.

For more information about Unicode and using non-ASCII characters:
- http://www.joelonsoftware.com/articles/Unicode.html
- https://docs.python.org/2/howto/unicode.html
- https://www.python.org/dev/peps/pep-0263/  (source encoding)
