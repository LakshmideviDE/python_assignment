import unittest
from python_assignments.src.assignment8.util import cal_avg_marks
class MyTestCase(unittest.TestCase):
    def test_something(self):
        res = cal_avg_marks()
        self.assertEqual(res, '81.00')

if __name__ == '__main__':
    unittest.main()
