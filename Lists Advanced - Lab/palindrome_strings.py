# words = input().split(" ")
# palindrome = input()
# palindromes = [word for word in words if word == word[::-1]]
#
# print(palindromes)
# print(f"Found palindrome {palindromes.count(palindrome)} times")

palindromes = [word for word in input().split(" ") if word == word[::-1]]

print(palindromes)
print(f"Found palindrome {palindromes.count(input())} times")