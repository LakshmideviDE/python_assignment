from python_assignments.src.assignment17.util import pro_letter
if __name__ == "__main__":
    n = int(input())
    letters = input().split()
    k = int(input())

    result = pro_letter(n, letters, k)
    print(result)
