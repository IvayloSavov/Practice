from collections import defaultdict
from functools import reduce

number_of_pairs = int(input())
academy = defaultdict(list)

for p in range(number_of_pairs):
    student_name = input()
    student_grade = input()

    academy[student_name].append(student_grade)

students_average_grades = {}

for student, grades in academy.items():
    average_grade = reduce(lambda acc, n: acc + float(n), grades, 0) / len(grades)
    if average_grade >= 4.50:
        students_average_grades[student] = average_grade

for student in sorted(students_average_grades.items(), key=lambda s: -s[1]):
    print(f"{student[0]} -> {student[1]:.2f}")

