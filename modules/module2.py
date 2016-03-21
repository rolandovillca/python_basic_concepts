# file module2.py

import module1

print 'Top level into module2.py'
module1.func()

# Run the main program:
if __name__ == '__main__':
    print 'module2.py is being run directly'
else:
    print 'module2.py is being imported into another module.'