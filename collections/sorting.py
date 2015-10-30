# Create a simple class Person
class Person(object):
    def __init__(self, age):
        self.age = age

# Print the three created persons
def print_persons(persons):
    for person in persons:
        print ' ---> %s' % (person.age)
    print ''

# Create three Person objects and set the age property
persons1 = [Person(age) for age in range(3) ]
print_persons(persons1)

# Create three Person objects and set age property
# To use different built-in python functions
persons2 = [Person(age) for age in map(lambda age: age * 10, range(3))]
print_persons(persons2)

# Using another built-in python functions
from collections import defaultdict
persons_by_age = defaultdict(list)

for person2 in persons2:
    persons_by_age[person2.age].append(person2)

# Print the three created persons
for person in persons_by_age:
    print person
