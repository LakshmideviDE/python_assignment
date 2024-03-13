import unittest
from python_assignments.src.assignment14.util import cal_hap

def cal_hap(n, m, array, set_a, set_b):
    happiness = 0
    for num in array:
        if num in set_a:
            happiness += 1
        elif num in set_b:
            happiness -= 1
    return happiness
class TestCalculateHappiness(unittest.TestCase):
    def test_example(self):
        n = 3
        m = 2
        array = [1, 5, 3]
        set_a = {3, 1}
        set_b = {5, 7}
        result = cal_hap(n, m, array, set_a, set_b)
        self.assertEqual(result, 1)
if __name__ == '__main__':
    unittest.main()
