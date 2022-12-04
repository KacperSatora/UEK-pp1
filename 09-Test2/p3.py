def f(array2D):
    finalList = [0,0,0,0]
    for row in array2D:
        index = 0
        for i in row:
            finalList[index] += i
            index += 1
    return finalList


print(f([[3, 6, 2, 7], [9, 5, 4, 0], [2, 8, 0, 9]]))
