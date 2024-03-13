import unittest
from python_assignments.src.assignment18.util import filter_valid_emails
class MyTestCase(unittest.TestCase):
    def test_case2(self):
        expected = ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
        actual = filter_valid_emails(3, ['lara@hackerrank.com', 'brian-23@hackerrank.com', 'britts_54@hackerrank.com'])
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

