# EXAMPLE 1:
# ==============================================================================
print list(range(-5, 5))
print list(filter((lambda x: x<0), range(-5,5)))


# EXAMPLE 2:
# ==============================================================================
result = []
for x in range(-5, 5):
	if x < 0:
		result.append(x)
print result

# EXAMPLE 3:
# ==============================================================================
from functools import reduce

print reduce((lambda x, y: x*y), [1,2,3,4])
print reduce((lambda x, y: x/y), [1,2,3,4])

L = [1,2,3,4]
result = L[0]
for x in L[1:]:
	result = result * x
print result


# EXAMPLE 4:
# ==============================================================================
def myreduce(fnc, seq):
	tally = seq[0]
	for next in seq[1:]:
		tally = fnc(tally, next)
	return tally

# EXAMPLE 4: Fibonacci array:
# ==============================================================================
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# Filter function to get even numbers
result1 = filter(lambda x: x % 2, fib)
print result1

# Filter function to get numbers equal to 2
result2 = filter(lambda x: x == 2, fib)
print reslt2
