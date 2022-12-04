def f(dictionary, x, y):
    sum = 0
    for key in dictionary:
        for number in dictionary[key]:
            if number >= x and number <= y:
                sum += number
    return sum