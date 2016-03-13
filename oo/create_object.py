# Create an Employee class
class Employee:
    """Common base class for all employees"""
    emp_count = 0

    # Create constructor of class.
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    # Define a method
    def display_count(self):
        print "Total Employee %d" % (Employee.emp_count)

    # Define another method
    def display_employee(self):
        print "Name: %s, Salary: %s" % (self.name, self.salary)

    # Define another method
    def print_attributes(self):
        print 'Employee.__doc__: ', Employee.__doc__
        print 'Employee.__name__: ', Employee.__name__
        print 'Employee.__module__: ', Employee.__module__
        print 'Employee.__bases__: ', Employee.__bases__
        print 'Employee.__dict__: ', Employee.__dict__

# Create Instance Objects
emp1 = Employee('Zara', 2000)
emp2 = Employee('Manni', 5000)

# Accessing Attributes:
emp1.display_employee()
emp2.display_employee()
print 'Total Employee %d' % Employee.emp_count
print
emp1.print_attributes()
