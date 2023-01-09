def f(d):
    parking = []
    for action in d:
        if action[1] == 'in':
            parking.append(action[0])
        else:
            parking.pop(parking.index(action[0]))

    parking.sort()
    return parking