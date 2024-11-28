n = int(input("How many elements have the list: "))
lst = []
while n > 0:
    lst.append(int(input("Enter the element: ")))
    n -= 1

for i in lst:
    print(i)
