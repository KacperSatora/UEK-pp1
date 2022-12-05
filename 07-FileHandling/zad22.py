import csv
csvList = []

with open("t22.csv", "r") as csvFile:
    csvData = csv.reader(csvFile)
    for line in csvData:
        print('{:<15} {:<15} {:<20}'.format(line[0], line[1], line[4]))
#     for line in csvFile:
#         line = line.strip()
#         line = line.split(',')
#         csvList.append(line)

# for i in range(1,len(csvList)):
#     print('{:<15} {:<15} {:<20}'.format(csvList[i][0], csvList[i][1], csvList[i][4]))
