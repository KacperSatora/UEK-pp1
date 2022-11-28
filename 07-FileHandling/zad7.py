f = open("countries.txt", "r")
count = 1
for line in f:
    print(f"{count}. {line}", end="")
    count +=1