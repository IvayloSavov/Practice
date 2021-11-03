initial_sequence = list(map(int, input().split(" ")))
k = int(input())
pop_index = 0
new_sequence = []

while len(initial_sequence) > 0:
    pop_index += k - 1
    if pop_index >= len(initial_sequence):
        pop_index %= len(initial_sequence)

    new_sequence.append(initial_sequence.pop(pop_index))

print("[" + ",".join(map(str, new_sequence)) + "]")