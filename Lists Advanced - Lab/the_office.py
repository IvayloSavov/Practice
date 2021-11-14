employees_happiness = map(int, input().split(" "))
factor = int(input())

employees_happiness = list(map(lambda e: e * factor, employees_happiness))
average_happiness = sum(employees_happiness) / len(employees_happiness)

happy_employees = sum(1 for e in employees_happiness if e >= average_happiness)

if happy_employees >= (len(employees_happiness) / 2):
    print(f"Score: {happy_employees}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {happy_employees}/{len(employees_happiness)}. Employees are not happy!")