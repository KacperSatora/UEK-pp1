with open("t21.txt", "w") as file:
    for i in range(1,11):
        file.write(f"{pow(i,1)},{pow(i,2)},{pow(i,3)}\n")        