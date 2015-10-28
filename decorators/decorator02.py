def print_call(fn):
    def fn_wrap(*args, **kwargs):
        print("Calling %s with arguments: \n\targs: %s\n\tkwargs:%s" % (fn.__name__, args, kwargs))
        retval = fn(*args, **kwargs)
        print("%s returning '%s'" % (fn.func_name, retval))
        return retval
    fn_wrap.func_name = fn.func_name
    return fn_wrap

def greeter(greeting, what='world'):
    return "%s %s!" % (greeting, what)

greeter = print_call(greeter)

# Calling method 1
greeter("Hi")

# Calling method 2
greeter("Hi", what="Python")

# Calling method 3
param = {'what': "Learning"}
greeter("Hi", **param)
