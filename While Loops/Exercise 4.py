import random

solution = random.randint(1,10)
ris = int(input("guess number between 1 and 10: "))

while ris != solution :
    ris = int(input("Try again! :  "))

print("Correct! ")
