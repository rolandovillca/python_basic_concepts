# Create a base class
class MyClass(object):
    def my_method(self):
        print 'Into my method!'

# Create a method
def another_method(self):
    print "Into another method!"

# Create hello world method
def hello_world(self):
    print 'Hello World method'

# Adding methods and properties to an existing class
MyClass.another_method = another_method
MyClass.hello = hello_world
MyClass.count = 10

# Create instance object
my_class = MyClass()

# Access to all methods and properties
my_class.my_method()
my_class.another_method()
my_class.hello()
print my_class.count
