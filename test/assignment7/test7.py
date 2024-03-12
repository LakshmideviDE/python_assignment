import unittest
from python_assignments.src.assignment7.util import find_day
class MyTestCase(unittest.TestCase):
    def test_something(self):
        date_input = "6 26 2015"
        expected_output = "FRIDAY"
        actual_output = find_day(date_input)
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
