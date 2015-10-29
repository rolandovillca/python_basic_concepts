# Python supports the creation of anonymous functions at runtime, using a construct called "lambda".
# This is not exactly the same as lambda in functional programming languages,
# but it is a very powerful concept that's well integrated into Python
# and is often used in conjunction with typical functional concepts like filter(), map() and reduce().

# A normal function:
def func (x):
    return x ** 2

# A lambda function:
result = lambda x: x ** 2

# Display both results:
print func(8)
print result(8)

# We can this example like this:
# $ python basic_example.py
