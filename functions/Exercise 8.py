def avg(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum / len(lst)

x = avg([2,5,6,7,8])
print(x)