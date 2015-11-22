# Define global functon.
def hello():
    print 'Global hello'

# Create a class.
class A:
    # Define local method.
    def hello(self):
        self.thing()
        hello()

    # Define another local method.
    def thing(self):
        print 'Local thing'

# Create object from A.
a = A()
a.hello()
