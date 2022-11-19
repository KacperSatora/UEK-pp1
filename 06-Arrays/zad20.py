arr = [12, 6, 4, 9, 10]


def star(n):
    return (f"{n}: {n * '*'}")

for i in arr:
    print(star(i))