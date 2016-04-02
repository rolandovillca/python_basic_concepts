'''
The inspect module provides several useful functions to help get information
about live objects such as modules, classes, methods, functions, tracebacks,
frame objects, and code objects. For example, it can help you examine
the contents of a class, retrieve the source code of a method,
extract and format the argument list for a function,
or get all the information you need to display a detailed traceback.

There are four main kinds of services provided by this module: type checking,
getting source code, inspecting classes and functions,
and examining the interpreter stack.
'''

>>> from inspect import getcallargs
>>> def f(a, b=1, *pos, **named):
...     pass
>>> getcallargs(f, 1, 2, 3)
{'a': 1, 'named': {}, 'b': 2, 'pos': (3,)}
>>> getcallargs(f, a=2, x=4)
{'a': 2, 'named': {'x': 4}, 'b': 1, 'pos': ()}
>>> getcallargs(f)
Traceback (most recent call last):
...
TypeError: f() takes at least 1 argument (0 given)

The interpreter stack

When the following functions return “frame records,” each record is a tuple of six items: the frame object, the filename, the line number of the current line, the function name, a list of lines of context from the source code, and the index of the current line within that list.

Note Keeping references to frame objects, as found in the first element of the frame records these functions return, can cause your program to create reference cycles. Once a reference cycle has been created, the lifespan of all objects which can be accessed from the objects which form the cycle can become much longer even if Python’s optional cycle detector is enabled. If such cycles must be created, it is important to ensure they are explicitly broken to avoid the delayed destruction of objects and increased memory consumption which occurs.
Though the cycle detector will catch these, destruction of the frames (and local variables) can be made deterministic by removing the cycle in a finally clause. This is also important if the cycle detector was disabled when Python was compiled or using gc.disable(). For example:
def handle_stackframe_without_leak():
    frame = inspect.currentframe()
    try:
        # do something with the frame
    finally:
        del frame