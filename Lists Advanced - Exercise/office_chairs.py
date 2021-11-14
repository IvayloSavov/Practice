number_of_rooms = int(input())

current_room = 0
free_chairs = 0
print_free = True
for _ in range(number_of_rooms):
    current_room += 1
    chairs, visitors = input().split(" ")
    if len(chairs) < int(visitors):
        print(f"{int(visitors) - len(chairs)} more chairs needed in room {current_room}")
        print_free = False
    elif len(chairs) > int(visitors):
        free_chairs += len(chairs) - int(visitors)

if print_free:
    print(f"Game On, {free_chairs} free chairs left")