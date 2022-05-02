# - add student: name , welcome message 
# - add mark to student
# - get avg marks

class Student:
    def __init__(self,name):
        print(f"welcome {name}")
        self.marks = []
    
    def add_mark(self,mark):
        self.marks.append(mark)
    def get_avg(self):
        return sum(self.marks)/len(self.marks)


s1 = Student("Ahmed")

s1.add_mark(70)
s1.add_mark(30)
s1.add_mark(60)
s1.add_mark(40)

print(s1.marks)
print(s1.get_avg())
# -------------

s2 = Student("Khaled")

s2.add_mark(100)
s2.add_mark(50)
s2.add_mark(90)
s2.add_mark(40)

print(s2.marks)
print(s2.get_avg())

