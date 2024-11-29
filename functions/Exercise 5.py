def length_words(lst):
    length = []
    for i in lst:
        length.append(len(i))
    return length


x = length_words(["Italy", "France", "Germany", "Spain"])
print(x)
