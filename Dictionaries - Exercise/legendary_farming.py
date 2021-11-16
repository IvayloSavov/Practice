from collections import deque

possible_items = {"shards": "shadowmourne", "fragments": "valanyr", "motes": "dragonwrath"}
junk = {}

items = ""

while True:
    line= input()
    if line == "":
        break
    items += line + " "

items = deque(items.rstrip().split(" "))
print(items)

# while len(items) > 0:
#     quantity, item_name = int(items.popleft()), items.popleft()
#     print(quantity, item_name)
