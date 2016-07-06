# EXAMPLE 1: A quick glance to inheritance:
# ==============================================================================
class Parent(object):
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class Child(Parent):
    pass

parent = Parent()
child = Child()

dir(parent)
dir(child)
dir(Parent)
dir(Child)
Parent.__dict__


'''
In Python method overriding occours simply defining in the child class a method
with the same name of a method in the parent class. When you define a method in
the object you make this latter able to satisfy that method call, so the
implementations of its ancestors do not come in play.
'''

# EXAMPLE 2: Method overriding in action:
# ==============================================================================
class Parent(object):
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class Child(Parent):
    def get_value(self):
        return self.value + 1

# Now Child objects behave differently:

child = Child()
child.get_value()
Parent.__dict__


# EXAMPLE 3: An example of pre-filtering:
# ==============================================================================
import datetime

class Logger(object):
    def log(self, message):
        print message

class TimestampLogger(Logger):
    def log(self, message):
        message = "{ts} {msg}".format(ts=datetime.datetime.now().isoformat(),
                                      msg=message)
        super(TimestampLogger, self).log(message)

# The TimestampLogger object adds some information to the message string before
# calling the original implementation of its log() method.

l = Logger()
l.log('hi!')
t = TimestampLogger()
t.log('hi!')


# EXAMPLE 4: An example of post-filtering:
# ==============================================================================
import os

class FileCat(object):
    def cat(self, filepath):
        f = file(filepath)
        lines = f.readlines()
        f.close()
        return lines

class FileCatNoEmpty(FileCat):
    def cat(self, filepath):
        lines = super(FileCatNoEmpty, self).cat(filepath)
        nonempty_lines = [l for l in lines if l != '\n']
        return nonempty_lines