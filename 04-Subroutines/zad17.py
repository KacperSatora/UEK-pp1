def numOfEs(word):
    count = 0
    for e in word:
        if e == "e":
            count += 1
    return count

print(numOfEs("You never get a second chance to make a first impression"))