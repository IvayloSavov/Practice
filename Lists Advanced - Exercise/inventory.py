items = input().split(", ")

command = input()

while command != "Craft!":
    operation, other = command.split(" - ")
    if operation == "Collect" and other not in items:
        items.append(other)
    elif operation == "Drop" and other in items:
        items.remove(other)
    elif operation == "Combine Items":
        old_item, new_item = other.split(":")
        if old_item in items:
            old_item_index = items.index(old_item)
            items.insert(old_item_index + 1, new_item)
    elif operation == "Renew" and other in items:
        items.remove(other)
        items.append(other)

    command = input()

print(", ".join(items))
