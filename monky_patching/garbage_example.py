module1 = __import__('pkg1.module1', globals(), locals(), ['Person'], -1) 
person = module1.Person('Rolando', 'Villca')

def patch():
    return 'Patched result'

import gc
for obj in gc.get_objects():
    if isinstance(obj, module1.Person):
        print 'Class Name: ', obj.__class__.__name__

print person.get_name()
person.get_name = patch
print person.get_name()

# The default is -1 which indicates both absolute and relative imports will be attempted.
# 0 means only perform absolute imports.