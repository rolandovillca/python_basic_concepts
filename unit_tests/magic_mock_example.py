from mock import MagicMock
from calculator import Calculator

thing = Calculator()
thing.mymethod = MagicMock(return_value = {'x':'X'})
thing.mymethod(1,2,3,4,5,6,7,8,9,0, k='val')

thing.mymethod.assert_called_with(1,2,3,4,5,6,7,8,9,0, k='val')


