#!/usr/bin/python

'''
Difference between items() and iteritems() is:

items(): It takes more space and time initially, but accessing each element is
fast dict.items() returns a list of 2-tuples ([(key, value), (key, value), ...])

iteritems(): It takes less space and time initially, but a bit more time in
generating each element. dict.iteritems() is a generator that yields 2-tuples.

dict.items(): Return a copy of the dictionary's list of (key, value) pairs.
dict.iteritems(): Return an iterator over the dictionary's (key, value) pairs.
'''

# EXAMPLE 1: Using d.items():
# ==============================================================================
d = {1:'one', 2:'two', 3:'three'}
print 'Example 1: d.items()'
for k, v in d.items():
   if d[k] is v:
       print '\tthey are the same object'
   else:
       print '\tthey are different'


# EXAMPLE 2: Using d.iteritems():
# ==============================================================================
print
print 'Example 2: d.iteritems()'
for k, v in d.iteritems():
   if d[k] is v:
       print '\tthey are the same object'
   else:
       print '\tthey are different'