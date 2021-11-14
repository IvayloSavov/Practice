command = input()
to_do_list = []
while command != "End":
    importance, note = command.split("-")
    to_do_list.append((int(importance), note))
    command = input()

print(list(dict(sorted(to_do_list, key=lambda kvp: kvp[0])).values()))