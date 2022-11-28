file = open("shopping.txt", "a")
product = input("Enter product name: \n>")
file.write(f"{product}\n")