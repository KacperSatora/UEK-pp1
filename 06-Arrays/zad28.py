def median(array: list):
    return array[len(array) // 2] if len(array) % 2 != 0 else ((array[(len(array) // 2) - 1] + array[len(array) // 2]) / 2)

print(median([1, 0, 9, 4, 6]))
print(median([6, 8, 3, 1, 0, 5, 7]))