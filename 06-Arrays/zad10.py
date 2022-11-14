import random

# random.randint(0,10) for i in range(100)
arr = [1,2,3]

even = 0
odd = 0
i = 0

while i < len(arr):
    if int(arr[i]) % 2 == 0:
        even += 1
    else:
        odd += 1
    i += 1

print(f"even -> {even}, odd -> {odd}")
