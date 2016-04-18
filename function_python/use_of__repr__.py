'''
__repr__ should return a printable representation of the object, most likely one
of the ways possible to create this object. See official documentation here.

__repr__ is more for developers while __str__ is for end users.


Python documentation:

repr(object): Return a string containing a printable representation of an object.
This is the same value yielded by conversions (reverse quotes).
It is sometimes useful to be able to access this operation as an ordinary function.
For many types, this function makes an attempt to return a string that would
yield an object with the same value when passed to eval(),
otherwise the representation is a string enclosed in angle brackets that
contains the name of the type of the object together with additional information
 often including the name and address of the object. A class can control what
 this function returns for its instances by defining a __repr__() method.
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point(x={}, y={})'.format(self.x, self.y)

point = Point(1, 2)
print point