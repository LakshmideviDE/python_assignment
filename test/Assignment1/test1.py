import unittest
from python_assignments.src.Assignment1.util import cal_avg

class TestCalAvg(unittest.TestCase):
    def test_cal_avg(self):
        n = 3
        student_data = ['Harsh 25 26.5 28', 'Anurag 26 28 30', 'Varun 25 26 28']
        query_name = 'Harsh'
        self.assertEqual(cal_avg(n,student_data, query_name), '26.50')

if __name__ == '__main__':
    unittest.main()
