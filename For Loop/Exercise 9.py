string = input("Enter a string: ")
letter = input("Enter a letter: ")
count = 0

for i in string:
    if i == letter:
        count += 1

print("In the string", string, "there are", count, "letters", letter)