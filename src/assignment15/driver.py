from python_assignments.src.assignment15.util import word_occ
input_values = "4\nbcdef\nabcdefg\nbcde\nbcdef\n"
n = int(input_values.split('\n')[0])
words = input_values.split('\n')[1:-1]

distinct_count, occurrences_list = word_occ(n, words)
print(distinct_count)
print(occurrences_list)
