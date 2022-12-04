import json


studentData = {}
while True:
    userValue = input(
        "Enter key nad value separated by '-' or press enter to finish:\n>")
    if userValue == "":
        break
    lineValues = [userValue.strip().split("-")]
    studentData[lineValues[0][0]] = lineValues[0][1]

with open("student.json", "a")as file:
    json.dump(studentData, file, indent=4)
