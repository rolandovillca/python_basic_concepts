'''
Else:

The else-statement can be used after a try-except block.
If no exception is thrown, the else-statements are executed.
The else must come after the excepts.

Tip:

In the else, you can perform an action required when no errors are encountered.

Here:

We show a while-True infinite loop. We accept input from the console,
and parse it with the int() built-in method.

Convert: Int, String

    Then:
    
    We attempt to divide by the number entered. If zero is entered,
    the except-block is reached. Otherwise, the else is reached.
'''

while True:
    # Read int from console.
    denominator = int(input())

    # Use int as denominator.
    try:
        i = 1 / denominator
    except:
        print("Error")
    else:
        print("OK")