from collections import defaultdict

line = input()
companies = defaultdict(list)

while line != "End":
    company, user = line.split(" -> ")
    if user not in companies[company]:
        companies[company].append(user)

    line = input()

for company in sorted(companies.keys()):
    print(company)
    for user in companies[company]:
        print(f"-- {user}")
