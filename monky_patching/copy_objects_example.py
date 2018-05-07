class Address():
    def __init__(self, street, city):
        self.street = street
        self.city = city

    def location(self):
        print self.street
        print self.city

class Person():
    def __init__(self, name, adress):
        self.name = name
        self.address = address

    def get_name(self):
        print self.name

    def set_name(self, name):
        self.name = name

    def print_address(self):
        self.address.location()

class Student(Person):
    def __init__(self, name, address):
        Person.__init__(self, name, address)
    def subject(self):
        print 'Mathematics'

address = Address('El Prado Av.', 'Cochabamba')
address.location()
print

student = Student('Rolando', address)
student.get_name()
student.print_address()
print

def patch():
    print 'Patched method'

import copy
orig_obj = copy.deepcopy(student)

student.subject()
student.subject = patch
student.subject()
print

orig_obj.subject()