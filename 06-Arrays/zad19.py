arr = [15, 8, 31, 47, 2, 19]

counter = 0
sum = 0

while counter < len(arr):
    sum += arr[counter]
    counter += 1

print(round(sum / len(arr),2))