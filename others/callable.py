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