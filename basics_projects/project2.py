phrase = input("enter your phrase: ")
y = phrase.split(" ")
b = []
for i in y :
    if i in b:
        continue
    else:
        b.append(i)
print(len(b))
