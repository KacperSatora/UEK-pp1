arr = [-15,8,-31,47,-2,19]

# print(f" max -> {max(arr)}, min -> {min(arr)}")

max = arr[0]
min = arr[0]

for i in range(1, len(arr)):
    if arr[i] > max:
        max = arr[i]
    if arr[i] < min:
        min = arr[i]

print(f"max -> {max}, min -> {min}")