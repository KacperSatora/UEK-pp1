x = 0
y = 10
if x == 0 and y == 0:
    print("point is at (0,0)")
else:
    if x > 0:
        if y > 0:
            print("First quadrant")
        else:
            print("Fourth quadrant")
    elif x < 0:
        if y > 0:
            print("Second quadrant")
        else:
            print("Third quadrant")
    elif x == 0:
        if y > 0:
            print("Top half of coordinate system")
        else:
            print("Bottom half of coordinate system")
    elif y == 0:
        if x > 0:
            print("Right half of coordinate system")
        else:
            print("Left half of coordinate system")