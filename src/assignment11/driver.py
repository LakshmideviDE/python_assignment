from python_assignments.src.assignment11.util import min_max_of_min
if __name__ == "__main__":
    n, m = map(int, input().split())
    input_array = [list(map(int, input().split())) for _ in range(n)]

    # Call the function and print the result
    output = min_max_of_min(input_array)
    print(output)
