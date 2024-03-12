from collections import namedtuple
def cal_avg_marks():
    # Read input
    n = int(input())
    columns = input().split()
    Student = namedtuple('Student', columns)

    # Calculate and print the average marks
    average = sum([int(Student(*input().split()).MARKS) for _ in range(n)]) / n
    return ('{:.2f}'.format(average))

