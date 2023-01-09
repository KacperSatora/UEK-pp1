def f(arr):
    if len(arr) == len(arr[0]):
        number = 1
        multiplier = 1
        for row in arr:
            for digit in row:
                if digit != number * multiplier:
                    return False
                multiplier += 1
            multiplier = 1
            number += 1
        return True
    else:
        return False


print(f([[1, 2, 3], [2, 4, 6], [3, 6, 9]]))
print(f([[1, 2], [2, 4]]))
print(f([[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]))
print(f([[1, 2], [3, 6]]))
print(f([[1, 2, 3], [2, 4, 6]]))
print(f([[1, 2, 3], [2, 5, 6]]))