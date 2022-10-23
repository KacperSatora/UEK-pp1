from re import T


for i in range(1, 31):
    byThree = not bool(i % 3)
    byFive = not bool(i % 5)
    if byFive and byThree:
        print("BINGO", end=" ")
    elif byThree:
        print("THREE", end=" ")
    elif byFive:
        print("FIVE", end=" ")
    else:
        print(i, end=" ")
