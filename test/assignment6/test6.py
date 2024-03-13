import unittest
from python_assignments.src.assignment6.util import print_pattern

class MyTestCase(unittest.TestCase):
    def test_something(self):
      expected_result = [
            '  H  ',
            ' HHH ',
            'HHHHH',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHHHHHHHHHHHHHH  ',
            ' HHHHHHHHHHHHHHH  ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            '            HHHHH ',
            '             HHH  ',
            '              H   ',
        ]
      self.assertEqual(expected_result, print_pattern(3))  # add assertion here

if __name__ == '__main__':
    unittest.main()
