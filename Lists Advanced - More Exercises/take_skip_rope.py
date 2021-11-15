string = input()

numbers_list = [int(ch) for ch in string if ch.isdigit()]
non_numbers_list = [ch for ch in string if not ch.isdigit()]

take_list = [numbers_list[i] for i in range(len(numbers_list)) if i % 2 == 0]
skip_list = [numbers_list[i] for i in range(len(numbers_list)) if i % 2 != 0]

result_string = ""

for i in range(len(take_list)):
    take_ch = take_list[i]
    skip_ch = skip_list[i]
    result_string += "".join(non_numbers_list[:take_ch])
    skipped_string = non_numbers_list[take_ch: take_ch + skip_ch]

    non_numbers_list = non_numbers_list[take_ch + skip_ch:]

print(result_string)
