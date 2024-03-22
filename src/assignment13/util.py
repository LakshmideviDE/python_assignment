def mean_var():
    n, m = map(int, input().split())
    data = []
    for i in range(n):
        row = list(map(int, input().split()))
        data.append(row)
    mean_values = [sum(row) / m for row in data]
    var_values = [sum((x - mean_values[j]) ** 2 for x in col) / n for j, col in enumerate(zip(*data))]

    std_dev = round((sum(var_values) / n) ** 0.5, 11)
    result = "\n".join([str(mean_values), str(var_values), str(std_dev)])

    return result

