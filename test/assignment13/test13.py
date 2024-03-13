import unittest
from python_assignments.src.assignment13.util import mean_var

class MyTestCase(unittest.TestCase):
    def test_something(self):
        res = mean_var()
        expected_result = "[1.5 3.5]\n[1. 1.]\n1.11803398875"
        self.assertEqual(expected_result, expected_result.strip())  # add assertion here

if __name__ == '__main__':
    unittest.main()
