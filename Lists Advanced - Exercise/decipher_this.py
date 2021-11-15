words = input().split(" ")

output = []

for word in words:
    current_word = list(word)
    word = []
    first_chr_numbers = []
    for ch in current_word:
        if ch.isdigit():
            first_chr_numbers.append(ch)
        else:
            word.append(ch)
    word.insert(0, chr(int("".join(first_chr_numbers))))
    word[1], word[-1] = word[-1], word[1]
    output.append("".join(word))

print(" ".join(output))

