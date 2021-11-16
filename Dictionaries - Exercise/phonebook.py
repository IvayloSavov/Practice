phonebook = {}

while True:
    command = input()

    if len(command) == 1:
        break
    name, number = command.split("-")
    phonebook[name] = number


for _ in range(int(command)):
    contact_name = input()
    if contact_name in phonebook:
        print(f"{contact_name} -> {phonebook[contact_name]}")
    else:
        print(f"Contact {contact_name} does not exist.")
