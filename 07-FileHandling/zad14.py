designatedFile = input("Input file name:\n>")
lines = 0
with open(designatedFile, "r") as file:
    for line in file:
        print(line.strip())
        if line.strip() != "":
            lines += 1
print(f"File name: {designatedFile}\nNumber of lines: {lines}")