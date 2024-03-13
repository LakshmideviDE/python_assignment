import unittest
from python_assignments.src.assignment12.util import determinant
class TestDeterminantFunction(unittest.TestCase):
    def test_valid_input(self):
        try:
            n=2
            matrix = [[1.1, 1.1], [1.1, 1.1]]
            self.assertEqual(determinant(matrix), 0.0)
        except ValueError as ve:
            self.fail(f"Unexpected ValueError: {ve}")
        except Exception as e:
            self.fail(f"Unexpected error: {e}")
        finally:
            print("Test for valid input completed.")

if __name__ == "__main__":
    unittest.main()
