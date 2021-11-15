neighborhood = list(map(int, input().split("@")))

command = input()
current_pos = 0

while command != "Love!":
    jump, length = command.split(" ")
    current_pos += int(length)
    if current_pos >= len(neighborhood):
        current_pos = 0

    if neighborhood[current_pos] <= 0:
        print(f"Place {current_pos} already had Valentine's day.")
    else:
        neighborhood[current_pos] -= 2

        if neighborhood[current_pos] <= 0:
            print(f"Place {current_pos} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {current_pos}.")

houses_greater_than_zeros = [house for house in neighborhood if house > 0]

if houses_greater_than_zeros:
    print(f"Cupid has failed {len(houses_greater_than_zeros)} places.")
else:
    print("Mission was successful.")
