'''
Raise:

We create exceptions in our code with raise.
This program uses the Exception type.
The mistake() method creates a custom string based on its parameter.
It then raises an exception.

Traceback:

The Python environment helpfully shows a traceback.
This contains the methods called. The mistake() call is shown.
'''

def mistake(name):
    # Raise an example with custom string.
    raise Exception(name + " caused exception")

# Call method.
mistake("Voorheesville")