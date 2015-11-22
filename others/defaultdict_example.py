from collections import defaultdict

# Example 1: using int as parameter.
mississippi = 'mississippi'
d = defaultdict(int)
for key in mississippi:
    d[key] += 1
d.items()

# Example 2: Using list as parameter.
colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for key, value in colors:
    d[key].append(value)
d.items()

# defaultdict means that if an key is not found in the dictionary that instead of a KeyError being thrown a new value is created.
# The type of this new pair is given by the argument of defaultdict.

# somedict = {}
# print(somedict[3]) # KeyError

someddict = defaultdict(int)
print(someddict[3]) # print int(), thus 0

# The standard dictionary includes the method setdefault() for retrieving a value and establishing a default if the value does not exist.
# By contrast, defaultdict lets the caller specify the default(value to be returned) up front when the container is initialized.

# Callable as its first argument(mandatory)
d_int = defaultdict(int)
d_list = defaultdict(list)
def foo():
    return 'default value'
d_foo = defaultdict(foo)
d_int
d_list
d_foo

# **kwargs as its second argument(optional)
d_int = defaultdict(int, a=10, b=12, c=13)
d_int

kwargs = {'a':10,'b':12,'c':13}
d_int = defaultdict(int, **kwargs)
d_int

# How does it works
# As is a child class of standard dictionary, it can perform all the same functions.
# But in case of passing an unknown key it returns the default value instead of error. For ex:

d_int['a']
d_int['d']
d_int

# In case you want to change default value overwrite default_factory:
d_int.default_factory = lambda: 1
d_int['e']
d_int

def foo():
    return 2
d_int.default_factory = foo
d_int['f']
d_int

from collections import defaultdict
ice_cream = defaultdict(lambda: 'Vanilla')
ice_cream = defaultdict(lambda: 'Vanilla')
ice_cream['Sarah'] = 'Chunky Monkey'
ice_cream['Abdul'] = 'Butter Pecan'
print ice_cream['Sarah']
print ice_cream['Joe']
