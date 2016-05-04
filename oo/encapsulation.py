'''
In an object oriented python program, you can restrict access to methods and
variables. This can prevent the data from being modified by accident and is
known as encapsulation.
'''

# EXAMPLE 1: Private methods:
# ==============================================================================
# The private method  __updateSoftware() can only be called within the class itself.
# It can never be called from outside the class.
class Car:
    def __init__(self):
        self.__update_software()

    def drive(self):
        print 'driving'

    def __update_software(self):
        print 'Updating sofware'

redcar = Car()
redcar.drive()
#redcar.__updateSoftware()  not accesible from object.
print


# EXAMPLE 2: Private variables:
# ==============================================================================
# Variables can be private which can be useful on many occasions.
# Objects can hold crucial data for your application and you do not want that
# data to be changeable from anywhere in the code.
class Car:
    __max_speed = 0
    __name = ''

    def __init__(self):
        self.__max_speed = 200
        self.__name = 'Supercar'

    def drive(self):
        print 'Driving. max_speed {}'.format(self.__max_speed)

redcar2 = Car()
redcar2.drive()
redcar2.__max_speed = 10 # will not change variable because its private
redcar2.drive()