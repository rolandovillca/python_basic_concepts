# The comprehentions really make it easy to add those loops and conditionals on the existing comprehentions.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# EXAMPLE 1: Print Lists in a simple way:
my_list1 = [n for n in nums]
my_list2 = [n*n for n in nums]
print my_list1
print my_list2
print


# EXAMPLE 2: Print Lists using map + lambda:
my_list3 = map(lambda n: n*n, nums)
print my_list3
print

# EXAMPLE 3: Print Lists using comprehentions:
my_list4 = [n for n in nums if n%2 == 0]
print my_list4
print

# EXAMPLE 4: Print Lists using filter + lambda:
my_list5 = filter(lambda n: n%2 == 0, nums)
print my_list5
print


# EXAMPLE 5: Print strings lists using comprehentions:
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

my_list6 = [(letter, num) for letter in 'abcd' for num in range(4)]
print my_list6
print


# EXAMPLE 6: Print Disctionary using comprehentions:
print zip(names, heros) # Both lists should match size or length.

my_dict1 = {name: hero for name, hero in zip(names, heros)}
print my_dict1
print


# EXAMPLE 7: Print Disctionary using filters + comprehentions:
my_dict2 = {name: hero for (name, hero) in zip(names, heros) if name != 'Peter'}
print my_dict2
print


# EXAMPLE 8: Sets - similar to List, but it DOES NOT allow duplicated elements:
my_set = {n for n in nums}
print my_set
print


# EXAMPLE 9: Using generators expressions:
my_gen = (n*n for n in nums)

for i in my_gen:
    print i