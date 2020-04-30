from django.test import TestCase
from app.calc import add, subtract

class CalcTests(TestCase):

    def test_add_numbers(self):
        """ Tests the addition of 2 numbers"""
        self.assertEqual(add(3,7), 10)

    def test_subtract_numbers(self):
        """Test the substraction of 2 numbers"""
        self.assertEqual(subtract(5,11), 6)
