# A callable is anything that can be called.

# Example 1:
class Foo:
    def __call__(self):
        print 'called'

foo = Foo()
foo()

# Example 2:
class Cached:
    def __init__(self, function):
        self.function = function
        self.cache = {}

    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError as e:
            ret = self.cache[args] = self.function(*args)
            return ret

@Cached
def ack(x, y):
    return ack(x-1, ack(x, y-1)) if x*y else (x + y + 1)

print ack(2, 4)

# Example 3:
# A callable is an object allows you to use round parenthesis ( )
# and eventually pass some parameters, just like functions.

# Every time you define a function python creates a callable object.
# In example, you could define the function func in these ways (it's the same):

class A(object):
    def __call__(self, *args):
        print 'Hello'

func = A()

# or ... 
def func(*args):
    print 'Hello'

# You could use this method instead of methods like doit or run,
# I think it's just more clear to see obj() than obj.doit()