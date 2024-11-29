def word_letter(words, letter):
    new_list = []
    for i in words:
        if letter == i[0]:
            new_list.append(i)
    return new_list

ris = word_letter(["apple", "banana", "orange", "pineapple"], "a")
print(ris)