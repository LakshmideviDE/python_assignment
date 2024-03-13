import unittest
from  python_assignments.src.assignment11.util import min_max_of_min
class TestMinMaxOfMin(unittest.TestCase):
    def test_min_max_of_min(self):
        input_array = [
            [2, 5],
            [3, 7],
            [1, 3],
            [4, 0]
        ]
        expected_output = 3
        actual_output = min_max_of_min(input_array)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
