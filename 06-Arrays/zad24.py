arr = [2, 3, 2, 5, 8, 1, 9, 8]

for element in arr:
    if arr.count(element) > 1:
        for i in range(arr.count(element)):
            arr.remove(element)

print(arr)