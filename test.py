def jumpingOnClouds(c):
    clouds = c
    index = 0
    moves = 0
    while index <= len(clouds) - 1:
        if index + 2 in range(len(clouds)) and clouds[index + 2] != "1":
            index += 2
            moves += 1
        elif index + 1 in range(len(clouds)) and clouds[index + 1] != "1":
            index += 1
            moves += 1
        else:
            break

    return moves


jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])