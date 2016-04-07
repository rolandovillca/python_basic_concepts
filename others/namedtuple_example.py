'''
*namedtuple* instances are just as memory efficient as regular tuples because
they do not have per-instance dictionaries. Each kind of namedtuple is
represented by its own class, created by using the namedtuple() factory function.

The arguments are the name of the new class and a string containing the names of the elements.
'''

# EXAMPLE 1:
# ==============================================================================
from collections import namedtuple

Person = namedtuple('Person', 'name age gender')
print 'Type of Person:', type(Person)
print

bob = Person(name='Bob', age=30, gender='male')
print 'Bob:', bob
print

jane = Person(name='Jane', age=29, gender='female')
print 'Jane.name:', jane.name
print

print 'Fields by index:'
for person in [ bob, jane ]:
    print '{} is a {} year old {}'.format(person[0], person[1], person[2])