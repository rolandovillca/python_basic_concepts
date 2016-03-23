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

with MyClass() as x:
    print x   # 123
    with MyClass() as y:
        print x, 'and', y   # 123 and 456

    # Printed "End of block with 456"
    print x   # 123
# Printted "End of block with 123"


# EXAMPLE 4:
# ==============================================================================
'''
The contextlib module contains utilities for working with context managers and the with statement.

Note Context managers are tied to the with statement.
Since with is officially part of Python 2.6,
you have to import it from __future__ before using contextlib in Python 2.5.

A context manager is enabled by the with statement, and the API involves two methods.
The __enter__() method is run when execution flow enters the code block inside the with.
It returns an object to be used within the context.
When execution flow leaves the with block, the __exit__() method of the context manager
is called to clean up any resources being used.
'''
class Context(object):

    def __init__(self):
        print '__init__()'

    def __enter__(self):
        print '__enter__()'
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print '__exit__()'
        
with Context():
    print 'Doing work in the context'


# EXAMPLE 6: Return a context manager that closes thing upon completion of the block:
# ==============================================================================
from contextlib import contextmanager

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

# And lets you write code like this:
from contextlib import closing
import urllib

with closing(urllib.urlopen('http://www.python.org')) as page:
    for line in page:
        print line
# without needing to explicitly close page.
# Even if an error occurs, page.close() will be called when the with block is exited.