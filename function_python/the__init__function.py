'''
What does self do? what is it meant to be? and is it mandatory?
What does the __init__ method do? why is it necessary?
'''


# EXAMPLE 1:
# ==============================================================================
# here's a simple example I used to understand the difference between a variable
# declared inside a class, and a variable declared inside an __init__ function:

# __init__ does act like a constructor. You'll need to pass "self" to any class
# functions as the first argument if you want them to behave as non-static methods.
# "self" are instance variables for your class.

class MyClass(object):
     i = 123
     def __init__(self):
         self.i = 345

a = MyClass()
print a.i
# 345

print MyClass.i
# 123


# EXAMPLE 2:
# ==============================================================================
class A(object):
    def __init__(self):
        self.x = 'Hello'

    def method_a(self, foo):
        print self.x + ' ' + foo

'''
The self variable represents the instance of the object itself.

Most object-oriented languages pass this as a hidden parameter to the methods
defined on an object; Python does not. You have to declare it explicitly.

When you create an instance of the A class and call its methods, it will be
passed automatically, as in ...
'''

a = A()               # We do not pass any argument to the __init__ method
a.method_a('Sailor!') # We only pass a single argument

'''
The __init__ method is roughly what represents a constructor in Python.

When you call A() Python creates an object for you, and passes it as the first
parameter to the __init__ method.

Any additional parameters (e.g., A(24, 'Hello')) will also get passed as
arguments--in this case causing an exception to be raised, since the constructor
isn't expecting them.
'''