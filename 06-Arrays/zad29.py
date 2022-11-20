value = int(input("Podaj wartość: "))
array = [1.5,2.3,6,4.54,13]

doneArray = []

for i in array:
    if i > value:
        doneArray.append(i)

print(doneArray)