import unittest
from python_assignments.src.assignment4.util import merge_the_tools
class MyTestCase(unittest.TestCase):
    def test_merge_the_tools(self):
        string,k = "AABCAAADA", 3
        expected_output = "AB\nCA\nAD"
        result = merge_the_tools(string, k)
        self.assertEqual(result, result)
if __name__ == '__main__':
    unittest.main()

