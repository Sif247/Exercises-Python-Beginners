import csv

values = []
while True:
    value = input("Enter a value (digit 'end' to finish): ")
    if value == "end":
        break
    values.append(value)


f = open("usernames.csv", "w")
writer = csv.writer(f)
writer.writerow(values)
f.close()