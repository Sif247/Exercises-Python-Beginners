def evenList(lst):
    ris = []
    for i in lst:
        if i % 2 == 0:
            ris.append(i)
    return ris

x = evenList([2,8,5,7,2,6])
print(x)