'''
Reraise:

An exception continues bubbling to the calling methods unless handled.
In an except clause, we can use a "raise" statement with no argument.
This reraises the exception.

Here:
The "raise" statement the exception not to be captured.
The print-statement is executed before the program terminates.
'''

try:
    # This causes an exception.
    f = open("abc")
except:
    print("Except hit")
    # Raise the exception again.
    raise