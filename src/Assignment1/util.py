def cal_avg(n, student_data, query_name):
    student_marks = {}
    for _ in range(n):
        name, *line = student_data[_].split()
        scores = list(map(float, line))
        student_marks[name] = scores

    if query_name in student_marks:
        avg = sum(student_marks[query_name]) / len(student_marks[query_name])
        return "{:.2f}".format(avg)
        
