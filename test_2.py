def missingNumbers(arr, brr):
    set_1 = set(brr)
    set_2 = set(arr)

    diff = set_1.difference(set_2)
    print(list(diff))

missingNumbers([1, 4], [1, 2, 3, 4])