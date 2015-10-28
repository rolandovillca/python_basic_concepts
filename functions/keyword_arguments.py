#!/usr/bin/python

# EXAMPLE 1:
# Function definition is here
def printme(str):
    "This prints a passed string into this function"
    print str
    return

# Now you can call printname function
if __name__ == '__main__':
    printme(str = "Hi Rolando, sending from a function with keyword parameters")

# EXAMPLE 2:
# Function definition here
def printinfo(name, age):
    "This prints a passed info this function"
    print 'Name: %s' % (name)
    print 'Age: %s' % (age)

    #print 'Name: ', name
    #print 'Age: ', age
    return

# Now we can call printinfo
printinfo(age = 50, name = "Rolando")