import unittest
from python_assignment.src.Assignment2.util import find_runner_up_score
class MyTestCase(unittest.TestCase):
    def test_find_runner_up_score(self):
        n=5
        arr = [3, 4, 6, 6, 7]
        self.assertEqual(find_runner_up_score(n,arr), 6)
    def test_find_runner_up_score2(self):
        n = 5
        arr = [3, 4, 6, 7, 8]
        self.assertEqual(find_runner_up_score(n, arr), 7)  # add assertion here


if __name__ == '__main__':
    unittest.main()
