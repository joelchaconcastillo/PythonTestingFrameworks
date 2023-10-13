import unittest
from my_module import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)

    def test_add_mixed_numbers(self):
        result = add(5, -3)
        self.assertEqual(result, 2)

    def test_add_zero(self):
        result = add(0, 7)
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()

