# Python supports the creation of anonymous functions at runtime, using a construct called "lambda".
# This is not exactly the same as lambda in functional programming languages,
# but it is a very powerful concept that's well integrated into Python
# and is often used in conjunction with typical functional concepts like filter(), map() and reduce().

# EXAMPLE 1: A normal lambda function:
# ==============================================================================
def func (x):
    return x ** 2

# A lambda function:
result = lambda x: x ** 2

# Display both results:
print func(8)
print result(8)
print

# We can this example like this:
# $ python basic_example.py

# EXAMPLE 2:
# ==============================================================================
func = lambda x: x * x
print [func(x) for x in range(10)]
print


# EXAMPLE 3:
# ==============================================================================
# print [lambda x: x*x for item in range(10)] # Only prints function objects.
print [(lambda x: x*x)(x) for x in range(10)]
print

# Or much better:
print [ x*x for x in range(10)]
print


# EXAMPLE 4: Using "if" statements with lambda
# ==============================================================================
# Case 1:
func1 = lambda x: True if x % 2 == 0 else False
func1(100)
func1(77)

# Case 2:
func2 = lambda x: x == 2 and x or None
func2(5)
func2(2)

# Case 3:
def if_else(condition, a, b) :
    if condition :
        return a
    else:
        return b

func3 = lambda x : if_else(x>100, 'big number', 'little number')
func3(100)
func3(1000)

# Case 4:
func4 = lambda x: x > 100 and 'big' or 'small'
for i in (1, 10, 99, 100, 101, 110):
    print i, 'is', func4(i)