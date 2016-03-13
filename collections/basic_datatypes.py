# Lists:
my_list = [10, 20, 30, 40, 50]
for i in my_list:
    print i

# Tuples:
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in my_tuple:
    print i

# Dict:
my_dict = {'name': 'Bronx', 'age':'2', 'occupation', "Corey's Dog"}
for k, v in my_dict.iteritems():
    print 'My {} is {}'.format(k, v)

# Set
my_set = {10, 20, 30, 40, 50, 10, 20, 30, 40, 50}
for i in my_set:
    print i