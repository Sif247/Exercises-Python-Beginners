char = input("Enter a character: ")
if char.isalpha() is True:
    if char in "aeiou":
        print("The character entered is a vowel")
    else:
        print("The character entered is a consonant")
else:
    print("The character is not a letter")