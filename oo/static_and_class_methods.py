'''
'''

# EXAMPLE 1: The Python @classmethod:
# ==============================================================================
# The benefit of this is: whether we call the method from the instance or the
# class, it passes the class as first argument.

class MyCounter(object):
    no_inst = 0

    def __init__(self):
        MyCounter.no_inst += 1

    @classmethod
    def get_no_of_instance(class_object):
        return class_object.no_inst

my_counter = MyCounter()

print my_counter.get_no_of_instance()
print MyCounter.get_no_of_instance()
print


# EXAMPLE 2: The Python @staticmethod:
# ==============================================================================
# The benefit of this is: whether we call the method from the instance or the
# class, it passes the class as first argument.

IND = 'ON'

class MyClass(object):
    def __init__(self, data):
        self.data = data

    @staticmethod
    def check_ind():
        return (IND == 'ON')

    def do_reset(self):
        if self.check_ind():
            print 'Reset done for {}'.format(self.data)

    def set_db(self):
        if self.check_ind():
            self.db = 'New db connection'
        print 'DB connection made for: {}'.format(self.data)

my_class = MyClass(12)
my_class.do_reset()
my_class.set_db()
print

# EXAMPLE 3: How @staticmethod and @classmethod are different:
# ==============================================================================

class Kls(object):
    def __init__(self, data):
        self.data = data

    def printd(self):
        print self.data

    @staticmethod
    def static_method(*arg):
        print 'Static method: {}'.format(arg)

    @classmethod
    def class_method(*arg):
        print 'Class method: {}'.format(arg)

ik = Kls(23)
ik.printd()

ik.static_method()
ik.class_method()
# Kls.printd()

Kls.static_method()
Kls.class_method()