# Create a simple class Person
class Person(object):
    def __init__(self, age):
        self.age = age

# Create three Person objects and set the age property
persons = [Person(age) for age in range(3) ]

# Print the three created persons
for person in persons:
    print person.age

# Create three Person objects and set age property
# To use different built-in python functions
persons = [Person(age) for age in map(lambda age: age * 10, range(3))]

# Print the three created persons
for person in persons:
    print person.age
