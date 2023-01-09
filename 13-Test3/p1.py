def f(n):
    returnString = ""
    if n > 0:
        for i in range(n):
            if i % 5 == 0:
                returnString += "-"
                returnString += "/"
            else:
                returnString += "/"
    return returnString[1:]