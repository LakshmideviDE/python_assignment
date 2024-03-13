import unittest
from python_assignments.src.assignment17.util import pro_letter
class MyTestCase(unittest.TestCase):
    def test_pro_letter(self):
        n = 4
        letters = ['a', 'a', 'c', 'd']
        k = 2
        expected = 0.8333
        result = pro_letter(n, letters, k)
        self.assertAlmostEqual(result, expected, places=4)
if __name__ == '__main__':
    unittest.main()

