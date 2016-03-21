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