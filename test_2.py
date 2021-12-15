#
# import math
# import os
# import random
# import re
# import sys
#
#
# #
# # Complete the 'closestNumbers' function below.
# #
# # The function accepts INTEGER_ARRAY numbers as parameter.
# #
#
# def closestNumbers(numbers):
#     minimal_absolute_difference = sys.maxsize
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             n_1 = numbers[i]
#             n_2 = numbers[j]
#             cur_difference = abs(n_1 - n_2)
#             if cur_difference < minimal_absolute_difference and cur_difference != 0:
#                 minimal_absolute_difference = cur_difference
#
#     pairs = []
#
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             n_1 = numbers[i]
#             n_2 = numbers[j]
#             cur_difference = abs(abs(n_1) - abs(n_2))
#             if cur_difference == minimal_absolute_difference:
#                 pairs.append([n_1, n_2])
#
#     sorted_pairs = sorted(pairs, key=lambda p: (p[0], p[1]))
#     for p in sorted_pairs:
#         p.sort()
#         print(" ".join(map(str, p)))
#
#
# closestNumbers([4, 4, -2, -1, 3])



class X:
    def __init__(self):
        self.__num1 = 5
        self.num2 = 2

    def display_values(self):
        print(self.__num1, self.num2)


class Y(X):
    def __init__(self):
        super().__init__()
        self.__num1 = 1
        self.num2 = 6
obj = Y()
obj.display_values()