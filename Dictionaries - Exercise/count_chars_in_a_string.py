string = input()

output = {}

for ch in string:
    if ch == " ":
        continue
    if ch not in output:
        output[ch] = 0
    output[ch] += 1

[print(f"{ch} -> {output[ch]}") for ch in output]
