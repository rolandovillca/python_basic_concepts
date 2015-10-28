# EXAMPLE 1: FILTER
print list(range(-5, 5))
print list(filter((lambda x: x<0), range(-5,5)))

# EXAMPLE 2: FILTER
result = []
for x in range(-5, 5):
	if x < 0:
		result.append(x)
print result


# EXAMPLE 3: FILTER
from functools import reduce

print reduce((lambda x, y: x*y), [1,2,3,4])
print reduce((lambda x, y: x/y), [1,2,3,4])

L = [1,2,3,4]
result = L[0]
for x in L[1:]:
	result = result * x
print result

# EXAMPLE 4: FILTER
def myreduce(fnc, seq):
	tally = seq[0]
	for next in seq[1:]:
		tally = fnc(tally, next)
	return tally
	
print myreduce((lambda x,y: x*y), [1,2,3,4])
print myreduce((lambda x,y: x/y), [1,2,3,4])

# EXAMPLE 5: REDUCE
import functools
L = ['Testing ', 'shows ', 'the ', 'presence', ', ','not ', 'the ', 'absence ', 'of ', 'bugs']
print functools.reduce((lambda x,y: x + y), L)

# EXAMPLE 5: SIMULATING REDUCE WITH JOIN:
print ''.join(L)
print

# EXAMPLE 6: SIMULATING REDUCE WITH OPERATOR:
import functools, operator
print functools.reduce(operator.add, L)
print
