shoppingList = open("shoppinglist.txt","w")

with open("MeatAndFish.txt", "r") as mf:
    for line in mf:
        line = line.strip()
        shoppingList.write(f"{line}\n")
with open("GrainsAndBread.txt", "r") as gb:
    for line in gb:
        line = line.strip()
        shoppingList.write(f"{line}\n")
shoppingList.close()