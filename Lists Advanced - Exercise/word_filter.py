# words = input().split(" ")
#
# output = (word for word in words if len(word) % 2 == 0)
# print('\n'.join(output))

print('\n'.join(word for word in input().split(" ") if len(word) % 2 == 0))