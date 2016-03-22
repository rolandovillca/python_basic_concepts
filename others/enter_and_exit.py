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