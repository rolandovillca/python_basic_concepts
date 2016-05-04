'''
In an object oriented python program, you can restrict access to methods and
variables. This can prevent the data from being modified by accident and is
known as encapsulation.
'''

# EXAMPLE 1: Private methods:
# ==============================================================================
# The private method  __updateSoftware() can only be called within the class itself.
# It can never be called from outside the class.
class Car1:
    def __init__(self):
        self.__update_software()

    def drive(self):
        print 'driving Car1'

    def __update_software(self):
        print 'Updating sofware'

redcar1 = Car1()
redcar1.drive()
#redcar.__updateSoftware()  not accesible from object.
print


# EXAMPLE 2: Private variables:
# ==============================================================================
# Variables can be private which can be useful on many occasions.
# Objects can hold crucial data for your application and you do not want that
# data to be changeable from anywhere in the code.

class Car2:
    __max_speed = 0
    __name = ''

    def __init__(self):
        self.__max_speed = 200
        self.__name = 'Supercar2'

    def drive(self):
        print 'Driving Car2. max_speed {}'.format(self.__max_speed)

redcar2 = Car2()
redcar2.drive()
redcar2.__max_speed = 10 # will not change variable because its private
redcar2.drive()
print


# EXAMPLE 3: Private variables with setters:
# ==============================================================================
# If you want to change the value of a private variable, a setter method is used.
# This is simply a method that sets the value of a private variable.

class Car3:
    __max_speed = 0
    __name = ''

    def __init__(self):
        self.__max_speed = 200
        self.__name = 'Supercar3'

    def drive(self):
        print 'Driving Car3. max_speed {}'.format(self.__max_speed)

    def set_max_speed(self, speed):
        self.__max_speed = speed

redcar3 = Car3()
redcar3.drive()
redcar3.set_max_speed(800)
redcar3.drive()