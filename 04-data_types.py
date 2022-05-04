# # Data Types
        # '''
        # - int
        # - floot
        # - bool
        #---
        # - str
        # - list
        # - tuple
        # - dict

        # '''


# Strings:
s = "python is my favorite languge"
s*3
s+s
s[0]
s[-1]
s[:7]
s[-1:-6:-1]
s.split(" ")
s.replace("my", "our")
s.upper()
s.lower()
s.title()
s.isupper()
# --------------------------------

# Lists:
c = [1, 2, 3, True, "m", [7, 8, 9]]
v = [1, 2, 3]
c[0] = 100
c[4:]
c+c 
c*3
c.append(10)
c.insert(1,90)
c.pop()
c.remove(90)
c.sort()
c.sort(reverse=True) ; c.reverse()
# --------------------------------

# Tuple:
k = (1,2,3,4,5)
min(k)
max(k)
len(k)
m = list(k)
k = tuple(m)
# --------------------------------

# Dictionary:
students = {"Ahmed":50 , "Ali": 80 }
for x,y in students.items():
    print(x,y)
students["Ahmed"] 
students.keys()
students.values()
students.items()


