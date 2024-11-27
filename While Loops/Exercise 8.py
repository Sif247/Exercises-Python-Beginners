n = int(input("number of elements:  "))
lst = []
i = n - 1
while i >= 0:
    element = int(input("Enter the element of the list:  "))
    lst.append(element)
    i -= 1

sum = 0
i = 0

while i < n :
    sum += lst[i]
    i += 1

print("The sum is: ",sum)

