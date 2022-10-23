dogAge = int(input("Input dog's age: "))
if dogAge > 2:
    humanAge = 21 + (dogAge - 2) * 4
else:
    humanAge = dogAge * 10.5
print(f"Dog's age in our years is {humanAge}")