# The map(aFunction, aSequence) function applies a passed-in function to each item in an iterable object
# and returns a list containing all the function call results.

# EXAMPLE 1:
items = [1, 2, 3, 4, 5]
squared = []

for x in items:
	squared.append(x * x)

print squared
print

# EXAMPLE 2:
def sqr(x):  return x ** 2
print list(map(sqr, items))

# EXAMPLE 3:
print list(map((lambda x: x ** 2), items))
print

# EXAMPLE 4:
def square(x):
	return x**2

def cube(x):
	return x**3
	
funcs = [square, cube]

for r in range(5):
	value = map(lambda x: x(r), funcs)
	print value
print

# EXAMPLE 4:
def mymap(aFunc, aSeq):
	result = []
	for x in aSeq: result.append(aFunc(x))
	return result

print list(map(sqr, [1,2,3]))
print mymap(sqr, [1,2,3])
print

# EXAMPLE 5:
result = list(map(ord,'Dostoyevsky'))
print result
