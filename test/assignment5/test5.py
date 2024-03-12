import unittest
from python_assignments.src.assignment5.util import print_format_num
class MyTestCase(unittest.TestCase):
    def test_print_formatted(self):
        expected_output = " 1 1 1 1\n 2 2 2 10" # Compare the actual and expected output
        self.assertEqual(print_format_num(2), ' 1  1  1  1\n 2  2  2 10')


if __name__ == '__main__':
    unittest.main()

