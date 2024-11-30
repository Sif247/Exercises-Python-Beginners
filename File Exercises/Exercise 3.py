f1 = open("file.txt", "r")
string = f1.read()
f1.close()

f2 = open("file2.txt", "w")
f2.write(string)
f2.close()