file = open("t15.txt", "r")
lines = []
for line in file:
    lines.append(line.strip())
for i in range(0,len(lines),5):
    if input("enter enter") == "":
        for j in range(0,5):
            print(lines[i + j])
file.close()