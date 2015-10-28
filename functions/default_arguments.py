#!/usr/bin/python

# A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument.

#Fucntion definition is here
def printinfo(name, age = 35):
    "Tjhis prints a passed info into this function"
    print "Name: ", name
    print "Age: ", age

# Now you can call printinfo function
if __name__ == "__main__":
    printinfo(age=50, name='miki')
    printinfo(name='miki')