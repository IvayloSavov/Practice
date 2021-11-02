numbers = list(map(int, input().split(", ")))
zeroesList = [n for n in numbers if n == 0]
otherNumbersList = [n for n in numbers if n!= 0]
zeroesList.extend(otherNumbersList)
print(zeroesList)