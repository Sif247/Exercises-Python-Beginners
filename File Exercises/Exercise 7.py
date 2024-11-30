f = open("file.txt", "r")
content = []
for j in f:
    content.append(j)
f.close()

f2 = open("file2.txt", "w")
for i in reversed(content):
    f2.write(i)

f2.close()