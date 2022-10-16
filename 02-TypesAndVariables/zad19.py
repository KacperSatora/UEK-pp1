height = float(input("Enter your height in centimeters:\n>")) / 100
mass = float(input("Enter your weight:\n>"))

print(f"your BMI is: {round(mass / (height ** 2), 2)}")