dct = {'name': 'Mario', 'surname': 'Rossi', 'age': 30, 'email': 'mario.rossi@email.com'}

#way1
lst = []
for i in dct.keys():
    lst.append(i)
print(lst)

#way2
lst2 = list(dct.keys())
print(lst2)