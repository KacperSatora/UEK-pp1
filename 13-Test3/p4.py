def f(d):
    parking = []
    for action in d:
        if action[1] == 'in':
            parking.append(action[0])
        else:
            parking.pop(parking.index(action[0]))

    parking.sort()
    return parking

print(f([["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
["BA111","in"],["BA123","out"],["KR234","in"]]
))
