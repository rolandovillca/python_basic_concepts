'''
The defining feature of a context manager is that it has two special methods:
__enter__() and __exit__(). These are used by the with statement to enter and
exit the context.

We'll often use context managers to make transient global changes.
This might be a change to the database transaction status or a change to the locking
status, something that we want to do and then undo when the transaction is complete.

Using these magic methods (__enter__, __exit__) allows you to implement objects
which can be used easily with the with statement.

The general idea is that it makes it easy to build code which needs some 'cleandown'
code executed (think of it as a try-finally block). Some more explanation here.

A useful example could be a database connection object (which then automagically
closes the connection once the corresponding 'with'-statement goes out of scope:
'''

# EXAMPLE 1:
# ==============================================================================
class DatabaseConnection(object):
    def __enter__(self):
        # Make database connection and return it.
        return self.dbconn

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Make sure the database connecton gets closed.
        self.dbconn.close()

# As explained above, use this object with the with statement
# (you may need to do from __future__ import with_statement
# at the top of the file if you're on Python 2.5).

with DatabaseConnection() as mydbconn:
    # Do stuff.


# EXAMPLE 2:
# ==============================================================================
class Rectangle:
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
    
    def __enter__(self):
        print 'in __enter__'
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        print '__exit__'

    def device_by_zero(self):
        # Causes ZeroDivisionError exception
        return self.width / 0

with Rectangle(3, 4) as rectangle:
    # Exception successfully pass to __exit__
    rectangle.device_by_zero()

# Output should be:
# "in __enter__"
# "in __exit__"
# Traceback (most recent call last):
#   File "e0235.py", line 27, in <module>
#     r.divide_by_zero()


# EXAMPLE 3:
# ==============================================================================
class MyClass(object):
    def __enter__(self):
        if moon_phase > 0:
            self.returnval = 123
        else:
            self.returnval = 456
        return returnval

    def __exit__(self, *args):
        number = self.returnval
        print 'End of block with', number