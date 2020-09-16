import unittest
from city_functions import format

class FormatTestCase(unittest.TestCase):
    """Test for city_functions.py"""

    def test_city_country(self):
        """Will it return the correct format when called?"""
        formatted = format('London', 'England')
        self.assertEqual(formatted, 'London, England')

    def test_city_country_population(self):
        """Will it return the correct format when population parameter is passed?"""
        formatted = format('Berlin', 'Germany', 10000000)
        self.assertEqual(formatted, 'Berlin, Germany - Population: 10000000')
unittest.main()
