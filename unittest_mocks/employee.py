
from requests import request

class Employee:
    def __init__(self):
        self.resp = []

    def request_employees(self, url='http://dummy.restapiexample.com/api/v1/employees'):
        self.resp = request('GET', url)

    def request_employee(self, employee_id=1):
        url = 'http://dummy.restapiexample.com/api/v1/employees/{}'.format(employee_id)
        return request('GET', url)

    def get_employees(self):
        return self.resp.json()

    def get_employee(self, employee_id):
        employees = self.get_employees()
        for employee in employees:
            if employee.get('id') == str(employee_id):
                return employee
        return {}

    def count_employees(self):
        return len(self.get_employees())


if __name__ == '__main__':
    employee = Employee()
    employee.request_employees()
    print
    print 'Employees:', employee.get_employees()
    print
    print 'Employee:', employee.get_employee(1)
    print
    print 'Total Employees:', employee.count_employees()

