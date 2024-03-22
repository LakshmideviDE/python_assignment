def determinant(matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Input matrix should be a 2x2 matrix.")

    a, b = matrix[0]
    c, d = matrix[1]

    return round((a * d - b * c), 2)
    
