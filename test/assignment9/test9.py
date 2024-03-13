import unittest
from python_assignments.src.assignment9.util import time_diff
class MyTestCase(unittest.TestCase):
    def test_something(self):
        timestamp1 = "Sun 10 May 2015 13:54:36 -0700"
        timestamp2 = "Sun 10 May 2015 13:54:36 -0000"

        self.assertEqual(time_diff(timestamp1, timestamp2), 25200)  # add assertion here


if __name__ == '__main__':
    unittest.main()
