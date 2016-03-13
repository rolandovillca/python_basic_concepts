# NOTES:
# Generators dont hold enterily result in memory.
# Generators yield one result at the time.
# Waiting for us to ask for the next result.
# JFYI Comprehentions are better in performance, because dont hold in memory.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# EXAMPLE 1: Square generator:
def square_numbers(nums):
    for i in nums:
        yield (i*i)

for num in nums:
    print num


# EXAMPLE 2: Fibonacci generator
def fib(num):
    a, b = 0, 1
    for i in range(0, num):
        yield '{}: {}'.format(i+1, a)
        a, b = b, a+b

for item in fib(10):
    print item


# EXAMPLE 3: Using existing generator thru comprehentions:
squares1 = [num*num for num in my_list]
print squares1
print


# EXAMPLE 4: Using existing generator thru comprehentions:
squares2 = (num*num for num in my_list)
print list(squares2)
print