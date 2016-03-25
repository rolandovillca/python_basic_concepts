'''
*is* checks that 2 arguments refer to the same object.
*==* checks that 2 arguments have the same value.

There is a simple rule of thumb to tell you when to use == or is:
    == is for value equality. Use it when you would like to know if two objects have the same value.
    IS is for reference equality. Use it when you would like to know if two references refer to the same object.
'''

# EXAMPLE 1: Double equals vs is in python:
# ==============================================================================
# dir() returns a list which contains the same data for both foo and 10,
# but the actual list instances for the 2 things are different.

num = 10

# == will return true if the objects referred to by the variables are equal.
dir(num) == dir(10)

# IS is will return True if two variables point to the same object.
dir(num) is dir(10)
