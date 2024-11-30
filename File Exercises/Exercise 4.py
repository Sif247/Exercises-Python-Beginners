f = open("file.txt", "r")
count = 0
lineEmpty = False
while lineEmpty == False:
    if f.readline() == "":
        lineEmpty = True
    else:
        count += 1
f.close()
print(count)