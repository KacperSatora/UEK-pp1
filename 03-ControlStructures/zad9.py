numbers = []
for i in range(2):
    x = int(input("Type in the number:\n>"))
    numbers.append(x)

if numbers[0] > 0 or numbers[1] > 0:
    print("One of them is positive")
else:
    print("Both are NOT positive")