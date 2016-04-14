import sys

# EXAMPLE 1: Define my own custom Error:
# ==============================================================================
class MyCustomError(Exception):
    
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


# EXAMPLE 2: The first way to raise my defined error:
# ==============================================================================
try:
    raise MyCustomError(2*2)
except MyCustomError as err:
    print "My custom error message: {} ".format(err.value)

print


# EXAMPLE 3: Another way to raise an exception is:
# ==============================================================================
raise MyCustomError('oops!')