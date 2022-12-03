fileDefault = open("t15.txt","r")

fileCopy = open("t17.txt", "w")

for line in fileDefault:
    fileCopy.write(line)

fileCopy.close()
fileDefault.close()
