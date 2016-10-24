# EXAMPLE 1:
# ==============================================================================
module1 = __import__('pkg1.module1', globals(), locals(), ['Person'], -1) 
person = module1.Person('Rolando', 'Villca')

def patch():
    return 'Patching your method '

print dir(module1)
print

print module1.get_country()
module1.set_country(country='USA')
print
print module1.get_country()
print

print person.get_name()
print
person.get_name = patch
print 
print person.get_name()
print


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