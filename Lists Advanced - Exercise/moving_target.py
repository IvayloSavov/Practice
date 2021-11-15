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
            targets.insert(index, int(other))
        else:
            print("Invalid placement!")
    elif operation == "Strike":
        radius = int(other)
        left_radius = index - radius
        right_radius = index + radius
        if 0 <= left_radius and right_radius < len(targets):
            targets = targets[0: left_radius] + targets[right_radius + 1:]
        else:
            print("Strike missed!")

    command = input()

print("|".join(map(str, targets)))
