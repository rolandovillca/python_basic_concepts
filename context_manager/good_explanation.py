'''
# There are two easy ways to implement this functionality yourself:
# 1. Using a class approach
# 2. using a generator approach
'''

# Implementation with the class approach:
# ==============================================================================
# This is just a regular Python object with two extra methods that are used by
# the with statement.
# CustomOpen is first instantiated and then its __enter__ method is called and 
# whatever __enter__ returns is assigned to f in the as f part of the statement.
# When the contents of the with block is finished executing, 
# the __exit__ method is then called.

class CustomOpen(object):
    def __init__(self, filename):
        self.file = open(filename)

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()

with CustomOpen('myfile.txt') as f:
    content = f.read()

# Implementation using the generator approach using Python's own contextlib:
# ==============================================================================
# This works in exactly the same way as the class example above.
# The custom_open function executes until it reaches the yield statement.
# It then gives control back to the with statement,
# which assigns whatever was yield’ed to f in the as f portion.
#
# The finally clause ensures that close() is called
# whether or not there was an exception inside the with.

from contextlib import contextmanager

@contextmanager
def custom_open(filename):
    f = open(filename)
    try:
        yield f
    finally:
        f.close()

with custom_open('myfile.txt') as f:
    content = f.read()

# Decision of which to use:
# Since the two approaches appear the same, we should follow the Zen of Python
# to decide when to use which.
# The class approach might be better if there's a considerable
# amount of logic to encapsulate.
# The function approach might be better for situations
# where we're dealing with a simple action.