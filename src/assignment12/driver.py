from python_assignments.src.assignment12.util import determinant
n = int(input("Enter the size of the square matrix: "))
matrix = [list(map(float, input().split())) for _ in range(n)]

if len(matrix) == 2 and all(len(row) == 2 for row in matrix):
    det = determinant(matrix)
    print("Determinant:", det)
else:
    print("Error: Input matrix should be a 2x2 matrix.")