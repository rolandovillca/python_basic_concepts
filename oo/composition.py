# Create the parent class
class Parent(object):
    # Create a method
    def override(self):
        print 'Parent override()'

    # Create a method
    def implicit(self):
        print 'Parent implicit()'

    # Create a method
    def altered(self):
        print 'Parent altered()'

# Create the child class
class Child(Parent):
    # Create constructor
    def __init__(self):
        self.parent = Parent()

    # Create a method
    def implicit(self):
        self.parent.implicit()

    # Create a method
    def override(self):
        print 'Child override()'

    # Create a method
    def altered(self):
        print 'Child, before Parent altered()'
        self.parent.altered()
        print 'Child, after Parent altered()'

# Create instance object
son = Child()

# Execute methods
son.implicit()
son.override()
son.altered()
