## Encapsulation : self
## Inheritance
class Calc:
    def __init__(self,name):
        print(f"welcome {name}")
    def sum(self,x,y):
        return x+y
    
    def mul(self,x,y):
        return x*y


# c1 = Calc()
# print(c1.sum(3,4))
# print(c1.mul(3,4))

class SciCalc(Calc):
    # def sum(self,x,y):        -----------> deleted for inheritance
    #     return x+y
    
    # def mul(self,x,y):        -----------> deleted for inheritance
    #     return x*y
    
    def power(self,x,y):
        return x**y


v1 = SciCalc("Ahmed")
print(v1.sum(3,5))
print(v1.mul(2,3))
print(v1.power(3,4))

#  ---------------------------------

class A:
    def do(self):
        print("in C")

class B(A):
    pass

class C:
    def do(self):
        print("in C")

class D(B,C):
    pass


dv = D()
dv.do()

print(D.mro())      # to know the inheritance way.

# ------------------------------------------------

    # Parent Class = Main Class = Super Class : Calc
    # Child Class = Sub Class = Derived Class : SciCalc