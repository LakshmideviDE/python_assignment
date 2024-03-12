import unittest
from python_assignments.src.assignment3.util import mutate_string


class MyTestCase(unittest.TestCase):
    def test_something(self):
        res = mutate_string()
        self.assertEqual(res, 'laksshmi')  # add assertion here


if __name__ == '__main__':
    unittest.main()
