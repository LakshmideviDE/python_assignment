import unittest

def array_operations(input_array):
    def apply_operations(x):
        return int(x), int(x) + 1 if x > 0 else int(x), round(x)

    results = [apply_operations(float(x)) for x in input_array]

    return (
        [result[0] for result in results],
        [result[1] for result in results],
        [result[2] for result in results]
    )
class TestArrayOperations(unittest.TestCase):
    def test_floor_values(self):
        input_array = ["1.1", "2.2", "3.3", "4.4", "5.5", "6.6", "7.7", "8.8", "9.9"]
        expected_floor = [ 1, 2,  3,  4,  5, 6,  7,  8, 9]
        self.assertEqual(array_operations(input_array)[0], expected_floor)

    def test_ceil_values(self):
        input_array = ["1.1", "2.2", "3.3", "4.4", "5.5", "6.6", "7.7", "8.8", "9.9"]
        expected_ceil = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(array_operations(input_array)[1], expected_ceil)

    def test_rint_values(self):
        input_array = ["1.1", "2.2", "3.3", "4.4", "5.5", "6.6", "7.7", "8.8", "9.9"]
        expected_rint = [1, 2, 3, 4, 6, 7, 8, 9, 10]
        self.assertEqual(array_operations(input_array)[2], expected_rint)

if __name__ == '__main__':
    unittest.main()
