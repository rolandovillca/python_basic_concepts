#file module1.py

# When the Python interpreter reads a source file, it executes all of the code found in it.
# Before executing the code, it will define a few special variables.
# For example, if the python interpreter is running that module (the source file)
# as the main program, it sets the special __name__ variable to have a value "__main__".
# If this file is being imported from another module, __name__ will be set to the module's name.

def func():
    print 'func() in %s' % (__name__)

print 'Top-level in %s' % (__name__)

if __name__ == '__main__':
    print 'module1.py is being run directly'
else:
    print 'module1.py is being imported into another module'
