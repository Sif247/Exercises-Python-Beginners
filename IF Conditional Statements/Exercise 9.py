side = []

side.insert(0,int(input("Enter the first side of triangle: ")))
side.insert(1,int(input("Enter the second side of triangle: ")))
side.insert(2,int(input("Enter the third side of triangle: ")))

side.sort()

if side[2] ** 2 == side[0] ** 2 + side[1] ** 2:
    print("The three numbers form a right triangle")
else:
    print("The three numbers do not form a right triangle")