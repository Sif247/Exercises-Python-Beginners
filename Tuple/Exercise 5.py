tpl = ("apple", "banana", "kiwi")

#way1
answer = False
for i in tpl:
     if i == "pineapple":
          answer = True
print("the answer is:", answer)

#way2
if "pineapple" in tpl:
     print("the answer is: True")
else:
     print("the answer is: False")
