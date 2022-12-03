import random

with open("t20.txt", "w") as f:
    for i in range(50):
        f.write(f"{str(random.randint(100,999))}\n")