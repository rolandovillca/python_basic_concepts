class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % (Employee.empCount)

    def displayEmployee(self):
        print "Name: %s, Salary: %s" % (self.name, self.salary)

    def printAttributes(self):
        print 'Employee.__doc__: ', Employee.__doc__
        print 'Employee.__name__: ', Employee.__name__
        print 'Employee.__module__: ', Employee.__module__
        print 'Employee.__bases__: ', Employee.__bases__
        print 'Employee.__dict__: ', Employee.__dict__

# Create Instance Objects
emp1 = Employee('Zara', 2000)
emp2 = Employee('Manni', 5000)

# Accessing Attributes:
emp1.displayEmployee()
emp2.displayEmployee()
print 'Total Employee %d' % Employee.empCount
print
emp1.printAttributes()
