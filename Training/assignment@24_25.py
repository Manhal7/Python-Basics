# تكليفات الدروس من الدرس 024 إلى 025

# التكليف 01
x= "osama",
print(x)
print(type(x))
print("=" * 70)
# =====================================================
# التكليف الثاني 
# قم بإنشاء Tuple تحتوي على أسماء 3 من أصدقاءك وأول إسم يكون Osama
# إستخدم خبرتك وما تعلمته سابقا لتغيير أول إسم من Osama إلى Elzero
# قم بطباعة محتوى ال Tuple في السطر الأول
# قم بطباعة النوع للتأكد من أنه Tuple وليس نوع بيانات آخر
# في السطر الثالث قم بطباعة عدد العناصر داخل ال Tuple

friends = ("Osama", "Ahmed", "Sayed")

# Needed Output

# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements
friends1 = list(friends)
friends1[0] = "Elzero"
friends = tuple(friends1)
print(friends)
print(type(friends))
print(len(friends))

print("=" * 70)
# ===============================================================
#  التكليف الثالث

# قم بإنشاء Tuple تحتوي على الأرقام من 1 إلى 3
# قم بإنشاء Tuple تحتوي على الحروف من A إلى C
# قم بعمل Concatenate لهم في Tuple جديدة وقم بطباعة محتواها في السطر الأول
# في السطر الثاني قم بحساب عدد العناصر الموجودة داخل ال Tuple الجديدة

nums = (1, 2, 3)
letters = ("A", "B", "C")

# Needed Output

# nums_and_letters_one = (1, 2, 3, "A", "B", "C")
# 6 Elements
newTuple = nums + letters
print(newTuple)
print(len(newTuple))
# ===============================================================
# التكليف الرابع

# قم بإنشاء Tuple تحتوي على 4 عناصر بأي نوع بيانات تريده
# قم بعمل Destruct لل Tuple وقم بعمل Assign لأول قيمة للمتغير a وثاني قيمة للمتغير b ورابع قيمة للمتغير c
# قم بطباعة المتغير a, b, c كل واحد في سطر مختلف
# تأكد أنك قمت بعمل ال Destruct بسطر واحد فقط

my_tuple = (1, 2, 3, 4)

# Needed Output

# 1
# 2
# 4
(a,b,_,c) = my_tuple
print(my_tuple)
print(a)
print(b)
print(c)