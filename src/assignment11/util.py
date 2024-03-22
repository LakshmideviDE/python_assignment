def min_max_of_min(arr):
    min_values = [min(row) for row in arr]
    result = max(min_values)
    return result
