# رنامج بياخد رقمني من المستخدم ويطبع كل األرقام اليت تقبل القسمة عىل
# الرقمني من ٠ ل ١00
n1 = int(input("enter number: "))
n2 = int(input("enter number: "))
for n in range(0,101):
    if n % n1 == 0 and n % n2 == 0:
        print(n)
