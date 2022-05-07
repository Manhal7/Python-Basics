# تكليفات 21-23
# ===================================================


# قم بعمل قائمة List تحتوي على أسماء أصدقائك ويكون فيها على الأقل 5 أسماء والمطلوب 
# في السطر الأول والثاني طباعة إسم أول صديق في القائمة بطريقتين 
# ثم في السطر الثالث والرابع تقوم بطباعة إسم آخر صديق في القائمة بطريقتين

# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# # Needed Output
# # "Osama" => Method One
# # "Osama" => Method Two
# # "Mahmoud" => Method One
# # "Mahmoud" => Method Two
# print(friends[0])
# print(friends[:1])
# print(friends[-1])
# print(friends.pop(-1))








# من القائمة السابقة قم بطباعة الأسماء الفردية في السطر الأول
#  وفي السطر الثاني قم بطباعة الأسماء الزوجية
# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# # Needed Output
# # "Osama", "Sayed", "Mahmoud"
# # "Ahmed", "Ali"

# print(friends[1],friends[3])
# print(friends[0],friends[2],friends[4])
# ==================================================

# قم بطباعة مجموعة الأسماء رقم
#  2 و 3 و 4 في السطر الأول ثم الأسم الأخير والذي قبله في السطر الثاني 
# مع العلم أن ال Code يجب أن يعمل في حالة قمنا بتغيير عدد العناصر الموجودة في القائمة
# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# # Needed Output
# # "Ahmed", "Sayed", "Ali",
# # "Ali", "Mahmoud"

# print(friends[1:4])
# print(friends[3:])
# =====================================================

# قم بتحديث آخر أسمين في القائمة لإسم “Elzero”


# friends[3],friends[4]= "Elzero","Elzero"
# print(friends)
# ====================================================


# print("=" * 50)
# myList = ["Osama", "Mohamed", "Elsayed"]
# print("-".join(myList))
# print(" ".join(myList))
# print(", ".join(myList))
# print(type(", ".join(myList)))

# ==================================================================

# قم بإضافة إسم من أصدقائك للقائمة في أول القائمة أولا ثم قم بإضافة إسم آخر في نهاية القائمة
# friends = ["Osama", "Ahmed", "Sayed"]

# # Needed Output
# # ["Nasser", "Osama", "Ahmed", "Sayed"]
# # ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
# friends.insert(0,"Nasser")
# #,friends.insert(4,"Salem")
# friends.append("Salem")
# print(friends)

#======================================================================================= 
# قم بحذف أول إسمين من القائمة ثم بعدها في سطر آخر قم بإزالة آخر إسم من القائمة

# friends.remove("Nasser")
# friends.remove("Osama")
# print(friends)
# friends.remove("Salem")
# print(friends)

# ==========================================================================

# قم بإنشاء قائمتين آخريين فيهم المزيد من الأصدقاء
#  ثم قم بضمهم على أول قائمة لتخرج بالقائمة النهائية فيها جميع الأصدقاء
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

# Needed Output
# ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
# new = friends + employees + school
# print(new)
# ===================>>>>> or -->:
friends.extend(employees+school)
print(friends)
# =========================================================================

# قم بترتيب الأسماء في القائمة في السطر الأول من A إلى Z وفي السطر الثاني من Z إلى A
friends.sort()
print(friends)
friends.sort(reverse=True)
# =========================================================================
# قم بحساب عدد الأصدقاء داخل القائمة

print(len(friends))
# =========================================================================


# التكليف العاشر
# قم بعمل قائمة فيها لغات البرمجة المشهورة وداخلها قائمة فرعية فيها أسماء أطر عمل مشهورة
#  ثم في السطر الأول قم بطباعة إسم اول اطار عمل في القائمة الفرعية
#  وفي السطر الثاني إسم آخر إطار عمل في القائمة الفرعية
#  مع مراعاة أن القائمة الفرعية يمكن أن تزيد ولكنها دائما آخر عنصر في القائمة الرئيسية

# technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]


# # Needed Output
# # Django
# # Web
# print(technologies[4][0])
# print(technologies[4][2])