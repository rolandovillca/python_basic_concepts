import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'Hello World'
        self.assertEqual(s.split(), ['Hello', 'World'])

        #Check that s.split fails when the separator is not a string.
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

# How to run this example:
# python basic_sample.py
# python basic_sample.py -v
# python -m unittest basic_sample
# $ python -m unittest basic_sample.TestStringMethods.test_upper