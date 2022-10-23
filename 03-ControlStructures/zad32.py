size = 7
temp = 0
for i in range(1, size + 1):
    temp = i
    for j in range(1, size + 1):
        print(f"{temp}", end=" ") if temp > 9 else print(f" {temp}", end=" ")
        temp += size
    print()
