# my_name = __import__('mod1.wrapper_file')
# print my_name

# _temp = __import__('mod1.wrapper_file', globals(), locals(), ['MyClass'], -1) 
# aaa = _temp.MyClass()
# print aaa.get()

_temp_module = __import__('pkg1.module1', globals(), locals(), ['MyClass'], -1) 
my_class = _temp_module.MyClass()
# my_class = getattr(_temp_module, "MyClass")

print _temp_module.get_name()
_temp_module.set_name(your_name='Carlos')
print _temp_module.get_name()
print
print dir(_temp_module)
print
print my_class.get()
print
print
print

class Person(object):
    def getname(self):
        return 'Rolando'

person = Person()
person1 = Person()

import gc
for obj in gc.get_objects():
    if isinstance(obj, Person):
        print obj.__class__.__name__

print person.getname()
print person1.getname()

# The default is -1 which indicates both absolute and relative imports will be attempted.
# 0 means only perform absolute imports.