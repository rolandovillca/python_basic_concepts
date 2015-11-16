# Difference between items() and iteritems() is:

# 1. items(): It takes more space and time initially, but accessing each element is fast
#   dict.items() returns a list of 2-tuples ([(key, value), (key, value), ...])

# 2. iteritems(): It takes less space and time initially, but a bit more time in generating each element.
#   dict.iteritems() is a generator that yields 2-tuples

# dict.items(): Return a copy of the dictionary’s list of (key, value) pairs.
# dict.iteritems(): Return an iterator over the dictionary’s (key, value) pairs.

#!/usr/bin/python

d={1:'one',2:'two',3:'three'}
print 'd.items():'
for k,v in d.items():
   if d[k] is v: print '\tthey are the same object'
   else: print '\tthey are different'

print 'd.iteritems():'
for k,v in d.iteritems():
   if d[k] is v: print '\tthey are the same object'
   else: print '\tthey are different'
