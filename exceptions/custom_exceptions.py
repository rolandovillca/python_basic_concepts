import sys

# Define my own Error:
class MyCustomError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# Raise my defined error.
try:
    # f = open('myfile.txt')
    # r = f.readline()
    # i = int(s.strip())
    raise MyCustomError(2*2)
except MyCustomError as err:
    print "My custom error message: {} ".format(err.value)

print

# Another way to raise an exception is.
raise MyCustomError('oops!')