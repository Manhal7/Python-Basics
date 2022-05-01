
num = [31, 62, 48, 63, 4, 33, 87]
odd = []
even = []
for x in num:
    if x % 2 == 0:
        odd.append(x)
    else:
        even.append(x)
print(odd)
print(even)
