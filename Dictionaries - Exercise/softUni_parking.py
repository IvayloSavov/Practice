lines_count = int(input())
cars = {}

while lines_count > 0:
    line = input().split()
    command, username = line[0], line[1]

    if command == "register":
        if username in cars:
            print(f"ERROR: already registered with plate number {cars[username]}")
        else:
            plate = line[2]
            cars[username] = plate
            print(f"{username} registered {plate} successfully")
    elif command == "unregister":
        if username not in cars:
            print(f"ERROR: user {username} not found")
        else:
            del cars[username]
            print(f"{username} unregistered successfully")

    lines_count -= 1

for username in cars:
    print(f"{username} => {cars[username]}")