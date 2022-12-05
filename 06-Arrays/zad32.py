def listToString(array):
    return ", ".join(str(num) for num in array)


print(listToString([1, 2, 3, 4, 5, 6]))