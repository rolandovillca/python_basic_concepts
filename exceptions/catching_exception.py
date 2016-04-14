# import module sys to get the type of exception.

import sys

while True:
    try:
        value = int(input('Enter an integer:'))
        result = 1/value
        break
    except:
        print 'Oops!', sys.exc_info()[0], 'occured.'
        print

print 'The reciprocal of', value, 'is', result