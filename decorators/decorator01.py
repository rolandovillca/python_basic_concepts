# EXAMPLE 1: A very simple function:
# ==============================================================================
def greeter():
    print 'Hello'

# An implementation of a repeat function:
def repeat(fn, times):
    for i in range(times):
        fn()

repeat(greeter, 3)
print


# EXAMPLE 2: Example of nested functions:
# ==============================================================================
# It hides utility functions in the scope of he function that uses them:
def print_integers(values):
    def is_integer(value):
        try:
            return value == int(value)
        except:
            return False
    for v in values:
        if is_integer(v):
            print v

print_integers([1, 2, 3, "4", "parrot", 3.14, 8, 9])
print


# EXAMPLE 3: Adding a trace output to a function:
# ==============================================================================
def print_call(fn):
    def fn_wrap(*args, **kwargs):
        print 'Calling {}'.format(fn.func_name)
        return fn(args, kwargs)
    return fn_wrap

my_print = print_call(greeter)
repeat(greeter, 2)
print
print greeter.func_name
print greeter.__name__
