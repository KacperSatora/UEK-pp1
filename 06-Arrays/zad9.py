arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
arr2 = []
for i in range(len(arr)):
    arr2.append(len(arr[i]))

print(f"{arr[arr2.index(max(arr2))]} - > {max(arr2)}")