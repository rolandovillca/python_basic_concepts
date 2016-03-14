# The map(aFunction, aSequence) function applies a passed-in function to each item in an iterable object
# and returns a list containing all the function call results.

# EXAMPLE 1:
# ==============================================================================
items = [1, 2, 3, 4, 5]
squared = []

for x in items:
	squared.append(x * x)

print squared
print

# EXAMPLE 2:
# ==============================================================================
def sqr(x):  return x ** 2
print list(map(sqr, items))


# EXAMPLE 3:
# ==============================================================================
print list(map((lambda x: x ** 2), items))
print


# EXAMPLE 4:
# ==============================================================================
def square(x):
	return x**2

def cube(x):
	return x**3

funcs = [square, cube]

for r in range(5):
	value = map(lambda x: x(r), funcs)
	print value
print


# EXAMPLE 5:
# ==============================================================================
def mymap(aFunc, aSeq):
	result = []
	for x in aSeq: result.append(aFunc(x))
	return result

print list(map(sqr, [1,2,3]))
print mymap(sqr, [1,2,3])
print


# EXAMPLE 6:
# ==============================================================================
result = list(map(ord,'Dostoyevsky'))
print result


# EXAMPLE 7:
# ==============================================================================
# Function that calculates fahrenheit formula
def fahrenheit(temperature):
    return ((float(9)/5) * temperature + 32)

# Function that calculates celcius formula
def celcius(temperature):
    return (float(5)/9) * (temperature - 32)

# The array with values as random temperatures
temperature = (36.5, 37, 37.5,39)

# Apply map function using fahrenheit function
F = map(fahrenheit, temperature)

# Apply map function using fahrenheit function
C = map(celcius, F)

# Display results
print F
print C
