def maxLengthWord(lst):
    maxWord = lst[0]
    for i in lst:
        if len(i) > len(maxWord):
            maxWord = i

    return maxWord


x = maxLengthWord(["Spain", "France", "Germany", "Italy"])
print(x)
