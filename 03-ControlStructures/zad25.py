a = 7
b = 15
for i in range(2):
    print(b * "*")
    if i < 1:
        for i in range(a - 2):
            print("*" + (b-2) * " " + "*")