from audioop import mul


multi = int(input("Enter number: "))
for i in range(10):
    print(f"{multi} x {i + 1} = {multi * (i + 1)}")