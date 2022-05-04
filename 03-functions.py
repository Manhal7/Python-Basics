#functions

# ---------------
# # parameters:
#         required
#         keyword= positional
#         default
#         Variable length




def mysum (x,y): # arguments , parameters
    print (x+y)

mysum(5,7)

def mysum (x,y): # keyword= positional
    print (x+y)

mysum(y=5,x=7)


def mysum (y,x=0): # defult x = 0 ; defult must be the last argument
    print (x+y)

mysum(5)
# -------------------------------
# functions structure
# def func_name(parameters):
#     func_body : logic
#     return target


def mysum(x,y):
    result = x+y
    return result
mysum(3,4)

x= mysum(3,4) #------return is important for this 
print (f'x = {x}')
    
# --------------------------------

#local VS global

f = 0
print (f)  # 0

def do ():
    global f
    f = 5      # local
    print (f)  # 5

do()

print (f)    
# --------------------------------

# anonymous function
#func_mame = lambda parameters : logic


mysum = lambda x,y : x+y

x= mysum (3,4)
print (x)
# ---------------------------------
# functions exampels :
        # print()
        # type()
        # rang()
        # enumerate()
# -------
# enumerate()
for x in 'manhal tamr':
    print(x)

for index , x in enumerate(range (10,20),1):
    print (index , x)