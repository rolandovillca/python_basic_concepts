from collections import defaultdict

# EXAMPLE 1: using int as parameter:
# ==============================================================================
mississippi = 'mississippi'
d = defaultdict(int)
for key in mississippi:
    d[key] += 1
print 'Example 1:'
print d.items()
print

# EXAMPLE 2: Using list as parameter:
# ==============================================================================
colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)

for key, value in colors:
    d[key].append(value)

print 'Example 2:'
print d.items()
print

# EXAMPLE 3:
# ==============================================================================
# defaultdict means that if an key is not found in the dictionary
# that instead of a KeyError being thrown a new value is created.
#
# The type of this new pair is given by the argument of defaultdict.
someddict = defaultdict(int)
print(someddict[3]) # print int(), thus 0
print

# EXAMPLE 4:
# ==============================================================================
# The standard dictionary includes the method setdefault() for retrieving a
# value and establishing a default if the value does not exist.
#
# By contrast, the defaultdict lets the caller specify the
# default(value to be returned) up front when the container is initialized.
#
# Notes:
# Callable as its first argument(mandatory)
def func():
    return 'default value'

dic_int = defaultdict(int)
dic_list = defaultdict(list)
dic_foo = defaultdict(func)
print dic_int
print dic_list
print dic_foo
print

# EXAMPLE 5: Initialize dictionary with ints, second argument is optional:
# ==============================================================================
dic_int = defaultdict(int, a=10, b=12, c=13)
print dic_int
print

# EXAMPLE 6: Initialize dictionary with int, and **kwargs as its second argument(optional):
# ==============================================================================
kwargs = {'a':10,'b':12,'c':13}
dic_int = defaultdict(int, **kwargs)
print dic_int
print

# How does it works
# As is a child class of standard dictionary, it can perform all the same functions.
# But in case of passing an unknown key it returns the default value instead of error. For ex:
print dic_int['a']
print dic_int['d']
print dic_int
print

# In case you want to change default value overwrite default_factory:
dic_int.default_factory = lambda: 1
dic_int['e']
dic_int

# EXAMPLE 7:
# ==============================================================================
def foo():
    return 2

dic_int.default_factory = foo
dic_int['f']
dic_int

# EXAMPLE 8: Another example, lambda with default value as string:
# ==============================================================================
ice_cream = defaultdict(lambda: 'Vanilla')
ice_cream['Sarah'] = 'Chunky Monkey'
ice_cream['Abdul'] = 'Butter Pecan'
print ice_cream['Sarah']
print ice_cream['Joe']