from python_assignments.src.assignment16.util import solve
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        _, integers = int(input()), input()
        print(solve(integers))
