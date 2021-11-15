output = {}


while True:
    command = input()
    if command == "stop":
        break
    resource = command
    quantity = int(input())

    if resource not in output:
        output[resource] = 0
    output[resource] += quantity

for item, quantity in output.items():
    print(f"{item} -> {quantity}")
