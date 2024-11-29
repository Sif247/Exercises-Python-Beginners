def only_palindromic(lst):
    ris = []
    for i in lst:
        if i[::-1] == i:
            ris.append(i)
    return ris

x = only_palindromic(["anna","vannav","paolo"])
print(x)