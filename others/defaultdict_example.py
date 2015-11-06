from collections import defaultdict

>>> s = 'mississippi'
>>> d = defaultdict(int)
>>> for k in s:
...     d[k] += 1
...
>>> d.items()
[('i', 4), ('p', 2), ('s', 4), ('m', 1)]
and

>>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
>>> d = defaultdict(list)
>>> for k, v in s:
...     d[k].append(v)
...
>>> d.items()
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]


# defaultdict means that if an key is not found in the dictionary that instead of a KeyError being thrown a new value is created.
# The type of this new pair is given by the argument of defaultdict.

somedict = {}
print(somedict[3]) # KeyError

someddict = defaultdict(int)
print(someddict[3]) # print int(), thus 0

# The standard dictionary includes the method setdefault() for retrieving a value and establishing a default if the value does not exist.
# By contrast, defaultdict lets the caller specify the default(value to be returned) up front when the container is initialized.

callable as its first argument(mandatory)
>>> d_int = defaultdict(int)
>>> d_list = defaultdict(list)
>>> def foo():
...     return 'default value'
...
>>> d_foo = defaultdict(foo)
>>> d_int
defaultdict(<type 'int'>, {})
>>> d_list
defaultdict(<type 'list'>, {})
>>> d_foo
defaultdict(<function foo at 0x7f34a0a69578>, {})


**kwargs as its second argument(optional)
>>> d_int = defaultdict(int, a=10, b=12, c=13)
>>> d_int
defaultdict(<type 'int'>, {'a': 10, 'c': 13, 'b': 12})
or

>>> kwargs = {'a':10,'b':12,'c':13}
>>> d_int = defaultdict(int, **kwargs)
>>> d_int
defaultdict(<type 'int'>, {'a': 10, 'c': 13, 'b': 12})

How does it works

As is a child class of standard dictionary, it can perform all the same functions.

But in case of passing an unknown key it returns the default value instead of error. For ex:

>>> d_int['a']
10
>>> d_int['d']
0
>>> d_int
defaultdict(<type 'int'>, {'a': 10, 'c': 13, 'b': 12, 'd': 0})
In case you want to change default value overwrite default_factory:

>>> d_int.default_factory = lambda: 1
>>> d_int['e']
1
>>> d_int
defaultdict(<function <lambda> at 0x7f34a0a91578>, {'a': 10, 'c': 13, 'b': 12, 'e': 1, 'd': 0})


or

>>> def foo():
...     return 2
>>> d_int.default_factory = foo
>>> d_int['f']
2
>>> d_int
defaultdict(<function foo at 0x7f34a0a0a140>, {'a': 10, 'c': 13, 'b': 12, 'e': 1, 'd': 0, 'f': 2})


#**********************************************************************************************

>>> from collections import defaultdict
>>> ice_cream = defaultdict(lambda: 'Vanilla')
>>>
>>> ice_cream = defaultdict(lambda: 'Vanilla')
>>> ice_cream['Sarah'] = 'Chunky Monkey'
>>> ice_cream['Abdul'] = 'Butter Pecan'
>>> print ice_cream['Sarah']
Chunky Monkey
>>> print ice_cream['Joe']
Vanilla
>>>
