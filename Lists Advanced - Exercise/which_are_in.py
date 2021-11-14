strings_to_be_searched = input().split(", ")
strings = input().split(", ")

output = list()

for string in strings_to_be_searched:
    for string_2 in strings:
        if string in string_2 and string not in output:
            output.append(string)

print(output)