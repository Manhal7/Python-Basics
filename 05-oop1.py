class Calculator:               # ----> conventions
    def sum(self,x,y):          # method = function
        return x+y              # property = attributes
    def mul(self,x,y):
        return x*y
    def __init__(self,name):         # constructor
        print(f"Welcome {name}")
        print(self.sum(5,6))

m = Calculator("Manhal")
print(m.sum(3,4))        

b = m.mul(7,4)                 # object.method_name
print(b)

