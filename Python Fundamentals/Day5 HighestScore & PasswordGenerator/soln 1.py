student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_result= student_scores[0]
max_function= max(student_scores)
for max in student_scores:
    if max>total_result:
        total_result= max
print(total_result)
print(max_function)
