def f(first_letter, last_letter):
    import re

    count = 0

    with open("test.txt", encoding='utf-8') as file:

        cleanFile = file.read().split()
        cleanList = []

        for word in cleanFile:
            cleanList.append("".join(re.findall("[a-zA-Z]", word))) # ew \w

        for word in cleanList:
            if word.startswith("w") and word.endswith("d"):
                count += 1

    return count


print(f("w", "d"))