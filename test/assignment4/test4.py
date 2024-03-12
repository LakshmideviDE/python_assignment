import unittest
from python_assignment.src.assignment4.util import merge_the_tools

class MyTestCase(unittest.TestCase):
    def test_merge_the_tools(self):
        # Sample input
        string = "AABCAAADA"
        k = 3
        merge_the_tools(string, k)
if __name__ == '__main__':
    unittest.main()

