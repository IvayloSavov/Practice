numbers = list(map(int, input().split(", ")))

current_group = 10

while len(numbers) > 0:
    numbers_in_current_group = [n for n in numbers if n <= current_group]
    numbers = [n for n in numbers if n > current_group]

    print(f"Group of {current_group}'s: {numbers_in_current_group}")
    current_group += 10
