# j = (lambda x : x*3)(10)
# print(j)

# map
'''
names = ['ahmed','ali','khaled']
m = []
def get_legnth(x):
    return len(x)

m = map(get_legnth,names)
print(list(m))
'''
names = ['ahmed','ali','khaled']
m= map(lambda x : len(x),names)
print(list(m))



