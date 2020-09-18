import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for the class Employee"""

    def setUp(self):
        """Create an instance of Employee and assign it to e"""
        self.e = Employee('Timo', 'Werner', 250000)

    def test_default_raise(self):
        """Test that the raise function works with default value"""
        self.e.give_raise()
        self.assertEqual(self.e.salary, 255000)

    def test_custom_raise(self):
        """Test that the raise function takes a number as a parameter"""
        self.e.give_raise(100000)
        self.assertEqual(self.e.salary, 350000)
        
unittest.main()
