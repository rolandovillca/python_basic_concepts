# EXAMPLE 1:
# ==============================================================================
module1 = __import__('pkg1.module1', globals(), locals(), ['Person'], -1) 
person = module1.Person('User01', 'UserLastname')

def patch_method(*args, **kwargs):
    print args
    print kwargs
    print 'Patching your method'

# Save the patch_obj method temoorarely.
patch_obj = getattr(person, 'where_live')
print 'My new object:', patch_obj

# Patching the 'method' we want it.
person.where_live = patch_method
print person.where_live('address111')
print

# Unpatching the object.
# person.where_live = patch_obj
# print person.where_live('address222')

# print person.get_name()
# print
# person.get_name = patch_method
# print 
# print person.get_name()
# print


# EXAMPLE 2:
# ==============================================================================
# def patch2():
#     return 'Patched result...'

# module1 = __import__('pkg1.module1', globals(), locals(), ['Person'], -1)
# person = getattr(module1, 'Person')
# print person.get_name()
# print

# setattr(person, "get_name", patch2)
# print person.get_name()
# print