import unittest
import my_module

class TestMyModule(unittest.TestCase):
    def test_add(self):
        result = my_module.add(2, 3)
        self.assertEqual(result, 5)

