number_of_electrons = int(input())

shells = []
n = 0
while number_of_electrons > 0:
    n += 1
    current_shell = 2 * (n ** 2)
    if number_of_electrons >= current_shell:
        shells.append(current_shell)
    else:
        shells.append(number_of_electrons)
        break

    number_of_electrons -= current_shell

print(shells)
