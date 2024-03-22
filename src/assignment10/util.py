def array_operations(input_array):
    # Define a single function for floor, ceil, and rint
    def apply_operations(x):
        return int(x), int(x) + 1 if x > 0 else int(x), round(x)

    # Apply the function to each element in the array
    results = [apply_operations(float(x)) for x in input_array]

    # Print the results
    print([result[0] for result in results])
    print([result[1] for result in results])
    print([result[2] for result in results])
