#  برنامج بياخد رقمني من المستخدم ويطبع كل األرقام اليت تقبل القسمة عىل
# الرقم الثاني من صفر للرقم االول
x1 = int(input("enter number: "))
x2 = int(input("enter number: "))
a = []
for i in range(0,x1+1):
        if i % x2 == 0:
            print(i)

