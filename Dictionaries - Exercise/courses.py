from collections import defaultdict

courses = defaultdict(list)
line = input()

while line != "end":
    course_name, student_name = line.split(" : ")
    courses[course_name].append(student_name)

    line = input()

for course, students in sorted(courses.items(), key=lambda c: -len(c[1])):
    print(f"{course}: {len(students)}")
    for student in sorted(students):
        print(f"-- {student}")