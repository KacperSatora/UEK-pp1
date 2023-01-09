import re

def f1(t):
    returnDict = {}
    names = re.findall(r'[A-Z][a-z]+', t)
    ages = re.findall(r'\d+', t)
    for i in range(len(names)):
        returnDict.update({names[i]:ages[i]})

    return (dict(sorted(returnDict.items())))

def f2(d):
    people = f1(d)
    sum = 0
    for person in people:
        sum += int(people[person])
    return sum