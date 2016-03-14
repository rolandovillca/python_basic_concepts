# EXAMPLE 1:
# ==============================================================================
print myreduce((lambda x, y: x * y), [1, 2, 3, 4])
print myreduce((lambda x, y: x / y), [1, 2, 3, 4])


# EXAMPLE 2:
# ==============================================================================
reduce(lambda x, y: x + y, [47, 11, 42, 13])


# EXAMPLE 3:
# ==============================================================================
f = lambda a, b: a if (a > b) else b
reduce(f, [47, 11, 42, 102, 13])


# EXAMPLE 4:
# ==============================================================================
reduce(lambda x, y: x + y, range(1, 101))


# EXAMPLE 5:
# ==============================================================================
import functools
L = ['Testing ', 'shows ', 'the ', 'presence', ', ','not ', 'the ', 'absence ', 'of ', 'bugs']
print functools.reduce((lambda x,y: x + y), L)
print


# EXAMPLE 6: Simulating 'reduce' with join.
# ==============================================================================
print ''.join(L)
print


# EXAMPLE 7: Simulating 'reduce' with operator.
# ==============================================================================
import functools, operator
print functools.reduce(operator.add, L)
print
