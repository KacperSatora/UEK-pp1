arr = [[3, 9, 2], [2, 4, 5], [7, 1, 6], [0, 4, 8]]

sum = 0

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] % 2 == 0:
            sum += arr[i][j]
            
print(sum)