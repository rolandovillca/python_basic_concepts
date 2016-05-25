'''
Inner Functions - What Are They Good For?

1. Encapsulation
You use inner functions to protect them from anything happening outside of the
function, meaning that they are hidden from the global scope.

2. Closures and Factory Functions
Now we come to the most important reason to use inner functions.
All of the inner function examples we’ve seen so far have been ordinary
functions that merely happened to be nested inside another function.
In other words, we could have defined these functions in another way
(as discussed); there is no specific reason for why they should be nested.

But when it comes to closure, that is not the case: You must utilize nested
functions.

What’s a closure?
A closure simply causes the inner function to remember the state of its
environment when called. Beginners often think that a closure is the inner
function, when it’s really caused by the inner function. The closure "closes"
the local variable on the stack and this stays around after the the stack
creation has finished executing.
'''


# EXAMPLE 1:
# ==============================================================================
# This is a simplified function to check if a certain user has the correct
# permissions to access a certain page. You could easily modify this to grab the
# user in session to check if they have the correct credentials to access a
# certain route. Instead of checking if the user is just equal to "Admin",
# you could query the database to check the permission then return the correct
# view depending on whether the credentials are correct or not.

def has_permission(page):
    def inner(username):
        if username == 'admin':
            return '{} have access to {}'.format(username, page)
        else:
            return '{} does not have access to {}'.format(username, page)
    return inner

current_user = has_permission('Admin Area')
print
print current_user('admin')

random_user = has_permission('Admin Area')
print random_user('not admin')
print


# EXAMPLE 2:
# ==============================================================================
# The ‘generate_power()’ function is a factory function – which simply means
# that it creates a new function each time it is called and then returns the
# newly created function.

# What does this inner function do? It takes a single argument, power,
# and returns number**power.

# Where does the inner function get the value of number from? This is where the
# closure comes into play: nth_power() gets the value of power from the outer
# function, the factory function.

def generate_power(number):
    def nth_power(power):
        return number ** power
    return nth_power


# EXAMPLE 3:
# ==============================================================================
# You use inner functions to protect them from anything happening outside of the
# function, meaning that they are hidden from the global scope.
# 
def make_adder(num1):
    def add(num2):
        return num1 + num2
    return add

sum_result = make_adder(3)
print sum_result(7)
print


# EXAMPLE 4:
# ==============================================================================
def print_msg(msg):
    '''This is the outer enclosing function'''

    def printer():
        '''This is the nested function'''
        print msg

    return printer

my_print_msg = print_msg('Hello')
my_print_msg()
print


# EXAMPLE 5:
# ==============================================================================
import sys

def Foo():
    def err(s):
        sys.stderr.write('ERROR: ')
        sys.stderr.write(s)
        sys.stderr.write('\n')
    err('I regret to inform you')
    err('that a shameful thing has happened.')
    err('Thus, I must issue this desultory message')
    err('across numerous lines.')
Foo()


# EXAMPLE 6:
# ==============================================================================
class SomeClass(object):
    def __init__(self):
        pass

    def _add(self, x, y):
        return x + y

    def doOp(self, x, y):
        return self._add(x, y)

print
print 'Result =', SomeClass().doOp(1, 2)
