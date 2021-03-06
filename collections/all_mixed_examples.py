# EXAMPLE 1: Simple comprehencion:
# ==============================================================================
x = [2, 3, 4, 5, 6]
y = [v * 5 for v in x]


# EXAMPLE 2: Combination of lambda and map():
# ==============================================================================
y = map(lambda v : v * 5, x)
print y

print [v * 5 for v in x]
print map(lambda for v: v * 5, in x)
print map(lambda v : v * 5, x)
print


# EXAMPLE 3: List comprehension of the same process:
# ==============================================================================
y = [v * 5 for v in x if v % 2]


# EXAMPLE 4: Combination of filter + map + lambda:
# ==============================================================================
# In order to produce the same results as our loop and list comprehension.
# Formula: filter(function, iterable) --> [item for item in iterable if function(item)]
y = map(lambda v : v * 5, filter(lambda u : u % 2, x))

[v * 5 for v in x if v % 2] # List comprehension
map(lambda for v: v * 5, for filter(lambda for v: if v % 2, in x)) # "pseudo" lambda and list comprehension
map(lambda v : v * 5, filter(lambda u : u % 2, x)) # Lambda, just a 'rearrangement' of what we had before


# EXAMPLE 5: Nested comprehencions:
# ==============================================================================
x = [2, 3, 4]
y = [4, 5]
z = [v + w for v in x for w in y]


# EXAMPLE 6: Combination map + lambdas:
# ==============================================================================
x = [2, 3, 4]
y = [4, 5]
t = map(lambda v : map(lambda w : v + w, y), x)
assert t == [[6, 7], [7, 8], [8, 9]]
z = sum(t, [])


# EXAMPLE 7: Playing with two maps:
# ==============================================================================
# Lets take a closer look and see how our list comprehension was "rearranged" to create this lambda.
[v + w for v in x for w in y] # List comprehension
map(lambda for v: in map(lambda for w: v + w, in y), in x) # "pseudo" lambda
map(lambda v : map(lambda w : v + w, y), x) # Lambda