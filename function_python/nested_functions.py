'''
This is a simplified function to check if a certain user has the correct
permissions to access a certain page. You could easily modify this to grab the
user in session to check if they have the correct credentials to access a
certain route. Instead of checking if the user is just equal to "Admin",
you could query the database to check the permission then return the correct
view depending on whether the credentials are correct or not.
'''

# EXAMPLE 1:
# ==============================================================================
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
def make_adder(num1):
    def add(num2):
        return num1 + num2
    return add

sum_result = make_adder(3)
print sum_result(7)
print


# EXAMPLE 3:
# ==============================================================================
def print_msg(msg):
    '''This is the outer enclosing function'''

    def printer():
        '''This is the nested function'''
        print msg

    return printer

my_print_msg = print_msg('Hello')
my_print_msg()