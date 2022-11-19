def compare(array1, array2):
    array1.sort()
    array2.sort()
    return array1 == array2

print(compare(["water", "book", "sky"], ["water", "book", "sky"]))
print(compare([True, False], [True, False, True]))
print(compare([3, 2, 1], [3, 2]))
