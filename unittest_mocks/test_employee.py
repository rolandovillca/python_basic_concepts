
from unittest import TestCase
from mock import Mock
from mock import MagicMock
from mock import patch

from employee import Employee
from data import list_employees

def my_employee():
    return [{
        "id":"1",
        "employee_name":"testing",
        "employee_salary":"1",
        "employee_age":"1",
        "profile_image":""
    }]

class TestEmployee(TestCase):

    def test_mock1(self):
        emp = Employee()
        emp.method = MagicMock(return_value=100)
        emp.method(1, 2, 3, 4, 5, key='value')
        emp.method.assert_called_with(1, 2, 3, 4, 5, key='value')

    def test_count_empty_employees(self):
        emp = Employee()
        emp.count_employees = MagicMock(return_value=0)
        emp.count_employees([])
        emp.count_employees.assert_called_with([])
        assert emp.count_employees([]) == 0

    def test_employee_instance(self):
        emp = MagicMock()
        emp.count_employees = MagicMock(return_value=0)
        emp.count_employees([])
        emp.count_employees.assert_called_with([])
        assert emp.count_employees([]) == 0

    #def test_exception(self):
    #    emp = Mock(side_effect=KeyError('My Key Error'))
    #    #self.assertRaises(KeyError, emp('My Key Error'))
    #    self.assertRaisesWithMessage(KeyError, 'My Key Error', )

