def maximumValue(lst):
    ris = lst[0]
    for i in lst:
        if i > ris:
            ris = i
    return ris


x = maximumValue([1, 5, 7, 9, 14, 3])
print(x)
