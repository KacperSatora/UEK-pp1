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