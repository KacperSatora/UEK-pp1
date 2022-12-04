import csv
csvList = []

with open("t22.csv", "r") as csvfile:
    for line in csvfile:
        line = line.strip()
        line = line.split(',')
        csvList.append(line)

for i in range(1,len(csvList)):
    print('{:<15} {:<15} {:<20}'.format(csvList[i][0], csvList[i][1], csvList[i][4]))
