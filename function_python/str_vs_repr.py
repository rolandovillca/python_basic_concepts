'''
__repr__

Called by the repr() built-in function and by string conversions (reverse quotes)
to compute the "official" string representation of an object. If at all possible,
this should look like a valid Python expression that could be used to recreate
an object with the same value (given an appropriate environment).

__str__

Called by the str() built-in function and by the print statement to compute the
"informal" string representation of an object.

Notes:

The __str__ is intended to be as human-readable as possible,
whereas the __repr__ should aim to be something that could be used to recreate the object,
although it often won't be exactly how it was created, as in this case.

It's also not unusual for both __str__ and __repr__ to return the same value
(certainly for built-in types).
'''


# EXAMPLE 1: str vs repr
# ==============================================================================
# The goal of __repr__ is to be unambiguous
# The goal of __str__ is to be readable

import datetime
import pytz

a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
b = str(b)
print

print 'str(a): {}'.format(str(a))
print 'str(b): {}'.format(str(b))
print

print 'repr(a): {}'.format(repr(a))
print 'repr(b): {}'.format(repr(b))
print