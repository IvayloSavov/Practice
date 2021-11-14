number_wagons = int(input())
train = [0 for _ in range(number_wagons)]
command = input()
while command != "End":
    operation, *args = command.split(" ")
    if operation == "add":
        people = int(args[0])
        train[-1] += people
    elif operation == "insert":
        index, people = args
        train[int(index)] += int(people)
    elif operation == "leave":
        index, people = args
        train[int(index)] -= int(people)
    command = input()

print(train)