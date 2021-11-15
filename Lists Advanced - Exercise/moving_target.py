targets = list(map(int, input().split(" ")))

command = input()

while command != "End":
    operation, index, other = command.split(" ")
    index = int(index)
    if operation == "Shoot" and 0 <= index < len(targets):
        targets[index] -= int(other)
        if targets[index] <= 0:
            targets.pop(index)
    elif operation == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, other)
        else:
            print("Invalid placement!")
    elif operation == "Strike":
        radius = int(other)
        

    command = input()
