def print_format_num(n):
    width = len(bin(n)[2:])
    s = []
    for i in range(1, n + 1):
        s.append("{:>{width}} {:>{width}o} {:>{width}X} {:>{width}b}".format(i, i, i, i, width=width))
    return '\n'.join(s)