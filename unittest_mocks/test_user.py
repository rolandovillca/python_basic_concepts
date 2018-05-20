from unittest import TestCase
from mock import Mock
from mock import MagicMock
from mock import patch

from employee import Employee
from user import User
from data import list_users

class TestEmployee(TestCase):
    def setUp(self):
        self.user = User()

    def test_user_description_equal(self):
        self.assertEqual(self.user.get_description(), 'My Description')

    def test_user_description_false(self):
        self.assertFalse(self.user.get_description().isupper())

    @patch('user.request')
    def test_user_request(self, req):
        url = MagicMock()
        self.user.request_users(url)
        req.assert_called_once_with('GET', url)

    @patch('user.User.get_users')
    def test_get_users(self, arg1):
        self.user.get_users()
        arg1.assert_called_once_with()

    @patch('user.User.get_users')
    @patch('user.User')
    def test_name_in_page_calls_get_page(self, arg1, getusers):
        user = arg1()
        user.get_users.return_value = []
        response = user.get_users()
        self.assertTrue(response == [])

    @patch('employee.Employee')
    @patch('user.User')
    def test_count_users_and_employees(self, userarg, employeearg):
        user_response = [{
                            "id":1,
                            "first_name":"George",
                            "last_name":"Bluth",
                            "avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/calebogden/128.jpg"
                        }]

        user = userarg()
        employee = employeearg()

        user.count_users.return_value = 1
        employee.count_employees.return_value = 0

        response_users = user.count_users(user_response)
        response_employees = employee.count_employees([])

        self.assertIsNotNone(response_users)
        #self.assertIsInstance(response_users[0], dict)

        self.assertTrue(response_users == 1)
        self.assertTrue(response_employees == 0)
