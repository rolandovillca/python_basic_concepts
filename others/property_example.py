'''
Thanks to Python scoping rules, static attributes can be accessed from instance
attributes and vice-versa, which is something that other languages might give
you some trouble with. What this allows you to do is use local variables
'''

# EXAMPLE 1: Encoding and Decoding Data in Strings:
# ==============================================================================

class PropertyClass(object):
    _prop = 5

    @property
    def prop(self):
        # Also acceptable is return self.__class__._prop,
        # but watch out on inheritance
        return PropertyClass._prop
    
    @prop.setter
    def prop(self, val):
        PropertyClass._prop = val

a = PropertyClass()
a.prop