def greaters_list(lst, value):
    ris = []
    for i in lst:
        if i > value:
            ris.append(i)
    return ris

x = greaters_list([5,8,9,7,1,2,3,4], 3)
print(x)