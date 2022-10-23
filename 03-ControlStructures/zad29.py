x = []
while True:
    number = int(input("Enter number: "))
    x.append(number)
    if number == 0:
        x.pop()
        break
print(f"RESULT: Quantity = {len(x)}, Sum = {sum(x)}, Mean = {int(sum(x)/len(x))}")