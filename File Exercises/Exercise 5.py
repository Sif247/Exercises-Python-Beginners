import csv

f = open("usernames.csv", "r")
reader = csv.reader(f)

for i in reader:
    print("|".join(i))
f.close()