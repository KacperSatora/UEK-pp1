asList = []

with open("t27.txt", "r") as file:
    for line in file:
        line = line.split()
        asList.append(line)


sum = 0

for i in range(1, len(asList), 2):
    line = asList[i]
    for j in range(1, len(line)):
        value = line[j]
        # print(value[-1])
        if (value[-1]) == ",":
            numValue = float(value[0:-1])
            sum += numValue
        else:
            numValue = float(value)
            sum += numValue


print(sum / len(asList[1][0]))