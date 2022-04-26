
# Nested while:
x = 0
while x < 5 : # 0 1 2 3 4
    y = 0
    while y <3 : # 0 1 2
        print(x,y)
        y +=1
    x += 1



# Multiplication Table :
mn = 1
while mn <=3: # 1 2 3 
    x = 1
    while x <= 10: # 1 2 3 4 5 6 7 8 9 10
        print(f' {mn} X {x} = {mn*x}') # f string
        x += 1
    mn += 1




# for :
name = "manhal"
for x in name :
    print(x)



# Range:
#    range(start=0,end,step=1)

# range(10)       # 0 1 2 3 4 5 6 7 8 9
# range(2,10)     # 2 3 4 5 6 7 8 9
# range(2,10,3)   # 2 5 8



for x in range(1,11):
    print(x)




# Multiplication Table with for:

for mn in range(1,4): # 1 2 3
    for x in range(1,11): # 1 2 3 4 5 6 7 8 9 10
        print(f' {mn} X {x} = {mn*x}')


# input
x = input('enter number: ')

mynumber = int( input('enter number : '))
print(type(mynumber))

for x in range(1,mynumber+1):
    print(x)


# Control Statment :
# Break

for x in range(1,11):
    if x == 6:
        break
    print(x)
print('welcome')

# Continue
for x in range(1,11):
    if x == 6:
        continue
    print(x)
print('welcome')





















































