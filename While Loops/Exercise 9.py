string = input("Enter a string: ")
i = 0

while i < len(string):
    if string[i] not in "aeiouAEIOU":
        print(string[i], end="")
    i += 1

