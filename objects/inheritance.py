# Define a parent class:
class Parent:
    parent_attr = 100

    # Create constructor of class
    def __init__(self):
        print 'Calling patent conrtuctor'

    # Create a method of class
    def parent_method(self):
        print 'Calling parent method'

    # Create another method of class
    def set_attr(self, attr):
        Parent.parent_attr = attr

    # Create another method of class
    def get_attr(self):
        print 'Parent attribute: ', Parent.parent_attr

    # Create another method of class
    def my_method(self):
        print 'This is my method into Parent'


# Define a child class:
class Child(Parent):
    # Create constructor of class
    def __init__(self):
        print 'Calling child contructor'

    # Create a method of class
    def child_method(self):
        print 'Callinf child method'

    # Override my_method in Parent class
    def my_method(self):
        print 'This is override method into Child'

# Create instance object of Child
c = Child()

# Some methods of child object
c.child_method()  # child calls its method
c.parent_method() # calls parent's method
c.set_attr(200)   # again call parent's method
c.get_attr()      # again call parent's method
c.my_method()     # override parent method
