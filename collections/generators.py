# EXAMPLE 1:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Give me each number in a list squared:
squares = [num*num for num in my_list]
print squares
print

# EXAMPLE 2:
# Fibonacci generator
def fib(num):
    a, b = 0, 1
    for i in range(0, num):
        yield '{}: {}'.format(i+1, a)
        a, b = b, a+b

for item in fib(10):
    print item