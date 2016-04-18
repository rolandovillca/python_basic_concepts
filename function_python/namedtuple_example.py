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

bob = Person(name='Bob', age=30, gender='male')
print 'Bob:', bob

jane = Person(name='Jane', age=29, gender='female')
print 'Jane.name:', jane.name

print 'Fields by index:'
for person in [ bob, jane ]:
    print '{} is a {} year old {}'.format(person[0], person[1], person[2])


# EXAMPLE 2:
# ==============================================================================
# Here we create an Employee namedtuple with three fields.
# We pass a list to collections.namedtuple to specify field names id, title and salary.

# Specify the Employee namedtuple.
Employee = namedtuple('Employee', ['id', 'title', 'salary'])

# Create Employee instance.
employee = Employee(1, 'engineer', 10000)

# Display Employee.
print
print employee
print 'Title is: ', employee.title
print


# EXAMPLE 3:
# ==============================================================================
import collections

# A namedtuple type.
Style = collections.namedtuple('Style', ['color', 'size', 'width'])

# A list containing three values.
values = ['red', 10, 15]

# Make a namedtuple from the list.
tuple = Style._make(values)
print tuple
print